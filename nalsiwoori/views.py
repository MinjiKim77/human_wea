from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'nalsiwoori/index.html')
    
def login(request):
    user_id = request.POST.get('user_id')
    user_pw = request.POST.get('user_pwd')
    print(user_id,user_pwd)
    request.session['user_id'] = user_id
    return HttpResponse("로그인완료")
    return render(request, 'nalsiwoori/login.html')

def logout(request):
    pass
