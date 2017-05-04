from django.conf.urls import url

# Local views shop
from . import views
from .views import IndexView

urlpatterns = [
    url(r'^shop/$', IndexView.as_view(), name='index'),
    # url(r'^(?P<id>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^shop/create/$', views.car_create, name='car_create'),
]
