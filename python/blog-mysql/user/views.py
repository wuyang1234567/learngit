import datetime
import os
import random
import string
from django.shortcuts import render
from django.http import HttpResponse
import json
from moudles import getdata,db
import pymysql

# 登陆页面的函数
def register(request):
    return render(request,"user/register.html")

def httpregister(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    time=datetime.datetime.now()
    # 判断blog_user表是否存在此用户名
    sql = "SELECT * FROM blog_user WHERE username=%s"
    data = username
    result=db.link.selectPart(sql,0,data)
    if result:
        return HttpResponse(getdata.dic(0,"该用户名已存在，请登录"))
    else:
        # 判断是否填写了邮箱
        uservalue = 'username,password,datetime'
        value = '%s, %s, %s'
        da = (username,password,time)
        if email:
            uservalue+=',email'
            value+=',%s'
            da= (username,password,time,email)
        sql = 'INSERT INTO blog_user(' + uservalue + ') values (' + value + ')'
        data=da
        result=db.link.insertPart(sql,data)
        db.link.conn.commit()
        return HttpResponse(result)

# 登录页面函数
def login(request):
    return render(request,"user/login.html")
# 登录时与数据库连接的函数
def httplogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    sql = "SELECT username,password,id FROM blog_user WHERE username=%s"
    data = username
    result = db.link.selectPart(sql,0, data)
    print(result)
    # 如果用户名存在
    if result:
        if result["password"]==password:
            return HttpResponse(getdata.dic(0,"登录成功",result["id"]))
        else:
            return HttpResponse(getdata.dic(1, "密码不正确"))
    else:
        return HttpResponse(getdata.dic(0, "用户名不存在"))
