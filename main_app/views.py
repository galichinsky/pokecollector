from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome to the Pokecollector App!</h1>') 

# Define the about view
def about(request):
    return HttpResponse('<h1>About the Pokecollector App</h1>')