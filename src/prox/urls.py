from django.conf.urls import url

# Local views
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
]