# Generated by Django 2.1.3 on 2018-12-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0007_auto_20181219_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='metro',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ближайшее метро'),
        ),
    ]
