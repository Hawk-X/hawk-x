from django.conf.urls import url

# Local views shop
from shop.views import IndexView, CreateCarView

urlpatterns = [
    url(r'^shop/$', IndexView.as_view(), name='index'),
    url(r'^shop/create/$', CreateCarView.as_view, name='car_create'),
    # url(r'^shop/(?P<slug>\d+)/$', DetailView.as_view, name='detail'),
]
