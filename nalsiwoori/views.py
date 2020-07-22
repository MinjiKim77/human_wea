from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.forms.models import model_to_dict


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

def weather(request):
    si = request.GET.get('si')
    gu = request.GET.get('gu')
    
    if si and gu:
        sel_list = Selection.objects.filter(state=si, city=gu).order_by('-pub_date')[:20]
    else:
        sel_list = Selection.objects.order_by('-pub_date')[:20]
    # sel_list = Selection.objects.all()
    html = ''

    for s in sel_list:
        html += s.state + '<br>'
    return render(request, 'nalsiwoori/weather.html',{'list': sel_list})
    
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

    sel = Selection(map_idx=0, map_data_id=1,user_data_id=1,state=state, city=city, cur_wea=cur_wea, pub_date=timezone.now())
    sel.save()
    # dict1 = {'result':'입력성공','data':state}
    return HttpResponse(state)

def sel_wea(request):
    # state = request.GET.get('state1')
    # city = request.GET.get('city1')
    # state = request.GET.get('si')
    # city = request.GET.get('gu')

    
    # request.session['wea']['si']=si
    # request.session['wea']['gu']=gu
    
    # dict1 = {'result':'입력성공','data':state}
    # return render(request, 'nalsiwoori/weather.html',{'state':state, 'city'})
    state = request.GET.get('si')
    city = request.GET.get('gu')
   

    # return render(request,{"state":state,"city":city} )
    return render(request, [state, city] )

def load_map_db(request):
    map_datas = map_data.objects.all()
    json_data = []
    for data in map_datas:
        json_data.append(model_to_dict(data))
    return JsonResponse(json_data, safe=False)
    
def zzzz(request):
    return 
