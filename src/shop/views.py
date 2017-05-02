from django.core.exceptions import ImproperlyConfigured
from django.views.generic.list import ListView
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.template.loader import render_to_string

from .models import TeslaCar
# from .forms import TeslaForm


class IndexView(ListView):
    model = TeslaCar
    template_name = 'index.html'

    def get_queryset(self):
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
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
                ordering = (ordering)
            queryset = queryset.order_by(*ordering)
        return queryset

# def car_create(request):
#     form = TeslaForm()
#     context = {'form': form}
#     html_form = render_to_string('partial_car_create.html', context, request=request)
#     return JsonResponse({'html_form': html_form})
