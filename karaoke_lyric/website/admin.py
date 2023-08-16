from django.contrib import admin
from .models import Karaoke


# Register your models here.
@admin.register(Karaoke)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'song_slug', 'lyric')