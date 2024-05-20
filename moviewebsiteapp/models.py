from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Genres(models.Model):
    name=models.CharField(max_length=250,unique=True)


    class Meta:
        ordering=('name',)
        verbose_name='genre'
        verbose_name_plural='genres'

    def __str__(self):
        return '{}'.format(self.name)
class Movie(models.Model):
    name = models.CharField(max_length=250,unique=True)
    desc = models.TextField()
    actors = models.CharField(max_length=250)
    genres = models.ForeignKey(Genres,on_delete=models.CASCADE,null=True,blank=True)
    img = models.ImageField(upload_to='gallery')
    date=models.DateField()
    youtube_trailer=models.URLField(max_length=250)

    class Meta :
         ordering=('name',)
         verbose_name='movie'
         verbose_name_plural='movies'

    def __str__(self):
        return '{}'.format(self.name)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.movie.name} by {self.user.username}"

