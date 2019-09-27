from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
def index(request):
    tem=loader.get_template("mydjango/base.html")
    context={

    }
    return HttpResponse(tem.render(context,request))
def loginbase(request):
    tem = loader.get_template("mydjango/loginedbase.html")
    context = {}
    return HttpResponse(tem.render(context, request))
def register(request):
    tem=loader.get_template("mydjango/register.html")
    context={}
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    if username!=''and password!='':
        tem = loader.get_template("mydjango/base.html")
    else:
        tem=loader.get_template("mydjango/register.html")
    return HttpResponse(tem.render(context, request))
def login(request):
    tem=loader.get_template("mydjango/login.html")
    context={}
    username=request.POST.get('username','')
    password=request.POST.get('password','')

    if username=="张三" and password=="123":
        context = {
            'username': username,
            "password": password,

        }
        tem = loader.get_template("mydjango/loginedbase.html")
    else:
        tem = loader.get_template("mydjango/login.html")
    return HttpResponse(tem.render(context, request))
def writeblog(request):
    tem = loader.get_template("mydjango/writeblog.html")
    context = {}
    title = request.POST.get('article-title', '')
    author = request.POST.get('article-author', '')
    time = request.POST.get('article-time', '')
    content = request.POST.get('article-content', '')
    if title!="" and author!="" and time!="" and content!='':
        context = {
            'title': title,
            "author": author,
            "time": time,
            "content":content
        }
        tem = loader.get_template("mydjango/list.html")
    return HttpResponse(tem.render(context, request))
def list(request):
    tem = loader.get_template("mydjango/list.html")
    context = {}
    return HttpResponse(tem.render(context, request))
def details(request):
    tem = loader.get_template("mydjango/details.html")
    context = {}
    return HttpResponse(tem.render(context, request))