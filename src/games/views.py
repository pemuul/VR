from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Sum
from taggit.models import Tag
from .forms import GameCommentForm

from games.models import Game, GameComment
from clubs.models import Club



def games_view(request):
    games_list = Game.objects.all()
    context = {
        'games_list': games_list,
    }
    return render(request, 'games/game_index.html', context)


def game_detail_view(request, slug):
    instance = get_object_or_404(Game, slug=slug)
    games = Game.objects.all()
    clubs = Club.objects.all()

    comments = GameComment.objects.all()
    comments_sum = GameComment.objects.all().aggregate(Avg('rating')).values()


    new_comment = None

    if request.method == 'POST':
        comment_form = GameCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.game = instance
            new_comment.instance = instance
            new_comment.save()
    else:
        comment_form = GameCommentForm()


    context = {
        'instance': instance,
        'games': games,
        'clubs': clubs,
        'comments': comments,
        'comments_sum': comments_sum,

        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'games/game_detail.html', context)
