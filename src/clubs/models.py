from django.db import models
from django.shortcuts import reverse

from games.models import Game



class Club(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название организации')
    desc = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    metro = models.CharField(max_length=50, verbose_name='Ближайшее метро', default='метро')
    adress = models.CharField(max_length=150, verbose_name='Адрес')
    site = models.CharField(max_length=50, verbose_name='Сайт')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    rating = models.CharField(max_length=50, verbose_name='Рейтинг')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name='ЧПУ')
    delivery = models.BooleanField(default=False, verbose_name='Возможность выезда на дом')
    games = models.ManyToManyField(Game, blank=True, verbose_name='Список игр клуба')

    def get_absolute_url(self):
        return reverse('club_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)