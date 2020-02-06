from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='notes-home'),
    path('about/', views.about, name='notes-about'),
]