from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_geonil, name="show_geonil"),
]