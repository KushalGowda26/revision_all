from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'first.html')

def two(request):
    return render(request, 'second.html')