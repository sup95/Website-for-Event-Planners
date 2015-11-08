from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.frontpage, name='frontpage'),
    url(r'^caterers_list.html$', views.caterers_list, name='caterers_list'),
    url(r'^caterers_indian.html$', views.caterers_indian, name='caterers_indian'),
    url(r'caterers_continental.html$', views.caterers_continental, name='caterers_continental'),
    url(r'caterers_mexican.html$', views.caterers_mexican, name='caterers_mexican'),
    url(r'^caterers_italian.html$', views.caterers_italian, name='caterers_italian'),
    url(r'^caterers_chinese.html$', views.caterers_chinese, name='caterers_chinese'),
    url(r'^photographers_list.html$', views.photographers_list, name='photographers_list'),
    url(r'^entertainers_list.html$', views.entertainers_list, name='entertainers_list'),
    url(r'^themes_list.html$', views.themes_list, name='themes_list'),
]


