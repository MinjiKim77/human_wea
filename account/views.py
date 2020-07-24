from django.http import HttpResponse, HttpResponseRedirect, Http404, request, JsonResponse
from django.shortcuts import render
from .models import *
from django.forms.models import model_to_dict
import requests

# from django.urls import reverse
# from django.template import loader

# home.html로 전송(유효한 코드인지 모름)
def home(request):
    return render(request, 'nalsiwoori/home.html')
# 로그인 렌더링
def login(request):
    return render(request, 'account/login.html')

# 로그인값 확인
def login_function(request):
    count = 0
    login_id = request.POST.get('login_id')
    login_pw = request.POST.get('login_pw')
    user_all = User.objects.all()
   
    # print(user_all)
    for i in range(len(user_all)):
        if user_all[i].user_id == login_id:
            if user_all[i].user_pw == login_pw:
                # user_all[i]가 dict이 아니기 때문에 model_to_dict 명령어로 강제로 dic형변환
                request.session['user'] = model_to_dict(user_all[i])
                obj = request.session['user']
                return JsonResponse(obj) # 로그인성공
            else:
                return HttpResponse('1') ##비밀번호 다시입력
            count = 1
    if count == 0:
        return HttpResponse('2') ## 아이디 다시입력

def signup(request):
    return render(request, 'account/signup.html')

def signup_function(request) :
    signup_nick = request.POST.get('signup_nick')
    signup_name = request.POST.get('signup_name')
    signup_email = request.POST.get('signup_email')
    signup_id = request.POST.get('signup_id')
    signup_pw = request.POST.get('signup_pw')
    user_all = User.objects.all()
    for i in range(len(user_all)):
        if (user_all[i].user_id == signup_id)&(user_all[i].email == signup_email):
            return HttpResponse('1')
    
    newbie = User(
        nick = signup_nick,
        name = signup_name,
        email = signup_email,
        user_id = signup_id,
        user_pw = signup_pw,)
    newbie.save()
    return HttpResponse('0')

def find_id(request):
    return render(request, 'account/find_id.html')

def find_pw(request):
    return render(request, 'account/find_pw.html')

# session값 클리어 후, 로그아웃_구현중

def find_id_function(request):
    find_id_name = request.POST.get('find_id_name')
    find_id_email = request.POST.get('find_id_email')
    # 해당 데이터만 조회
    try:
        user = User.objects.get(name=find_id_name, email=find_id_email)
        return JsonResponse(model_to_dict(user), safe=False)
    except:
        return JsonResponse({'result':'fail'}, safe=False)

def find_pw_function(request):
    find_pw_id = request.POST.get('find_pw_id')
    find_pw_email = request.POST.get('find_pw_email')
    # 해당 데이터만 조회
    try:
        user = User.objects.get(user_id=find_pw_id, email=find_pw_email)
        return JsonResponse(model_to_dict(user), safe=False)
    except:
        return JsonResponse({'result':'fail'}, safe=False)

def logout(request):
    request.session.clear()
    return render(request, 'account/login.html')