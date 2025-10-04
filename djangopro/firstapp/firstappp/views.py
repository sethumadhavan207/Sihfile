from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    msg = "<h1>Welcome to Django my friend</h1>"
    return HttpResponse(msg)
