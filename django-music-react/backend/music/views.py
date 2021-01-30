from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SongRecSerializer
from .serializers import SongRecListSerializer
from .models import SongRec
from .models import SongRecList

# Create your views here.
class SongRecView(viewsets.ModelViewSet):
    serializer_class = SongRecSerializer
    queryset = SongRec.objects.all()

class SongRecListView(viewsets.ModelViewSet):
    serializer_class = SongRecListSerializer
    queryset = SongRecList.objects.all()