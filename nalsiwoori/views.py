from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request, 'nalsiwoori/home.html')

def login(request):
    if request.method == 'POST':
        user_email= request.POST.get('user_email')
        user_pw = request.POST.get('user_pw')

        res_data={}
        if not (user_email and user_pw):
            res_data['error'] ="모든 칸을 다 입력해주세요"
        else:
            user = user.objects.get(user_email=user_email)
            if check_password(user_pw, user_pw):
                user_pw = request.POST.get('user_pw')
                request.session['user_email'] ='user_email'
                return HttpResponseRedirect("/home/")
            else:
                res_data['error'] ="아이디나 비밀번호가 틀렸습니다. "

        return render(request, 'nalsiwoori/login.html')
    #     request.session ['user_email']='user_email'
    #     return HttpResponseRedirect("/home/")
    return render(request, 'nalsiwoori/login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST.get('user_pw1') == request.POST.get('user_pw2'):
            user_nick = request.POST.get("user_nick")
            user_email = request.POST.get("user_email")
            user_name = request.POST.get("user_name")
            user_pw = request.POST.get("user_pw1")

            # 1
            u = Users.objects.filter(Q(user_email=user_email) | Q(user_nick=user_nick))            
            if u: # 가입되어 있는 경우
                return HttpResponse('이미 가입되어 있습니다.')

        else :
            return HttpResponse("비밀번호가 다름")

        # 2

        user = Users()
        user.user_email = user_email
        user.user_pw = user_pw
        user.user_nick = user_nick
        user.user_name = user_name    
        
        user.save()
        return render(request, 'nalsiwoori/login.html')
    else :
        pass


def logout(request):

    return render(request, 'nalsiwoori/logout.html')


def change_pw(request):
    context= {}
    if request.method == "POST":
        new_password = request.POST.get("password1")
        password_confirm = request.POST.get("password2")
        if new_password == password_confirm:
            user.set_password(new_password)
            user.save()
            return HttpResponseRedirect("/home/")
        else:
            context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "nalsiwoori/changepw.html",context)

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