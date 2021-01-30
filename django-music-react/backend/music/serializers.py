from rest_framework import serializers
from .models import SongRec
from .models import SongRecList

class SongRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRec
        fields = ('title', 'artist', 'spotifyID')

class SongRecListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRecList
        fields = ('list')