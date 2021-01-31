from django.db import models

# Create your models here.

class SongRec(models.Model):
    name = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    album = models.CharField(max_length=120)
    external_url = models.CharField(max_length=200)
    preview_url = models.CharField(max_length=200)

    def _str_(self):
        return self.name