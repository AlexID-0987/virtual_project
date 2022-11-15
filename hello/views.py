from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def son(request):
    return HttpResponse('<h1>hello me son!!!</h1>')

def greet(request, name):
    return render(request, 'hello/greet.html',{
        'name':name.capitalize()
    })