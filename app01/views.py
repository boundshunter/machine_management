from django.shortcuts import render, redirect, HttpResponse
from app01 import models
# Create your views here.


def login(request):
    print(request.method)
    u = request.POST.get('user')
    p = request.POST.get('pwd')
    user = models.User.objects.all().values().filter(username=u)
    pwd = models.User.objects.all().values().filter(password=p).filter(username=u)
    # user = models.User.objects.filter(username='admin').values().filter()
    err_msg = ""
    if request.method == 'POST':
        if user and pwd:
            return redirect('/mac_list')
        else:
            print(user, pwd)
            err_msg = '用户名或密码错误'
    print(err_msg)
    return render(request, 'login.html', {'error_msg': err_msg})


def mac_list(request):
    return HttpResponse("mac_list")