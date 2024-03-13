from django.urls import path
from .views import *

urlpatterns = [
  path('', index, name='index'),
  
  path('list/', request_list, name='request-list'),
  path('js/criar/', ReservationCreate.as_view(), name='js-create'),
  path('js/editar/<int:pk>/', ReservationUpdate.as_view(), name='js-update'),
  path('js/excluir/<int:pk>/', ResevertionDelete.as_view(), name='js-delete'),

  path('list-status/', status_list, name='status-list'),
  path('js/criar/status/', StatusCreate.as_view(), name='js-create-status'),
  path('js/editar/<int:pk>/status/', StatusUpdate.as_view(), name='js-update-status'),
  path('js/deletar/<int:pk>/status/', StatusDelete.as_view(), name='js-delete-status'),
]
