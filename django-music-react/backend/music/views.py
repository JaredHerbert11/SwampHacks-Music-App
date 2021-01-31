from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from .serializers import SongRecSerializer
from .models import SongRec, User
from .song_recommendation import getRecommendedSongs
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def songrec_list(request, pk):
    curr_user = None
    if not request.session.session_key: #Checks if there is currently a cookie session
        request.session.create()
        request.session.set_expiry(120) #Expires after 2 minutes (for testing reasons), regardless of whether browser closes or not
        curr_user = User(session_id=request.session.session_key)
        curr_user.save() #Saves in database
    else:
        curr_user = User.objects.get(session_id=request.session.session_key)

    print('pk is: ')
    print(pk)
    reclist = []
    if request.method == 'GET':
        url = "https://youtube.com/watch/?" + pk
        print("url is:")
        print(url)
        df = getRecommendedSongs(url)
        for index, row in df.iterrows():
            if row['preview_url'] == None: #Avoids null error for preview_url
                row['preview_url'] = "N/A"
            rec = SongRec(name=row['name'], album=row['album'], artist=row['artists'], external_url=row['external_url'], preview_url=row['preview_url'])

            reclist.append(rec)

            if not duplicate_check(row): #Check if rec is already in the database
                rec.save() 
                curr_user.song_recs.add(rec) #Add rec to user's recommended list

        reclist_serializer = SongRecSerializer(reclist, many=True)
        return JsonResponse(reclist_serializer.data, safe=False)

def duplicate_check(row):
    try:
        SongRec.objects.get(name=row['name'], album=row['album'], artist=row['artists'], external_url=row['external_url'], preview_url=row['preview_url'])
        return True
    except SongRec.DoesNotExist:
        return False
        