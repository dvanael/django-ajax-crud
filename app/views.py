from django.shortcuts import render
from django.core.paginator import *
from .models import *
from .forms import *
from .utils import *

# Create your views here.
def index(request):
  return render(request, 'index.html')

def request_list(request):
  usages = UsageRequest.objects.all()
  paginator = Paginator(usages, 7)
  page_num = request.GET.get('page')
  page = paginator.get_page(page_num)
  context = {
    'object_list': page,
    'page': page,
    }
  return render(request, 'request/request-list.html', context)

def status_list(request):
  status = Status.objects.all()
  paginator = Paginator(status, 5)
  page_num = request.GET.get('page')
  page = paginator.get_page(page_num)
  context = {
    'status': page,
    'page': page,
    }
  return render(request, 'status/status-list.html', context)

class ReservationCreate(JsonCreateView):
  template_name = 'partials/request/create.html'
  partial_list = 'partials/request/list.html'
  model = UsageRequest
  form_class = UsageRequestForm
  paginate_by = 7
  
class ReservationUpdate(JsonUpdateView):
  template_name = 'partials/request/update.html'
  partial_list = 'partials/request/list.html'
  model = UsageRequest
  form_class = UsageRequestForm
  paginate_by = 7

class ResevertionDelete(JsonDeleteView):
  template_name = 'partials/request/delete.html'
  partial_list = 'partials/request/list.html'
  model = UsageRequest
  form_class = UsageRequestForm
  paginate_by = 7

class StatusCreate(JsonCreateView):
    template_name = 'partials/status/create.html'
    partial_list = 'partials/status/list.html'
    model = Status
    form_class = StatusForm
    paginate_by = 5
    object_list = 'status'

class StatusUpdate(JsonUpdateView):
    template_name = 'partials/status/update.html'
    partial_list = 'partials/status/list.html'
    model = Status
    form_class = StatusForm
    paginate_by = 5

class StatusDelete(JsonDeleteView):
    template_name = 'partials/status/delete.html'
    partial_list = 'partials/status/list.html'
    model = Status
    paginate_by = 5
    