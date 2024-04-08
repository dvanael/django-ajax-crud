from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template.loader import render_to_string

class PaginateMixin:
    """
    Provides pagination capabilities to a list of objects for class-based views.
    """
    paginate_by = None
    partial_list = None
    partial_pagination = 'partials/pagination.html'

    def paginate(self, request, paginate_by, object_list):
        """
        Paginates the given object list based on the request's page number.
        """
        paginator = Paginator(object_list, paginate_by)
        page_num = request.GET.get('page')
        
        try:
            object_list = paginator.get_page(page_num)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return object_list

class ContextMixin:
    """
    Provides a basic context mixin that can be extended to include additional context for templates.
    """
    context = None
    def get_context(self):
        """
        Returns the context dictionary to be used in rendering templates.
        """
        context = {}
        return context

class AjaxResponseMixin(ContextMixin, PaginateMixin):
    """
    Mixin to handle AJAX responses, providing methods for returning JSON responses.
    """
    object_list = 'object_list'
    model = None
    template_name = None


    def ajax_response(self, form=None, object_list=None, context=None, template_name=None, paginate_by=None):
        """
        Constructs a JSON response for an AJAX request with optional form validation, object listing, and pagination.
        """
        data = {}
        if form:
            data['html_form'] = render_to_string(template_name, {'form': form}, request=self.request)
            data['form_is_valid'] = form.is_valid()

        if object_list:
            if paginate_by:
                object_list = self.paginate(self.request, paginate_by, object_list)
                context['page'] = context[f'{self.object_list}'] = object_list
                data['html_pagination'] = render_to_string(self.partial_pagination, context)
            
            data['html_list'] = render_to_string(self.partial_list, {f'{self.object_list}': object_list})
        return JsonResponse(data)
    
    def get_queryset(self):
        """
        Returns the queryset of the model's objects to be listed.
        """
        queryset = self.model.objects.all()
        return queryset
    

class FormResponseMixin(AjaxResponseMixin):
    """
    Mixin to handle form responses via AJAX, including validation and rendering.
    """
    form = None

    def form_valid(self, form):
        """
        Processes a valid form, returns an AJAX response.
        """
        context = self.get_context()
        object_list = self.model.objects.all()
        return self.ajax_response(form=form, object_list=object_list, context=context, template_name=self.template_name, paginate_by=self.paginate_by)
    
    def render_form(self, form):
        """
        Renders the specified form as part of the AJAX response.
        """
        return self.ajax_response(form=form, template_name=self.template_name, paginate_by=self.paginate_by)

class DeleteReponseMixin(AjaxResponseMixin):
    """
    Mixin to handle AJAX responses for delete operations.
    """
    def render_form(self, instance):
        """
        Renders a form for confirming a delete operation on an instance.
        """
        data = {'form_is_valid': False}
        data['html_form'] = render_to_string(self.template_name, {'object': instance}, request=self.request)
        return JsonResponse(data)
    
    def form_valid(self):
        """
        Processes a successful delete operation, returning an AJAX response.
        """
        data = {'form_is_valid': True}
        object_list = self.model.objects.all()
        
        if self.paginate_by:
            object_list = self.paginate(self.request, self.paginate_by, object_list)
            context = {'page': object_list}
            data['html_pagination'] = render_to_string(f'{self.partial_pagination}', context)

        data['html_list'] = render_to_string(self.partial_list, {f'{self.object_list}': object_list})
        return JsonResponse(data)