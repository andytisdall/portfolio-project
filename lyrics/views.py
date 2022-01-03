
from django.shortcuts import render, get_object_or_404
from .models import Lyrics, Album

# Create your views here.


def lyrics(request):
    murder_lyrics = Lyrics.objects.filter(
        album__title="Murder Eyes").order_by('track_no')
    dress_lyrics = Lyrics.objects.filter(
        album__title="Dress to Disappear").order_by('track_no')
    dress = get_object_or_404(Album, title="Dress to Disappear")
    murder = get_object_or_404(Album, title="Murder Eyes")
    return render(request, 'lyrics/all_lyrics.html', {'lyrics': lyrics, 'dress': dress, 'murder': murder, 'murder_lyrics': murder_lyrics, 'dress_lyrics': dress_lyrics})


def detail(request, title):
    lyrics = get_object_or_404(Lyrics, title=title)
    return render(request, 'lyrics/detail.html', {'lyrics': lyrics})
