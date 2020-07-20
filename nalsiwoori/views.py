from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    return render(request, 'nalsiwoori/home.html')
    
def login(request):
    user_id = request.POST.get('user_id')
    user_pwd = request.POST.get('user_pwd')
    print(user_id,user_pwd)
    request.session['user_id'] = user_id
    return render(request, 'nalsiwoori/login.html')

def logout(request):
    pass
def course(request):
    return render(request, 'nalsiwoori/course.html')

def home(request):
    # sel_list = Selection.objects.order_by('-pub_date')[:5]
    sel_list = Selection.objects.all()
    html = ''

    for s in sel_list:
        html += s.state + '<br>'
    return render(request, 'nalsiwoori/home.html', {'list': sel_list})
    # return HttpResponse(html)