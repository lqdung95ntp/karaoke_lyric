from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Karaoke

# Create your views here.
def homepage(request):
    return redirect('personal')

@login_required(login_url='login')
def search(request, song_slug=""):
    if song_slug == "":
        return redirect('personal')
    song_obj = Karaoke.objects.filter(user_update=request.user, song_slug=song_slug).first()
    if song_obj is None:
        return redirect('personal')
    return render(request, 'search.html', 
                    context={
                        "song_obj": song_obj
                    })

@login_required(login_url='login')
def personal(request):
    # get song
    all_songs = Karaoke.objects.filter(user_update=request.user).order_by('time_update')
    # add song
    if request.method == "POST":
        song = request.POST["song_txt"]
        lyric = request.POST["lyric_txt"]
        song_obj = Karaoke.objects.filter(song=song, user_update=request.user).first()
        if song_obj is None:
            song_obj = Karaoke.objects.create(song=song, user_update=request.user)
        song_obj.lyric = lyric
        song_obj.save()
    return render(request, 'personal.html',
                  context={
                      "all_songs": all_songs,
                  })