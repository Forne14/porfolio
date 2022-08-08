from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home/index_files/index.html')

def about(request):
    return HttpResponse('<p>about me</p>')
