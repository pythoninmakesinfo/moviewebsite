from .models import Genres


def menu_links(request):
    links=Genres.objects.all()
    return dict(links=links)
def genre_list(request):
    return {
        'genre_list': Genres.objects.all()
    }
