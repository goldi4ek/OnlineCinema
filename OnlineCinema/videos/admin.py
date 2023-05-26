from django.contrib import admin

from .models import Video, Genre, Actor, Director

admin.site.register(Video)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)