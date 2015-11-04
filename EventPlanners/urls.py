from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.caterers_list, name='caterers_list'),
]

