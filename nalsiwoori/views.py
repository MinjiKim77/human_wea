from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    return render(request, 'nalsiwoori/home.html')
    
from django.shortcuts import render
from .models import Users


def register(request):
    user_nick = request.POST['user_nick']
    user_email = request.POST['user_email']
    user_name = request.POST['user_name']
    user_pw = request.POST['user_pw']
    #re_password = request.POST['re-password']
    user = Users(
        user_email = user_email,
        user_pw = user_pw,
        user_nick = user_nick,
        user_name = user_name    
    )
    user.save()
    return render(request, 'login.html')

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