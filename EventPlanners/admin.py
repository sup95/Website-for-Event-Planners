from django.contrib import admin
from .models import Caterers
from .models import Photographers
from .models import Entertainment
from .models import Themes
from .models import Venue
from .models import Accomodations
from .models import Decorators

admin.site.register(Caterers)
admin.site.register(Photographers)
admin.site.register(Entertainment)
admin.site.register(Themes)
admin.site.register(Venue)
admin.site.register(Accomodations)
admin.site.register(Decorators)
