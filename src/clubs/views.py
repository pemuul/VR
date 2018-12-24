from django.shortcuts import render, get_object_or_404
from .models import Club

#from .filters import GamesFilter


def clubs_view(request):
    clubs_list = Club.objects.all()
    context = {
        'clubs_list': clubs_list
    }
    return render(request, 'clubs/index.html', context)


def club_detail_view(request, slug):
    instance = get_object_or_404(Club, slug=slug)
    club_games_list = instance.games.all().order_by('id')
#    club_games_filter = GamesFilter(request.GET, queryset=club_games_list)

    context = {
        'title': instance.title,
        'desc': instance.desc,
        'img': instance.image,
        'club_games_list': club_games_list,
#        'filter': club_games_filter,

#        'club_games_list': Game.objects.all().filter(genre_id=1).order_by('id'),
#        'club_games_genre': GameGenre.objects.all().filter(genre__iexact='Action'),
    }
    return render(request, 'clubs/club_detail.html', context)
