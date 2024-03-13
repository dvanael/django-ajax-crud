from django.db import models
from django.utils import timezone
from datetime import date

class Status(models.Model):
  name = models.CharField(max_length=15)

  class Meta:
      verbose_name = ("Status")
      verbose_name_plural = ("Status")

  def __str__(self):
      return self.name

class UsageRequest(models.Model):
  status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status", to_field='id', default='1')
  justification = models.CharField(default="" ,max_length=150)
  entry_time = models.TimeField(default=timezone.now)
  exit_time = models.TimeField(default=timezone.now)
  date = models.DateField(default=date.today)
  timestamp = models.DateTimeField(auto_now=True)

  class Meta:
      verbose_name = ("Usage Request")
      verbose_name_plural = ("Usage Requests")
      ordering = ['-timestamp']

  def __str__(self):
      return f"Solicitação {self.status} - {self.date}"
