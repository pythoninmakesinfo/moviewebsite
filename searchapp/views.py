
from django.shortcuts import render

from moviewebsiteapp.models import Movie




def searchbar(request):
    if request.method=="GET":
        query=request.GET.get('query')
        if query:
            moviess=Movie.objects.filter(genres__name__icontains=query)
            print(moviess)
            return render(request,'searchbar.html',{'movie':moviess})
        else:
            print("no information to show")
            return request(request,'searchbar.html',{})