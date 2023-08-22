from django.contrib import admin
from django.urls import path
from . import views

#django admin header customization

admin.site.site_header = "Login to Indu"
admin.site.site_title = "welcome to Indu's Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('',views.index,name="index"),
    #path('about/',views.about,name="about"),
    path('projects/',views.projects,name="projects"),
    path('contact/',views.contact,name="contact"),
]

