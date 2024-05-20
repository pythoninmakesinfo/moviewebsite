from django import forms
from .models import Movie, Genres, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','actors','genres','img','date','youtube_trailer']



class GenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = ['name']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(UserCreationForm):
   model=User
   fields= ('username','password')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
