from django.shortcuts import render
from django.http import Http404



def index(request):
    return render(request, 'home/home.html')

def index1(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'contact/contact.html')

def comments(request):
    return render(request, 'comments/comments.html')

'''
def music(request):
    all_albums = Album.objects.all()  # gets all the album class database(album_title etc.)
    return render(request, 'music/index.html', {'all_albums': all_albums, })

def detail(request, album_id):
    try:
        album =Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album, })
'''
