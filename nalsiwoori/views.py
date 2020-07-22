from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request, 'nalsiwoori/home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        password = request.POST.get('user_pw1')
        user = auth.authenticate(request, email=email , password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/home/")
        else:
            return render(request, 'nalsiwoori/login.html',{'이메일이나 비밀번호가 맞지 않습니다'})
    else:
        return render(request, 'nalsiwoori/login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST.get('user_pw1') == request.POST.get('user_pw2'):
            user = User.objects.create_user(
                username = request.POST.get('user_name'),
                usernick = request.POST.get('user_nick'),
                email =request.POST.get('user_email'),
                password= request.POST.get('user_pw1')
            )
            auth.login(request,user)
            return render(request, 'nalsiwoori/login.html')
        return HttpResponse( '가입완료')    
    return render(request, 'nalsiwoori/login.html') 
       


def logout(request):
    return render(request, 'nalsiwoori/logout.html')

def course(request):
    return render(request, 'nalsiwoori/course.html')

def home(request):
    sel_list = Selection.objects.order_by('-pub_date')[:10]
    # sel_list = Selection.objects.all()
    html = ''

    for s in sel_list:
        html += s.state + '<br>'
    return render(request, 'nalsiwoori/home.html', {'list': sel_list})
    # return HttpResponse(html)

def log_wea(request):
    state = request.GET.get('state1')
    city = request.GET.get('city1')
    cur_wea = request.GET.get('cur_wea')

    sel = Selection(state=state, city=city, street='', cur_wea=cur_wea, pub_date=timezone.now())
    sel.save()

    return JsonResponse({'result':'날씨가 입력되었습니다.'})
    # return HttpResponse(html)