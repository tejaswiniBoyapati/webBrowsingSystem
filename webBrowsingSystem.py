# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:50:35 2022

@author: teju3
"""

import time

#t = time.localtime()

class Browser:
    class Queue:
        def _init_(self):
            self.sz=0
            self.arr_site=[]
            self.arr_time=[]
    class Tab:
        class Stack:
            def _init_(self):
                self.size=0
                self.arr=[]
        def _init_(self,tabname,site):
            self.tabn=tabname
            self.current_site=site
            self.ForwardStack=self.Stack()
            self.BackwardStack=self.Stack()
            self.next=None
            self.prev=None
        
    def _init_(self):
        self.no_tabs=0
        self.first_Tab=None
        self.q=self.Queue()
    
    def create_tab(self):  #O(n) - n :no of tabs
        is_there=1
        while(is_there==1):
            print("\n Enter the Tab name: ",end="")
            tabname=input()
            is_there=0
            fir=self.first_Tab
            while(fir!=None):
                if(fir.tabn == tabname):
                    is_there=1
                    break
                else:
                    fir=fir.next
            if(is_there==1):
                print("\n\n !! Tab already exists, Try another one !!")
            
        print(" Enter the Site to open in ",tabname,": ",end="")
        site=input()
        
        newt=self.Tab(tabname,site)
        if(self.no_tabs!=0):
            newt.next=self.first_Tab
            self.first_Tab.prev=newt
        self.first_Tab=newt
        self.no_tabs+=1
        print("\n\n >> Tab created!!")
        self.show_tabs()
        t = time.localtime()
        self.q.arr_time.append(str(time.strftime("%H:%M:%S", t)))
        self.q.arr_site.append(self.first_Tab.current_site)
        self.q.sz+=1
        
    def delete_tab(self,site):  #O(n) - n :no of tabs
        f=self.first_Tab
        nfound=1
        while(f!=None and nfound):
            if(f.tabn==site):
                if(f.prev!=None and f.next!=None):
                    f.prev.next=f.next
                    f.next.prev=f.prev
                elif(f.next==None):
                    if(f.prev!=None):
                        f.prev.next=None
                elif(f==self.first_Tab):
                    f.next.prev=None
                    self.first_Tab=f.next
                nfound=0
            else:
                f=f.next
        if(nfound==1):
            print("\n\n !! Tab not found, Not deleted !!")
        else:
            self.no_tabs-=1
            print("\n\n >> Tab deleted!!")
            self.show_tabs()

    def show_tabs(self):  #O(n) - n :no of tabs
        if(self.no_tabs!=0):
            f=self.first_Tab
            print("\n >> Showing all : ",self.no_tabs," Tab(s)\n")
            while(f!=None):
                print("|\t",f.tabn, end="\t|x|")
                f=f.next
            print()
            f=self.first_Tab
            while(f!=None):
                print("( ",f.current_site," )",end=" ")
                f=f.next
            print()
        else:
            print("\n\n !! No Tabs exists !!")
            
    def switch_tab(self,site):  #O(n) - n :no of tabs
        f=self.first_Tab
        nfound=1
        while(f!=None and nfound):
            if(f.tabn==site):
                if(f.prev!=None and f.next!=None):
                    f.prev.next=f.next
                    f.next.prev=f.prev
                if(f.next==None):
                    f.prev.next=None
                f.prev=None
                if(f!=self.first_Tab):
                    f.next=self.first_Tab
                    self.first_Tab.prev=f
                    self.first_Tab=f
                    
                nfound=0
            else:
                f=f.next
        if(nfound==1):
            print("\n\n !! Tab not found, Not switched !!")
        else:
            print("\n\n >> Tab switched!!")
            self.show_tabs()
    
    def current_tab(self):  #O(1)
        print("\n\n >> Current Tab")
        print("\n",self.first_Tab.tabn," ( ",self.first_Tab.current_site," )")
        
    def open_link(self,site):  #O(n) - n :size of forward stack
        self.first_Tab.BackwardStack.arr.append(self.first_Tab.current_site)
        self.first_Tab.BackwardStack.size+=1
        self.first_Tab.current_site=site
        while(self.first_Tab.ForwardStack.size!=0):
            self.first_Tab.ForwardStack.arr.pop()
            self.first_Tab.ForwardStack.size-=1
        t = time.localtime()
        self.q.arr_time.append(str(time.strftime("%H:%M:%S", t)))
        self.q.arr_site.append(self.first_Tab.current_site)
        self.q.sz+=1
            
    def move_back(self):  #O(1)
        if(self.first_Tab.BackwardStack.size!=0):
            self.first_Tab.ForwardStack.arr.append(self.first_Tab.current_site)
            self.first_Tab.ForwardStack.size+=1
            self.first_Tab.BackwardStack.size-=1
            self.first_Tab.current_site=self.first_Tab.BackwardStack.arr[self.first_Tab.BackwardStack.size]
            self.first_Tab.BackwardStack.arr[self.first_Tab.BackwardStack.size]=None
            self.first_Tab.BackwardStack.arr=[i for i in self.first_Tab.BackwardStack.arr if i!=None]
            print("\n\n >> Gone 1 Site back")
            t = time.localtime()
            self.q.arr_time.append(str(time.strftime("%H:%M:%S", t)))
            self.q.arr_site.append(self.first_Tab.current_site)
            self.q.sz+=1
        else:
            print("\n\n !! Cannot Go back !!")
            
    def move_front(self):  #O(1)
        if(self.first_Tab.ForwardStack.size!=0):
            self.first_Tab.BackwardStack.arr.append(self.first_Tab.current_site)
            self.first_Tab.BackwardStack.size+=1
            self.first_Tab.ForwardStack.size-=1
            self.first_Tab.current_site=self.first_Tab.ForwardStack.arr[self.first_Tab.ForwardStack.size]
            self.first_Tab.ForwardStack.arr[self.first_Tab.ForwardStack.size]=None
            self.first_Tab.ForwardStack.arr=[i for i in self.first_Tab.ForwardStack.arr if i!=None]
            print("\n\n >> Gone 1 Site forward")
            t = time.localtime()
            self.q.arr_time.append(str(time.strftime("%H:%M:%S", t)))
            self.q.arr_site.append(self.first_Tab.current_site)
            self.q.sz+=1
        else:
            print("\n\n !! Cannot Go forward !!")
    
firefox = Browser()
print("\n===== Browser Opened =====")
cont=1
while(cont==1):
    while True:
        print("\nEnter the number of corresponding operation-\n 1.Create Tab\n 2.Show Tabs\n 3.Switch Tab\n 4.Current Tab\n 5.Delete Tab\n 6.Move Back\n 7.Move Front\n 8.Open Link\n 9.History\n 10.Exit: ",end="")
        opt=int(input())
        if(opt<1 or opt>10):
            continue
        else:
            break
    if(opt==1):
        #Create Tab
        firefox.create_tab()
        
    elif(opt==2):
        #Show Tabs
        firefox.show_tabs()
        
    elif(opt==3):
        #Switch Tabs
        if(firefox.no_tabs>1):
            print("\n Enter the Tab name: ",end="")
            tabz=input()
            firefox.switch_tab(tabz)
        else:
            print("\n\n !! Either no tabs or only 1 Tab !!")
        
    elif(opt==4):
        #Current Tab
        if(firefox.no_tabs>0):
            firefox.current_tab()
        else:
            print("\n\n !! No Tabs !!")
            
    elif(opt==5):
        #Remove Tab
        if(firefox.no_tabs>1):
            print("\n Enter the Tab name: ",end="")
            tabz=input()
            print("\n Are you sure?\n 1.Yes\n 2.No: ",end="")
            yesno=int(input())
            if(yesno==1):
                firefox.delete_tab(tabz)
            else:
                print("\n\n !! Not deleted !!")
                firefox.show_tabs()
        elif(firefox.no_tabs==0):
            print("\n\n !! No Tabs, Not deleted !!")
        elif(firefox.no_tabs==1):
            print("\n Are you sure?\n 1.Yes\n 2.No: ",end="")
            yesno=int(input())
            if(yesno==1):
                firefox.no_tabs-=1
                print("\n\n >> Only 1 Tab (",firefox.first_Tab.tabn,") exists, deleted!!")
                firefox.first_Tab=None
                firefox.show_tabs()
            else:
                print("\n\n !! Not deleted !!")
                firefox.show_tabs()
        
    elif(opt==6):
        #Move Back
        if(firefox.no_tabs>0):
            firefox.move_back()
            firefox.show_tabs()
        else:
            print("\n\n !! No Tabs !!")
            
    elif(opt==7):
        #Move Front
        if(firefox.no_tabs>0):
            firefox.move_front()
            firefox.show_tabs()
        else:
            print("\n\n !! No Tabs !!")
            
    elif(opt==8):
        #Open Link
        if(firefox.no_tabs>0):
            print("\n Enter the Site: ",end="")
            site=input()
            firefox.open_link(site)
            print("\n\n >> Link opened")
            firefox.show_tabs()
        else:
            print("\n\n !! No Tabs !!")
            
    elif(opt==9):
        #History
        print("\n >> History : \n")
        for i in range(firefox.q.sz):
            print("|\t",firefox.q.arr_site[i], end="\t|x|")
        print()
        for i in range(firefox.q.sz):
            print("( ",firefox.q.arr_time[i]," )",end=" ")
        print()
        
    elif(opt==10):
        break
    
    while True:
        print("\nDo you want to continue?\n 1.Yes\n 2.No: ",end="")
        cont=int(input())
        if(cont<1 or cont>2):
            continue
        else:
            break
        
print("\n\n !! Terminating.., Thank you !!")