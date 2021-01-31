from rest_framework import serializers
from .models import SongRec

class SongRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRec
        fields = ('name', 'artist', 'album','album_id', 'external_url', 'preview_url')
