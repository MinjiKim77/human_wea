from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'nalsiwoori/index.html')
    
def login(request):
    return render(request, 'nalsiwoori/login.html')

def logout(request):
    pass
