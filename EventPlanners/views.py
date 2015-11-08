from django.shortcuts import render
from .models import Caterers
from .models import Photographers
from .models import Entertainment
from .models import Themes


def frontpage(request):
    return render(request, 'EventPlanners/frontpage.html', {})


def caterers_list(request):
    cats = Caterers.objects.all()
    return render(request, 'EventPlanners/caterers_list.html', {'cats': cats})


def caterers_indian(request):
    cats_i = Caterers.objects.filter(cuisine='Indian')
    return render(request, 'EventPlanners/caterers_indian.html', {'cats_i': cats_i})


def caterers_continental(request):
    cats_c = Caterers.objects.filter(cuisine='Continental')
    return render(request, 'EventPlanners/caterers_continental.html', {'cats_c': cats_c})


def caterers_mexican(request):
    cats_m = Caterers.objects.filter(cuisine='Mexican')
    return render(request, 'EventPlanners/caterers_mexican.html', {'cats_m': cats_m})


def caterers_italian(request):
    cats_it = Caterers.objects.filter(cuisine='Italian')
    return render(request, 'EventPlanners/caterers_italian.html', {'cats_it': cats_it})

def caterers_chinese(request):
    cats_c = Caterers.objects.filter(cuisine='Chinese')
    return render(request, 'EventPlanners/caterers_chinese.html', {'cats_c': cats_c})


def photographers_list(request):
    photos = Photographers.objects.all()
    return render(request, 'EventPlanners/photographers_list.html', {'photos': photos})


def entertainers_list(request):
    entertain = Entertainment.objects.all()
    return render(request, 'EventPlanners/entertainers_list.html', {'entertain': entertain})


def themes_list(request):
    themes = Themes.objects.all()
    return render(request, 'EventPlanners/themes_list.html', {'themes': themes})

