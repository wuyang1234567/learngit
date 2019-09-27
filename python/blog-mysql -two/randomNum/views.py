from django.shortcuts import render
import random
import string
from datetime import datetime, date, timedelta


def randomnumber():
    # 第一遍
    # print(random.randrange(1,100))#（包含头不包含尾）
    # print(random.randint(1,100))#(包括头和尾）
    # print(random.randrange(1,10,2))#随机一个大于等于1且小于等于10之间的奇数，其中2表示递增基数
    # print(random.sample([1,2,3,4,5,6,7],2))#在一个列表里随机取两个数字
    # print(random.choice(['123','abc',52,[1,2]])) #随机返回参数列表中任意一个元素
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))  # 随机返回参数列表中任意两个元素，参数二指定返回的数量
    #
    # print(string.ascii_letters)#获取大写字母和小写字母
    # print(string.ascii_lowercase)#获取小写字母
    # print(string.ascii_uppercase)#获取大写字母
    # print(string.digits)#获取数字
    # print(string.punctuation)#获取特殊字符
    # print(string.printable)#获取大小写字母数字和特殊字符
    # print(string.hexdigits)#0123456789abcdefABCDEF获取十六进制字符
    # print("".join(random.sample(string.ascii_letters+string.digits,4)))
    # 第二遍
    # print(random.randrange(1,100))
    # print(random.randint(1,100))
    # print(random.randrange(1,19,2))
    # print(random.sample([1,2,3,4,5,6,7],2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1,2,3,4,5,5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))
    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    # print(string.hexdigits)
    # print("".join(random.sample(string.ascii_letters+string.digits,4)))
    # 第三遍
    # print(random.randrange(1,100))
    # print(random.randint(1,100))
    # print(random.randrange(0,100,2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))
    
    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.hexdigits)
    # print(string.printable)

    # 第四遍
    # print(random.randrange(1, 100))
    # print(random.randint(1, 100))
    # print(random.randrange(0, 100, 2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))
    
    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    # 第五遍
    # print(random.randrange(1, 100))
    # print(random.randint(1, 100))
    # print(random.randrange(0, 100, 2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))

    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    # 第六遍
    # print(random.randrange(1, 100))
    # print(random.randint(1, 100))
    # print(random.randrange(0, 100, 2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))

    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    # 第七遍
    # print(random.randrange(1, 100))
    # print(random.randint(1, 100))
    # print(random.randrange(0, 100, 2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))

    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    # 第八遍
    # print(random.randrange(1, 100))
    # print(random.randint(1, 100))
    # print(random.randrange(0, 100, 2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))

    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    # 第九遍
    # print(random.randrange(1, 100))
    # print(random.randint(1, 100))
    # print(random.randrange(0, 100, 2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))

    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    # 第十遍
    # print(random.randrange(1, 100))
    # print(random.randint(1, 100))
    # print(random.randrange(0, 100, 2))
    # print(random.sample([1, 2, 3, 4, 5, 6, 7], 2))
    # print(random.choice(['123', 'abc', 52, [1, 2]]))
    # print(random.choice([1, 2, 3, 4, 5, 5]))
    # print(random.sample(['123', 'abc', 52, [1, 2]], 2))

    # print(string.ascii_letters)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)
    # print(string.digits)
    # print(string.punctuation)
    # print(string.printable)
    return "random"
randomnumber()
def times():
    # 第一遍
    # now=date.today()
    # print(now)#2019-09-21
    # print(now.strftime("%Y.%m.%d"))#格式化时间日期
    # time=now.strftime('%Y{}%m{}%d{}').format("年","月","日")
    # print(time)
    # birthday=date(2000,1,1)
    # print(birthday)
    # age=now-birthday
    # print(age.days)
    # now=datetime.now()
    # print(now)
    # dt=datetime(2015,4,19,12,20)
    # print(dt)
    # print(dt.timestamp())#转换为时间戳模式
    # t=1429417200.0
    # print(datetime.fromtimestamp(t))#把时间戳转换为datetime模式
    # print(datetime.utcfromtimestamp(t))#utc时间
    # # str转换成datetime格式
    # day=datetime.strptime("2015-6-1 19:19:19","%Y-%m-%d %H:%M:%S")
    # print(day)
    # # datetime转换为str模式
    # now=datetime.now()
    # da=now.strftime("%Y-%m-%d")
    # print(da)
    # print(datetime.strptime(da,"%Y-%m-%d"))
    # print(now+timedelta(days=1,hours=1,minutes=1,seconds=70))

    # 第二遍
    # now=date.today()
    # print(now)
    # print(now.strftime("%Y-%m-%d"))
    # now=datetime.now()
    # print(now)
    # print(now.timestamp())
    # da=now.timestamp()
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dt=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dt,"%Y-%m-%d"))
    # print(now+timedelta(days=10))

    # 第三遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    # 第四遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    # 第五遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    # 第六遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    # 第七遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    # 第八遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    # 第九遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    # 第十遍
    # nowtime=date.today()
    # print(nowtime)
    # print(nowtime.strftime("%a,%b,%d"))
    # now=datetime.now()
    # print(now)
    # da=now.timestamp()
    # print(da)
    # print(datetime.fromtimestamp(da))
    # print(datetime.utcfromtimestamp(da))
    # print(now.strftime("%Y-%m-%d"))
    # dd=now.strftime("%Y-%m-%d")
    # print(datetime.strptime(dd,"%Y-%m-%d"))
    # print(now+timedelta(days=100))
    return "times"
times()