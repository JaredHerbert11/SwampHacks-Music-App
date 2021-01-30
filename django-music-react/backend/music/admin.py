from django.contrib import admin
from .models import SongRec
# Register your models here.

class SongRecAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'spotifyID')

admin.site.register(SongRec, SongRecAdmin)