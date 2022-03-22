# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:06:57 2022

@author: DELL
"""


class SqList:###顺序线性表
    def __init__(self):
        self.initcapacity=5
        self.capacity=self.initcapacity
        self.data=[None]*self.capacity
        self.size=0
    
    def resize(self,newcapacity):
        assert newcapacity>=0
        olddata=self.data
        self.data=[None]*newcapacity
        self.capacity=newcapacity
        for i in range(self.size):
            self.data[i]=olddata[i]
        
    def CreateList(self,a):
        for i in range(0,len(a)):
            if self.size==self.capacity:
                self.resize(2*self.size)
            self.data[self.size]=a[i]
            self.size+=1
            
    def Add(self,e):
        if self.size==self.capacity:
            self.resize(2*self.size)
        self.data[self.size]=e
        self.size+=1
    
    def getsize(self):
        return self.size
    
    def __getitem__(self,i):
        assert 0<=i<=self.size
        return self.data[i]
   
    def __setitem__(self,i,x):
        assert 0<=i<self.size
        self.data[i]=x
        
    def GetNo(self,e):
        i=0
        while i<self.size and self.data[i]!=e:
            i+=1
        if (i>=self.size):
            return -1
        else:
            return i
        
    def Insert(self,i,e):
        assert 0<=i<=self.size
        if self.size==self.capacity:
            self.resize(2*self.size)
        for j in range(self.size,i-1,-1):
            self.data[j]=self.data[j-1]
        self.data[i]=e
        self.size+=1
        
    def Delete(self,i):
        assert 0<=i<=self.size-1
        for j in range(i,self.size-1):
            self.data[j]=self.data[j-1]
        self.size-=1
        if self.capacity>self.initcapacity and self.size<=self.capacity/4:
            self.resize(self.capacity//2)
    
    def display(self):
        for i in range(0,self.size):
            print(self.data[i],end=' ')
        print()


###题目:这里不妨设a=[1,3,5,7,9] b=[2,4,6,8]
a=[1,3,5,7,9]
b=[0,2,4,6,8]
A=SqList()
A.CreateList(a)
B=SqList()
B.CreateList(b)
def Merge2(A, B):
    C=SqList()
    i=j=0
    while i<A.getsize() and j<B.getsize():
        if A[i]<B[j]:
            C.Add(A[i])
            i+=1
        else:
            C.Add(B[j])
            j+=1
    while i<A.getsize():
        C.Add(A[i])
        i+=1
    while j<B.getsize():
        C.Add(B[j])
        j+=1
    return C
C=Merge2(A,B)
A.display();B.display()
print("合并为")
C.display()