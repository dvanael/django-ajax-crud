from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User

class Genre(models.Model):
  name = models.CharField(max_length=15)

  class Meta:
    verbose_name = ("Genre")
    ordering = ['-pk']
    
  def __str__(self):
    return self.name

class Book(models.Model):
    CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=150)
    availability = models.CharField(max_length=20, choices=CHOICES, default='available')
    timestamp = models.DateTimeField(auto_now=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name