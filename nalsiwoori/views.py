from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.utils import timezone

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
    sel_list = Selection.objects.order_by('-pub_date')[:5]
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
//
    return JsonResponse({'result':'날씨가 입력되었습니다.'})
    # return HttpResponse(html)