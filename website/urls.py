from django.urls import path
from . import views 
urlpatterns = [
	path('', views.home, name = "home"),
	path('contact.html', views.contact, name = "contact"),
	path('service.html', views.service, name = "service"),
    path('about.html', views.about, name = "about"),
    path('appointment.html', views.appointment, name = "appointment"),
    path('book.html', views.book, name = "book"),
]
