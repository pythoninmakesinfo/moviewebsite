from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm, ReviewForm
from .models import Movie, Review, Genres
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    moviess = Movie.objects.all()
    context = {'Movie_list': moviess}
    return render(request, 'index.html', context)

def detail(request, movie_id):
    moviess = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=moviess)
    genres = Genres.objects.filter(movie=moviess)
    return render(request, "detail.html", {'movies': moviess, 'reviews': reviews, 'genres': genres})

@login_required
def youtube_trailer(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, "youtube_trailer.html", {'movies': movie})

@login_required
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})

@login_required
def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if movie.added_by != request.user:
        messages.error(request, 'You do not have permission to update this movie.')
        return redirect('moviewebsiteapp:detail', movie_id=id)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie updated successfully!')
            return redirect('/')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form, 'movie': movie})

@login_required
def delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if movie.added_by != request.user:
        messages.error(request, 'You do not have permission to delete this movie.')
        return redirect('moviewebsiteapp:detail', movie_id=id)

    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Movie deleted successfully!')
        return redirect('/')
    return render(request, 'delete.html', {'movie': movie})

@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('moviewebsiteapp:detail', movie_id=movie_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'movie': movie})

@login_required
def movies_by_genre(request, genre_id):
    genre = get_object_or_404(Genres, id=genre_id)
    movies = Movie.objects.filter(genres=genre)
    return render(request, 'movies_by_genre.html', {'genre': genre, 'movies': movies})


