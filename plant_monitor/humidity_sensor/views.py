from django.shortcuts import render

# Create your views here.

# Home f(x) to handle traffic from the homepage
def home(request):
    return HttpResponse('<h1> Humidity Home</h1>')
