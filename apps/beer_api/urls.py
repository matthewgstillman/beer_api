from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^datasets$', views.datasets, name="datasets"),
    url(r'^stores$', views.stores, name="stores"),
]