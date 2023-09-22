'''
n=int(input("请输入要排序的数字数量"))

a=[3]
for i in range(n):
   b=int(input("请输入数字"))
   a.append(b) 
def bubble(x,y):
    long=len(x)
    
    for i in range(long-1):
        for j in range(0,long-1-i):
            if y==31:
                if x[j]>x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]
            else:
                if  x[j]<x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]
    return x
                    
a=bubble(a,0)
print(a)  
--------------------------------------------------------
  
class Commodity:
    def __init__(self,id,name,sum=0,rest=0,price=0) :
        self.id=id
        self.name=name
        self.sum=sum
        self.rest=sum
        self.price=price
    def display(self):
        print(self.id)
        print(self.name)
        print(self.sum)
        print(self.rest)
        
    def buy(self,num):
        self.rest=self.rest-num
    def calculate(self):
        return  self.price*(self.sum-self.rest)
a=set()
l1=Commodity(id=1,name="汉堡",sum=1,rest=1,price=15)
l1.display()
l1.buy(1)
l1.display()
print(l1.calculate())


 --------------------------------------------------------------------------------       
       
       
       

a=[[1 for i in range(5)] for j in range(10) ]
  
b=map(lambda x:map(lambda y:y+2,x),a)
print(list(list(b)))

matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = [list(col) for col in zip(*matrix)]
print(transposed_matrix)  # 输出: [[1, 4], [2, 5], [3, 6]]





------------------------------------------------------------------------------------
import random
def daozhi(a):
    if type(a)!=list:
        print("倒了几次，醉成这样")
        return None
    else:
        for i in a:
            if type(i)!=list:
                return "这也能倒?"
    return [list(j) for j in zip(*a)]
print("你要生成几行几列的矩阵")
Ind=int(input("行数是"))
Clo=int(input("列数是"))
list1=[[random.randint(0,100) for i in range(Clo)] for j in range(Ind) ]
print(daozhi())

--------------------------------------------------------------------------------------------
import random

def wrichangestr(a):
    b=""
    for i in a:
        b=b+i+"  "
    return b
def FAPAI():

    
    b=["2","3","4","5","6","7","8","9","10","J","K","Q","A"]
    c=["梅花","方块","红桃","黑桃"]
    a=[]
    player=[1,2,3]
    player_=[1,2,3]
    dizhu=0
    pingming=[]
    for i in c:
        for j in b:
         a.append(i+j)#列表a存放所有牌
    dizhu=0

    flag=0
    while True:
        random.shuffle(a)
        for i in range(1,4):
            print("是否选择叫地主,请回答是或不是")
            choice=input()
            if choice=="是":
                dizhu=i
                flag=1
            if flag==1:
                break
        break
    player.pop(dizhu-1)


    for i in player:
        print("是否抢地主\n")
        choice1=input("回答是或不是\n")
        if choice1=="是":
            dizhu=i
    print("地主是",dizhu)
    player_.pop(dizhu-1)
    p="player"
    for i in player_:
        pingming.append("player"+str(i))
    
    for i in range(len(pingming)):
        t=open(pingming[i]+".txt","w+",encoding="utf-8")
        t.write(wrichangestr(a[i*17:i*17+17]))
        t.close()
    p=open("player"+str(dizhu)+".txt","w+",encoding="utf-8")
    p.write(wrichangestr(a[34::]))
    p.close()


-----------------------------------------------------------------------------------


import time
def observetime(f):
    def wrapper(*args,**kwargs):
        Start=time.time()
        a=f(*args,**kwargs)
        end=time.time()
        print(Start-end)
    return wrapper
        
        
        
        
        
        
        
@observetime
def func(t):
    for i in range(t):
        i=i+i
    return i

--------------------------------------------------------------------------------------



import time
def observerun(times):
    
    def diaoyonghanshu(func):
        
        def wrapper(*args,**kwargs):
            
            start=time.time()
            for i in range(times):
                
                b=func(*args,**kwargs)
            end=time.time()
                
            
            print("运行",times,"次","函数",func,"所需的时间为",end-start)
            return b
        return wrapper
    return diaoyonghanshu
n=int(input("你要运行几次函数\n"))
@observerun(n)
def sample(a):
    s=0
    for i in range(a):
        s=i+a
    return s
sample(10)

-------------------------------------------------------------------------------------------


class Myzoo:
    def __init__(self,animals=None):
        if animals==None:
            self.animals={}
        else:
            self.animals=animals
    def __str__(self):
        
        

----------------------------------------------------------------
from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/hello') #路由
def hello(): #视图函数
    return '软二的同学你好！'
@app.route('/hello/<name>') #URL 内包含变量
def hello_name(name): #路由函数声明变量
    return 'hello,%s!'%name #使用变量
@app.route("/la")
def partition():
    return render_template("part.html")
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)        
'''  
        
import requests
import json
url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
city=input("请输入\n")
param={"op":"keyword","cname":"","pid":"","keyword":city,"pageIndex":1,"pageSize":10}
response=requests.post(url=url,headers=headers,data=param)
page_json=response.text
with open("bili.txt","w+",encoding="utf-8") as fp:
    fp.write(page_json)
    
print("duquwanbi")



'''        
-------------------------------------------------------------------------    


import random

while True:
    ty=input("真心话还是大冒险:\n")
    content=input("内容是:")
    with open("content.txt","w+",encoding="utf-8") as fp:
        fp.write()
    
    
        
            

'''        
    





