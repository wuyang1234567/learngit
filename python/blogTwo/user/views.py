import datetime
import random
import string

from django.shortcuts import render
from django.http import HttpResponse
import json
import pymysql


def mysql():
    # conn = pymysql.Connect(
    #     host='localhost',  ##mysql服务器地址
    #     port=3306,  ##mysql服务器端口号
    #     user='root',  ##用户名
    #     passwd='Wjl123@321',  ##密码
    #     db='log',  ##数据库名
    #     charset='utf8'  ##连接编码
    # )
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # print(conn)
    # cursor = conn.cursor()
    # print(cursor)
    # sql="SELECT * FROM users"
    # cursor.execute(sql)
    # print(cursor.rowcount)
    # rs = cursor.fetchone()
    # print(rs)
    # re = cursor.fetchmany(3)
    # print(re)
    # rr = cursor.fetchall()
    # print(rr)
    # for row in rr:
    #     print(row['username'])

    # rr = cursor.fetchall()
    # print(rr)
    # sql_insert="INSERT INTO users(username,password) value (%s,%s)"
    # data = ("赵六","4444444444444")
    # # cursor.execute(sql_insert)
    # # conn.commit()users
    # try:
    #     print("成功了")
    #     # 执行sql语句
    #     cursor.execute(sql_insert,data)
    #
    #     # 提交到数据库执行
    #     conn.commit()
    #     rr = cursor.fetchall()
    #     print(rr)
    # except:
    #     # 发生错误时回滚
    #     conn.rollback()

    # conn.close()
    # cursor.close()

    # conn1=pymysql.Connect(
    #     host='localhost',  ##mysql服务器地址
    #     port=3306,  ##mysql服务器端口号
    #     user='root',  ##用户名
    #     passwd='wjl123',  ##密码
    #     db='blog',  ##数据库名
    #     charset='utf8'  ##连接编码
    # )
    #
    # cursor = conn1.cursor(cursor=pymysql.cursors.DictCursor)
    # sql = 'SELECT * FROM blog_user  '
    # cursor.execute(sql)
    # rr = cursor.fetchall()
    # print(rr)
    # for row in rr:
    #     # print(row)
    #     print("ID是：=%s, 姓名是：=%s, 密码是：=%s" % (row['id'],row['username'],row['password']))

    # sql_insert="INSERT INTO blog_user(username,password) value (%s,%s)"
    # data = ("赵六","4444444444444")
    # # cursor.execute(sql_insert)
    # # conn.commit()users
    #
    # try:
    #     print("成功了")
    #     # 执行sql语句
    #     cursor.execute(sql_insert,data)
    #
    #     # 提交到数据库执行
    #     conn1.commit()
    #     rr = cursor.fetchall()
    #     print(rr)
    # except:
    #     # 发生错误时回滚
    #     conn1.rollback()
    # for i in range(1, 101):
    #     # username = random.choice(['Lucy', 'Tom', 'Lily', 'Amy', 'Dave', 'Aaron', 'Baron']) + str(i)
    #     # password = '1' + str(random.choice([3, 5, 7, 8])) + str(random.random())[2:11]
    #     sql_insert="INSERT INTO blog_user(username,password) value (%s,%s)"
    #     data = ("赵六","4444444444444")
    #     # cursor.execute(sql_insert)
    #     cursor.execute(sql_insert, data)
    #     conn1.commit()  # 插入数据完后提交数据
    # sql='SELECT username,password FROM blog_user WHERE username="zhangsan"||username="lisi"'
    # cursor.execute(sql)
    # print(cursor.rowcount)
    # rr=cursor.fetchall()
    # print(rr)
    # sql='SELECT username,password FROM blog_user WHERE username="zhangsan"&&username="lisi"'
    # cursor.execute(sql)
    # print(cursor.rowcount)
    # sql='SELECT * FROM blog_user ORDER BY id DESC '
    # cursor.execute(sql)
    # print(cursor.fetchall())
    # sql="SELECT * FROM blog_user WHERE username like '%zhangsan%'"
    # cursor.execute(sql)
    # print(cursor.rowcount)
    # print(cursor.fetchall())
    # sql="INSERT INTO blog_user(username,password) values (%s,%s)"
    # data = [('admin4', 'admin3'), ('admin4', 'admin3'), ('admin3', 'admin3')]
    # cursor.executemany(sql, data)
    # conn1.commit()
    # sql_update="UPDATE blog_user SET username='zhangsan1111' WHERE id=1"
    # cursor.execute(sql_update)
    # sql_delete="DELETE FROM blog_user WHERE id=5"
    # cursor.execute(sql_delete)
    # conn1.commit()






    # conn1=pymysql.Connect(
    #     host='localhost',  ##mysql服务器地址
    #     port=3306,  ##mysql服务器端口号
    #     user='root',  ##用户名
    #     passwd='wjl123',  ##密码
    #     db='log',  ##数据库名
    #     charset='utf8'  ##连接编码
    # )
    # cursor=conn1.cursor(pymysql.cursors.DictCursor)
    # sql="INSERT INTO ipone(tel) value (%s)"
    # for i in range(0,1001):
    #     data= ''.join(random.sample(string.digits,9))
    #     cursor.execute(sql,data)
    #     conn1.commit()

    # conn1=pymysql.Connect(
    #     host='localhost',  ##mysql服务器地址
    #     port=3306,  ##mysql服务器端口号
    #     user='root',  ##用户名
    #     passwd='wjl123',  ##密码
    #     db='blog',  ##数据库名
    #     charset='utf8'  ##连接编码
    # )
    # time=datetime.datetime.now()
    # str1 = time.strftime('%Y-%m-%d %H:%M:%S')
    # print(str1)
    # cursor=conn1.cursor(pymysql.cursors.DictCursor)
    # # sql="INSERT INTO blog_article(title,author,time,content) values ('文章五','张三','2019-09-17 13:09:48','123434343')"
    # sql = "INSERT INTO blog_article(title,author,time,content) values (%s,%s,%s,%s)"
    # data=('文章五','张三',str1,'123434343')
    # cursor.execute(sql,data)
    # conn1.commit()

    cursor.close()


    conn1.close()


mysql()


def register(request):

    return render(request,"user/register.html")
def httpregister(request):
    username = request.POST.get('username')
    password = request.POST.get('password')


    if username!='' and password!='':
        dic = {
            'code': 0,
            'message': "注册成功"
        }
        data = json.dumps(dic)
        return HttpResponse(data)
    else:
        dic = {
            'code': 1,
            'message': "注册失败"
        }
        data = json.dumps(dic)
        return HttpResponse(data)
def login(request):
    return render(request,"user/login.html")
def httplogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    dic = {
        'code': 0,
        'message': "登录成功"
    }
    data = json.dumps(dic)
    return HttpResponse(data)