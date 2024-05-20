from django.contrib import admin


from .models import Genres, Review

from .models import Movie
# Register your models here.

admin.site.register(Review)
admin.site.register(Movie)
admin.site.register(Genres)

