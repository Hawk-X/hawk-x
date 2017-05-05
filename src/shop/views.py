import six
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import CreateView
from django.views.generic.list import ListView

from .models import TeslaCar
from .forms import TeslaForm


class IndexView(ListView):
    model = TeslaCar
    template_name = 'shop/index.html'

    def get_queryset(self):
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, six.string_types):
                ordering = ordering
            queryset = queryset.order_by(*ordering)
        return queryset


class CreateCarView(CreateView):
    model = TeslaCar
    form_class = TeslaForm
    template_name = ''
    slug_field = 'slug'
    success_url = 'shop/index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
            return self.form_class(**self.get_form_class())

    def get(self, request, *args, **kwargs):
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
               Handles POST requests, instantiating a form instance with the passed
               POST variables and then checked for validity.
               """
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
