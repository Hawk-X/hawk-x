from django.conf.urls import url

# Local views shop
from . import views
# from .views import CarCreateView

urlpatterns = [
    url(r'^shop/$', views.index, name='index'),
    url(r'^shop/create/$', views.car_create, name='car_create'),
]
