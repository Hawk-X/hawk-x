from django.conf.urls import url

# Local views prox
from .views import HomeView, ContactFormView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/$', ContactFormView.as_view(), name='contact'),
]
