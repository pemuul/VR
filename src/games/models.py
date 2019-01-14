from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from taggit.managers import TaggableManager


class GameGenre(models.Model):
    title = models.CharField(max_length=50, verbose_name='Жанр игры')

    def __str__(self):
        return str(self.title)


class GamePlatform(models.Model):
    title = models.CharField(max_length=50, verbose_name='Платформа игры')

    def __str__(self):
        return str(self.title)


class Game(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название игры')
    desc = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    video = models.URLField(blank=True, verbose_name='Ссылка на видео YouTube')
    platform = models.ManyToManyField(GamePlatform, blank=True, verbose_name='Платформа')
    genre = models.ForeignKey(GameGenre, on_delete=models.CASCADE, default=None, verbose_name='Жанр')
    num_players = models.PositiveIntegerField(verbose_name='Кол-во игроков', default=0, blank=True, null=True)
    age_players = models.PositiveIntegerField(verbose_name='Допустимый возраст', default=0, blank=True, null=True)
    year = models.DateField(auto_now=False, auto_now_add=False, blank=True, verbose_name='Дата выпуска')
    language_choices = (
        ('Русский', 'Русский'),
        ('Английский', 'Английский'),
    )
    language = models.CharField(max_length=50, choices=language_choices, blank=True, verbose_name='Язык')
    owner = models.CharField(max_length=50, blank=True, verbose_name='Разработчик')
    country = models.CharField(max_length=50, blank=True, verbose_name='Страна')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='ЧПУ')
    tags_taggit = TaggableManager()

    def get_absolute_url(self):
        return reverse('game_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)


class GameImage(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')

    def __str__(self):
        return str(self.img)


class GameComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    comment = models.TextField(max_length=None, verbose_name='')
    RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=0, verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.game)