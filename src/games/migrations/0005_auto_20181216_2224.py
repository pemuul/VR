# Generated by Django 2.1.3 on 2018-12-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20181216_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='language',
            field=models.CharField(blank=True, choices=[('Русский', 'Русский'), ('Английский', 'Английский')], max_length=50, verbose_name='Язык'),
        ),
    ]