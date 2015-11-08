from django.contrib import admin
from .models import Caterers
from .models import Photographers
from .models import Entertainment
from .models import Themes

admin.site.register(Caterers)
admin.site.register(Photographers)
admin.site.register(Entertainment)
admin.site.register(Themes)
