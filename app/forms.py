from django import forms
from .models import *

class UsageRequestForm(forms.ModelForm):
  class Meta:
    model = UsageRequest
    fields = ('justification', 'date', 'entry_time', 'exit_time')

class StatusForm(forms.ModelForm):
    
    class Meta:
        model = Status
        fields = ('__all__')
