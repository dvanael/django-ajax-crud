from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .ajax import AjaxListView, AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from .forms import BookForm, BookStatusForm, GenreForm
from .models import Book, Genre

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Book's CRUD
class BookMixin:
    template_name = 'book/list.html'
    partial_list = 'partials/book/list.html'
    model = Book
    paginate_by = 7

class BookList(BookMixin, AjaxListView):

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

class BookCreate(BookMixin, AjaxCreateView):
    template_name = 'partials/book/create.html'
    form_class = BookForm

    def save_form(self, form):
        form.instance.user = get_object_or_404(User, id=self.request.user.id) 
        return super().save_form(form)
    
class BookUpdate(BookMixin, AjaxUpdateView):
    template_name = 'partials/book/update.html'
    form_class = BookForm

class BookStatusUpdate(BookMixin, AjaxUpdateView):
    template_name = 'partials/book/update-status.html'
    form_class = BookStatusForm

class BookDelete(BookMixin, AjaxDeleteView):
    template_name = 'partials/book/delete.html'
 
# Genre's CRUD
class GenreMixin:
    template_name = 'genre/list.html'
    partial_list = 'partials/genre/list.html'
    model = Genre
    paginate_by = 5
    object_list = 'genre'

class GenreList(GenreMixin, AjaxListView):

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

class GenreCreate(GenreMixin, AjaxCreateView):
    template_name = 'partials/genre/create.html'
    form_class = GenreForm

class GenreUpdate(GenreMixin, AjaxUpdateView):
    template_name = 'partials/genre/update.html'
    form_class = GenreForm

class GenreDelete(GenreMixin, AjaxDeleteView):
    template_name = 'partials/genre/delete.html'