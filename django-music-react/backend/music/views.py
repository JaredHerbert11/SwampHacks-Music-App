from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SongRecSerializer
from .models import SongRec

# Create your views here.
class SongRecView(viewsets.ModelViewSet):
    serializer_class = SongRecSerializer
    queryset = SongRec.objects.all()