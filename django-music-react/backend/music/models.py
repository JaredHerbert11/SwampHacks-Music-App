from django.db import models

# Create your models here.

class SongRec(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    spotifyID = models.CharField(max_length=120)

    def _str_(self):
        return self.title

class SongRecList(models.Model):
    list = models.CharField(max_length=120)

    def _str_(self):
        return self.list