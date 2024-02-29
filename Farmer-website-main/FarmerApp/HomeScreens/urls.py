from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/',aboutus),
    path('blogs/',blogs),
    path('contactus/',contactus),
    path('testimonials/',testimonial),
]
