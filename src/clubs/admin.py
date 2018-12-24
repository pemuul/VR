from django.contrib import admin

# Register your models here.
from .models import Club


class ClubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Club, ClubAdmin)