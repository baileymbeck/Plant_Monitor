from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# Home f(x) to handle traffic from the homepage
def home(request):
    # return HttpResponse('<h1> Notes Home</h1>')
    return render(request, 'notes/home.html')

def about(request):
    # return HttpResponse('<h1>Notes About</h1>')
    return render(request, 'notes/about.html')