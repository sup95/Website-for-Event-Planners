from django.shortcuts import render
from .models import Caterers
from .models import Photographers
from .models import Entertainment


def frontpage(request):
    return render(request, 'EventPlanners/frontpage.html', {})


def caterers_list(request):
    cats = Caterers.objects.all()
    return render(request, 'EventPlanners/caterers_list.html', {'cats': cats})


def photographers_list(request):
    photos = Photographers.objects.all()
    return render(request, 'EventPlanners/photographers_list.html', {'photos': photos})


def entertainers_list(request):
    entertain = Entertainment.objects.all()
    return render(request, 'EventPlanners/entertainers_list.html', {'entertain': entertain})

