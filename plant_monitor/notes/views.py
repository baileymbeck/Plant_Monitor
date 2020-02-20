from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# dummy data

posts = [
    {
        'author': 'Bailey',
        'title': 'Notes post 1',
        'content': 'first note content',
        'date_posted': 'February 19, 2020'
    },
    {
        'author': 'Sean',
        'title': 'Notes post 2',
        'content': 'second note content',
        'date_posted': 'February 20, 2020'
    }
]

# Home f(x) to handle traffic from the homepage


def home(request):
    context = {
        'posts': posts
    }
    # return HttpResponse('<h1> Notes Home</h1>')
    return render(request, 'notes/home.html', context)


def about(request):
    # return HttpResponse('<h1>Notes About</h1>')
    return render(request, 'notes/about.html', {'title': 'About'})
