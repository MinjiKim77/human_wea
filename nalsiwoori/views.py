from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    return render(request, 'nalsiwoori/index.html')
    
def login(request):
    return render(request, 'nalsiwoori/login.html')

def logout(request):
    pass

def board(request):
    sel_list = Selection.objects.order_by('pub_date')[:5]
    html = ''

    for s in sel_list:
        html += s.state + '<br>'
    return render(request, 'nalsiwoori/board.html', {'list': sel_list})
    # return HttpResponse(html)