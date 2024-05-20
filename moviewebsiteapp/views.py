
from django.http import HttpResponse

from .forms import MovieForm, ReviewForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Movie, Review, Genres


def index(request):
    moviess=Movie.objects.all()
    context={'Movie_list':moviess}
    return render(request, 'index.html', context)

@login_required
def detail(request,movie_id):
    moviess =get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=moviess)
    genres=Genres.objects.filter(movie=moviess)
    return render(request,"detail.html", {'movies': moviess,'reviews':reviews,'genres':genres})
    return HttpResponse("this is movies no %s"% movie_id)
@login_required
def youtube_trailer(request,movie_id):
    movies=Movie.objects.get(id=movie_id)
    return render(request, "youtube_trailer.html", {'movies': movies})
    return HttpResponse("this is movies no %s"% movie_id)

@login_required
def add_movie(request):
    if request.method=="POST" and request.FILES['img']:
        name=request.POST.get('name',)
        desc= request.POST.get('desc',)
        actors= request.POST.get('actors',)
        img =request.FILES['img']
        date=request.POST.get('date',)
        youtube_trailer=request.POST.get('youtube_trailer',)
        movie=Movie(name=name,desc=desc,actors=actors,img=img,date=date,youtube_trailer=youtube_trailer)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')

@login_required
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
@login_required
def delete(request,id):
    if request.method=='POST':
       movie=Movie.objects.get(id=id)
       movie.delete()
       return redirect('/')
    return render(request,'delete.html')

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
            return redirect('moviewebsiteapp:detail', movie_id=movie_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'movie': movie})





