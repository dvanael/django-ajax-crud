from django import forms
from .models import *

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ('name', 'genre')

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('__all__')

class BookStatusForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('availability',)