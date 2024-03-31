from django.shortcuts import render
from django.core.paginator import *
from .models import *
from .forms import *
from .ajax import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Book's CRUD
class BookList(JsonListView):
    template_name = 'book/list.html'
    partial_list = 'partials/book/list.html'
    model = Book
    paginate_by = 7
    
    def get_queryset(self):
        queryset = Book.objects.all()
        
        genre = self.request.GET.get('genre', '')
        if genre:
            queryset = queryset.filter(genre__name__icontains=genre)

        name = self.request.GET.get('search', '')    
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def get_context(self):
        gernes = Genre.objects.all()
        genre = self.request.GET.get('genre', '')
        name = self.request.GET.get('search', '')
        
        context = {
            'name': name,
            'genres': gernes,
            'gerne': genre,
        }
        
        if self.paginate_by:
            context.update({
                'filter': f'&search={name}&genre={genre}'
            })
        return context

class BookCreate(JsonCreateView, BookList):
    template_name = 'partials/book/create.html'
    form_class = BookForm

    def get_instance(self, form):
        form.instance.user = get_object_or_404(User, id=self.request.user.id) 
        instance = form.instance
        return instance
    
    
class BookUpdate(JsonUpdateView, BookList):
    template_name = 'partials/book/update.html'
    form_class = BookForm

class BookStatusUpdate(JsonUpdateView, BookList):
    template_name = 'partials/book/update-status.html'
    form_class = BookStatusForm

class BookDelete(JsonDeleteView, BookList):
    template_name = 'partials/book/delete.html'
 
# Genre's CRUD
class GenreList(JsonListView):
    template_name = 'genre/list.html'
    partial_list = 'partials/genre/list.html'
    model = Genre
    paginate_by = 5
    object_list = 'genre'

    def get_queryset(self):
        queryset = Genre.objects.all()

        name = self.request.GET.get('search', '')    
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def get_context(self):
        name = self.request.GET.get('search', '')
        
        context = {'name': name}
        
        if self.paginate_by:
            context.update({
                'filter': f'&search={name}'
            })
        return context

class GenreCreate(JsonCreateView, GenreList):
    template_name = 'partials/genre/create.html'
    form_class = GenreForm

class GenreUpdate(JsonUpdateView, GenreList):
    template_name = 'partials/genre/update.html'
    form_class = GenreForm

class GenreDelete(JsonDeleteView, GenreList):
    template_name = 'partials/genre/delete.html'