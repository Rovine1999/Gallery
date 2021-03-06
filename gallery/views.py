from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location,Category

# Create your views here.
def gallery(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'gallery.html', {"date": date,"images":images})


    
def search_location(request):
    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get("location")
        searched_images = Image.filter_by_location(location)
        message = f"{location}"
        print("Image.......",searched_images)
        return render(request, 'location.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image"
        return render(request, 'location.html', {"message": message})
