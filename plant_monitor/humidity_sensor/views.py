from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

#dummy data

humidity_data = [
    {
        'Humidity': '10%',
        'Temperature': '68 F',
        'date': 'February 19, 2020',
        'time': '21:21:21',  
    },
    {
        'Humidity': '12%',
        'Temperature': '70 F',
        'date': 'February 19, 2020',
        'time': '22:22:22',  
    }
]

# Home f(x) to handle traffic from the homepage
def home(request):
    context = {
        'humidity_data': humidity_data
    }
    # return HttpResponse('<h1> Humidity Home</h1>')
    return render(request, 'humidity_sensor/home.html', context)