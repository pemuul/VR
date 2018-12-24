import django_filters
from django import forms

'''
from .models import Club, Game, GameGenre, GamePlatform


class GamesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    genre = django_filters.ChoiceFilter(
        choices=[(game.id, game.title) for game in GameGenre.objects.all()],
    )
    num_players = django_filters.ChoiceFilter(
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('4', '4'),
            ('8', '8'),
        ],
    )
    age_players = django_filters.ChoiceFilter(
        choices=[
            ('12', '12'),
            ('16', '16'),
            ('18', '18'),
        ],
    )
    platform = django_filters.ModelMultipleChoiceFilter(queryset=GamePlatform.objects.all(),
                                                        widget=forms.CheckboxSelectMultiple)

    # platform = django_filters.ModelMultipleChoiceFilter(queryset=Game.objects.all(),
    #                                                   widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Club
        fields = ['title', 'genre', 'num_players', 'age_players', 'platform']
'''