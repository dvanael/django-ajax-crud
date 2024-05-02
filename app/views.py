from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from ajax.views import AjaxListView, AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from .forms import BookForm, BookStatusForm, GenreForm
from .models import Book, Genre

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Book's CRUD
class BookList(AjaxListView):
    model = Book
    template_name = 'book/list.html'
    partial_list = 'partials/book/list.html'
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

class BookCreate(AjaxCreateView):
    form_class = BookForm
    template_name = 'partials/book/create.html'
    success_url = reverse_lazy('book-list')
    success_message = 'Book has been ADDED!'

    def form_valid(self, form):
        user = self.request.user
        if not user.is_authenticated:
            form.instance.user = None

        if user.is_authenticated:
            form.instance.user = get_object_or_404(User, id=self.request.user.id) 

        return super().form_valid(form)
    
class BookUpdate(AjaxUpdateView):
    form_class = BookForm
    template_name = 'partials/book/update.html'
    success_url = reverse_lazy('book-list')
    success_message = 'Book has been UPDATED!'

class BookStatusUpdate(AjaxUpdateView):
    form_class = BookStatusForm
    template_name = 'partials/book/update-status.html'
    success_url = reverse_lazy('book-list')
    success_message = 'Book STATUS has been UPDATED'

class BookDelete(AjaxDeleteView):
    model = Book
    template_name = 'partials/book/delete.html'
    success_url = reverse_lazy('book-list')
    success_message = 'Book has been DELETED!'
 
# Genre's CRUD
class GenreList(AjaxListView):
    model = Genre
    object_list = 'genre'
    template_name = 'genre/list.html'
    partial_list = 'partials/genre/list.html'
    paginate_by = 5

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

class GenreCreate(AjaxCreateView):
    template_name = 'partials/genre/create.html'
    form_class = GenreForm
    success_url = reverse_lazy('genre-list')

class GenreUpdate(AjaxUpdateView):
    template_name = 'partials/genre/update.html'
    form_class = GenreForm
    success_url = reverse_lazy('genre-list')

class GenreDelete(AjaxDeleteView):
    model = Genre
    template_name = 'partials/genre/delete.html'
    success_url = reverse_lazy('genre-list')