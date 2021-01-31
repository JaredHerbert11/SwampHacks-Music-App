from django.contrib import admin
from .models import SongRec
# Register your models here.

class SongRecAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'album', 'external_url', 'preview_url')

admin.site.register(SongRec, SongRecAdmin)