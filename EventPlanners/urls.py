from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.frontpage, name='frontpage'),
    url(r'^caterers_list.html$', views.caterers_list, name='caterers_list'),
    url(r'^photographers_list.html$', views.photographers_list, name='photographers_list'),
    url(r'^entertainers_list.html$', views.entertainers_list, name='entertainers_list'),
]


