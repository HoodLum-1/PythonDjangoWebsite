from django.http import HttpResponse
from .models import Album  # Imports album table from models
# Create your views here.


# function returns a web page
def index(request):
    # variables for function index
    all_albums = Album.objects.all()  # fetches data from albums table
    html = ''
    for album in all_albums:  # loops all the data in album table
        url = '/music/' + str(album.id) + '/'  # creates url to album id
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'  # displays album title and link
    return HttpResponse(html)  # returns variable


# function returns a web page
def detail(request, album_id):
    return HttpResponse('<h2>Details for Album is:' + str(album_id) + '</h2>')
