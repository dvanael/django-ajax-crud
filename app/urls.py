from django.urls import path
from .views import *

urlpatterns = [
  path('', index, name='index'),
  
  path('books/', BookList.as_view(), name='book-list'),
  path('js/create/book/', BookCreate.as_view(), name='js-create-book'),
  path('js/update/<int:pk>/', BookUpdate.as_view(), name='js-update-book'),
  path('js/delete/<int:pk>/', BookDelete.as_view(), name='js-delete-book'),

  path('genres/', GenreList.as_view(), name='genre-list'),
  path('js/create/genre/', GenreCreate.as_view(), name='js-create-genre'),
  path('js/update/<int:pk>/genre/', GenreUpdate.as_view(), name='js-update-genre'),
  path('js/delete/<int:pk>/genre/', GenreDelete.as_view(), name='js-delete-genre'),
]
