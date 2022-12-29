from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1 align="center">This page is created using string</h1>')

def second(request):
    return HttpResponse('<h1 align="center">This page is created using same application</h1>')