from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm


# generic.ListView means that we will display LIST items, like <li>


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'  # can be changed to w/e we want

    # returns all the albums, always should be in generic.ListView
    def get_queryset(self):
        return Album.objects.all()

# generic.DetailView doesn't display list, it displays information or details


class DetailView(generic.DetailView):
    model = Album
    # if there is a model Album, display music/detail.html
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    # Create an object
    # Creates a new Album
    model = Album
    # list of things that the user  can select to edit ( taken from the models.py Album class)
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'is_favorite']

    def get_success_url(self):
        return reverse('music:detail')


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    # when the thing was successfully deleted ( we will be redirected to inxed.html )
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # whenever a get request, this function comes in play
    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # whenever a post request, this function comes in play
    # process form data
    def post(self, request):
        form = self.form_class(request.POST) # whenever they hit submit, all the data is stored in request.POST

        if form.is_valid():

            user = form.save(commit=False) # creates an object from the form, it doesn't save it to the database yet

            # cleaned (normalized) data
            # data that is formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password) # change the password
            user.save() # saves it to the database, going to appear in the admin interface

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password) # checks if the username and password already exist in the database

            if user is not None:

                if user.is_active: # if user exists
                    login(request, user) # they are logged in the website after this
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

def logout(request):
    pass



