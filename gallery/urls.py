from . import views
from django.urls import include, path

urlpatterns = [
    path('^$', views.gallery, name = 'gallery'),
    path('gallery/', include('gallery.urls')),
    path('search/location', views.search_location, name = 'search_location')
]