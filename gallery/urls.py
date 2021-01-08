from . import views
from django.urls import path

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('search/location', views.search_location, name = 'search_location')
]