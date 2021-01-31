from rest_framework import serializers
from .models import SongRec

class SongRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRec
        fields = ('name', 'artist', 'album', 'external_url', 'preview_url')
