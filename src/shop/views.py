from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
# from django.views import View

from .models import TeslaCar
from .forms import TeslaForm


def index(request):
    items = TeslaCar.objects.all()
    context = {'items': items}
    template_name = 'index.html'
    return render(request, template_name, context)


# class CarCreateView(View):
#     form_tesla = TeslaForm()
#     template = 'partial_car_create.html'
# 	html_form = render_to_string(template, context, request=request)
#
#     def get(self, request):
#         form = self.form_tesla()
#         return render(request, self.template, {'form': form})
#
#     def post(self, request):
# 		form = self.form_tesla(request.POST)
# 		if form.is_valid():
# 			pass
# 		form.save()
# 		return redirect('/')
#         return JsonResponse()

def car_create(request):
    form = TeslaForm()
    context = {'form': form}
    html_form = render_to_string('book/partial_car_create.html', context, request=request)
    return JsonResponse({'html_form': html_form})
