from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from .serializers import SongRecSerializer
from .models import SongRec
from .song_recommendation import getRecommendedSongs
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def songrec_list(request, pk):
    print('pk is: ')
    print(pk)
    reclist = []
    if request.method == 'GET':
        url = "https://youtube.com/watch/?" + pk
        print("url is:")
        print(url)
        df = getRecommendedSongs(url)
        for index, row in df.iterrows():
            reclist.append(SongRec(name=row['name'], album=row['album'], artist=row['artists'], external_url=row['external_url'], preview_url=row['preview_url']))
        reclist_serializer = SongRecSerializer(reclist, many=True)
        return JsonResponse(reclist_serializer.data, safe=False)
