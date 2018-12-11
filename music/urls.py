from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [

    url(r'^music/$', views.IndexView.as_view(), name='index'),
    url(r'^music/register/$', views.UserFormView.as_view(), name='register'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/pk/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/pk/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),


    # /music/album/add/
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),
]