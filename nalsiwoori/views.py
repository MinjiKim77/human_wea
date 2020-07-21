from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.utils import timezone


def index(request):
    return render(request, 'nalsiwoori/home.html')

def login(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_pw = request.POST.get('user_pw')
        request.session ['user_email']='user_email'
        return HttpResponseRedirect("/home/")
    return render(request, 'nalsiwoori/login.html')


def signup(request):
    if request.method == 'POST':
        user_nick = request.POST.get('user_nick')
        user_email = request.POST.get('user_email')
        user_name = request.POST.get('user_name')
        user_pw = request.POST.get('user_pw')
    #re_password = request.POST['re-password']

        user = Users()
        user.user_email = user_email,
        user.user_pw = user_pw,
        user.user_nick = user_nick,
        user.user_name = user_name    
        
        user.save()
        return render(request, 'nalsiwoori/login.html')
    else :
        pass


def logout(request):
    pass

def course(request):
    return render(request, 'nalsiwoori/course.html')

def home(request):
    sel_list = Selection.objects.order_by('-pub_date')[:20]
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
def zzzz(request):
    return 