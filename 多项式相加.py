# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:10:14 2022

@author: DELL
"""


from operator import itemgetter

class PolyList:###多项式顺序表
    def __init__(self):
        self.data=[]###存放多项式的列表
    
    def Add(self,e):
        self.data.append(e)
    
    def CreateList(self,fname):###读取文件
        fin=open(fname,'r')
        n=int(fin.readline().strip())
        for i in range(n):
            p=fin.readline().strip().split()
            self.data.append([float(p[0]),int(p[1])])
        fin.close()
    
    def getsize(self):
        return len(self.data)
    
    def __getitem__(self,i):
        return self.data[i]

    def getdata(self):
        return self.data
    
    def Sort(self):###对data按指数递减排列
        self.data=sorted(self.data,key=itemgetter(1),reverse=True)
        
    def PolyAdd(self,B):
        C=PolyList()
        m=len(self.data)###A的项数
        n=B.getsize()###B的项数
        i,j=0,0
        while i<m and j<n:
            p,q=self.data[i],B[j]
            if p[1]<q[1]:
                C.Add(p)
                i+=1
            elif q[1]<p[1]:
                C.Add(q)
                j+=1
            else:
                k=p[0]+q[0]
                if (k!=0):
                    C.Add([k,p[1]])
                    i+=1
                    j+=1
        while i<m:
            p=self.data[i]
            C.Add(p)
            i+=1
        while j<n:
            q=B[j]
            C.Add(q)
            j+=1
        return C

###主程序
fout=open(r"C:\Users\DELL\Desktop\学术垃圾堆\数据结构\abc.out.txt","w+")        
p=PolyList()
p.CreateList(r"C:\Users\DELL\Desktop\学术垃圾堆\数据结构\abc1.in.txt")
print("第一个多项式:",end=' ',file=fout)
print(p.getdata(),file=fout)
p.Sort()
print("排序后结果：",end=' ',file=fout)
print(p.getdata(),file=fout)
q=PolyList()
q.CreateList(r"C:\Users\DELL\Desktop\学术垃圾堆\数据结构\abc2.in.txt")
print("第二个多项式:",end=' ',file=fout)
print(q.getdata(),file=fout)
q.Sort()
print("排序后结果：",end=' ',file=fout)
print(q.getdata(),file=fout)
r=p.PolyAdd(q)
print("相加多项式：",end=' ',file=fout)
print(r.getdata(),file=fout)
fout.close()    