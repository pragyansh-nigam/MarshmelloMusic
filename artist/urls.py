from django.urls import path

from . import views

urlpatterns = [
    			path("home", views.home),
    			path("bio", views.bio),
    			path("gallery", views.gallery),
    			path("music", views.music),
    			path("spotify", views.spotify),
    			path("videos", views.videos),
    			path("tour", views.tour),
    			path("booking", views.booking),
    			path("contact", views.contact)
              ]