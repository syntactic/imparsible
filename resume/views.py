#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"content" : "Hello World!"}
    return render(request, "resume/index.html", context)
