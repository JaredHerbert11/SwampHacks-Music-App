from rest_framework import serializers
from .models import SongRec

class SongRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRec
        fields = ('title', 'artist', 'spotifyID')