# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:05:12 2022

@author: DELL
"""


###链表    
class LinkNode:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=LinkNode()
        self.head.next=None
###插入节点操作：
###s.next=p.next
###p.next=s
###删除节点操作：
###p.next=p.next.next        
    def CreateListF(self,a):
        for i in range(0,len(a)):
            s=LinkNode(a[i])
            s.next=self.head.next
            self.head.next=s
            
    def CreateListR(self,a):
        t=self.head
        for i in range(0,len(a)):
            s=LinkNode(a[i])
            t.next=s
            t=s
        t.next=None
    
    def geti(self,i):
        p=self.head
        j=-1
        while (j<i and p is not None):
            j+=1
            p=p.next
        return p
    
    def Add(self,e):
        s=LinkNode(e)
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=s
     
    def getsize(self):
        p=self.head
        cnt=0
        while p.next is not None:
            cnt+=1
            p=p.next
        return cnt

    def ___getitem__(self,i):
        assert i>=0
        p=self.geti(i)
        assert p is not None
        return p.data
    
    def __setitem__(self,i,e):
        assert i>=0
        p=self.geti(i)
        assert p is not None
        p.data=e
    
    def GetNo(self,e):
        j=0
        p=self.head.nest
        while p is not None and p.data!=e:
            j+=1
            p=p.next
        if p is None:
            return -1
        else:
            return j
    
    def Insert(self,i,e):
        assert i>=0
        s=LinkNode(e)
        p=self.geti(i-1)
        assert p is not None
        s.next=p.next
        p.next=s
        
    def Delete(self,i):
        assert i >=0
        p=self.geti(i-1)
        assert p!=None and p.next is not None
        p.next=p.next.next
        
    def display(self):
        p=self.head.next
        while p is not None:
            print(p.data,end=' ')
            p=p.next
        print()
        

###题目
A=LinkList()
A.CreateListR([1,3,5,7,9])
B=LinkList()
B.CreateListR([0,2,4,6,8])
def Merge2(A,B):
    p=A.head.next
    q=B.head.next
    C=LinkList()
    t=C.head
    while p!=None and q!=None:
        if p.data<q.data:
            t.next=p
            t=p
            p=p.next
        else:
            t.next=q
            t=q
            q=q.next
        t.next=None
    if p!=None:
        t.next=p
    if q!=None:
        t.next=q
    return C
C=Merge2(A,B)
C.display()
