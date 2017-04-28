from django.conf.urls import url

# Local views shop
from . import views


urlpatterns = [
	url(r'^shop/', views.index, name='index'),
]