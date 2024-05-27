from django.urls import path


from .import views


app_name='moviewebsiteapp'
urlpatterns = [

    path('', views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),

    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('movie/<int:id>/',views.youtube_trailer,name='youtube_trailer'),
    path('add/',views.add_movie,name='add_movie'),
    path('add_review/<int:movie_id>/', views.add_review, name='add_review'),
    path('genre/<int:genre_id>/', views.movies_by_genre, name='movies_by_genre'),




]
