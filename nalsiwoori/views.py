from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password

# def index(request):
#     return render(request, 'nalsiwoori/home.html')

def weather(request):
    si = request.GET.get('si')
    gu = request.GET.get('gu')
    
    if si and gu:
        sel_list = Selection.objects.filter(state=si, city=gu).order_by('-pub_date')[:20]
    else:
        sel_list = Selection.objects.order_by('-pub_date')[:20]
    # sel_list = Selection.obㄴjects.all()
    html = ''
    for s in sel_list:
        html += s.state + '<br>'
    return render(request, 'nalsiwoori/weather.html',{'list': sel_list})
    
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