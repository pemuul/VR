from django.contrib import admin


from .models import *

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(GameComment)
class GameCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'comment', 'rating', 'created')

@admin.register(GameImage)
class GameImageAdmin(admin.ModelAdmin):
    list_display = ('game', 'img')

@admin.register(GameGenre)
class GameGenreAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(GamePlatform)
class GamePlatformAdmin(admin.ModelAdmin):
    list_display = ('title',)
