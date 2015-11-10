from django.shortcuts import render
from .models import Caterers
from .models import Photographers
from .models import Entertainment
from .models import Themes
from .models import Venue


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


def entertainers_dj(request):
    entertain_dj = Entertainment.objects.filter(entertainers_type = 'DJ')
    return render(request, 'EventPlanners/entertainers_dj.html', {'entertain_dj': entertain_dj})


def entertainers_musicians(request):
    entertain_m = Entertainment.objects.filter(entertainers_type = 'Music')
    return render(request, 'EventPlanners/entertainers_musicians.html', {'entertain_m': entertain_m})


def entertainers_dance(request):
    entertain_d = Entertainment.objects.filter(entertainers_type = 'Dance')
    return render(request, 'EventPlanners/entertainers_dance.html', {'entertain_d': entertain_d})


def entertainers_comedians(request):
    entertain_c = Entertainment.objects.filter(entertainers_type = 'Comedians')
    return render(request, 'EventPlanners/entertainers_comedians.html', {'entertain_c': entertain_c})


def themes_list(request):
    themes = Themes.objects.all()
    return render(request, 'EventPlanners/themes_list.html', {'themes': themes})


def themes_birthday(request):
    themes_b = Themes.objects.filter(theme_type='Birthday Party')
    return render(request, 'EventPlanners/themes_birthday.html', {'themes_b': themes_b})


def themes_corporate_event(request):
    themes_ce = Themes.objects.filter(theme_type='Corporate Event')
    return render(request, 'EventPlanners/themes_corporate_event.html', {'themes_ce': themes_ce})


def themes_wedding(request):
    themes_w = Themes.objects.filter(theme_type='Wedding')
    return render(request, 'EventPlanners/themes_wedding.html', {'themes_w': themes_w})


def themes_get_together(request):
    themes_g = Themes.objects.filter(theme_type='Get Together')
    return render(request, 'EventPlanners/themes_get_together.html', {'themes_g': themes_g})


def venues_list(request):
    venues = Venue.objects.all()
    return render(request, 'EventPlanners/venues_list.html', {'venues': venues})


