from django.shortcuts import render
from django.views import generic

from .models import SlideShow, Team, Event, Gallery

# Create your views here.

def home(request):
    return render(request,'Menus/Home.html')

def about(request):
    return render(request,'Menus/About.html')

def team(request):
    card = Team.objects.all()
    return render(request,'Menus/Team.html',{'card':card})

def events(request):
    event = Event.objects.all()
    return render(request,'Menus/Events.html',{'event':event})

def gallery(request):
    images = Gallery.objects.all()
    return render(request,'Menus/Gallery.html',{'images':images})

def contact(request):
    return render(request,'Menus/Contact.html')



# <nav>
#         <ul class="menu">
#             <li class="logo"><a href="https://www.pes.edu/" target="_blank"><img src="{% static 'Menus/Images/PES.png' %}" class="PES"> </a></li>
#             <li class="logo"><a href=""><img src="{% static 'Menus/Images/Rotaract.jpg' %}" class="Rotaract"> </a></li>
#             <li class="item button">{% block nav-home %}<a href="{% url 'Menus:home' %}">Home</a>{% endblock %}</li>
#             <li class="item button">{% block nav-about %}<a href="{% url 'Menus:about' %}">About</a>{% endblock %}</li>
#             <li class="item">{% block nav-team %}<a href="{% url 'Menus:team' %}">Our Team</a>{% endblock %}</li>
#             <li class="item events">{% block nav-events %}<a href="{% url 'Menus:events' %}">Events</a>{% endblock %}</li>
#             <li class="item">{% block nav-gallery %}<a href="{% url 'Menus:gallery' %}">Gallery</a>{% endblock %}</li>
#             <li class="item">{% block nav-contact %}<a href="{% url 'Menus:contact' %}">Contact</a>{% endblock %}</li>
#             <li class="toggle"><span class="bars"></span></li>
#         </ul>
#     </nav>