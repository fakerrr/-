#!/usr/bin/env python
#coding=utf-8

from tkinter import *
import time
import random
import os

class App:
    def __init__(self,master):
        #设置窗口标题
        self.ct = master
        self.ct.title('东安年会抽奖V1.7最终版')
        
        #获取屏幕高度和宽度，使窗口居中
        # screenwidth = master.winfo_screenwidth()
        # screenheight = master.winfo_screenheight()
        # print(screenwidth)
        # print(screenheight)
        # master.resizable(False,False)
        # master.geometry('%sx%s+%s+%s' % (master.winfo_width() + 10, master.winfo_height() + 10, (screenwidth - master.winfo_width())/2,(screenheight - master.winfo_height())/2) )
        master.maxsize(900,1000)
        master.minsize(900,700)
        master.bind("<Return>",self.callback)
        master.bind("<space>",self.callback2)
        self.pd = 1
        self.i = 1
        self.GetImage()
        self.main()

    def main(self):
        self.lable = Label(self.ct,image=self.a[0])
        self.lable.bm = self.a[0]
        self.lable.pack(fill=X,expand=1)
        self.lable.after(100,self.changeImage)
        # Button(self.ct,text='开始',command=self.callback).pack()
        # Button(self.ct,text='暂停',command=self.callback2).pack()
        # self.lable.after(2000,self.changeImage)
        
    def GetImage(self):
        
        self.a = []
        self.b = []
        image_list = os.listdir('1/')
        print(image_list)
        for x in  image_list:
            c = PhotoImage(file='1/'+x)
            self.a.append(c)
            self.b.append(c)
            print('正在装载')
        print(self.a)
        print(self.b)

    def changeImage(self):
        print("change image"+str(self.pd))
        if self.pd ==2 :
            return
        while 1:
            if self.i < len(self.a):
                self.lable.configure(image = self.a[self.i]) 
                self.i += 1
                self.lable.after(100,self.changeImage)
                if self.i == len(self.a):
                    self.i = 0
                return
            break
                # self.lable.configure(image = self.pp1)


    def callback(self,event):
        print('i got start')
        self.pd = 1
        self.lable.after(100,self.changeImage)

    def callback2(self,event):
        self.pd = 2
        print('i got stop')
        self.zjr = random.randint(0,len(self.a)-1)
        # print((self.)
        print(self.zjr)
        weishu = self.zjr
        self.zjr = self.a[self.zjr]
        print(self.zjr)
        for i in self.b:
            print('这是i：',i)
            if i == self.zjr:
                print(i)
                print('匹配')
                image_zjr = i
        self.lable.configure(image = image_zjr) 
        del self.a[weishu]
        print('已从self.a中删除此人')
        print('现在还有几个人：',len(self.a))


    
root = Tk()
app = App(root)

root.mainloop()
