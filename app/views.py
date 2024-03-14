from django.shortcuts import render
from django.core.paginator import *
from .models import *
from .forms import *
from .utils import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Book's CRUD
class BookList(JsonListView):
    template_name = 'book/book-list.html'
    partial_list = 'partials/book/list.html'
    model = Book
    paginate_by = 7

class BookCreate(JsonCreateView, BookList):
    template_name = 'partials/book/create.html'
    form_class = BookForm
    
class BookUpdate(JsonUpdateView, BookList):
    template_name = 'partials/book/update.html'
    form_class = BookForm

class BookDelete(JsonDeleteView, BookList):
    template_name = 'partials/book/delete.html'
 
# Genre's CRUD
class GenreList(JsonListView):
    template_name = 'genre/genre-list.html'
    partial_list = 'partials/genre/list.html'
    model = Genre
    paginate_by = 5
    object_list = 'genre'

class GenreCreate(JsonCreateView, GenreList):
    template_name = 'partials/genre/create.html'
    form_class = GenreForm

class GenreUpdate(JsonUpdateView, GenreList):
    template_name = 'partials/genre/update.html'
    form_class = GenreForm

class GenreDelete(JsonDeleteView, GenreList):
    template_name = 'partials/genre/delete.html'