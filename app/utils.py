from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views import View
from .models import *
from .forms import *

class JsonListView(View):
    template_name = None
    partial_list = None
    partial_pagination = 'partials/pagination.html'
    model = None
    paginate_by = None
    object_list = 'object_list'
    
    def get(self, request, *args, **kwargs):
        object_list = self.get_queryset()
        context = self.get_context()

        context[f'{self.object_list}'] = object_list
        
        if self.paginate_by:
            object_list = self.paginate(request, self.paginate_by, object_list)
            
            context.update({
                'page': object_list,
                f'{self.object_list}': object_list,
            })

            data = {
                'html_list': render_to_string(self.partial_list, {f'{self.object_list}': object_list}),
                'html_pagination': render_to_string(self.partial_pagination, context)
            }
        else:
            data = {
                'html_list': render_to_string(self.partial_list, {f'{self.object_list}': object_list})
            }

        # Verifica se o cabeçalho está presente na requisição
        if request.headers.get('header') == 'XMLHttpRequest':
            return JsonResponse(data)
        else:
            # Caso contrário, retorne a resposta como uma renderização de template
            return render(request, self.template_name, context)
      
    def paginate(self, request, paginate_by, object_list):
        paginator = Paginator(object_list, self.paginate_by)
        page_num = request.GET.get('page')
        
        try:
            object_list = paginator.get_page(page_num)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return object_list

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context(self):
        context = {}
        return context

class FormView(JsonListView):
    form_class = None

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_form(request, form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return self.form_valid(request, form)

    def form_valid(self, request, form):
        data = {}
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True

            object_list = self.model.objects.all()
            
            if self.paginate_by:
                object_list = self.paginate(request, self.paginate_by, object_list)
                context = {'page': object_list}

                data['html_pagination'] = render_to_string(f'{self.partial_pagination}', context)

            data['html_list'] = render_to_string(self.partial_list, {f'{self.object_list}': object_list})
        else:
            data['form_is_valid'] = False

        data['html_form'] = render_to_string(self.template_name, {'form': form}, request=request)
        return JsonResponse(data)

    def render_form(self, request, form):
        data = {}
        context = {'form': form}
        data['html_form'] = render_to_string(self.template_name, context, request=request)
        return JsonResponse(data)


class JsonCreateView(FormView):

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class JsonUpdateView(FormView):

    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=instance)
        return self.render_form(request, form)

    def post(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=instance)
        return self.form_valid(request, form)


class JsonDeleteView(JsonListView):

    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        data = {'form_is_valid': False}
        data['html_form'] = render_to_string(self.template_name, {'object': instance}, request=request)

        return JsonResponse(data)

    def post(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=pk)
        instance.delete()
        data = {'form_is_valid': True}

        object_list = self.model.objects.all()
            
        if self.paginate_by:
            object_list = self.paginate(request, self.paginate_by, object_list)
            context = {'page': object_list}

            data['html_pagination'] = render_to_string(f'{self.partial_pagination}', context)

        data['html_list'] = render_to_string(self.partial_list, {f'{self.object_list}': object_list})

        return JsonResponse(data)
