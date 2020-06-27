from django.contrib import admin
from .models import Team, Event, SlideShow, Gallery

# Register your models here.

admin.site.register(Team)
admin.site.register(Event)
admin.site.register(SlideShow)
admin.site.register(Gallery)