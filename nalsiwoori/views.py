from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.db.models import Q
from django.forms.models import model_to_dict
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

    md = map_data.objects.get(state=state, city=city)

    sel = Selection(map_idx=0, map_data=md, user_data_id=1, state=state, city=city, cur_wea=cur_wea, pub_date=timezone.now())
    sel.save()

    return JsonResponse({'result':'날씨가 입력되었습니다.'})
    # return HttpResponse(html)

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
        obj = model_to_dict(data)
        try:
            # cur_wea = data.selection_set.all().order_by('-pub_date')[:1][0].cur_wea
            cur_wea = data.selection_set.all().order_by('-pub_date')[:][0].cur_wea
        except:
            cur_wea = ''

        obj['cur_wea'] = cur_wea
        
        if cur_wea == "맑음":
            obj['icon'] = "sunny"
        elif cur_wea == "흐림":
            obj['icon'] = "cloud"
        elif cur_wea == "비":
            obj['icon'] = "rain"
        elif cur_wea == "눈":
            obj['icon'] = "snow"
        elif cur_wea == "천둥":
            obj['icon'] = "thunder"
        elif cur_wea == "우박":
            obj['icon'] = "hail"

        
        # print(obj)
        # print(obj.city, cur_wea)
        json_data.append(obj)

    return JsonResponse(json_data, safe=False)


def load_sel_db(request):
    # sel_datas = Selection.objects.all().select_related('map_data').values_list('state','city','map_data_id__lat','map_data_id__lng')
    # temp = map_data.objects.all()  # map_data 모두 조회
    # sel_datas = []
    # for data in temp:
    #     selections = data.selection_set.order_by('-pub_date')
    #     if selections:
    #         sel = data.selection_set.order_by('-pub_date')[:1][0]
    #         obj = model_to_dict(data)
    #         obj['cur_wea'] = sel.cur_wea
    #         sel_datas.append(obj)

    temp = Selection.objects.all().select_related('map_data')
    sel_datas = []
    for data in temp:
        obj = model_to_dict(data)
        obj['lat'] = data.map_data.lat
        obj['lng'] = data.map_data.lng
        sel_datas.append(obj)
        # print(obj)

    return JsonResponse(sel_datas, safe=False)