import pymysql
from django.http import HttpResponse
from moudles import getdata

class  link(object):
    cursor=None
    conn=None
    @staticmethod
    def selectPart(sql,type,data=()):
        link.mysqllink()
        print(type)
        try:
            link.cursor.execute(sql,data)
        except Exception as e:
            print(e)
            return getdata.dic(1, "error")
        if type == 0:
            return link.cursor.fetchone()
        elif type == 1:
            return link.cursor.fetchall()
        elif type == 2:
            return link.cursor.rowcount
    @staticmethod
    def insertPart(sql,data=(),type=0):
        link.mysqllink()
        try:
            link.cursor.execute(sql,data)
            if type==1:
                return link.conn.insert_id()
            return getdata.dic(0, "注册成功")
        except Exception as e:
            return getdata.dic(1, "注册失败")
    @staticmethod
    def commit():
        link.conn.commit()
    @staticmethod
    def mysqllink():
        if link.conn!=None or link.cursor!=None:
            return
        link.conn = pymysql.Connect(
            host='localhost',  ##mysql服务器地址
            port=3306,  ##mysql服务器端口号
            user='root',  ##用户名
            passwd='wjl123',  ##密码
            db='blog',  ##数据库名
            charset='utf8'  ##连接编码
        )
        link.cursor = link.conn.cursor(cursor=pymysql.cursors.DictCursor)
    def __del__(self):
        self.conn.close()
        self.cursor.close()