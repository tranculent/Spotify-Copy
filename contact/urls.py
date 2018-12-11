from django.conf.urls import url, include
from . import views

app_name = 'front page'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^comments/$', views.comments, name='comments'),
]