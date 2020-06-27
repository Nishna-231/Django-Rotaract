from django.urls import path
from . import views

app_name='Menus'

urlpatterns = [
    path('',views.home,name='home'),
    path('About/',views.about,name='about'),
    path('Our_Team/',views.team,name='team'),
    path('Events/',views.events,name='events'),
    path('Gallery/',views.gallery,name='gallery'),
    path('Contact/',views.contact,name='contact'),
]