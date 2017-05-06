from django.views.generic import CreateView
from django.views.generic.list import ListView

from .models import TeslaCar
from .forms import TeslaForm


class IndexView(ListView):
    model = TeslaCar
    paginate_by = 2
    queryset = TeslaCar.objects.all()   # Default: Model.objects.all()
    context_object_name = 'tesla_list'   # Default = object_list
    template_name = 'shop/index.html'


class CreateCarView(CreateView):
    model = TeslaCar
    form_class = TeslaForm
    template_name = ''
    slug_field = 'slug'
    success_url = 'shop/index.html'
