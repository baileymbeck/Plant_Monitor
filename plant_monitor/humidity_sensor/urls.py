from django.urls import path
from . import views

urlpatterns = [
    path('humidity/', views.home, name='humidity-home'),
]