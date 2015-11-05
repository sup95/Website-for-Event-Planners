from django.shortcuts import render
from .models import Caterers


def frontpage(request):
    return render(request, 'EventPlanners/frontpage.html', {})


def caterers_list(request):
    cats = Caterers.objects.all()
    return render(request, 'EventPlanners/caterers_list.html', {'cats': cats})

