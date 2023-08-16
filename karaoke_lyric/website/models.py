from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Karaoke(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.CharField(max_length=200)
    song_slug = models.SlugField(max_length=200, editable=False)
    lyric = models.TextField(max_length=2000)

    user_update = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)
    
    def save(self, *args, **kwargs):
        self.song_slug = slugify(self.song)
        super().save(*args, **kwargs)