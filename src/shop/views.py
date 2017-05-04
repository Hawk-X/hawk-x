import six
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse


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
                ordering = (ordering)
            queryset = queryset.order_by(*ordering)
        return queryset





def car_create(request):
    data = dict()

    if request.method == 'POST':
        form = TeslaForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = TeslaForm()

    context = {'form': form}
    data['html_form'] = render('shop/partical_car_create.html', context, request=request)
    return JsonResponse(data)
