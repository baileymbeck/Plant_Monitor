from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home f(x) to handle traffic from the homepage
def home(request):
    # return HttpResponse('<h1> Humidity Home</h1>')
    return render(request, 'humidity_sensor/home.html')