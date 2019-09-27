from datetime import datetime
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
# Create your views here.
from polls.models import *
def show_class(request):
    # class_list = user.objects.all().order_by('id')
    # newarticle = user(usernames="张三", passwords="123456",emails="123456", times=datetime.now())
    # newarticle.save()
    # obj=user.objects.all()
    # print(obj)
    # for item in obj:
    #     print(item.usernames)
    #     print(item.passwords)
    # list=user.objects.values("usernames","passwords").get(id=2)
    # print(list)
    # user.objects.filter(id=2).delete()
    # user.objects.filter(usernames="张三").update(usernames="李四")
    # obj=user.objects.get(id=1)
    # obj.c1='111'
    # obj.save()
    # obj=user.objects.filter(usernames="李四").count()
    obj=user.objects.values("usernames","id").filter(id__gt=1)
    print(obj)
    for item in obj:
        print(item['usernames'])
    # obj=user.objects.filter(id__lt=10)
    # obj=user.objects.filter(id__lte=10)
    # obj=user.objects.filter(id__lt=10,id__gt=1)
    # obj=user.objects.filter(id__in=[3,4])
    # obj=user.objects.filter(usernames__contains="李四")
    # obj=user.objects.exclude(id__in=[3,4])
    # obj=user.objects.filter(usernames__icontains="李四")
    # obj=user.objects.exclude(usernames="张三")
    # obj=user.objects.filter(id__range=[1,5])
    # obj = user.objects.filter(usernames__startswith="李四")
    # obj=user.objects.filter(usernames="张三").order_by('id')
    # obj=user.objects.filter(usernames="李四").order_by('-id')
    # print(obj)
    # for item in obj:
    #     print(item.usernames,item.id)

    return render(request,'index.html')
def login(request):
    # u=request.POST.get("name")
    response = HttpResponse('test')
    newuser="王佳利"
    newuser=json.dumps(newuser)
    # newuser = username.encode('utf-8').decode('latin-1')
    response.set_cookie('uname', newuser,max_age=60*60*24*7)
    request.session['key'] = "1234567890"
    # del request.session['key']
    # request.session.delete()
    # request.session.flush()
    # print(request.session['key'])
    # userna = request.COOKIES['uname'].encode('latin-1').decode('utf-8')
    # print(userna)
    # response.set_cookie('name','王',max_age=60*60*24*7)
    return response
    # v=request.COOKIES.get("username")
    # print(v)
    # if not v:
    #     return redirect("/polls")
    # return render(request,'index.html',{"curr_name":v})
    # response = HttpResponse('ok')
    # response.delete_cookie('username')
    # request.session['key'] = "123456"
    # obj=request.session['key']
    # print(obj)

