import math
import random
import string
from builtins import int

from django.http import HttpResponse
from django.shortcuts import render
import pymysql
import json
import datetime
from moudles import getdata,db
# 列表页面函数
def list(request):
    return render(request,"article/list.html")
# 详情页面函数
def details(request):
    return render(request,"article/details.html")
# 写博客页面函数
def write(request):
    return render(request,"article/write.html")
def writeid(request):
    id = request.GET["id"]
    sql = "SELECT username FROM blog_user WHERE id=%s"
    data = id
    result = db.link.selectPart(sql, 0, data)
    return HttpResponse(getdata.dic(0, "", result))
# 列表与数据库连接函数
def listhttp(request):
    id=request.GET["id"]
    page=request.GET["page"]

    # 查找文章列表的表
    sql = "SELECT * FROM blog_article WHERE uid=%s"
    data = id
    count=db.link.selectPart(sql,2,data)#总条数
    pagerows=3#每页的条数
    offset=(int(page)-1)*pagerows
    print("page", page,"offset",offset)
    pages=math.ceil(count/pagerows)#总共多少页
    sql = "SELECT * FROM blog_article WHERE uid=%s LIMIT %s,%s"
    data = (id,offset,pagerows)
    result = db.link.selectPart(sql,1, data)
    # 如果当前用户写了文章
    if result:
        li = []
        for item in result:
            time=item["writetime"]
            time=time.strftime("%Y-%m-%d %H:%M:%S")
            dic={
                "code":0,
                "title":item["title"],
                'author':item["author"],
                'time': time,
                "id":item["id"],
            }
            li.append(dic)
        return HttpResponse(getdata.dic(0,"",{"content":li,"count":pages}))
    else:
        return HttpResponse(getdata.dic(0, "", ''))
# 填写博客页面与数据库连接的函数
def writehttp(request):
    articletitle = request.POST.get('articletitle')
    articleauthor = request.POST.get('articleauthor')
    articlecontent = request.POST.get('articlecontent')
    userid = request.POST.get('userid')
    # 插入信息
    time = datetime.datetime.now()
    data = (articletitle, articleauthor, time, userid)
    sql = 'INSERT INTO blog_article(title,author,writetime,uid) values (%s,%s,%s,%s)'
    result = db.link.insertPart(sql, data,1)
    articleid=result
    # 插入信息到blog_articlecontent中
    data2 = (articleid, articlecontent)
    sql = 'INSERT INTO blog_articlecontent(aid,content) values (%s,%s)'
    db.link.insertPart(sql, data2)
    db.link.commit()
    return HttpResponse(articleid)
# 文章详情页面与数据库连接函数
def articlehttp(request):
    id=request.GET["id"]
    sql = "SELECT content FROM blog_articlecontent WHERE aid=%s"
    data = id
    result = db.link.selectPart(sql, 0, data)
    if result:
        return HttpResponse(getdata.dic(0, "", result["content"]))
    else:
        return HttpResponse(getdata.dic(1, "", ""))





