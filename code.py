#!/usr/bin/env python
#coding=utf-8

from Tkinter import *
import time
import random

class App:
    def __init__(self,master):
        #设置窗口标题
        self.ct = master
        self.ct.title('东安年会抽奖V1.0测试版')
        
        #获取屏幕高度和宽度，使窗口居中
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight() - 100
        master.resizable(False,False)
#         master.geometry('%sx%s+%s+%s' % (master.winfo_width() + 10, master.winfo_height() + 10, (screenwidth - master.winfo_width())/2,
#  (screenheight - master.winfo_height())/2) )

        self.main()

    def main(self):
        self.pp1 = PhotoImage(file='1.gif')
        self.pp2 = PhotoImage(file='2.gif')
        # pp3 = PhotoImage(file='3.jpg')
        # pp4 = PhotoImage(file='4.jpg')
        # pp5 = PhotoImage(file='5.jpg')

        self.lable = Label(self.ct,image=self.pp1)
        self.lable.bm = self.pp1
        self.lable.pack(fill=X,expand=1)
        self.lable.after(2000,self.changeImage)
        

    def changeImage(self):
        self.lable.configure(image = self.pp2)

root = Tk()

app = App(root)

root.mainloop()
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
        self.ct.title('东安年会抽奖V1.0测试版')
        
        #获取屏幕高度和宽度，使窗口居中
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight() - 100
        master.resizable(False,False)
#         master.geometry('%sx%s+%s+%s' % (master.winfo_width() + 10, master.winfo_height() + 10, (screenwidth - master.winfo_width())/2,
#  (screenheight - master.winfo_height())/2) )
        self.i = 1
        self.GetImage()
        self.main()

    def main(self):
        self.lable = Label(self.ct,image=self.a[0])
        self.lable.bm = self.a[0]
        self.lable.pack(fill=X,expand=1)
        self.lable.after(100,self.changeImage)
        # self.lable.after(2000,self.changeImage)
        
    def GetImage(self):
        
        self.a = []
        image_list = os.listdir('id_image/')
        print(image_list)
        for x in  image_list:
            b = PhotoImage(file='id_image/'+x)
            self.a.append(b)
            print('正在装载')

    def changeImage(self):
        while 1:
            if self.i < len(self.a):
                self.lable.configure(image = self.a[self.i]) 
                self.i += 1
                self.lable.after(100,self.changeImage)
                return
            break
                # self.lable.configure(image = self.pp1)



        

    
root = Tk()
app = App(root)

root.mainloop()
