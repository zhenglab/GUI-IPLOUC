#!/usr/bin/env python
#coding=utf-8

import sqlite3 as lite
import wx,os,sys,string
import wx.lib.buttons
import wx.lib.buttons as buttons
import os.path
import os 
import math
import subprocess
import itertools
import wx.grid
from wxPython.wx import *  

#注意定义全局变量中的列表的声明方法。
PicFlag = ['radion1',]
ParaFlag=['P_radion1',]
Flag1=0
Flag2=0
Flag3=0
Flag4=0
a=['FilesPath',]
aa=['FilesPath',]
threshold=7
foF1='NULL'
foF2='NULL'
fxF2='NULL'
hF1='NULL'
hF2='NULL'
fmin='NULL'

find_data1=[]
find_data=[]

par_several=['NULL',]
place="NULL"
par_time="NULL"
filename=['NULL',]
ReadFileSeePara_main=['NULL',]
fre=1
result=0

fminFlag=0
foF1Flag=0
foF2Flag=0
fxF2Flag=0
hF1Flag=0
hF2Flag=0

sqlitenumber=1

posX=0
posY=0
FlagClick=0

timeFlag1=0
timeFlag3=0
timeFlag5=0
timeFlag8=0
timeFlag9=0
timeFlag14=0

spinFlag=0
spinFlagUp=0
spinFlagDown=0
NumspinFlagUp=2
NumspinFlagDown=1

spinFlag3=0
spinFlagUp3=0
spinFlagDown3=0
NumspinFlagUp3=2
NumspinFlagDown3=1


spinFlag5=0
spinFlagUp5=0
spinFlagDown5=0
NumspinFlagUp5=2
NumspinFlagDown5=1

spinFlag8=0
spinFlagUp8=0
spinFlagDown8=0
NumspinFlagUp8=2
NumspinFlagDown8=1

spinFlag9=0
spinFlagUp9=0
spinFlagDown9=0
NumspinFlagUp9=2
NumspinFlagDown9=1

spinFlag14=0
spinFlagUp14=0
spinFlagDown14=0
NumspinFlagUp14=2
NumspinFlagDown14=1

#界面############################主页############################################
class InFrame(wx.Frame):
    def __init__(self, parent, id,):
        wx.Frame.__init__(self, parent, id,'中国电波传播研究所电离图度量'.decode('utf-8')
                            ,size=(1100,730), #style=wx.DEFAULT_FRAME_STYLE)
                            style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        panel = wx.Panel(self,-1)


   
##        ####sizer为新添加的，使得同时扩大化。
##        self.sizer = sizerFunc(panel)
##        panel.SetSizer(self.sizer)
##        self.sizer.Fit(panel)
##        
        self.tb  = TestTB(panel,id)
        self.tb.Bind(wx.EVT_TOOLBOOK_PAGE_CHANGED, self.OnPageChanged)
        
        menubar = wx.MenuBar(wx.MB_DOCKABLE)
        
        file = wx.Menu()
        manage=wx.MenuItem(file, 1, "&管理(M)\tCtrl+M".decode('utf-8'))
        imgManage = wx.Image('D:/DBS/FacePic/manage.png',wx.BITMAP_TYPE_ANY).Scale(22,22)
        manage.SetBitmap(wx.BitmapFromImage(imgManage))

        printer=wx.MenuItem(file, 2, "&打印(P)\tCtrl+P".decode('utf-8'))
        imgprinter = wx.Image('D:/DBS/FacePic/printer.png',wx.BITMAP_TYPE_ANY).Scale(17,17)
        printer.SetBitmap(wx.BitmapFromImage(imgprinter))
    
        quit = wx.MenuItem(file, 3, "&退出(Q)\tCtrl+Q".decode('utf-8'))
        imgQuit = wx.Image('D:/DBS/FacePic/quit.png',wx.BITMAP_TYPE_ANY).Scale(17,17)
        quit.SetBitmap(wx.BitmapFromImage(imgQuit))
        
        file.AppendItem(manage)
        file.AppendItem(printer)
        file.AppendItem(quit)
        
        self.Bind(wx.EVT_MENU, self.OnLoad, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=3)
        
        menubar.Append(file, "&文件(F)".decode('utf-8'))        

        help = wx.Menu()
        helps=wx.MenuItem(help, 5,"&帮助(H)\tCtrl+H".decode('utf-8'))
        about=wx.MenuItem(help, 4,"&关于(A)\tCtrl+A".decode('utf-8'))
        imgHelps = wx.Image('D:/DBS/FacePic/help.png',wx.BITMAP_TYPE_ANY).Scale(19,19)
        helps.SetBitmap(wx.BitmapFromImage(imgHelps))
        imgabout = wx.Image('D:/DBS/FacePic/about.png',wx.BITMAP_TYPE_ANY).Scale(22,22)
        about.SetBitmap(wx.BitmapFromImage(imgabout))
        help.AppendItem(helps)
        help.AppendItem(about)
        menubar.Append(help, "&帮助(H)".decode('utf-8'))
        self.Bind(wx.EVT_MENU, self.OnHelp, id=5)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=4)


        self.SetMenuBar(menubar)
        self.Centre()
        self.Show(True)



        
    def OnLoad(self, event):
        dlg=LoginDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnQuit(self, event):
        self.Close()

    def OnHelp(self, event):
        os.popen("notepad 'D:\DBS\Help.txt'")
        
    def OnAbout(self,event):
        os.popen("notepad 'D:\DBS\About.txt'")

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.tb.GetSelection()
        event.Skip()



class LoginDialog(wx.Dialog):
    def __init__(self, parent, id=-1):
        dlgManage=wx.Dialog.__init__(self, parent, id, '管理员登录'.decode('utf-8'))
        self.ctrl_username = wx.TextCtrl(self, -1)
        self.ctrl_passwd = wx.TextCtrl(self, -1,style=wx.TE_PASSWORD)
        self.ctrl_login = wx.Button(self, -1, '登录'.decode('utf-8'))
        self.ctrl_login.Bind(wx.EVT_BUTTON, self.OnDecide)
        self.ctrl_login.SetDefault()
        self.ctrl_cancel = wx.Button(self, wx.ID_CANCEL, '取消'.decode('utf-8'))
        #self.ctrl_register = wx.Button(self, -1, u'注册')
        self.pwDesign()
        
    def OnDecide(self,event):
        if self.ctrl_username.GetValue()=='Ace' and self.ctrl_passwd.GetValue()=='1234':
            self.Destroy()
        else:
            #下面新建密码输入错误的提示对话框并完成相应的设置。
            dlgError = wx.MessageDialog(None, "请您输入正确的用户名与密码".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlgError.ShowModal()
            if (retCode == wx.ID_YES):
                dlgError.Destroy()

    def pwDesign(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        b = wx.StaticBoxSizer(wx.StaticBox(self, -1, '登录'.decode('utf-8')), wx.VERTICAL)
        #b.Add(wx.StaticText(self, -1, u'请输入用户名和密码\n'
                #u'（游客请输入guest，密码为空）'), 0, wx.ALL, 3)
        grid = wx.FlexGridSizer(2, 0, 3, 3)
        grid.AddGrowableCol(1)
        grid.Add(wx.StaticText(self, -1, '用户名：'.decode('utf-8')))
        grid.Add(self.ctrl_username, 0, wx.GROW)
        grid.Add(wx.StaticText(self, -1, '密码：'.decode('utf-8')))
        grid.Add(self.ctrl_passwd, 0, wx.GROW)
        b.Add(grid, 0, wx.GROW|wx.ALL, 3)
        sizer.Add(b, 0, wx.GROW|wx.ALL, 3)

        h = wx.BoxSizer(wx.HORIZONTAL)
        h.Add(self.ctrl_login, 0, wx.ALL, 3)
        h.Add(self.ctrl_cancel, 0, wx.ALL, 3)
        h.Add((0, 0), 1)
        #h.Add(self.ctrl_register, 0, wx.ALL, 3)
        sizer.Add(h, 0, wx.GROW)

        self.SetAutoLayout(True)
        self.SetSizerAndFit(sizer)


class TestTB(wx.Toolbook): 
     def __init__(self,parent,id):
        wx.Toolbook.__init__(self, parent, id,size=(1100,700),pos=(0,2),style=wx.BK_DEFAULT)

        panel = wx.Panel(self)

        
        img1 = wx.Image('D:/DBS/FacePic/1.png',wx.BITMAP_TYPE_ANY).Scale(50,50)
        img2 = wx.Image('D:/DBS/FacePic/2.png',wx.BITMAP_TYPE_ANY).Scale(50,50)
        img3 = wx.Image('D:/DBS/FacePic/3.png',wx.BITMAP_TYPE_ANY).Scale(50,50)
        img4 = wx.Image('D:/DBS/FacePic/4.png',wx.BITMAP_TYPE_ANY).Scale(50,50)
        
        il = wx.ImageList(50,50)
        bmp1 =img1.ConvertToBitmap()
        bmp2 =img2.ConvertToBitmap()
        bmp3 =img3.ConvertToBitmap()
        bmp4 =img4.ConvertToBitmap()
        index1 = il.Add(bmp1)
        index2 = il.Add(bmp2)
        index3 = il.Add(bmp3)
        index4 = il.Add(bmp4)
        self.AssignImageList(il)

        page1 = PageOne(self)
        self.AddPage(page1, "    使用说明    ".decode('utf-8'), imageId = index1)
        page3 = PageThree(self);
        page2 = PageTwo(self, page3);
        page4 = PageFour(self)
        self.AddPage(page2, "    自动度量    ".decode('utf-8'), imageId = index3)
        self.AddPage(page3, "    手动度量    ".decode('utf-8'), imageId = index2)
        self.AddPage(page4, "    数据管理    ".decode('utf-8'), imageId = index4)

       
        page1.SetFocus() 
        
     
###########################使用说明######################################
class PageOne(wx.Panel):
     def __init__(self, parent,):
         wx.Panel.__init__(self, parent)         
         panel = wx.Panel(self)

         #######添加box################
         box=wx.BoxSizer(wx.HORIZONTAL)

         
         colour = [(255,255,255),(153,204,255),(151,253,225),]
         self.SetBackgroundColour(colour[0])
         #下面几句设置“使用说明”的显示图片。
         self.title=wx.Image('D:/DBS/FacePic/11.png',wx.BITMAP_TYPE_ANY).Scale(100,25)
         self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.title),pos=(455,30))         
         Font= wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
         self.Introduction1=wx.StaticText(self, -1, "1：本度量软件的核心功能是“手动度量”。就是当您手动操作对图像进行度量的时候".decode('utf-8'), (200, 92),(200,-1),wx.ALIGN_LEFT)
         self.Introduction11=wx.StaticText(self, -1,"系统会根据......".decode('utf-8'), (225, 117),(200,-1),wx.ALIGN_LEFT)  
         self.Introduction2=wx.StaticText(self, -1, "2：本度量软件的关键功能是“自动度量”。就是当您在此模块中输入文件控制信息后".decode('utf-8'), (200, 152),(200,-1),wx.ALIGN_LEFT)
         self.Introduction22=wx.StaticText(self, -1, "系统自动读取参数和文件信息，通过运算输出参数和描迹图。".decode('utf-8'), (225, 177),(200,-1),wx.ALIGN_LEFT)
         self.Introduction3=wx.StaticText(self, -1, "3：在“自动度量”模块中，设置有重置功能，方便用户多次度量。同时设“图片显示”".decode('utf-8'), (200, 212),(200,-1),wx.ALIGN_LEFT)
         self.Introduction33=wx.StaticText(self, -1, "方便Matlab研究人员观察自动度量过程中的中间过程效果图。".decode('utf-8'), (225, 237),(200,-1),wx.ALIGN_LEFT)
         self.Introduction4=wx.StaticText(self, -1, "4：在“手动度量”模块中，设置有重置功能，方便用户多次度量。同时设“查看详情”".decode('utf-8'), (200, 272),(200,-1),wx.ALIGN_LEFT)
         self.Introduction44=wx.StaticText(self, -1, "按钮，以查看......".decode('utf-8'), (225, 297),(200,-1),wx.ALIGN_LEFT)
         self.Introduction5=wx.StaticText(self, -1, "5：在“文件”-->“管理”选项中设置了管理员登陆对话框，这是为了以后的数据库管理".decode('utf-8'), (200, 332),(200,-1),wx.ALIGN_LEFT)
         self.Introduction55=wx.StaticText(self, -1, "方便（目前还未开发完全），普通用户可忽略此功能。".decode('utf-8'), (225, 357),(200,-1),wx.ALIGN_LEFT)
         self.Introduction6=wx.StaticText(self, -1, "6：具体使用方法请参阅“Help.txt”或点击菜单栏中的“帮助(H)”(Ctrl+H)。".decode('utf-8'), (200,392),(200,-1),wx.ALIGN_LEFT)
         self.Introduction7=wx.StaticText(self, -1, "7：如有疑问请联系我们：wugengkun@126.com。".decode('utf-8'), (200,432),(200,-1),wx.ALIGN_LEFT)
         self.Introduction1.SetFont(Font)
         self.Introduction2.SetFont(Font)
         self.Introduction3.SetFont(Font)
         self.Introduction4.SetFont(Font)
         self.Introduction5.SetFont(Font)
         self.Introduction11.SetFont(Font)
         self.Introduction22.SetFont(Font)
         self.Introduction33.SetFont(Font)
         self.Introduction44.SetFont(Font)
         self.Introduction55.SetFont(Font)
         self.Introduction6.SetFont(Font)
         self.Introduction7.SetFont(Font)

         box.Add( self.Introduction1, 2 )   
         box.Add( self.Introduction11, 3 )   
         box.Add( self.Introduction2, 3 )   
         box.Add( self.Introduction22, 2 )   
         box.Add( self.Introduction3, 2 )   
         box.Add( self.Introduction33, 3 )   
         box.Add( self.Introduction4, 2 )   
         box.Add( self.Introduction44, 1 )   
         box.Add( self.Introduction5, 1 )
         box.Add( self.Introduction55, 1 )   
         box.Add( self.Introduction6, 1 )   
         box.Add( self.Introduction7, 1 )   
 
         
         panel.SetSizer(box)   
         self.Centre()   
 


############################数据管理######################################
class PageFour(wx.Panel):
     def __init__(self, parent):          
        wx.Panel.__init__(self, parent)
        self.toolkit = parent

        colour = [(255,255,255),(153,204,255),(151,253,225),]
        self.SetBackgroundColour(colour[0])

        #绑定画板的边线底纹绘制（Paint0部分）。
        self.Bind(wx.EVT_PAINT, self.Paint0)

        #添加grid报表模块。
        self.panel = wx.Panel(self)
        self.grid = wx.grid.Grid(self,pos=(272, 32), #修改pos位置
                size=(788,405), #修改size
                style=wx.WANTS_CHARS)
        
        self.grid.CreateGrid(2000,18)
        
##        #以下是给报表单元格的内容赋值。
##        for row in range(2000):
##            for col in range(18):
##                grid.SetCellValue(row, col,"NULL" )
##                ##grid.SetCellValue(row, col,"(%d,%d)" % (row, col))

        #grid.SetCellSize(2, 2, 2, 3)  #合并单元格
        #grid.SetRowSize(1, 50)#设置行高。
        
        for i in range(2,16):               
            self.grid.SetColSize(i, 70) #设置列宽。 
        self.grid.SetColSize(17,40)
        self.grid.SetColSize(16,90)
        self.grid.SetColSize(0,33)
        self.grid.SetColSize(1,180)

        self.grid.SetCellValue(0,0,"P_id")
        self.grid.SetCellValue(0,1,"file_name")
        self.grid.SetCellValue(0,2,"fmin")
        self.grid.SetCellValue(0,3,"fbEs")
        self.grid.SetCellValue(0,4,"foF2")
        self.grid.SetCellValue(0,5,"hE")
        self.grid.SetCellValue(0,6,"hF")
        self.grid.SetCellValue(0,7,"M3F2")
        self.grid.SetCellValue(0,8,"foE")
        self.grid.SetCellValue(0,9,"foF1")
        self.grid.SetCellValue(0,10,"fx1")
        self.grid.SetCellValue(0,11,"foEs")
        self.grid.SetCellValue(0,12,"M3F1")
        self.grid.SetCellValue(0,13,"hEs")
        self.grid.SetCellValue(0,14,"Es")
        self.grid.SetCellValue(0,15,"hF2")
        self.grid.SetCellValue(0,16,"time")
        self.grid.SetCellValue(0,17,"place")

        #self.grid.SetCellValue(1,1,"201002020930p30s1.0h0.0V.O")
        #self.grid.SetCellValue(1,16,"201002020930")
        #self.grid.SetCellValue(1,17,"青岛站".decode('utf-8'))
        #self.grid.SetCellValue(2,2,"190.000000")
        #生成下拉菜单选项及按钮和静态文本框，并设置字体格式。
        DownFont1 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)
        DownFont2 = wx.Font(14,wx.SWISS,wx.NORMAL,wx.BOLD) 

        self.Platexx=wx.StaticText(self,-1,"数据查询：".decode('utf-8'),(30,60))
        self.Platexx.SetFont(DownFont2)


        self.PlatePlace=wx.StaticText(self,-1,"观测站点：".decode('utf-8'),(40,100))
        self.PlatePlace.SetFont(DownFont1)

        

        

        self.Plate0=wx.StaticText(self,-1,"年：".decode('utf-8'),(40,140))
        self.Plate0.SetFont(DownFont1)
        
        self.Plate1=wx.StaticText(self,-1,"月：".decode('utf-8'),(40,180))
        self.Plate1.SetFont(DownFont1)

        self.Plate2=wx.StaticText(self,-1,"日：".decode('utf-8'),(40,220))
        self.Plate2.SetFont(DownFont1)

        self.Plate3=wx.StaticText(self,-1,"时：".decode('utf-8'),(40,260))
        self.Plate3.SetFont(DownFont1)

        self.Plate4=wx.StaticText(self,-1,"分：".decode('utf-8'),(40,300))
        self.Plate4.SetFont(DownFont1)



        #生成观测站点的选择的下拉菜单项。
        self.sampleList00 = ['青岛站'.decode('utf-8'),'青海站'.decode('utf-8'),'新乡站'.decode('utf-8'), '济南站'.decode('utf-8'),]
        self.choicePlace = wx.Choice(self, -1, (115, 100), choices=self.sampleList00,style=wx.SL_VERTICAL,
                                 name="Time")




        #生成年选择的下拉菜单项。
        self.sampleList0 = ['2000'.decode('utf-8'),'2001'.decode('utf-8'), '2002'.decode('utf-8'),'2003'.decode('utf-8'),
                            '2004'.decode('utf-8'),'2005'.decode('utf-8'), '2006'.decode('utf-8'),'2007'.decode('utf-8'),
                            '2008'.decode('utf-8'),'2009'.decode('utf-8'), '2010'.decode('utf-8'),'2011'.decode('utf-8'),
                            '2012'.decode('utf-8'),'2013'.decode('utf-8'), '2014'.decode('utf-8'),'2015'.decode('utf-8'),
                            '2016'.decode('utf-8'),'2017'.decode('utf-8'), '2018'.decode('utf-8'),'2019'.decode('utf-8'),
                            '2020'.decode('utf-8'),'2021'.decode('utf-8'), '2022'.decode('utf-8'),'2023'.decode('utf-8'),
                            '2024'.decode('utf-8'),'2025'.decode('utf-8'), '2026'.decode('utf-8'),'2027'.decode('utf-8'),]
        self.choice0 = wx.Choice(self, -1, (70, 140), choices=self.sampleList0,style=wx.SL_VERTICAL,
                                 name="Time")
        
        #生成月的下拉菜单选择项。
        self.sampleList1 = ['01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'), '04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'), '09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'), ]
        self.choice1 = wx.Choice(self, -1, (75, 180), choices=self.sampleList1,style=wx.SL_VERTICAL,
                                 name="Threshold")

        #生成日选择的下拉菜单项。
        self.sampleList2 = ['01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'),'04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'),'09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'),'13'.decode('utf-8'),'14'.decode('utf-8'),'15'.decode('utf-8'),
                            '16'.decode('utf-8'),'17'.decode('utf-8'),'18'.decode('utf-8'),'19'.decode('utf-8'),'20'.decode('utf-8'),
                            '21'.decode('utf-8'),'22'.decode('utf-8'),'23'.decode('utf-8'),'24'.decode('utf-8'),'25'.decode('utf-8'),
                            '26'.decode('utf-8'),'27'.decode('utf-8'),'28'.decode('utf-8'),'29'.decode('utf-8'),'30'.decode('utf-8'),
                            '31'.decode('utf-8'),]
        self.choice2 = wx.Choice(self, -1, (75, 220), choices=self.sampleList2,style=wx.SL_VERTICAL,
                                 name="Time")

        
        #生成时的下拉菜单选择项。
        self.sampleList3 = ['00'.decode('utf-8'),'01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'), '04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'), '09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'),
                            '13'.decode('utf-8'),'14'.decode('utf-8'),'15'.decode('utf-8'), '16'.decode('utf-8'),'17'.decode('utf-8'),
                            '18'.decode('utf-8'),'19'.decode('utf-8'),'20'.decode('utf-8'), '21'.decode('utf-8'),'22'.decode('utf-8'),
                            '23'.decode('utf-8'),]
        self.choice3 = wx.Choice(self, -1, (75, 260), choices=self.sampleList3,style=wx.SL_VERTICAL,
                                 name="Threshold")
        self.choice3.SetSelection(0)
        #生成分选择的下拉菜单项。
        self.sampleList4 = ['00'.decode('utf-8'),'01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'),'04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'),'09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'),'13'.decode('utf-8'),'14'.decode('utf-8'),'15'.decode('utf-8'),
                            '16'.decode('utf-8'),'17'.decode('utf-8'),'18'.decode('utf-8'),'19'.decode('utf-8'),'20'.decode('utf-8'),
                            '21'.decode('utf-8'),'22'.decode('utf-8'),'23'.decode('utf-8'),'24'.decode('utf-8'),'25'.decode('utf-8'),
                            '26'.decode('utf-8'),'27'.decode('utf-8'),'28'.decode('utf-8'),'29'.decode('utf-8'),'30'.decode('utf-8'),
                            '31'.decode('utf-8'),'32'.decode('utf-8'),'33'.decode('utf-8'),'34'.decode('utf-8'),'35'.decode('utf-8'),
                            '36'.decode('utf-8'),'37'.decode('utf-8'),'38'.decode('utf-8'),'39'.decode('utf-8'),'40'.decode('utf-8'),
                            '41'.decode('utf-8'),'42'.decode('utf-8'),'43'.decode('utf-8'),'44'.decode('utf-8'),'45'.decode('utf-8'),
                            '46'.decode('utf-8'),'47'.decode('utf-8'),'48'.decode('utf-8'),'49'.decode('utf-8'),'50'.decode('utf-8'),
                            '51'.decode('utf-8'),'52'.decode('utf-8'),'53'.decode('utf-8'),'54'.decode('utf-8'),'55'.decode('utf-8'),
                            '56'.decode('utf-8'),'57'.decode('utf-8'),'58'.decode('utf-8'),'59'.decode('utf-8'),]
        self.choice4 = wx.Choice(self, -1, (75, 300), choices=self.sampleList4,style=wx.SL_VERTICAL,
                                 name="Time")
        self.choice4.SetSelection(0)
#######################


        #生成年选择的下拉菜单项。
        self.sampleList01 = ['2000'.decode('utf-8'),'2001'.decode('utf-8'), '2002'.decode('utf-8'),'2003'.decode('utf-8'),
                            '2004'.decode('utf-8'),'2005'.decode('utf-8'), '2006'.decode('utf-8'),'2007'.decode('utf-8'),
                            '2008'.decode('utf-8'),'2009'.decode('utf-8'), '2010'.decode('utf-8'),'2011'.decode('utf-8'),
                            '2012'.decode('utf-8'),'2013'.decode('utf-8'), '2014'.decode('utf-8'),'2015'.decode('utf-8'),
                            '2016'.decode('utf-8'),'2017'.decode('utf-8'), '2018'.decode('utf-8'),'2019'.decode('utf-8'),
                            '2020'.decode('utf-8'),'2021'.decode('utf-8'), '2022'.decode('utf-8'),'2023'.decode('utf-8'),
                            '2024'.decode('utf-8'),'2025'.decode('utf-8'), '2026'.decode('utf-8'),'2027'.decode('utf-8'),]
        self.choice01 = wx.Choice(self, -1, (170, 140), choices=self.sampleList01,style=wx.SL_VERTICAL,
                                 name="Time")
        
        #生成月的下拉菜单选择项。
        self.sampleList11 = ['01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'), '04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'), '09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'), ]
        self.choice11 = wx.Choice(self, -1, (175, 180), choices=self.sampleList11,style=wx.SL_VERTICAL,
                                 name="Threshold")

        #生成日选择的下拉菜单项。
        self.sampleList21 = ['01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'),'04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'),'09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'),'13'.decode('utf-8'),'14'.decode('utf-8'),'15'.decode('utf-8'),
                            '16'.decode('utf-8'),'17'.decode('utf-8'),'18'.decode('utf-8'),'19'.decode('utf-8'),'20'.decode('utf-8'),
                            '21'.decode('utf-8'),'22'.decode('utf-8'),'23'.decode('utf-8'),'24'.decode('utf-8'),'25'.decode('utf-8'),
                            '26'.decode('utf-8'),'27'.decode('utf-8'),'28'.decode('utf-8'),'29'.decode('utf-8'),'30'.decode('utf-8'),
                            '31'.decode('utf-8'),]
        self.choice21 = wx.Choice(self, -1, (175, 220), choices=self.sampleList21,style=wx.SL_VERTICAL,
                                 name="Time")

        
        #生成时的下拉菜单选择项。
        self.sampleList31 = ['00'.decode('utf-8'),'01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'), '04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'), '09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'),
                            '13'.decode('utf-8'),'14'.decode('utf-8'),'15'.decode('utf-8'), '16'.decode('utf-8'),'17'.decode('utf-8'),
                            '18'.decode('utf-8'),'19'.decode('utf-8'),'20'.decode('utf-8'), '21'.decode('utf-8'),'22'.decode('utf-8'),
                            '23'.decode('utf-8'),]
        self.choice31 = wx.Choice(self, -1, (175, 260), choices=self.sampleList31,style=wx.SL_VERTICAL,
                                 name="Threshold")
        #self.choice31.SetSelection(23)
        #生成分选择的下拉菜单项。
        self.sampleList41 = ['00'.decode('utf-8'),'01'.decode('utf-8'),'02'.decode('utf-8'),'03'.decode('utf-8'),'04'.decode('utf-8'),'05'.decode('utf-8'),
                            '06'.decode('utf-8'),'07'.decode('utf-8'),'08'.decode('utf-8'),'09'.decode('utf-8'),'10'.decode('utf-8'),
                            '11'.decode('utf-8'),'12'.decode('utf-8'),'13'.decode('utf-8'),'14'.decode('utf-8'),'15'.decode('utf-8'),
                            '16'.decode('utf-8'),'17'.decode('utf-8'),'18'.decode('utf-8'),'19'.decode('utf-8'),'20'.decode('utf-8'),
                            '21'.decode('utf-8'),'22'.decode('utf-8'),'23'.decode('utf-8'),'24'.decode('utf-8'),'25'.decode('utf-8'),
                            '26'.decode('utf-8'),'27'.decode('utf-8'),'28'.decode('utf-8'),'29'.decode('utf-8'),'30'.decode('utf-8'),
                            '31'.decode('utf-8'),'32'.decode('utf-8'),'33'.decode('utf-8'),'34'.decode('utf-8'),'35'.decode('utf-8'),
                            '36'.decode('utf-8'),'37'.decode('utf-8'),'38'.decode('utf-8'),'39'.decode('utf-8'),'40'.decode('utf-8'),
                            '41'.decode('utf-8'),'42'.decode('utf-8'),'43'.decode('utf-8'),'44'.decode('utf-8'),'45'.decode('utf-8'),
                            '46'.decode('utf-8'),'47'.decode('utf-8'),'48'.decode('utf-8'),'49'.decode('utf-8'),'50'.decode('utf-8'),
                            '51'.decode('utf-8'),'52'.decode('utf-8'),'53'.decode('utf-8'),'54'.decode('utf-8'),'55'.decode('utf-8'),
                            '56'.decode('utf-8'),'57'.decode('utf-8'),'58'.decode('utf-8'),'59'.decode('utf-8'),]
        self.choice41 = wx.Choice(self, -1, (175, 300), choices=self.sampleList41,style=wx.SL_VERTICAL,
                                 name="Time")
        #self.choice41.SetSelection(59)





 #创建单选按钮。   
        self.radio1 = wx.RadioButton(self, -1, "时刻数据查询".decode('utf-8'), pos=(35, 350), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(self, -1, "时间数据查询".decode('utf-8'), pos=(150, 350))   

 #绑定单选按钮。
        for eachRadio in [self.radio1, self.radio2, ]:#绑定事件   
            self.Bind(wx.EVT_RADIOBUTTON, self.OnFind_P, eachRadio)

        global ParaFlag
        #global filename

        if self.radio1.GetValue()==True:
            ParaFlag[0]='P_radion1'
        else:
            ParaFlag[0]='P_radion2'
     

        #生成“重置”“度量”按钮，并绑定鼠标单击事件。

        colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167)]
        
        self.resetButton = buttons.GenButton(self, -1,'重置'.decode('utf-8'),size=(80,25),pos=(40, 400))
        self.resetButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.resetButton.SetBezelWidth(1000)
        self.resetButton.SetBackgroundColour(colour[3])
        self.resetButton.SetForegroundColour("white")
        self.resetButton.SetToolTipString("点击以清屏...".decode('utf-8'))
        
        self.resetButton.Bind(wx.EVT_BUTTON, self.OnClearMe)

        self.findButton = buttons.GenButton(self, -1,'查询'.decode('utf-8'),size=(80,25),pos=(155, 400))
        self.findButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.findButton.SetBezelWidth(1000)
        self.findButton.SetBackgroundColour(colour[3])
        self.findButton.SetForegroundColour("white")
        self.findButton.SetToolTipString("点击以查询数据库中的数据...".decode('utf-8'))

        self.findButton.Bind(wx.EVT_BUTTON, self.OnFindMe)


        #生成参数输出的位图表示。
        self.PicDataPutout=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(50,452),size=(27,115))
        img1= wx.Image('D:/DBS/FacePic/44.png',wx.BITMAP_TYPE_ANY).Scale(27,115)
        self.PicDataPutout.SetBitmap(wx.BitmapFromImage(img1))

        #以下生成14个参数值的文本标签。
        self.Result1=wx.StaticText(self,-1,"fmin：".decode('utf-8'),(165,460))
        self.Result1.SetFont(DownFont1)

        self.Result11=wx.TextCtrl(self, -1, "NULL", (225,460),(70,-1))
        self.Result11.DiscardEdits()

        self.Result2=wx.StaticText(self,-1,"fbEs：".decode('utf-8'),(165,504))
        self.Result2.SetFont(DownFont1)

        self.Result22=wx.TextCtrl(self, -1, "NULL", (225,504),(70,-1))
        self.Result22.DiscardEdits()

        self.Result3=wx.StaticText(self,-1,"foF2：".decode('utf-8'),(165,549))
        self.Result3.SetFont(DownFont1)

        self.Result33=wx.TextCtrl(self, -1, "NULL", (225,549),(70,-1))
        self.Result33.DiscardEdits()

        self.Result4=wx.StaticText(self,-1,"hE：".decode('utf-8'),(335,460))
        self.Result4.SetFont(DownFont1)

        self.Result44=wx.TextCtrl(self, -1, "NULL", (395,460),(70,-1))
        self.Result44.DiscardEdits()

        self.Result5=wx.StaticText(self,-1,"hF：".decode('utf-8'),(335,504))
        self.Result5.SetFont(DownFont1)

        self.Result55=wx.TextCtrl(self, -1, "NULL", (395,504),(70,-1))
        self.Result55.DiscardEdits()

        self.Result6=wx.StaticText(self,-1,"M3F2：".decode('utf-8'),(335,549))
        self.Result6.SetFont(DownFont1)

        self.Result66=wx.TextCtrl(self, -1, "NULL", (395,549),(70,-1))
        self.Result66.DiscardEdits()
        
        self.Result7=wx.StaticText(self,-1,"foE：".decode('utf-8'),(505,460))
        self.Result7.SetFont(DownFont1)

        self.Result77=wx.TextCtrl(self, -1, "NULL", (565,460),(70,-1))
        self.Result77.DiscardEdits()

        self.Result8=wx.StaticText(self,-1,"foF1：".decode('utf-8'),(505,504))
        self.Result8.SetFont(DownFont1)

        self.Result88=wx.TextCtrl(self, -1, "NULL", (565,504),(70,-1))
        self.Result88.DiscardEdits()

        self.Result9=wx.StaticText(self,-1,"fxI：".decode('utf-8'),(505,549))
        self.Result9.SetFont(DownFont1)

        self.Result99=wx.TextCtrl(self, -1, "NULL", (565,549),(70,-1))
        self.Result99.DiscardEdits()

        self.Result10=wx.StaticText(self,-1,"foEs：".decode('utf-8'),(675,460))
        self.Result10.SetFont(DownFont1)

        self.Result1010=wx.TextCtrl(self, -1, "NULL", (735,460),(70,-1))
        self.Result1010.DiscardEdits()

        self.Result11m=wx.StaticText(self,-1,"M3F1：".decode('utf-8'),(675,504))
        self.Result11m.SetFont(DownFont1)

        self.Result1111=wx.TextCtrl(self, -1, "NULL", (735,504),(70,-1))
        self.Result1111.DiscardEdits()

        self.Result12=wx.StaticText(self,-1,"hES：".decode('utf-8'),(675,549))
        self.Result12.SetFont(DownFont1)

        self.Result1212=wx.TextCtrl(self, -1, "NULL", (735,549),(70,-1))
        self.Result1212.DiscardEdits()

        self.Result13=wx.StaticText(self,-1,"Es类型：".decode('utf-8'),(845,460))
        self.Result13.SetFont(DownFont1)

        self.Result1313=wx.TextCtrl(self, -1, "NULL", (905,460),(70,-1))
        self.Result1313.DiscardEdits()

        self.Result14=wx.StaticText(self,-1,"hF2：".decode('utf-8'),(845,504))
        self.Result14.SetFont(DownFont1)

        self.Result1414=wx.TextCtrl(self, -1, "NULL", (905,504),(70,-1))
        self.Result1414.DiscardEdits()



     def OnFind_P(self,event):
        print "a"
        global ParaFlag  #此处也要注意列表的声明。
        if self.radio1.GetValue()==True:
            ParaFlag[0]='P_radion1'
            self.choicePlace.Clear()
            self.choicePlace.SetItems(self.sampleList00)
            self.choice3.Clear()
            self.choice3.SetItems(self.sampleList3)
            self.choice4.Clear()
            self.choice4.SetItems(self.sampleList4)
            self.choice31.Clear()
            self.choice31.SetItems(self.sampleList31)
            self.choice41.Clear()
            self.choice41.SetItems(self.sampleList41)
 
            self.choice3.SetSelection(0)
            self.choice4.SetSelection(0)

            #print '1'
        else:
            self.choice31.SetSelection(23)
            self.choice41.SetSelection(59)
            ParaFlag[0]='P_radion2'
        #print ParaFlag[0]
 


     def OnClearMe(self,event):

        self.choicePlace.Clear()
        self.choicePlace.SetItems(self.sampleList00)
        self.choice0.Clear()
        self.choice0.SetItems(self.sampleList0)
        self.choice1.Clear()
        self.choice1.SetItems(self.sampleList1)
        self.choice2.Clear()
        self.choice2.SetItems(self.sampleList2)
        self.choice3.Clear()
        self.choice3.SetItems(self.sampleList3)
        self.choice4.Clear()
        self.choice4.SetItems(self.sampleList4)

        self.choice01.Clear()
        self.choice01.SetItems(self.sampleList01)
        self.choice11.Clear()
        self.choice11.SetItems(self.sampleList11)
        self.choice21.Clear()
        self.choice21.SetItems(self.sampleList21)
        self.choice31.Clear()
        self.choice31.SetItems(self.sampleList31)
        self.choice41.Clear()
        self.choice41.SetItems(self.sampleList41)
 
        self.choice3.SetSelection(0)
        self.choice4.SetSelection(0)


        
        self.Result11.SetLabel("NULL".decode('utf-8'))
        self.Result22.SetLabel("NULL".decode('utf-8'))
        self.Result33.SetLabel("NULL".decode('utf-8'))
        self.Result44.SetLabel("NULL".decode('utf-8'))
        self.Result55.SetLabel("NULL".decode('utf-8'))
        self.Result66.SetLabel("NULL".decode('utf-8'))
        self.Result77.SetLabel("NULL".decode('utf-8'))
        self.Result88.SetLabel("NULL".decode('utf-8'))
        self.Result99.SetLabel("NULL".decode('utf-8'))
        self.Result1010.SetLabel("NULL".decode('utf-8'))
        self.Result1111.SetLabel("NULL".decode('utf-8'))
        self.Result1212.SetLabel("NULL".decode('utf-8'))
        self.Result1313.SetLabel("NULL".decode('utf-8'))
        self.Result1414.SetLabel("NULL".decode('utf-8'))


        #以下是给报表单元格的内容重置。
        for row in range(2000):
            for col in range(18):
                self.grid.SetCellValue(row, col,"" )

        self.grid.SetCellValue(0,0,"P_id")
        self.grid.SetCellValue(0,1,"file_name")
        self.grid.SetCellValue(0,2,"fmin")
        self.grid.SetCellValue(0,3,"fbEs")
        self.grid.SetCellValue(0,4,"foF2")
        self.grid.SetCellValue(0,5,"hE")
        self.grid.SetCellValue(0,6,"hF")
        self.grid.SetCellValue(0,7,"M3F2")
        self.grid.SetCellValue(0,8,"foE")
        self.grid.SetCellValue(0,9,"foF1")
        self.grid.SetCellValue(0,10,"fx1")
        self.grid.SetCellValue(0,11,"foEs")
        self.grid.SetCellValue(0,12,"M3F1")
        self.grid.SetCellValue(0,13,"hEs")
        self.grid.SetCellValue(0,14,"Es")
        self.grid.SetCellValue(0,15,"hF2")
        self.grid.SetCellValue(0,16,"time")
        self.grid.SetCellValue(0,17,"place")


     def OnFindMe(self,event):
        global find_data
        global find_data1
        global filename
        global ParaFlag
        global par_several

        filename[:]=[]


        ##遍历数据库并保存数据库文件名字。
        ii=1
        while 1:
            con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
            cur=con.cursor()
            cur.execute("Select * From parameters where P_id=\'%s\'" %(ii))
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            if len(ReadFileSeePic)==0:
                break               
            else:
                filename.append(ReadFileSeePic[0][1])
                ii=ii+1

        print filename,"filename在此处很关键的一部遍历"
        par_several[:]=[]
        
        filename_flag=0
        find_data[:]=[]
        find_data1[:]=[]

        find_data.append(self.choice0.GetStringSelection())
        find_data.append(self.choice1.GetStringSelection())
        find_data.append(self.choice2.GetStringSelection())
        find_data.append(self.choice3.GetStringSelection())
        find_data.append(self.choice4.GetStringSelection())
        s = "".join(itertools.chain(*find_data))

        find_data1.append(self.choice01.GetStringSelection())
        find_data1.append(self.choice11.GetStringSelection())
        find_data1.append(self.choice21.GetStringSelection())
        find_data1.append(self.choice31.GetStringSelection())
        find_data1.append(self.choice41.GetStringSelection())
        s1 = "".join(itertools.chain(*find_data1))
 
        
        print s
        print len(s1),'len(s1)'
        #print filename
        for i in range(0,len(filename)):
            if len(filename[i])>12:
                s2=filename[i]
                s11=s2[0:12]
                print s11
                if s11==s:
                    filename_flag=1
        if filename_flag==0 and ParaFlag[0]=='P_radion1':
            #下面新建错误输入的提示对话框并完成设置。
            dlg = wx.MessageDialog(None, "检索不到您要查询的数据文件！".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                dlg.Destroy()
        elif filename_flag==1 and ParaFlag[0]=='P_radion1':
            print "I can find it!!!lalalal~~"       

            #cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
            con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
            cur=con.cursor()
            cur.execute("Select * From parameters where time=\'%s\'" %(s))
            ReadFileSeePara=cur.fetchall()
            cur.close()
            print ReadFileSeePara[0][31]
            if ReadFileSeePara[0][31]!=self.choicePlace.GetStringSelection():
                #下面新建站点可能输入错误的提示对话框并完成设置。
                dlg = wx.MessageDialog(None, "检索到要查询的数据文件但是站点不符合！请再次检查您输入的检测站点！".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
                retCode = dlg.ShowModal()
                if (retCode == wx.ID_YES):
                    dlg.Destroy()
            else:
                self.Result11.SetLabel(ReadFileSeePara[0][2].decode('utf-8'))
                self.Result22.SetLabel(ReadFileSeePara[0][3].decode('utf-8'))
                self.Result33.SetLabel(ReadFileSeePara[0][4].decode('utf-8'))
                self.Result44.SetLabel(ReadFileSeePara[0][5].decode('utf-8'))
                self.Result55.SetLabel(ReadFileSeePara[0][6].decode('utf-8'))
                self.Result66.SetLabel(ReadFileSeePara[0][7].decode('utf-8'))
                self.Result77.SetLabel(ReadFileSeePara[0][8].decode('utf-8'))
                self.Result88.SetLabel(ReadFileSeePara[0][9].decode('utf-8'))
                self.Result99.SetLabel(ReadFileSeePara[0][10].decode('utf-8'))
                self.Result1010.SetLabel(ReadFileSeePara[0][11].decode('utf-8'))
                self.Result1111.SetLabel(ReadFileSeePara[0][12].decode('utf-8'))
                self.Result1212.SetLabel(ReadFileSeePara[0][13].decode('utf-8'))
                self.Result1313.SetLabel(ReadFileSeePara[0][14].decode('utf-8'))
                self.Result1414.SetLabel(ReadFileSeePara[0][15].decode('utf-8'))
                
                #########下面是针对单个的数据查询赋值区域###########################
                
                self.grid.SetCellValue(1, 0,"%s" % (ReadFileSeePara[0][0].decode('utf-8')))
                self.grid.SetCellValue(1, 1,"%s" % (ReadFileSeePara[0][1].decode('utf-8')))
                self.grid.SetCellValue(1, 2,"%s" % (ReadFileSeePara[0][2].decode('utf-8')))
                self.grid.SetCellValue(1, 3,"%s" % (ReadFileSeePara[0][3].decode('utf-8')))
                self.grid.SetCellValue(1, 4,"%s" % (ReadFileSeePara[0][4].decode('utf-8')))
                self.grid.SetCellValue(1, 5,"%s" % (ReadFileSeePara[0][5].decode('utf-8')))
                self.grid.SetCellValue(1, 6,"%s" % (ReadFileSeePara[0][6].decode('utf-8')))
                self.grid.SetCellValue(1, 7,"%s" % (ReadFileSeePara[0][7].decode('utf-8')))
                self.grid.SetCellValue(1, 8,"%s" % (ReadFileSeePara[0][8].decode('utf-8')))
                self.grid.SetCellValue(1, 9,"%s" % (ReadFileSeePara[0][9].decode('utf-8')))
                self.grid.SetCellValue(1, 10,"%s" % (ReadFileSeePara[0][10].decode('utf-8')))
                self.grid.SetCellValue(1, 11,"%s" % (ReadFileSeePara[0][11].decode('utf-8')))
                self.grid.SetCellValue(1, 12,"%s" % (ReadFileSeePara[0][12].decode('utf-8')))
                self.grid.SetCellValue(1, 13,"%s" % (ReadFileSeePara[0][13].decode('utf-8')))
                self.grid.SetCellValue(1, 14,"%s" % (ReadFileSeePara[0][14].decode('utf-8')))
                self.grid.SetCellValue(1, 15,"%s" % (ReadFileSeePara[0][15].decode('utf-8')))
                self.grid.SetCellValue(1, 16,"%s" % (ReadFileSeePara[0][30].decode('utf-8')))
                self.grid.SetCellValue(1, 17,"%s" % (ReadFileSeePara[0][31].encode('gbk')))


                


#############以下是核心检索数据库的时间段数据。
        elif ParaFlag[0]=='P_radion2':

##            global filename
##            filename[:]=[]
##            for i in range(1,3):
##                con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
##                cur=con.cursor()
##                cur.execute("Select * From parameters where P_id=\'%s\'" %(i))
##                ReadFileSeePic=cur.fetchall()
##                cur.close()
##                cur.close()
##                if len(ReadFileSeePic)==0:
##                    #break
##                    print 'ss'
##                else:
##                    filename.append(ReadFileSeePic[0][1])
##


           
            if len(s1)!=12 and len(s)!=12 :
                dlg = wx.MessageDialog(None, "请您正确输入检索数据的信息！".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
                retCode = dlg.ShowModal()
                if (retCode == wx.ID_YES):
                    dlg.Destroy()
            else :
                for i in range(0,len(filename)):
                    if len(filename[i])>12:
                        s2=filename[i]
                        s11=s2[0:12]
                        print s,s11,s1,"s s11 s1"
                        if int(s1)>=int(s11)>=int(s):
                            par_several.append(filename[i])
                            print par_several,"par_several"
                if len(par_several)==0 :
                    dlg = wx.MessageDialog(None, "检索不到您输入的时间段的数据文件！".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
                    retCode = dlg.ShowModal()
                    if (retCode == wx.ID_YES):
                        dlg.Destroy()
                else:
                    for i in range(0,len(par_several)):
                        print par_several[i],"par_several[i]"
                        con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
                        cur=con.cursor()
                        cur.execute("Select * From parameters where time=\'%s\'" %(par_several[i][0:12]))
                        ReadFileSeePic=cur.fetchall()
                        cur.close()
                        cur.close()

                        #print ReadFileSeePic
                        #print ReadFileSeePic[0]
                        #print ReadFileSeePic[0][0]
                        
                        self.grid.SetCellValue(i+1, 0,"%s" % (ReadFileSeePic[0][0].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 1,"%s" % (ReadFileSeePic[0][1].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 2,"%s" % (ReadFileSeePic[0][2].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 3,"%s" % (ReadFileSeePic[0][3].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 4,"%s" % (ReadFileSeePic[0][4].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 5,"%s" % (ReadFileSeePic[0][5].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 6,"%s" % (ReadFileSeePic[0][6].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 7,"%s" % (ReadFileSeePic[0][7].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 8,"%s" % (ReadFileSeePic[0][8].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 9,"%s" % (ReadFileSeePic[0][9].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 10,"%s" % (ReadFileSeePic[0][10].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 11,"%s" % (ReadFileSeePic[0][11].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 12,"%s" % (ReadFileSeePic[0][12].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 13,"%s" % (ReadFileSeePic[0][13].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 14,"%s" % (ReadFileSeePic[0][14].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 15,"%s" % (ReadFileSeePic[0][15].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 16,"%s" % (ReadFileSeePic[0][30].decode('utf-8')))
                        self.grid.SetCellValue(i+1, 17,"%s" % (ReadFileSeePic[0][31].encode('gbk')))



        #grid.SetCellValue(row, col,"(%d,%d)" % (row, col))
        #grid.SetCellValue(1,1,"201002020930p30s1.0h0.0V.O")
        #grid.SetCellValue(1,16,"201002020930")
        #grid.SetCellValue(1,17,"青岛站".decode('utf-8'))
        #grid.SetCellValue(2,2,"190.000000")            

#绘画Paint0。
     def Paint0(self,event):
        dc = wx.PaintDC(self)
        
        dc.SetPen(wx.Pen((192,192,192),1))
        rect7 = wx.Rect(10,15,1065,425)
        dc.DrawRoundedRectangleRect(rect7, 10)        
        rect4 = wx.Rect(20,30,250,410)
        dc.DrawRoundedRectangleRect(rect4, 10)        
        rect5 = wx.Rect(270,30,792,410)
        dc.DrawRoundedRectangleRect(rect5, 10)
        rect6 = wx.Rect(65,440,965,150)
        dc.DrawRoundedRectangleRect(rect6, 10)

        #以下是给数据输出区域画图。
        dc.SetPen(wx.Pen((192,192,192),1))
        rect8 = wx.Rect(115,445,880,139)
        dc.DrawRoundedRectangleRect(rect8,10)
        rect9 = wx.Rect(115,445,880,46)
        dc.DrawRoundedRectangleRect(rect9,10)
        rect10 = wx.Rect(115,491,880,46)
        dc.DrawRoundedRectangleRect(rect10,10)
        rect11 = wx.Rect(115,537,880,46)
        dc.DrawRoundedRectangleRect(rect11,10)


        #以下是给按钮画出边框，使之立体化。
        dc.SetPen(wx.Pen('black',1))
        rect1 = wx.Rect(33+5, 398, 84, 29) 
        dc.DrawRoundedRectangleRect(rect1, 1)
        rect2 = wx.Rect(148+5, 398, 84, 29) 
        dc.DrawRoundedRectangleRect(rect2, 1)    


############################手动度量######################################
class PageThree(wx.Panel):
     def __init__(self, parent):          
        wx.Panel.__init__(self, parent)
        self.toolkit = parent

        
        #绑定画板的边线底纹绘制（Paint0部分）。
        self.Bind(wx.EVT_PAINT, self.Paint0)

        #绑定键盘事件。
        #self.PicShow.Bind(wx.EVT_KEY_UP , self.OnKeyUp1)
        
        colour = [(255,255,255),(153,204,255),(151,253,225),]
        self.SetBackgroundColour(colour[0])


        #注意定义全局变量中的列表的声明方法。
        global PicFlag
        global Flag1,Flag2,Flag3
        global a
        global threshold
        global foF1
        global foF2
        global fxF2
        global hF1
        global hF2
        global fmin
        global posX
        global posY
        global FlagClick
        global timeFlag1
        global timeFlag3
        global fre
        global result

#生成空位图。下面这一段关系到缓冲区画图的前置，非常重要！

        self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(245, 35),size=(820,400))
        self.img = wx.Image('D:/DBS/FacePic/a.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
        #very important！！！
        self.bitmap=wx.BitmapFromImage(self.img)
        self.PicShow.SetBitmap(self.bitmap)
        #绑定键盘事件。
        #self.PicShow.Bind(wx.EVT_KEY_UP , self.OnKeyUp1)

#制作标尺游标图。
        self.PicY1=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 30),size=(9,8))
        self.img1 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap1=wx.BitmapFromImage(self.img1)
        self.PicY1.SetBitmap(self.bitmap1)
        self.PicY11=wx.StaticText(self, -1, "800", pos=(213, 27))

        self.PicY2=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 80),size=(9,8))
        self.img2 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap2=wx.BitmapFromImage(self.img2)
        self.PicY2.SetBitmap(self.bitmap2)
        self.PicY22=wx.StaticText(self, -1, "700", pos=(213, 77))

        self.PicY3=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 130),size=(9,8))
        self.img3 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap3=wx.BitmapFromImage(self.img3)
        self.PicY3.SetBitmap(self.bitmap3)
        self.PicY33=wx.StaticText(self, -1, "600", pos=(213, 127))

        self.PicY4=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 180),size=(9,8))
        self.img4 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap4=wx.BitmapFromImage(self.img4)
        self.PicY4.SetBitmap(self.bitmap4)
        self.PicY44=wx.StaticText(self, -1, "500", pos=(213, 177))

        self.PicY5=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 230),size=(9,8))
        self.img5 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap5=wx.BitmapFromImage(self.img5)
        self.PicY5.SetBitmap(self.bitmap5)
        self.PicY55=wx.StaticText(self, -1, "400", pos=(213, 227))

        self.PicY6=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 280),size=(9,8))
        self.img6 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap6=wx.BitmapFromImage(self.img6)
        self.PicY6.SetBitmap(self.bitmap6)
        self.PicY66=wx.StaticText(self, -1, "300", pos=(213, 277))

        self.PicY7=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 330),size=(9,8))
        self.img7 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap7=wx.BitmapFromImage(self.img7)
        self.PicY7.SetBitmap(self.bitmap7)
        self.PicY77=wx.StaticText(self, -1, "200", pos=(213, 327))

        self.PicY8=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 380),size=(9,8))
        self.img8 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap8=wx.BitmapFromImage(self.img8)
        self.PicY8.SetBitmap(self.bitmap8)
        self.PicY88=wx.StaticText(self, -1, "100", pos=(213, 377))

        self.PicY9=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(234, 429),size=(9,8))
        self.img9 = wx.Image('D:/DBS/FacePic/left.ico',wx.BITMAP_TYPE_ANY).Scale(9,8)
        self.bitmap9=wx.BitmapFromImage(self.img9)
        self.PicY9.SetBitmap(self.bitmap9)
        self.PicY99=wx.StaticText(self, -1, "000", pos=(213, 425))

        self.PicX1=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(240, 25),size=(8,9))
        self.imgx1 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx1=wx.BitmapFromImage(self.imgx1)
        self.PicX1.SetBitmap(self.bitmapx1)
        self.PicX11=wx.StaticText(self, -1, "1.0", pos=(235, 11))



        self.PicX2=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(291, 25),size=(8,9))
        self.imgx2 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx2=wx.BitmapFromImage(self.imgx2)
        self.PicX2.SetBitmap(self.bitmapx2)
        self.PicX22=wx.StaticText(self, -1, '2.2', pos=(286, 11))


        self.PicX3=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(342, 25),size=(8,9))
        self.imgx3 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx3=wx.BitmapFromImage(self.imgx3)
        self.PicX3.SetBitmap(self.bitmapx3)
        self.PicX33=wx.StaticText(self, -1, "3.4", pos=(337, 11))



        self.PicX4=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(394, 25),size=(8,9))
        self.imgx4 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx4=wx.BitmapFromImage(self.imgx4)
        self.PicX4.SetBitmap(self.bitmapx4)
        self.PicX44=wx.StaticText(self, -1, "4.6", pos=(389, 11))


        self.PicX5=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(445, 25),size=(8,9))
        self.imgx5 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx5=wx.BitmapFromImage(self.imgx5)
        self.PicX5.SetBitmap(self.bitmapx5)
        self.PicX55=wx.StaticText(self, -1, "5.8", pos=(440, 11))

        self.PicX6=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(496, 25),size=(8,9))
        self.imgx6 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx6=wx.BitmapFromImage(self.imgx6)
        self.PicX6.SetBitmap(self.bitmapx6)
        self.PicX66=wx.StaticText(self, -1, "7.0", pos=(491, 11))

        self.PicX7=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(548, 25),size=(8,9))
        self.imgx7 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx7=wx.BitmapFromImage(self.imgx7)
        self.PicX7.SetBitmap(self.bitmapx7)
        self.PicX77=wx.StaticText(self, -1, "8.2", pos=(543, 11))

        self.PicX8=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(599, 25),size=(8,9))
        self.imgx8 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx8=wx.BitmapFromImage(self.imgx8)
        self.PicX8.SetBitmap(self.bitmapx8)
        self.PicX88=wx.StaticText(self, -1, "9.4", pos=(594, 11))


        self.PicX9=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(650, 25),size=(8,9))
        self.imgx9 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx9=wx.BitmapFromImage(self.imgx9)
        self.PicX9.SetBitmap(self.bitmapx9)
        self.PicX99=wx.StaticText(self, -1, "10.6", pos=(642, 11))


        self.PicX10=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(702, 25),size=(8,9))
        self.imgx10 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx10=wx.BitmapFromImage(self.imgx10)
        self.PicX10.SetBitmap(self.bitmapx10)
        self.PicX1010=wx.StaticText(self, -1, "11.8", pos=(694, 11))

        self.PicX11=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(753, 25),size=(8,9))
        self.imgx11 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx11=wx.BitmapFromImage(self.imgx11)
        self.PicX11.SetBitmap(self.bitmapx11)
        self.PicX1111=wx.StaticText(self, -1, "13", pos=(749, 11))

        self.PicX12=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(804, 25),size=(8,9))
        self.imgx12 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx12=wx.BitmapFromImage(self.imgx12)
        self.PicX12.SetBitmap(self.bitmapx12)
        self.PicX1212=wx.StaticText(self, -1, "14.2", pos=(796, 11))

        self.PicX13=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(856, 25),size=(8,9))
        self.imgx13 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx13=wx.BitmapFromImage(self.imgx13)
        self.PicX13.SetBitmap(self.bitmapx13)
        self.PicX1313=wx.StaticText(self, -1, "15.4", pos=(848, 11))

        self.PicX14=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(907, 25),size=(8,9))
        self.imgx14 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx14=wx.BitmapFromImage(self.imgx14)
        self.PicX14.SetBitmap(self.bitmapx14)
        self.PicX1414=wx.StaticText(self, -1, "16.6", pos=(899, 11))


        self.PicX15=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(959, 25),size=(8,9))
        self.imgx15 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx15=wx.BitmapFromImage(self.imgx15)
        self.PicX15.SetBitmap(self.bitmapx15)
        self.PicX1515=wx.StaticText(self, -1, "17.8", pos=(951, 11))


        self.PicX16=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(1010, 25),size=(8,9))
        self.imgx16 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx16=wx.BitmapFromImage(self.imgx16)
        self.PicX16.SetBitmap(self.bitmapx16)
        self.PicX1616=wx.StaticText(self, -1, "19", pos=(1005, 11))


        self.PicX17=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(1060, 25),size=(8,9))
        self.imgx17 = wx.Image('D:/DBS/FacePic/up.ico',wx.BITMAP_TYPE_ANY).Scale(8,9)
        self.bitmapx17=wx.BitmapFromImage(self.imgx17)
        self.PicX17.SetBitmap(self.bitmapx17)
        self.PicX1717=wx.StaticText(self, -1, "20.2", pos=(1048, 11))


        
        
                
#绑定位图的鼠标移动位置标记（OnMove事件）
        self.PicShow.Bind(wx.EVT_MOTION, self.OnMove)


#创建展示鼠标位置所需的文本框。
        TextPos=wx.StaticText(self, -1, "Pos:", pos=(30, 302)) 
        self.posCtrl = wx.TextCtrl(self, -1, "",size=(120,20), pos=(60, 300) , style=wx.TE_READONLY)

        TextPosX=wx.StaticText(self, -1, "PosX:", pos=(30, 342)) 
        self.posCtrlX = wx.TextCtrl(self, -1, "",size=(80,20), pos=(60, 340), style=wx.TE_MULTILINE|wx.TE_READONLY)

        TextPosY=wx.StaticText(self, -1, "PosY:", pos=(30, 382)) 
        self.posCtrlY = wx.TextCtrl(self, -1, "",size=(80,20), pos=(60, 380), style=wx.TE_MULTILINE|wx.TE_READONLY)

        #self.PicShow.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown) 
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClick)
        self.leftDown = 0

#绑定图片显示区的画标尺事件。
        #self.PicShow.Bind(wx.EVT_PAINT, self.OnClick)



#生成参数输出的位图表示。
        self.PicDataPutout=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(50,452),size=(27,115))
        img1= wx.Image('D:/DBS/FacePic/44.png',wx.BITMAP_TYPE_ANY).Scale(27,115)
        self.PicDataPutout.SetBitmap(wx.BitmapFromImage(img1))


        DownFont1 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)


        #以下生成14个参数值的文本标签。
        self.Result1=wx.StaticText(self,-1,"fmin：".decode('utf-8'),(165,460))
        self.Result1.SetFont(DownFont1)

        self.Result11=wx.TextCtrl(self, -1, "NULL", (210,460),(45,-1))
        self.Result11.DiscardEdits()

        h = self.Result11.GetSize().height
        self.spin1 = wx.SpinButton(self, -1,(255, 459),(h*2/3, h),wx.SP_VERTICAL)
        self.spin1.SetRange(1, 1000)
        #self.spin1.SetValue()
        self.Bind(wx.EVT_SPIN, self.OnSpin1, self.spin1)
        

        self.Result2=wx.StaticText(self,-1,"fbEs：".decode('utf-8'),(165,504))
        self.Result2.SetFont(DownFont1)

        self.Result22=wx.TextCtrl(self, -1, "NULL", (210,504),(45,-1))
        self.Result22.DiscardEdits()
        h = self.Result22.GetSize().height
        self.spin2 = wx.SpinButton(self, -1,(255, 503),(h*2/3, h),wx.SP_VERTICAL)


        self.Result3=wx.StaticText(self,-1,"foF2：".decode('utf-8'),(165,549))
        self.Result3.SetFont(DownFont1)

        self.Result33=wx.TextCtrl(self, -1, "NULL", (210,549),(45,-1))
        self.Result33.DiscardEdits()
        h = self.Result33.GetSize().height
        self.spin3 = wx.SpinButton(self, -1,(255, 548),(h*2/3, h),wx.SP_VERTICAL)
        self.spin3.SetRange(1, 1000)
        #self.spin3.SetValue()
        self.Bind(wx.EVT_SPIN, self.OnSpin3, self.spin3)


        self.Result4=wx.StaticText(self,-1,"hE：".decode('utf-8'),(335,460))
        self.Result4.SetFont(DownFont1)

        self.Result44=wx.TextCtrl(self, -1, "NULL", (380,460),(45,-1))
        self.Result44.DiscardEdits()
        h = self.Result44.GetSize().height
        self.spin4 = wx.SpinButton(self, -1,(425, 459),(h*2/3, h),wx.SP_VERTICAL)

        self.Result5=wx.StaticText(self,-1,"hF：".decode('utf-8'),(335,504))
        self.Result5.SetFont(DownFont1)

        self.Result55=wx.TextCtrl(self, -1, "NULL", (380,504),(45,-1))
        self.Result55.DiscardEdits()
        h = self.Result55.GetSize().height
        self.spin5 = wx.SpinButton(self, -1,(425, 503),(h*2/3, h),wx.SP_VERTICAL)
        self.spin5.SetRange(1, 1000)
        #self.spin5.SetValue()
        self.Bind(wx.EVT_SPIN, self.OnSpin5, self.spin5)


        self.Result6=wx.StaticText(self,-1,"M3F2：".decode('utf-8'),(335,549))
        self.Result6.SetFont(DownFont1)

        self.Result66=wx.TextCtrl(self, -1, "NULL", (380,549),(45,-1))
        self.Result66.DiscardEdits()
        h = self.Result66.GetSize().height
        self.spin6 = wx.SpinButton(self, -1,(425, 548),(h*2/3, h),wx.SP_VERTICAL)
        
        self.Result7=wx.StaticText(self,-1,"foE：".decode('utf-8'),(505,460))
        self.Result7.SetFont(DownFont1)

        self.Result77=wx.TextCtrl(self, -1, "NULL", (550,460),(45,-1))
        self.Result77.DiscardEdits()
        h = self.Result77.GetSize().height
        self.spin7 = wx.SpinButton(self, -1,(595, 459),(h*2/3, h),wx.SP_VERTICAL)

        self.Result8=wx.StaticText(self,-1,"foF1：".decode('utf-8'),(505,504))
        self.Result8.SetFont(DownFont1)

        self.Result88=wx.TextCtrl(self, -1, "NULL", (550,504),(45,-1))
        self.Result88.DiscardEdits()
        h = self.Result88.GetSize().height
        self.spin8 = wx.SpinButton(self, -1,(595, 503),(h*2/3, h),wx.SP_VERTICAL)
        self.spin8.SetRange(1, 1000)
        #self.spin8.SetValue()
        self.Bind(wx.EVT_SPIN, self.OnSpin8, self.spin8)


        self.Result9=wx.StaticText(self,-1,"fxI：".decode('utf-8'),(505,549))
        self.Result9.SetFont(DownFont1)

        self.Result99=wx.TextCtrl(self, -1, "NULL", (550,549),(45,-1))
        self.Result99.DiscardEdits()
        h = self.Result99.GetSize().height
        self.spin9 = wx.SpinButton(self, -1,(595, 548),(h*2/3, h),wx.SP_VERTICAL)
        self.spin9.SetRange(1, 1000)
        #self.spin9.SetValue()
        self.Bind(wx.EVT_SPIN, self.OnSpin9, self.spin9)        

        self.Result10=wx.StaticText(self,-1,"foEs：".decode('utf-8'),(675,460))
        self.Result10.SetFont(DownFont1)

        self.Result1010=wx.TextCtrl(self, -1, "NULL", (720,460),(45,-1))
        self.Result1010.DiscardEdits()
        h = self.Result1010.GetSize().height
        self.spin10 = wx.SpinButton(self, -1,(765, 459),(h*2/3, h),wx.SP_VERTICAL)
        

        self.Result11m=wx.StaticText(self,-1,"M3F1：".decode('utf-8'),(675,504))
        self.Result11m.SetFont(DownFont1)

        self.Result1111=wx.TextCtrl(self, -1, "NULL", (720,504),(45,-1))
        self.Result1111.DiscardEdits()
        h = self.Result1111.GetSize().height
        self.spin11 = wx.SpinButton(self, -1,(765, 503),(h*2/3, h),wx.SP_VERTICAL)
    

        self.Result12=wx.StaticText(self,-1,"hES：".decode('utf-8'),(675,549))
        self.Result12.SetFont(DownFont1)

        self.Result1212=wx.TextCtrl(self, -1, "NULL", (720,549),(45,-1))
        self.Result1212.DiscardEdits()
        h = self.Result1212.GetSize().height
        self.spin12 = wx.SpinButton(self, -1,(765, 548),(h*2/3, h),wx.SP_VERTICAL)
        

        self.Result13=wx.StaticText(self,-1,"Es类型：".decode('utf-8'),(841,460))
        self.Result13.SetFont(DownFont1)

        self.Result1313=wx.TextCtrl(self, -1, "NULL", (890,460),(45,-1))
        self.Result1313.DiscardEdits()
        h = self.Result1313.GetSize().height
        self.spin13 = wx.SpinButton(self, -1,(935, 459),(h*2/3, h),wx.SP_VERTICAL)
        

        self.Result14=wx.StaticText(self,-1,"hF2：".decode('utf-8'),(845,504))
        self.Result14.SetFont(DownFont1)

        self.Result1414=wx.TextCtrl(self, -1, "NULL", (890,504),(45,-1))
        self.Result1414.DiscardEdits()
        h = self.Result1414.GetSize().height
        self.spin14 = wx.SpinButton(self, -1,(935, 503),(h*2/3, h),wx.SP_VERTICAL)
        self.spin14.SetRange(1, 1000)
        #self.spin14.SetValue()
        self.Bind(wx.EVT_SPIN, self.OnSpin14, self.spin14)        

#生成手指pointy图片。
        
        self.Result11Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(275,453),size=(40,30))
        self.Result11.Bind(wx.EVT_LEFT_DOWN, self.OnPointy1)
        
        

        self.Result22Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(275,497),size=(40,30))
        self.Result22.Bind(wx.EVT_LEFT_DOWN, self.OnPointy2)



        self.Result33Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(275,542),size=(40,30))
        self.Result33.Bind(wx.EVT_LEFT_DOWN, self.OnPointy3)


        self.Result44Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(445,453),size=(40,30))
        self.Result44.Bind(wx.EVT_LEFT_DOWN, self.OnPointy4)


        self.Result55Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(445,497),size=(40,30))
        self.Result55.Bind(wx.EVT_LEFT_DOWN, self.OnPointy5)


        self.Result66Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(445,542),size=(40,30))
        self.Result66.Bind(wx.EVT_LEFT_DOWN, self.OnPointy6)

        self.Result77Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(615,453),size=(40,30))
        self.Result77.Bind(wx.EVT_LEFT_DOWN, self.OnPointy7)



        self.Result88Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(615,497),size=(40,30))
        self.Result88.Bind(wx.EVT_LEFT_DOWN, self.OnPointy8)



        self.Result99Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(615,542),size=(40,30))
        self.Result99.Bind(wx.EVT_LEFT_DOWN, self.OnPointy9)



        self.Result1010Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(785,453),size=(40,30))
        self.Result1010.Bind(wx.EVT_LEFT_DOWN, self.OnPointy10)



        self.Result1111Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(785,497),size=(40,30))
        self.Result1111.Bind(wx.EVT_LEFT_DOWN, self.OnPointy11)



        self.Result1212Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(785,542),size=(40,30))
        self.Result1212.Bind(wx.EVT_LEFT_DOWN, self.OnPointy12)


        self.Result1313Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(954,453),size=(40,30))
        self.Result1313.Bind(wx.EVT_LEFT_DOWN, self.OnPointy13)



        self.Result1414Pic=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(954,497),size=(40,30))
        self.Result1414.Bind(wx.EVT_LEFT_DOWN, self.OnPointy14)



        colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167)]
        self.ChangeButton = buttons.GenButton(self, -1,'保存修改'.decode('utf-8'),size=(80,22),pos=(865, 549))
        self.ChangeButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.ChangeButton.SetBezelWidth(1000)
        self.ChangeButton.SetBackgroundColour(colour[3])
        self.ChangeButton.SetForegroundColour("white")
        self.ChangeButton.SetToolTipString("点击以保存修改后的参数...".decode('utf-8'))

        self.ChangeButton.Bind(wx.EVT_BUTTON, self.PChange)

        #缓冲记忆标尺的图片。
        self.memDC=wx.MemoryDC(self.bitmap)

     def OnSpin1(self,event):
         
        global spinFlag
        global spinFlagUp
        global spinFlagDown
        global NumspinFlagUp
        global NumspinFlagDown
        global fre
        global result
        
        if self.Result11.GetValue()[0:4]=='NULL':
            event.Skip()
        else:
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Unbind(wx.EVT_LEFT_UP,id=-1,handler=None)
            #img = wx.Image('D:/DBS/PaintedOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
            #self.PicShow.SetBitmap(wx.BitmapFromImage(img))
            if fre==1:
                MiniData=float(self.Result11.GetValue()[0:5])
                result=MiniData
            fre=fre+1
            result=result
            spinFlag=event.GetPosition()
            if NumspinFlagUp>1:
                if  int(NumspinFlagUp)==int(spinFlag):
                    result=result+0.02
                    result1=result
                                      
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))                            
                                 
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp=NumspinFlagUp+1
                else:
                    result=result-0.02
                    result1=result
                                       
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))

                    else:

                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))                        
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp=NumspinFlagUp-1
            else:
                print 'pos',event.GetPosition()
                if int(event.GetPosition())==2:
                    result=result+0.02
                    result1=result
                    
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))                       
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp=NumspinFlagUp+2
                else:
                    result=result-0.02
                    result1=result
                    
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result11.SetValue(str(q))
                        else:
                            self.Result11.SetValue(str(p))                    
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp=2
        

            #以下是给图片显示区画移动标尺。
            x=(result-1)*42.7083
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine(x, 0, x, 400)
            self.posCtrlX.SetValue(str(result))
            #self.posCtrlY.SetValue(str(result))  

     def OnSpin3(self,event):
         
        global spinFlag3
        global spinFlagUp3
        global spinFlagDown3
        global NumspinFlagUp3
        global NumspinFlagDown3
        global fre
        global result
        
         
        if self.Result33.GetValue()[0:4]=='NULL':
            event.Skip()
        else:
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Unbind(wx.EVT_LEFT_UP,id=-1,handler=None)
            #img = wx.Image('D:/DBS/PaintedOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
            #self.PicShow.SetBitmap(wx.BitmapFromImage(img))
            #MiniData=float(self.Result33.GetValue()[0:5])
            if fre==1:
                MiniData=float(self.Result33.GetValue()[0:5])
                result=MiniData
            fre=fre+1
            result=result
    
            spinFlag3=event.GetPosition()

            ##############
            if NumspinFlagUp3>1:
                if  int(NumspinFlagUp3)==int(spinFlag3):
                    result=result+0.02
                    result1=result
                                      
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))                            
                                 
                    #self.Result11.SetValue(str(result))

                    
                    NumspinFlagUp3=NumspinFlagUp3+1
                else:
                    result=result-0.02
                    result1=result
                                       
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))

                    else:

                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))                        
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp3=NumspinFlagUp3-1
            else:
                print 'pos',event.GetPosition()
                if int(event.GetPosition())==2:
                    result=result+0.02
                    result1=result
                    
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))                       
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp3=NumspinFlagUp3+2
                else:
                    result=result-0.02
                    result1=result
                    
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result33.SetValue(str(q))
                        else:
                            self.Result33.SetValue(str(p))                    
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp3=2
        

            #以下是给图片显示区画标尺。
            x=(result-1)*42.7083
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine(x, 0, x, 400)
            self.posCtrlX.SetValue(str(result))
            #self.posCtrlY.SetValue(str(result)) 


     def OnSpin5(self,event):
         
        global spinFlag5
        global spinFlagUp5
        global spinFlagDown5
        global NumspinFlagUp5
        global NumspinFlagDown5
        global fre
        global result
        
        
        if self.Result55.GetValue()[0:4]=='NULL':
            event.Skip()
        else:
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Unbind(wx.EVT_LEFT_UP,id=-1,handler=None)
            #img = wx.Image('D:/DBS/PaintedOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
            #self.PicShow.SetBitmap(wx.BitmapFromImage(img))
            MiniData=float(self.Result55.GetValue()[0:5])

            spinFlag5=event.GetPosition()


            if NumspinFlagUp5>1:
                if  int(NumspinFlagUp5)==int(spinFlag5):
                    result=MiniData+1
                    self.Result55.SetValue(str(result))
                    NumspinFlagUp5=NumspinFlagUp5+1
                else:
                    result=MiniData-1
                    self.Result55.SetValue(str(result))
                    NumspinFlagUp5=NumspinFlagUp5-1
            else:
                print 'pos',event.GetPosition()
                if int(event.GetPosition())==2:
                    result=MiniData+1
                    self.Result55.SetValue(str(result))
                    NumspinFlagUp5=NumspinFlagUp5+2
                else:
                    result=MiniData-1
                    self.Result55.SetValue(str(result))                    
                    NumspinFlagUp5=2
        

            #以下是给图片显示区画标尺。
            y=(800-result)/2
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine(0, y, 820, y)
            self.posCtrlY.SetValue(str(result)) 

     def OnSpin8(self,event):
        global fre
        global result         
        global spinFlag8
        global spinFlagUp8
        global spinFlagDown8
        global NumspinFlagUp8
        global NumspinFlagDown8
        
        if self.Result88.GetValue()[0:4]=='NULL':
            event.Skip()
        else:
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Unbind(wx.EVT_LEFT_UP,id=-1,handler=None)
            #img = wx.Image('D:/DBS/PaintedOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
            #self.PicShow.SetBitmap(wx.BitmapFromImage(img))
            if fre==1:
                MiniData=float(self.Result88.GetValue()[0:5])
                result=MiniData
            fre=fre+1
            result=result

            spinFlag8=event.GetPosition()



            if NumspinFlagUp8>1:
                if  int(NumspinFlagUp8)==int(spinFlag8):
                    result=result+0.02
                    result1=result
                                      
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))                            
                                 
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp8=NumspinFlagUp8+1
                else:
                    result=result-0.02
                    result1=result
                                       
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))

                    else:

                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))                        
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp8=NumspinFlagUp8-1
            else:
                print 'pos',event.GetPosition()
                if int(event.GetPosition())==2:
                    result=result+0.02
                    result1=result
                    
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))                       
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp8=NumspinFlagUp8+2
                else:
                    result=result-0.02
                    result1=result
                    
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result88.SetValue(str(q))
                        else:
                            self.Result88.SetValue(str(p))                    
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp8=2
        

            #以下是给图片显示区画标尺。
            x=(result-1)*42.7083
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine(x, 0, x, 400)
            self.posCtrlX.SetValue(str(result))
            #self.posCtrlY.SetValue(str(result)) 


     def OnSpin9(self,event):
         
        global spinFlag9
        global spinFlagUp9
        global spinFlagDown9
        global NumspinFlagUp9
        global NumspinFlagDown9
        global fre
        global result         
        if self.Result99.GetValue()[0:4]=='NULL':
            event.Skip()
        else:
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Unbind(wx.EVT_LEFT_UP,id=-1,handler=None)
            #img = wx.Image('D:/DBS/PaintedOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
            #self.PicShow.SetBitmap(wx.BitmapFromImage(img))
            if fre==1:
                MiniData=float(self.Result99.GetValue()[0:5])
                result=MiniData
            fre=fre+1
            result=result
            spinFlag9=event.GetPosition()


            if NumspinFlagUp9>1:
                if  int(NumspinFlagUp9)==int(spinFlag9):
                    result=result+0.02
                    result1=result
                                      
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))                            
                                 
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp9=NumspinFlagUp9+1
                else:
                    result=result-0.02
                    result1=result
                                       
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))

                    else:

                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))                        
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp9=NumspinFlagUp9-1
            else:
                print 'pos',event.GetPosition()
                if int(event.GetPosition())==2:
                    result=result+0.02
                    result1=result
                    
                    if result1<10:
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))                       
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp9=NumspinFlagUp9+2
                else:
                    result=result-0.02
                    result1=result
                    
                    if result1<10:                        
                        p=(str(result1))[0:3]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))

                    else:
                        p=(str(result1))[0:4]
                        if float(p)+0.0599<result1:
                            q=float(p)+0.1
                            self.Result99.SetValue(str(q))
                        else:
                            self.Result99.SetValue(str(p))                    
                    
                    #self.Result11.SetValue(str(result))
                    NumspinFlagUp9=2
        

            #以下是给图片显示区画标尺。
            x=(result-1)*42.7083
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine(x, 0, x, 400)
            self.posCtrlX.SetValue(str(result))
            #self.posCtrlY.SetValue(str(result))



     def OnSpin14(self,event):
         
        global spinFlag14
        global spinFlagUp14
        global spinFlagDown14
        global NumspinFlagUp14
        global NumspinFlagDown14
        global fre
        global result         
        if self.Result1414.GetValue()[0:4]=='NULL':
            event.Skip()
        else:
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Unbind(wx.EVT_LEFT_UP,id=-1,handler=None)
            #img = wx.Image('D:/DBS/PaintedOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
            #self.PicShow.SetBitmap(wx.BitmapFromImage(img))
            MiniData=float(self.Result1414.GetValue()[0:5])

            spinFlag14=event.GetPosition()


            if NumspinFlagUp14>1:
                if  int(NumspinFlagUp14)==int(spinFlag14):
                    result=MiniData+1
                    self.Result1414.SetValue(str(result))
                    NumspinFlagUp14=NumspinFlagUp14+1
                else:
                    result=MiniData-1
                    self.Result1414.SetValue(str(result))
                    NumspinFlagUp14=NumspinFlagUp14-1
            else:
                print 'pos',event.GetPosition()
                if int(event.GetPosition())==2:
                    result=MiniData+1
                    self.Result1414.SetValue(str(result))
                    NumspinFlagUp14=NumspinFlagUp14+2
                else:
                    result=MiniData-1
                    self.Result1414.SetValue(str(result))                    
                    NumspinFlagUp14=2
        

            #以下是给图片显示区画标尺。
            y=(800-result)/2
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine(0, y, 820, y)
            self.posCtrlY.SetValue(str(result)) 
                
#参数修改项的选定。
################
     def OnPointy1(self,event):
        global fmin
        global fminFlag
        
        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre

        fre=1

        
        # 创建定时器
        timeFlag1=1
        self.timer1 = wx.Timer(self)#创建定时器
        self.timer1.Start(1200)#设置定时器的时间为1200ms
        self.Bind(wx.EVT_TIMER, self.OnTimer1, self.timer1)#绑定一个定时器事件

        #绑定键盘事件。
        #self.Result11.Unbind(wx.EVT_LEFT_DOWN,  id=-1,handler=None)
        #self.Result11.Bind(wx.EVT_KEY_UP,self.OnKeyUp0)


        #终止其他定时器。
        if timeFlag3==1:
            self.timer3.Stop()
            self.timer33.Stop()
            self.Result33Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag3=0
        if timeFlag5==1:
            self.timer5.Stop()
            self.timer55.Stop()
            self.Result55Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag5=0
        if timeFlag8==1:
            self.timer8.Stop()
            self.timer88.Stop()
            self.Result88Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag8=0
            
        if timeFlag9==1:
            self.timer9.Stop()
            self.timer99.Stop()
            self.Result99Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag9=0

        if timeFlag14==1:
            self.timer14.Stop()
            self.timer1414.Stop()
            self.Result1414Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag14=0

        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result11Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        if self.Result11.GetValue()[0:4]!='NULL':
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine((float(fmin[0:5])-1)*42.7083, 0, (float(fmin[0:5])-1)*42.7083, 400)
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX11)
            #参数值修改。
            fminFlag=1
            #foF1Flag=0
            #foF2Flag=0
            #fxF2Flag=0



        else:
            fmin='NULL'
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
            dc.DrawLine( 0, 0,0,0)  

     def OnTimer1(self,event):
        self.Result11Pic.SetBitmap(wxNullBitmap)
        # 创建定时器   
        self.timer11 = wx.Timer(self)#创建定时器
        self.timer11.Start(600)#设置定时器的时间为600ms
        self.Bind(wx.EVT_TIMER, self.OnTimer11, self.timer11)#绑定一个定时器事件

     def OnTimer11(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result11Pic.SetBitmap(wx.BitmapFromImage(img))
        #self.Result11Pic.SetBitmap(wxNullBitmap)
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)
        
#############        
     def OnPointy2(self,event):
        global fbEs
        global fbEsFlag


        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result22Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result11Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()
        #self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2))
        #self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        #self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2))

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX22)

############       
     def OnPointy3(self,event):
        global foF2
        global foF2Flag
        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre

        fre=1
        
        # 创建定时器
        timeFlag3=1
        
        #终止其他定时器。
        if timeFlag1==1:
            self.timer1.Stop()
            self.timer11.Stop()
            self.Result11Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag1=0
        if timeFlag5==1:
            self.timer5.Stop()
            self.timer55.Stop()
            self.Result55Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag5=0
        if timeFlag8==1:
            self.timer8.Stop()
            self.timer88.Stop()
            self.Result88Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag8=0
            
        if timeFlag9==1:
            self.timer9.Stop()
            self.timer99.Stop()
            self.Result99Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag9=0

        if timeFlag14==1:
            self.timer14.Stop()
            self.timer1414.Stop()
            self.Result1414Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag14=0
        self.timer3 = wx.Timer(self)#创建定时器
        self.timer3.Start(1200)#设置定时器的时间为1200ms
        self.Bind(wx.EVT_TIMER, self.OnTimer3, self.timer3)#绑定一个定时器事件

        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result33Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result11Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        if self.Result33.GetValue()[0:4]!='NULL':
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine((float(foF2[0:5])-1)*42.7083, 0, (float(foF2[0:5])-1)*42.7083, 400)
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX33)
            foF2Flag=1
            #fminFlag=0
            #foF1Flag=0
            #fxF2Flag=0


        else:
            foF2='NULL'
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
            dc.DrawLine( 0, 0,0,0)  

    #定时器事件
     def OnTimer3(self,event):
        self.Result33Pic.SetBitmap(wxNullBitmap)
        # 创建定时器   
        self.timer33 = wx.Timer(self)#创建定时器
        self.timer33.Start(600)#设置定时器的时间为1000ms
        self.Bind(wx.EVT_TIMER, self.OnTimer33, self.timer33)#绑定一个定时器事件

     def OnTimer33(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result33Pic.SetBitmap(wx.BitmapFromImage(img))
        #self.Result11Pic.SetBitmap(wxNullBitmap)
        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

###############        
     def OnPointy4(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result44Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result11Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickY44)


################        
     def OnPointy5(self,event):
        global hF1
        global hF1Flag

        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre

        fre=1        
        # 创建定时器
        timeFlag5=1
        
        #终止其他定时器。
        if timeFlag1==1:
            self.timer1.Stop()
            self.timer11.Stop()
            self.Result11Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag1=0
        if timeFlag3==1:
            self.timer3.Stop()
            self.timer33.Stop()
            self.Result33Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag3=0
        if timeFlag8==1:
            self.timer8.Stop()
            self.timer88.Stop()
            self.Result88Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag8=0
            
        if timeFlag9==1:
            self.timer9.Stop()
            self.timer99.Stop()
            self.Result99Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag9=0

        if timeFlag14==1:
            self.timer14.Stop()
            self.timer1414.Stop()
            self.Result1414Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag14=0
        self.timer5 = wx.Timer(self)#创建定时器
        self.timer5.Start(1200)#设置定时器的时间为1200ms
        self.Bind(wx.EVT_TIMER, self.OnTimer5, self.timer5)#绑定一个定时器事件

        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result55Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result11Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        if self.Result55.GetValue()[0:4]!='NULL':
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine( 0, (800-float(hF1[0:5]))/2,820,(800-float(hF1[0:5]))/2)
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickY55)
            hF1Flag=1
            #hF2Flag=0

        else:
            hF1='NULL'
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
            dc.DrawLine( 0, 0,0,0)  

    #定时器事件
     def OnTimer5(self,event):
        self.Result55Pic.SetBitmap(wxNullBitmap)

        # 创建定时器   
        self.timer55 = wx.Timer(self)#创建定时器
        self.timer55.Start(600)#设置定时器的时间为1000ms
        self.Bind(wx.EVT_TIMER, self.OnTimer55, self.timer55)#绑定一个定时器事件

     def OnTimer55(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result55Pic.SetBitmap(wx.BitmapFromImage(img))
        #self.Result11Pic.SetBitmap(wxNullBitmap)
        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)


###############        
     def OnPointy6(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result66Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result11Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX66)

############
     def OnPointy7(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result77Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result11Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)
        pos = event.GetPosition()

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX77)

##############
     def OnPointy8(self,event):
        global foF1
        global foF1Flag

        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre

        fre=1        
        # 创建定时器
        timeFlag8=1
        
        #终止其他定时器。
        if timeFlag1==1:
            self.timer1.Stop()
            self.timer11.Stop()
            self.Result11Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag1=0
        if timeFlag3==1:
            self.timer3.Stop()
            self.timer33.Stop()
            self.Result33Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag3=0
        if timeFlag5==1:
            self.timer5.Stop()
            self.timer55.Stop()
            self.Result55Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag5=0
            
        if timeFlag9==1:
            self.timer9.Stop()
            self.timer99.Stop()
            self.Result99Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag9=0

        if timeFlag14==1:
            self.timer14.Stop()
            self.timer1414.Stop()
            self.Result1414Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag14=0
        self.timer8 = wx.Timer(self)#创建定时器
        self.timer8.Start(1200)#设置定时器的时间为1200ms
        self.Bind(wx.EVT_TIMER, self.OnTimer8, self.timer8)#绑定一个定时器事件

        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result88Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result11Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        if self.Result88.GetValue()[0:4]!='NULL':

            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine((float(foF1[0:5])-1)*42.7083, 0, (float(foF1[0:5])-1)*42.7083, 400)
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX88)
            foF1Flag=1
            #fminFlag=0
            #foF2Flag=0
            #fxF2Flag=0

        else:
            foF1='NULL'
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
            dc.DrawLine( 0, 0,0,0)

    #定时器事件
     def OnTimer8(self,event):
        self.Result88Pic.SetBitmap(wxNullBitmap)

        # 创建定时器   
        self.timer88 = wx.Timer(self)#创建定时器
        self.timer88.Start(600)#设置定时器的时间为1000ms
        self.Bind(wx.EVT_TIMER, self.OnTimer88, self.timer88)#绑定一个定时器事件

     def OnTimer88(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result88Pic.SetBitmap(wx.BitmapFromImage(img))
        #self.Result11Pic.SetBitmap(wxNullBitmap)
        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)
            
##############        
     def OnPointy9(self,event):
        global fxF2
        global fxF2Flag

        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre

        fre=1        
        # 创建定时器
        timeFlag9=1
        
        #终止其他定时器。
        if timeFlag1==1:
            self.timer1.Stop()
            self.timer11.Stop()
            self.Result11Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag1=0
        if timeFlag3==1:
            self.timer3.Stop()
            self.timer33.Stop()
            self.Result33Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag3=0
        if timeFlag5==1:
            self.timer5.Stop()
            self.timer55.Stop()
            self.Result55Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag5=0
            
        if timeFlag8==1:
            self.timer8.Stop()
            self.timer88.Stop()
            self.Result88Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag8=0

        if timeFlag14==1:
            self.timer14.Stop()
            self.timer1414.Stop()
            self.Result1414Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag14=0
        self.timer9 = wx.Timer(self)#创建定时器
        self.timer9.Start(1200)#设置定时器的时间为1200ms
        self.Bind(wx.EVT_TIMER, self.OnTimer9, self.timer9)#绑定一个定时器事件


        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)
        
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result99Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result11Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        if self.Result99.GetValue()[0:4]!='NULL':
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine((float(fxF2[0:5])-1)*42.7083, 0, (float(fxF2[0:5])-1)*42.7083, 400)
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX99)
            fxF2Flag=1
            #fminFlag=0
            #foF1Flag=0
            #foF2Flag=0

        else:
            fxF2='NULL'
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
            dc.DrawLine( 0, 0,0,0)

    #定时器事件
     def OnTimer9(self,event):
        self.Result99Pic.SetBitmap(wxNullBitmap)

        # 创建定时器   
        self.timer99 = wx.Timer(self)#创建定时器
        self.timer99.Start(600)#设置定时器的时间为1000ms
        self.Bind(wx.EVT_TIMER, self.OnTimer99, self.timer99)#绑定一个定时器事件

     def OnTimer99(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result99Pic.SetBitmap(wx.BitmapFromImage(img))
        #self.Result11Pic.SetBitmap(wxNullBitmap)
        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)


            
##############        
     def OnPointy10(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result1010Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result11Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX1010)

###########        
     def OnPointy11(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result1111Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result11Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickX1111)
                                                        

###############        
     def OnPointy12(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result1212Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result11Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickY1212)

################        
     def OnPointy13(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result1313Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result11Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        pos = event.GetPosition()

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
        dc.DrawLine( 0, 0,0,0)
        #解除绑定并添加绑定。
        self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickY1313)

##################
     def OnPointy14(self,event):
        global hF2
        global hF2Flag

        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre

        fre=1        
        # 创建定时器
        timeFlag14=1
        
        #终止其他定时器。
        if timeFlag1==1:
            self.timer1.Stop()
            self.timer11.Stop()
            self.Result11Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag1=0
        if timeFlag3==1:
            self.timer3.Stop()
            self.timer33.Stop()
            self.Result33Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag3=0
        if timeFlag5==1:
            self.timer5.Stop()
            self.timer55.Stop()
            self.Result55Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag5=0
            
        if timeFlag8==1:
            self.timer8.Stop()
            self.timer88.Stop()
            self.Result88Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag8=0

        if timeFlag9==1:
            self.timer9.Stop()
            self.timer99.Stop()
            self.Result99Pic.SetBitmap(wxNullBitmap)
        else:
            timeFlag9=0
        self.timer14 = wx.Timer(self)#创建定时器
        self.timer14.Start(1200)#设置定时器的时间为1200ms
        self.Bind(wx.EVT_TIMER, self.OnTimer14, self.timer14)#绑定一个定时器事件


        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)
        
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result1414Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result11Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        if self.Result1414.GetValue()[0:4]!='NULL':
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
            dc.DrawLine( 0, (800-float(hF2[0:5]))/2,820,(800-float(hF2[0:5]))/2)
            self.PicShow.Unbind(wx.EVT_MOTION, id=-1,handler=None)
            self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClickY1414)
            hF2Flag=1
            #hF1Flag=0
        else:
            hF2='NULL'
            dc = wx.ClientDC(self.PicShow) 
            dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
            dc.SetPen(wx.Pen(wx.Colour(65,105,225), 1, wx.DOT))
            dc.DrawLine( 0, 0,0,0)

    #定时器事件
     def OnTimer14(self,event):
        self.Result1414Pic.SetBitmap(wxNullBitmap)

        # 创建定时器   
        self.timer1414 = wx.Timer(self)#创建定时器
        self.timer1414.Start(600)#设置定时器的时间为1000ms
        self.Bind(wx.EVT_TIMER, self.OnTimer1414, self.timer1414)#绑定一个定时器事件

     def OnTimer1414(self,event):
        img= wx.Image('D:/DBS/FacePic/pointy.jpg',wx.BITMAP_TYPE_ANY).Scale(40,30)
        self.Result1414Pic.SetBitmap(wx.BitmapFromImage(img))
        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)
        #self.Result11Pic.SetBitmap(wxNullBitmap)
     #def OnChoice1(self,event):
        #print self.choice1.GetStringSelection()

#参数修改保存事件。
     def PChange(self,event):
        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre
        fre=1
        
        for ResultPic in  [self.Result11Pic,self.Result22Pic,self.Result33Pic,self.Result44Pic,self.Result55Pic,self.Result66Pic,
                           self.Result77Pic,self.Result88Pic,self.Result99Pic,self.Result1010Pic,self.Result1111Pic,
                           self.Result1212Pic,self.Result1313Pic,self.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        print self.Result11.GetValue()
        self.PicShow.Bind(wx.EVT_MOTION, self.OnMove)
        self.PicShow.Bind(wx.EVT_LEFT_UP, self.OnClick)
        self.Result11.Bind(wx.EVT_LEFT_DOWN, self.OnPointy1)

        if timeFlag1==1 :
            self.timer1.Stop()
            self.timer11.Stop()
            self.Result11Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag3==1 :
            self.timer3.Stop()
            self.timer33.Stop()
            self.Result33Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag5==1 :
            self.timer5.Stop()
            self.timer55.Stop()
            self.Result55Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag8==1 :
            self.timer8.Stop()
            self.timer88.Stop()
            self.Result88Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag9==1 :
            self.timer9.Stop()
            self.timer99.Stop()
            self.Result99Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag14==1 :
            self.timer14.Stop()
            self.timer1414.Stop()
            self.Result1414Pic.SetBitmap(wxNullBitmap)

        
        
        print "PageThree.PChange"
        #self.Result11.SetLabel("kk".decode('utf-8'))
        #print self.Result11.GetValue()

############手动度量里面的数据库处理####################
        global a
        global sqlitenumber
        global filename
        global place
        global par_time
        #sqlitenumber=sqlitenumber+1
        sqlite_number=str(sqlitenumber)
        print sqlite_number
        print a[0]
        a2=a[0]
        a0=a2[16:42]
        print a0

        filename_flag=0
        filename_flag1=0
        filename_flag2=0
        filename_flag3=0
        filename_flag4=0
        filename_flag5=0
        filename_flag6=0
        filename_flag7=0
        filename_flag8=0
        filename_flag9=0
        filename_flag10=0
        filename_flag11=0
        filename_flag12=0
        filename_flag13=0
        filename_flag14=0
        
        #filename.append("NULL")

        r1= self.Result11.GetValue()
        r2= self.Result22.GetValue()
        r3= self.Result33.GetValue()
        r4= self.Result44.GetValue()
        r5= self.Result55.GetValue()
        r6= self.Result66.GetValue()
        r7= self.Result77.GetValue()
        r8= self.Result88.GetValue()
        r9= self.Result99.GetValue()
        r10=self.Result1010.GetValue()
        r11=self.Result1111.GetValue()
        r12=self.Result1212.GetValue()
        r13=self.Result1313.GetValue()
        r14=self.Result1414.GetValue()
        
        r_flag1="0"
        r_flag2="0"
        r_flag3="0"
        r_flag4="0"
        r_flag5="0"
        r_flag6="0"
        r_flag7="0"
        r_flag8="0"
        r_flag9="0"
        r_flag10="0"
        r_flag11="0"
        r_flag12="0"
        r_flag13="0"
        r_flag14="0"
        

        for i in range(0,len(filename)):
            if filename[i]==a0:
                filename_flag=1
            else:
                filename_flag=0

        if filename_flag==1:
              #cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
              con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
              cur=con.cursor()
              cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
              ReadFileSeePara=cur.fetchall()
              print ReadFileSeePara
              print ReadFileSeePara[0][2]
              if ReadFileSeePara[0][2]!=r1:
                  r_flag1="1"
              if ReadFileSeePara[0][3]!=r2:
                  r_flag2="1"
              if ReadFileSeePara[0][4]!=r3:
                  r_flag3="1"
              if ReadFileSeePara[0][5]!=r4:
                  r_flag4="1"
              if ReadFileSeePara[0][6]!=r5:
                  r_flag5="1"
              if ReadFileSeePara[0][7]!=r6:
                  r_flag6="1"
              if ReadFileSeePara[0][8]!=r7:
                  r_flag7="1"
              if ReadFileSeePara[0][9]!=r8:
                  r_flag8="1"
              if ReadFileSeePara[0][10]!=r9:
                  r_flag9="1"
              if ReadFileSeePara[0][11]!=r10:
                  r_flag10="1"
              if ReadFileSeePara[0][12]!=r11:
                  r_flag11="1"     
              if ReadFileSeePara[0][13]!=r12:
                  r_flag12="1"      
              if ReadFileSeePara[0][14]!=r13:
                  r_flag13="1"
              if ReadFileSeePara[0][15]!=r14:
                  r_flag14="1"
      
                
              cur.execute("update parameters set fmin='%s' where file_name=\'%s\'" %(r1,a0))
              cur.execute("update parameters set fbEs='%s' where file_name=\'%s\'" %(r2,a0))
              cur.execute("update parameters set foF2='%s' where file_name=\'%s\'" %(r3,a0))
              cur.execute("update parameters set hE='%s' where file_name=\'%s\'" %(r4,a0))
              cur.execute("update parameters set hF='%s' where file_name=\'%s\'" %(r5,a0))
              cur.execute("update parameters set M3F2='%s' where file_name=\'%s\'" %(r6,a0))
              cur.execute("update parameters set foE='%s' where file_name=\'%s\'" %(r7,a0))
              cur.execute("update parameters set foF1='%s' where file_name=\'%s\'" %(r8,a0))
              cur.execute("update parameters set fx1='%s' where file_name=\'%s\'" %(r9,a0))
              cur.execute("update parameters set foEs='%s' where file_name=\'%s\'" %(r10,a0))
              cur.execute("update parameters set M3F1='%s' where file_name=\'%s\'" %(r11,a0))
              cur.execute("update parameters set hEs='%s' where file_name=\'%s\'" %(r12,a0))
              cur.execute("update parameters set Es='%s' where file_name=\'%s\'" %(r13,a0))
              cur.execute("update parameters set hF2='%s' where file_name=\'%s\'" %(r14,a0))
              cur.execute("update parameters set Flag_1='%s' where file_name=\'%s\'" %(r_flag1,a0))
              cur.execute("update parameters set Flag_2='%s' where file_name=\'%s\'" %(r_flag2,a0))
              cur.execute("update parameters set Flag_3='%s' where file_name=\'%s\'" %(r_flag3,a0))
              cur.execute("update parameters set Flag_4='%s' where file_name=\'%s\'" %(r_flag4,a0))
              cur.execute("update parameters set Flag_5='%s' where file_name=\'%s\'" %(r_flag5,a0))
              cur.execute("update parameters set Flag_6='%s' where file_name=\'%s\'" %(r_flag6,a0))
              cur.execute("update parameters set Flag_7='%s' where file_name=\'%s\'" %(r_flag7,a0))
              cur.execute("update parameters set Flag_8='%s' where file_name=\'%s\'" %(r_flag8,a0))
              cur.execute("update parameters set Flag_9='%s' where file_name=\'%s\'" %(r_flag9,a0))
              cur.execute("update parameters set Flag_10='%s' where file_name=\'%s\'" %(r_flag10,a0))
              cur.execute("update parameters set Flag_11='%s' where file_name=\'%s\'" %(r_flag11,a0))
              cur.execute("update parameters set Flag_12='%s' where file_name=\'%s\'" %(r_flag12,a0))
              cur.execute("update parameters set Flag_13='%s' where file_name=\'%s\'" %(r_flag13,a0))
              cur.execute("update parameters set Flag_14='%s' where file_name=\'%s\'" %(r_flag14,a0))
              con.commit()####这一步很重要，关于提交的commit！务必谨记！！！
              cur.close()
              cur.close()
        else:       

              #以下部分为连接数据库并且插入。
              con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
              cur=con.cursor()

              cur.execute("insert into parameters Values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    %(sqlite_number,a0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r_flag1,r_flag2,r_flag3,r_flag4,r_flag5,r_flag6,r_flag7,r_flag8,r_flag9,r_flag10,r_flag11,r_flag12,r_flag13,r_flag14,par_time,place))
              con.commit()
              cur.close()
              cur.close()
        filename.append(a0)
 


                              
 #绘画Paint0。
     def Paint0(self,event):
        global FlagClick
        global posX
        global posY
        

        
        dc = wx.PaintDC(self)
        
        dc.SetPen(wx.Pen((192,192,192),1))
        rect7 = wx.Rect(10,5,1065,435)
        dc.DrawRoundedRectangleRect(rect7, 10)        
        rect4 = wx.Rect(20,10,190,430)
        dc.DrawRoundedRectangleRect(rect4, 10)        
        rect5 = wx.Rect(210,10,860,430)
        dc.DrawRoundedRectangleRect(rect5, 10)
        rect6 = wx.Rect(65,440,965,150)
        dc.DrawRoundedRectangleRect(rect6, 10)
        
        #以下是给数据输出区域画图。
        
        dc.SetPen(wx.Pen((192,192,192),1))
        rect8 = wx.Rect(115,445,880,139)
        dc.DrawRoundedRectangleRect(rect8,10)
        rect9 = wx.Rect(115,445,880,46)
        dc.DrawRoundedRectangleRect(rect9,10)
        rect10 = wx.Rect(115,491,880,46)
        dc.DrawRoundedRectangleRect(rect10,10)
        rect11 = wx.Rect(115,537,880,46)
        dc.DrawRoundedRectangleRect(rect11,10)
        

        #以下是给按钮画出边框，使之立体化。
        
        dc.SetPen(wx.Pen('black',1))
        rect3 = wx.Rect(863, 547, 84, 26) 
        dc.DrawRoundedRectangleRect(rect3, 1)
        
        #画坐标轴。

        dc.SetPen(wx.Pen(wx.Colour(138,43,226), 1))
        dc.DrawLine(244, 34, 1065, 34)
        dc.DrawLine(244, 34, 244, 436)


#关于鼠标移动的标记。
     def OnMove(self, event):
        pos = event.GetPosition()
        #self.posX = pos.x 
        #self.posY = pos.y
        
        self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2)) 
        #设置鼠标变化为十字指针。
        cursors = [wx.CURSOR_CROSS,]
        cnum = cursors[0]
        cursor = wx.StockCursor(cnum)
        self.PicShow.SetCursor(cursor)

        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
            self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(46, 139, 87), 1, wx.DOT))
        dc.CrossHair(pos.x, pos.y)
        
        
         
#绑定鼠标在图片上的的单击事件。
     def OnClick(self,event):
        self.leftDown = 0
        
        pos=event.GetPosition()
        
        self.posX = pos.x
        self.posY = pos.y
        
        FlagClick=1
        posX=pos.x
        posY=pos.y
        print posX,posY
        print "上面输出的鼠标的横坐标要作为结果输出，以便于用户更精确地进行手动度量。".decode('utf-8')

        pos = event.GetPosition()        
        self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2)) 
        
        #以下是给图片显示区画标尺。
        
        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
            self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
        dc.CrossHair(posX, posY)


#绑定鼠标在图片上的的单击更改频率事件。
     def OnClickX11(self,event):

        global fminFlag
        global foF1Flag
        global foF2Flag
        global fxF2Flag
        global hF1Flag
        global hF2Flag
        global posX
        global posY
        self.leftDown = 0
        
        pos=event.GetPosition()
        
        self.posX = pos.x
        self.posY = pos.y
        
        FlagClick=1
        posX=pos.x
        posY=pos.y

        #绑定键盘事件。
        #self.Bind(wx.EVT_KEY_UP , self.OnKeyUp1)

        #以下是给图片显示区画标尺。
        pos=event.GetPosition()
        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
            self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
        dc.DrawLine(pos.x, 0, pos.x, 400)
        self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2))
        self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2)) 

        pos = event.GetPosition()
        print pos.x,   pos.y, 
        self.Result11.SetLabel(str(pos.x/42.7083+1))



     def OnClickX22(self,event):
         print '22'


     def OnClickX33(self,event):

        global fminFlag
        global foF1Flag
        global foF2Flag
        global fxF2Flag
        global hF1Flag
        global hF2Flag
        self.leftDown = 0
        
        pos=event.GetPosition()
        
        self.posX = pos.x
        self.posY = pos.y
        
        FlagClick=1
        posX=pos.x
        posY=pos.y

        #以下是给图片显示区画标尺。
        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
            self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
        dc.DrawLine(pos.x, 0, pos.x, 400)
        self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2))
        self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2)) 
        pos = event.GetPosition()
        print pos.x,   pos.y
        self.Result33.SetLabel(str(pos.x/42.7083+1))

     def OnClickY44(self,event):
         print '44'




     def OnClickX66(self,event):
         print '66'

     def OnClickX77(self,event):
         print '77'




     def OnClickX88(self,event):


        global fminFlag
        global foF1Flag
        global foF2Flag
        global fxF2Flag
        global hF1Flag
        global hF2Flag
        self.leftDown = 0
        
        pos=event.GetPosition()
        
        self.posX = pos.x
        self.posY = pos.y
        
        FlagClick=1
        posX=pos.x
        posY=pos.y

        #以下是给图片显示区画标尺。
        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
                self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
        dc.DrawLine(pos.x, 0, pos.x, 400)
        self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2))
        self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2)) 
        #if f0F1Flag==1:            
        pos = event.GetPosition()
        print pos.x,   pos.y
        self.Result88.SetLabel(str(pos.x/42.7083+1))






            
     def OnClickX99(self,event):

        global fminFlag
        global foF1Flag
        global foF2Flag
        global fxF2Flag
        global hF1Flag
        global hF2Flag
        self.leftDown = 0
        
        pos=event.GetPosition()
        
        self.posX = pos.x
        self.posY = pos.y
        
        FlagClick=1
        posX=pos.x
        posY=pos.y

        #以下是给图片显示区画标尺。
        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
            self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
        dc.DrawLine(pos.x, 0, pos.x, 400)
        self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2))
        self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2)) 
        pos = event.GetPosition()
        print pos.x,   pos.y
        self.Result99.SetLabel(str(pos.x/42.7083+1))

     def OnClickX1010(self,event):
         print '1010'

     def OnClickX1111(self,event):
         print '1111'





#绑定鼠标在图片上的的单击更改高度事件。
     def OnClickY55(self,event):
        self.leftDown = 0
        global fminFlag
        global foF1Flag
        global foF2Flag
        global fxF2Flag
        global hF1Flag
        global hF2Flag        
        pos=event.GetPosition()
        
        self.posX = pos.x
        self.posY = pos.y
        
        FlagClick=1
        posX=pos.x
        posY=pos.y

        #以下是给图片显示区画标尺。
        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
            self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
        dc.DrawLine( 0, pos.y, 820,pos.y)

        self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2))
        self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2)) 
        pos = event.GetPosition()
        print pos.x,   pos.y
        self.Result55.SetLabel(str(800-pos.y*2))

     def OnClickY1212(self,event):
         print '1212'

     def OnClickY1313(self,event):
         print '1313'


     def OnClickY1414(self,event):
        self.leftDown = 0
        global fminFlag
        global foF1Flag
        global foF2Flag
        global fxF2Flag
        global hF1Flag
        global hF2Flag        
        pos=event.GetPosition()
        
        self.posX = pos.x
        self.posY = pos.y
        
        FlagClick=1
        posX=pos.x
        posY=pos.y

        #以下是给图片显示区画标尺。
        dc = wx.ClientDC(self.PicShow) 
        dc.Blit(0, 0, dc.GetSize().x, dc.GetSize().y,
            self.memDC, 0, 0)
        dc.SetPen(wx.Pen(wx.Colour(255,0,0), 1, wx.DOT))
        dc.DrawLine( 0, pos.y, 820,pos.y)

        self.posCtrl.SetValue("F=%-5.1f ,  H=%-5.1f" % (pos.x/42.7083+1, 800-pos.y*2))
        self.posCtrlX.SetValue("F=%-5.1f" % (pos.x/42.7083+1))
        self.posCtrlY.SetValue("H=%-5.1f" % (800-pos.y*2)) 
        pos = event.GetPosition()
        self.Result1414.SetLabel(str(800-pos.y*2))
############################自动度量######################################
class PageTwo(wx.Panel):
     
     def __init__(self, parent,page3):
        wx.Panel.__init__(self, parent)
        self.toolkit = parent
        panel = wx.Panel(self)

        self.page3 = page3 
        
        #绑定画板的边线底纹绘制（Paint0部分）。
        self.Bind(wx.EVT_PAINT, self.Paint0)
        
        colour = [(255,255,255),(153,204,255),(151,253,225),]
        self.SetBackgroundColour(colour[0])

        #注意定义全局变量中的列表的声明方法。
        global PicFlag
        global Flag1,Flag2,Flag3
        global a
        global threshold
        global foF1
        global foF2
        global fxF2
        global hF1
        global hF2
        global fmin
        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
            

        #生成下拉菜单选项及按钮和静态文本框，并设置字体格式。
        DownFont1 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)

        self.Plate1=wx.StaticText(self,-1,"输入控制".decode('utf-8'),(35,23))
        self.Plate1.SetFont(DownFont1)

        self.Plate2=wx.StaticText(self,-1,"图片显示".decode('utf-8'),(1005,23))
        self.Plate2.SetFont(DownFont1)


        #FileOpen的创建按钮。
        b = wx.Button(self, -1, "打开文件".decode('utf-8'), (30,72))
        self.Bind(wx.EVT_BUTTON, self.OnFileOpen, b)

        
        #创建丰富文本控件
        self.Plateb=wx.TextCtrl(self, -1, "提示：请点击上面按钮，选择您所要打开的文件。".decode('utf-8'),(40,121),
                size=(200, 40), style=wx.TE_MULTILINE|wx.TE_READONLY ) 


        self.Plate0=wx.StaticText(self,-1,"日出日落：".decode('utf-8'),(30,250))
        self.Plate0.SetFont(DownFont1)
        
        self.Plate1=wx.StaticText(self,-1,"阈值选择：".decode('utf-8'),(30,200))
        self.Plate1.SetFont(DownFont1)

        self.Plate2=wx.StaticText(self,-1,"观测站点：".decode('utf-8'),(30,300))
        self.Plate2.SetFont(DownFont1)

        #生成白天黑夜选择的下拉菜单项。
        self.sampleList0 = ['白天'.decode('utf-8'),'黑夜'.decode('utf-8'), ]
        self.choice0 = wx.Choice(self, -1, (95, 250), choices=self.sampleList0,style=wx.SL_VERTICAL,
                                 name="Time")
        
        #生成阈值选择的下拉菜单选择项。
        self.sampleList1 = ['0'.decode('utf-8'),'1'.decode('utf-8'),'2'.decode('utf-8'), '3'.decode('utf-8'),'4'.decode('utf-8'),
                            '5'.decode('utf-8'),'6'.decode('utf-8'),'7'.decode('utf-8'),'8'.decode('utf-8'), '9'.decode('utf-8'),
                            'A'.decode('utf-8'),'B'.decode('utf-8'),'C'.decode('utf-8'),'D'.decode('utf-8'),'E'.decode('utf-8'), ]
        self.choice1 = wx.Choice(self, -1, (95, 200), choices=self.sampleList1,style=wx.SL_VERTICAL,
                                 name="Threshold")

        #生成观测站点选择的下拉菜单项。
        self.sampleList2 = ['青岛站'.decode('utf-8'),'新乡站'.decode('utf-8'),'济南站'.decode('utf-8'),'青海站'.decode('utf-8') ]
        self.choice2 = wx.Choice(self, -1, (95, 300), choices=self.sampleList2,style=wx.SL_VERTICAL,
                                 name="Time")
  

        #绑定阈值下拉选择项。
        #self.choice1.Bind(wx.EVT_CHOICE,self.OnChoice1)
        #阈值事件。

        #生成“重置”“度量”按钮，并绑定鼠标单击事件。

        colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167)]
        
        self.resetButton = buttons.GenButton(self, -1,'重置'.decode('utf-8'),size=(80,25),pos=(35, 350))
        self.resetButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.resetButton.SetBezelWidth(1000)
        self.resetButton.SetBackgroundColour(colour[3])
        self.resetButton.SetForegroundColour("white")
        self.resetButton.SetToolTipString("点击以清屏...".decode('utf-8'))
        
        self.resetButton.Bind(wx.EVT_BUTTON, self.OnClearMe)

        self.findButton = buttons.GenButton(self, -1,'度量'.decode('utf-8'),size=(80,25),pos=(150, 350))
        self.findButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.findButton.SetBezelWidth(1000)
        self.findButton.SetBackgroundColour(colour[3])
        self.findButton.SetForegroundColour("white")
        self.findButton.SetToolTipString("点击以度量运算出参数...".decode('utf-8'))

        self.findButton.Bind(wx.EVT_BUTTON, self.OnFindMe)



 #创建单选按钮。   
        self.radio1 = wx.RadioButton(self, -1, "原数据描迹图".decode('utf-8'), pos=(285, 75), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(self, -1, "分层后E区图".decode('utf-8'), pos=(285, 115))   
        self.radio3 = wx.RadioButton(self, -1, "分层后F区图".decode('utf-8'), pos=(285, 155))
        self.radio4 = wx.RadioButton(self, -1, "E层描迹图".decode('utf-8'), pos=(285, 195))   
        self.radio5 = wx.RadioButton(self, -1, "Es层描迹图".decode('utf-8'), pos=(285, 235))
        self.radio6 = wx.RadioButton(self, -1, "L类描迹图".decode('utf-8'), pos=(285, 275))   
        self.radio7 = wx.RadioButton(self, -1, "去二反射F图".decode('utf-8'), pos=(285, 315))
        self.radio8 = wx.RadioButton(self, -1, "原数据阈值图".decode('utf-8'), pos=(285, 355))
 #绑定单选按钮。
        for eachRadio in [self.radio1, self.radio2, self.radio3,self.radio4, self.radio5, self.radio6,self.radio7,self.radio8]:#绑定事件   
            self.Bind(wx.EVT_RADIOBUTTON, self.OnShowPic, eachRadio)
 #生成空位图。

        self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(420, 65),size=(625,360))
        img = wx.Image('D:/DBS/FacePic/a.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
        self.PicShow.SetBitmap(wx.BitmapFromImage(img))

 #生成参数输出的位图表示。
        self.PicDataPutout=wx.StaticBitmap(self,-1,wxNullBitmap,pos=(50,452),size=(27,115))
        img1= wx.Image('D:/DBS/FacePic/44.png',wx.BITMAP_TYPE_ANY).Scale(27,115)
        self.PicDataPutout.SetBitmap(wx.BitmapFromImage(img1))

        #以下生成14个参数值的文本标签。
        self.Result1=wx.StaticText(self,-1,"fmin：".decode('utf-8'),(165,460))
        self.Result1.SetFont(DownFont1)

        self.Result11=wx.TextCtrl(self, -1, "NULL", (225,460),(70,-1))
        self.Result11.DiscardEdits()

        self.Result2=wx.StaticText(self,-1,"fbEs：".decode('utf-8'),(165,504))
        self.Result2.SetFont(DownFont1)

        self.Result22=wx.TextCtrl(self, -1, "NULL", (225,504),(70,-1))
        self.Result22.DiscardEdits()

        self.Result3=wx.StaticText(self,-1,"foF2：".decode('utf-8'),(165,549))
        self.Result3.SetFont(DownFont1)

        self.Result33=wx.TextCtrl(self, -1, "NULL", (225,549),(70,-1))
        self.Result33.DiscardEdits()

        self.Result4=wx.StaticText(self,-1,"hE：".decode('utf-8'),(335,460))
        self.Result4.SetFont(DownFont1)

        self.Result44=wx.TextCtrl(self, -1, "NULL", (395,460),(70,-1))
        self.Result44.DiscardEdits()

        self.Result5=wx.StaticText(self,-1,"hF：".decode('utf-8'),(335,504))
        self.Result5.SetFont(DownFont1)

        self.Result55=wx.TextCtrl(self, -1, "NULL", (395,504),(70,-1))
        self.Result55.DiscardEdits()

        self.Result6=wx.StaticText(self,-1,"M3F2：".decode('utf-8'),(335,549))
        self.Result6.SetFont(DownFont1)

        self.Result66=wx.TextCtrl(self, -1, "NULL", (395,549),(70,-1))
        self.Result66.DiscardEdits()
        
        self.Result7=wx.StaticText(self,-1,"foE：".decode('utf-8'),(505,460))
        self.Result7.SetFont(DownFont1)

        self.Result77=wx.TextCtrl(self, -1, "NULL", (565,460),(70,-1))
        self.Result77.DiscardEdits()

        self.Result8=wx.StaticText(self,-1,"foF1：".decode('utf-8'),(505,504))
        self.Result8.SetFont(DownFont1)

        self.Result88=wx.TextCtrl(self, -1, "NULL", (565,504),(70,-1))
        self.Result88.DiscardEdits()

        self.Result9=wx.StaticText(self,-1,"fxI：".decode('utf-8'),(505,549))
        self.Result9.SetFont(DownFont1)

        self.Result99=wx.TextCtrl(self, -1, "NULL", (565,549),(70,-1))
        self.Result99.DiscardEdits()

        self.Result10=wx.StaticText(self,-1,"foEs：".decode('utf-8'),(675,460))
        self.Result10.SetFont(DownFont1)

        self.Result1010=wx.TextCtrl(self, -1, "NULL", (735,460),(70,-1))
        self.Result1010.DiscardEdits()

        self.Result11m=wx.StaticText(self,-1,"M3F1：".decode('utf-8'),(675,504))
        self.Result11m.SetFont(DownFont1)

        self.Result1111=wx.TextCtrl(self, -1, "NULL", (735,504),(70,-1))
        self.Result1111.DiscardEdits()

        self.Result12=wx.StaticText(self,-1,"hES：".decode('utf-8'),(675,549))
        self.Result12.SetFont(DownFont1)

        self.Result1212=wx.TextCtrl(self, -1, "NULL", (735,549),(70,-1))
        self.Result1212.DiscardEdits()

        self.Result13=wx.StaticText(self,-1,"Es类型：".decode('utf-8'),(845,460))
        self.Result13.SetFont(DownFont1)

        self.Result1313=wx.TextCtrl(self, -1, "NULL", (905,460),(70,-1))
        self.Result1313.DiscardEdits()

        self.Result14=wx.StaticText(self,-1,"hF2：".decode('utf-8'),(845,504))
        self.Result14.SetFont(DownFont1)

        self.Result1414=wx.TextCtrl(self, -1, "NULL", (905,504),(70,-1))
        self.Result1414.DiscardEdits()

        self.ChangeButton = buttons.GenButton(self, -1,'保存修改'.decode('utf-8'),size=(80,22),pos=(865, 549))
        self.ChangeButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.ChangeButton.SetBezelWidth(1000)
        self.ChangeButton.SetBackgroundColour(colour[3])
        self.ChangeButton.SetForegroundColour("white")
        self.ChangeButton.SetToolTipString("点击以保存修改后的参数...".decode('utf-8'))

        self.ChangeButton.Bind(wx.EVT_BUTTON, self.PChange)


        self.PicY11=wx.StaticText(self, -1, "800", pos=(393,56))
        self.PicY22=wx.StaticText(self, -1, "700", pos=(393,56+45*1))
        self.PicY33=wx.StaticText(self, -1, "600", pos=(393,56+45*2))
        self.PicY44=wx.StaticText(self, -1, "500", pos=(393,56+45*3))
        self.PicY55=wx.StaticText(self, -1, "400", pos=(393,56+45*4))
        self.PicY66=wx.StaticText(self, -1, "300", pos=(393,56+45*5))
        self.PicY77=wx.StaticText(self, -1, "200", pos=(393,56+45*6))
        self.PicY88=wx.StaticText(self, -1, "100", pos=(393,56+45*7))
        self.PicY99=wx.StaticText(self, -1, "000", pos=(393,55+45*8))

        self.PicX11=wx.StaticText(self, -1, "1.0", pos=(410,44))
        self.PicX22=wx.StaticText(self, -1, "2.2", pos=(410+39*1,44))
        self.PicX33=wx.StaticText(self, -1, "3.4", pos=(410+39*2,44))
        self.PicX44=wx.StaticText(self, -1, "4.6", pos=(410+39*3,44))
        self.PicX55=wx.StaticText(self, -1, "5.8", pos=(410+39*4,44))
        self.PicX66=wx.StaticText(self, -1, "7.0", pos=(410+39*5,44))
        self.PicX77=wx.StaticText(self, -1, "8.2", pos=(410+39*6,44))
        self.PicX88=wx.StaticText(self, -1, "9.4", pos=(410+39*7,44))
        self.PicX99=wx.StaticText(self, -1, "10.6", pos=(410+39*8,44))
        self.PicX1010=wx.StaticText(self, -1, "11.8", pos=(410+39*9,44))
        self.PicX1111=wx.StaticText(self, -1, "13", pos=(410+39*10,44))
        self.PicX1212=wx.StaticText(self, -1, "14.2", pos=(408+39*11,44))
        self.PicX1313=wx.StaticText(self, -1, "15.4", pos=(410+39*12,44))
        self.PicX1414=wx.StaticText(self, -1, "16.6", pos=(410+39*13,44))
        self.PicX1515=wx.StaticText(self, -1, "17.8", pos=(410+39*14,44))
        self.PicX1616=wx.StaticText(self, -1, "19", pos=(410+39*15,44))
        self.PicX1717=wx.StaticText(self, -1, "20.2", pos=(404+39*16,44))
        

        
     #def OnChoice1(self,event):
        #print self.choice1.GetStringSelection()

#参数修改保存事件。
     def PChange(self,event):
        global a
        global sqlitenumber
        global filename
        global place
        global par_time
        #sqlitenumber=sqlitenumber+1
        sqlite_number=str(sqlitenumber)
        print sqlite_number
        print a[0]
        a2=a[0]
        a0=a2[16:42]
        print a0

        filename_flag=0
        filename_flag1=0
        filename_flag2=0
        filename_flag3=0
        filename_flag4=0
        filename_flag5=0
        filename_flag6=0
        filename_flag7=0
        filename_flag8=0
        filename_flag9=0
        filename_flag10=0
        filename_flag11=0
        filename_flag12=0
        filename_flag13=0
        filename_flag14=0
        
        #filename.append("NULL")

        r1= self.Result11.GetValue()
        r2= self.Result22.GetValue()
        r3= self.Result33.GetValue()
        r4= self.Result44.GetValue()
        r5= self.Result55.GetValue()
        r6= self.Result66.GetValue()
        r7= self.Result77.GetValue()
        r8= self.Result88.GetValue()
        r9= self.Result99.GetValue()
        r10=self.Result1010.GetValue()
        r11=self.Result1111.GetValue()
        r12=self.Result1212.GetValue()
        r13=self.Result1313.GetValue()
        r14=self.Result1414.GetValue()
        
        r_flag1="0"
        r_flag2="0"
        r_flag3="0"
        r_flag4="0"
        r_flag5="0"
        r_flag6="0"
        r_flag7="0"
        r_flag8="0"
        r_flag9="0"
        r_flag10="0"
        r_flag11="0"
        r_flag12="0"
        r_flag13="0"
        r_flag14="0"
        

        for i in range(0,len(filename)):
            if filename[i]==a0:
                filename_flag=1
            else:
                filename_flag=0

        if filename_flag==1:
              #cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
              con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
              cur=con.cursor()
              cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
              ReadFileSeePara=cur.fetchall()
              print ReadFileSeePara
              print ReadFileSeePara[0][2]
              if ReadFileSeePara[0][2]!=r1:
                  r_flag1="1"
              if ReadFileSeePara[0][3]!=r2:
                  r_flag2="1"
              if ReadFileSeePara[0][4]!=r3:
                  r_flag3="1"
              if ReadFileSeePara[0][5]!=r4:
                  r_flag4="1"
              if ReadFileSeePara[0][6]!=r5:
                  r_flag5="1"
              if ReadFileSeePara[0][7]!=r6:
                  r_flag6="1"
              if ReadFileSeePara[0][8]!=r7:
                  r_flag7="1"
              if ReadFileSeePara[0][9]!=r8:
                  r_flag8="1"
              if ReadFileSeePara[0][10]!=r9:
                  r_flag9="1"
              if ReadFileSeePara[0][11]!=r10:
                  r_flag10="1"
              if ReadFileSeePara[0][12]!=r11:
                  r_flag11="1"     
              if ReadFileSeePara[0][13]!=r12:
                  r_flag12="1"      
              if ReadFileSeePara[0][14]!=r13:
                  r_flag13="1"
              if ReadFileSeePara[0][15]!=r14:
                  r_flag14="1"
      
                
              cur.execute("update parameters set fmin='%s' where file_name=\'%s\'" %(r1,a0))
              cur.execute("update parameters set fbEs='%s' where file_name=\'%s\'" %(r2,a0))
              cur.execute("update parameters set foF2='%s' where file_name=\'%s\'" %(r3,a0))
              cur.execute("update parameters set hE='%s' where file_name=\'%s\'" %(r4,a0))
              cur.execute("update parameters set hF='%s' where file_name=\'%s\'" %(r5,a0))
              cur.execute("update parameters set M3F2='%s' where file_name=\'%s\'" %(r6,a0))
              cur.execute("update parameters set foE='%s' where file_name=\'%s\'" %(r7,a0))
              cur.execute("update parameters set foF1='%s' where file_name=\'%s\'" %(r8,a0))
              cur.execute("update parameters set fx1='%s' where file_name=\'%s\'" %(r9,a0))
              cur.execute("update parameters set foEs='%s' where file_name=\'%s\'" %(r10,a0))
              cur.execute("update parameters set M3F1='%s' where file_name=\'%s\'" %(r11,a0))
              cur.execute("update parameters set hEs='%s' where file_name=\'%s\'" %(r12,a0))
              cur.execute("update parameters set Es='%s' where file_name=\'%s\'" %(r13,a0))
              cur.execute("update parameters set hF2='%s' where file_name=\'%s\'" %(r14,a0))
              cur.execute("update parameters set Flag_1='%s' where file_name=\'%s\'" %(r_flag1,a0))
              cur.execute("update parameters set Flag_2='%s' where file_name=\'%s\'" %(r_flag2,a0))
              cur.execute("update parameters set Flag_3='%s' where file_name=\'%s\'" %(r_flag3,a0))
              cur.execute("update parameters set Flag_4='%s' where file_name=\'%s\'" %(r_flag4,a0))
              cur.execute("update parameters set Flag_5='%s' where file_name=\'%s\'" %(r_flag5,a0))
              cur.execute("update parameters set Flag_6='%s' where file_name=\'%s\'" %(r_flag6,a0))
              cur.execute("update parameters set Flag_7='%s' where file_name=\'%s\'" %(r_flag7,a0))
              cur.execute("update parameters set Flag_8='%s' where file_name=\'%s\'" %(r_flag8,a0))
              cur.execute("update parameters set Flag_9='%s' where file_name=\'%s\'" %(r_flag9,a0))
              cur.execute("update parameters set Flag_10='%s' where file_name=\'%s\'" %(r_flag10,a0))
              cur.execute("update parameters set Flag_11='%s' where file_name=\'%s\'" %(r_flag11,a0))
              cur.execute("update parameters set Flag_12='%s' where file_name=\'%s\'" %(r_flag12,a0))
              cur.execute("update parameters set Flag_13='%s' where file_name=\'%s\'" %(r_flag13,a0))
              cur.execute("update parameters set Flag_14='%s' where file_name=\'%s\'" %(r_flag14,a0))
              con.commit()####这一步很重要，关于提交的commit！务必谨记！！！
              cur.close()
              cur.close()
        else:       

              #以下部分为连接数据库并且插入。
              con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
              cur=con.cursor()

              cur.execute("insert into parameters Values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                    %(sqlite_number,a0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r_flag1,r_flag2,r_flag3,r_flag4,r_flag5,r_flag6,r_flag7,r_flag8,r_flag9,r_flag10,r_flag11,r_flag12,r_flag13,r_flag14,par_time,place))
              con.commit()
              cur.close()
              cur.close()
        filename.append(a0)
        
#绘画Paint0。
     def Paint0(self,event):
        dc = wx.PaintDC(self)
        
        dc.SetPen(wx.Pen((192,192,192),1))
        rect7 = wx.Rect(10,15,1065,425)
        dc.DrawRoundedRectangleRect(rect7, 10)        
        rect4 = wx.Rect(20,30,250,410)
        dc.DrawRoundedRectangleRect(rect4, 10)        
        rect5 = wx.Rect(270,30,792,410)
        dc.DrawRoundedRectangleRect(rect5, 10)
        rect6 = wx.Rect(65,440,965,150)
        dc.DrawRoundedRectangleRect(rect6, 10)

        #以下是给数据输出区域画图。
        dc.SetPen(wx.Pen((192,192,192),1))
        rect8 = wx.Rect(115,445,880,139)
        dc.DrawRoundedRectangleRect(rect8,10)
        rect9 = wx.Rect(115,445,880,46)
        dc.DrawRoundedRectangleRect(rect9,10)
        rect10 = wx.Rect(115,491,880,46)
        dc.DrawRoundedRectangleRect(rect10,10)
        rect11 = wx.Rect(115,537,880,46)
        dc.DrawRoundedRectangleRect(rect11,10)

        #以下是给图片输出区域画线框。
        dc.SetPen(wx.Pen((192,192,192),1))
        rect12=wx.Rect(390,41,660,390)
        dc.DrawRoundedRectangleRect(rect12,6)


        #画标尺线及其尺度点。
        dc.SetPen(wx.Pen(wx.Colour(138,43,226), 1))
        dc.DrawLine(418, 64, 1045, 64)
        dc.DrawLine(419, 63, 419, 426)

        dc.SetPen(wx.Pen(wx.Colour(255,0,0),1))
        dc.DrawLine(415,63,419,63)
        dc.DrawLine(415,108,419,108)
        dc.DrawLine(415,153,419,153)
        dc.DrawLine(415,198,419,198)
        dc.DrawLine(415,243,419,243)
        dc.DrawLine(415,288,419,288)
        dc.DrawLine(415,333,419,333)
        dc.DrawLine(415,378,419,378)
        dc.DrawLine(415,424,419,424)

        dc.DrawLine(418,60,418,63)
        dc.DrawLine(418+39*1,60,418+39*1,64)
        dc.DrawLine(418+39*2,60,418+39*2,64)
        dc.DrawLine(418+39*3,60,418+39*3,64)
        dc.DrawLine(418+39*4,60,418+39*4,64)
        dc.DrawLine(418+39*5,60,418+39*5,64)
        dc.DrawLine(418+39*6,60,418+39*6,64)
        dc.DrawLine(418+39*7,60,418+39*7,64)
        dc.DrawLine(418+39*8,60,418+39*8,64)
        dc.DrawLine(418+39*9,60,418+39*9,64)
        dc.DrawLine(418+39*10,60,418+39*10,64)
        dc.DrawLine(418+39*11,60,418+39*11,64)
        dc.DrawLine(418+39*12,60,418+39*12,64)
        dc.DrawLine(418+39*13,60,418+39*13,64)
        dc.DrawLine(418+39*14,60,418+39*14,64)
        dc.DrawLine(419+39*15,60,419+39*15,64)
        dc.DrawLine(420+39*16,60,420+39*16,64)
        


        
        #以下是给按钮画出边框，使之立体化。
        dc.SetPen(wx.Pen('black',1))
        rect1 = wx.Rect(33, 348, 84, 29) 
        dc.DrawRoundedRectangleRect(rect1, 1)
        rect2 = wx.Rect(148, 348, 84, 29) 
        dc.DrawRoundedRectangleRect(rect2, 1)
        rect3 = wx.Rect(863, 547, 84, 26) 
        dc.DrawRoundedRectangleRect(rect3, 1)
        

     def OnFileOpen(self, evt):
        wildcard = "data source (*.O)|*.O|" \
            "All files (*.*)|*.*"                             #默认保存类型
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), 
            "", wildcard, wx.OPEN)       # wx.OPEN 表示这是打开filelog，保存用SAVE
        if dialog.ShowModal() == wx.ID_OK: # 当点击确定即是ID_OK， 就执行下面代码
            a[0] = dialog.GetPath()  # 通过GetPath 可以获得打开目标文件路径
            self.Plateb.SetLabel(a[0].decode('utf-8'))                        # 把a的内容（也就是打开文件的路径放到Plateb中显示在界面上）
            file = open(a[0])             # 通过open方法来读取这文件，再后台读取
            m = file.read()            # 用open的read 来读取文件中的数据
            #print m                        #我同样用print 来查看读取究竟是什么东西，结果跟上一步分析一样
            file.close()                  #open后关闭，必须的。
        dialog.Destroy()   



    #重置事件。
     def OnClearMe(self,event):
        
        #注意定义全局变量中的列表的声明方法。
        global PicFlag
        global Flag1,Flag2,Flag3
        global a
        global threshold
        global foF1
        global foF2
        global fxF2
        global hF1
        global hF2
        global fmin
        global timeFlag1
        global timeFlag3
        global timeFlag5
        global timeFlag8
        global timeFlag9
        global timeFlag14
        global fre
        global result
        result=0
        fre=1
        unsure=['不确定'.decode('utf-8'),]
        nothing=['',]
        self.choice0.Clear()
        self.choice0.SetItems(self.sampleList0)
        self.choice1.Clear()
        self.choice1.SetItems(self.sampleList1)
        self.choice2.Clear()
        self.choice2.SetItems(self.sampleList2)
        self.Plateb.SetLabel("提示：请点击上面按钮，选择您所要打开的文件。".decode('utf-8'))
        PicFlag[0]='radion1'       
        Flag1=0
        Flag2=0
        Flag3=0
        Flag4=0
        self.Result11.SetLabel("NULL".decode('utf-8'))
        self.Result22.SetLabel("NULL".decode('utf-8'))
        self.Result33.SetLabel("NULL".decode('utf-8'))
        self.Result44.SetLabel("NULL".decode('utf-8'))
        self.Result55.SetLabel("NULL".decode('utf-8'))
        self.Result66.SetLabel("NULL".decode('utf-8'))
        self.Result77.SetLabel("NULL".decode('utf-8'))
        self.Result88.SetLabel("NULL".decode('utf-8'))
        self.Result99.SetLabel("NULL".decode('utf-8'))
        self.Result1010.SetLabel("NULL".decode('utf-8'))
        self.Result1111.SetLabel("NULL".decode('utf-8'))
        self.Result1212.SetLabel("NULL".decode('utf-8'))
        self.Result1313.SetLabel("NULL".decode('utf-8'))
        self.Result1414.SetLabel("NULL".decode('utf-8'))

        fmin="NULL"
        foF2="NULL"
        foF1="NULL"
        fxF2="NULL"
        hF2="NULL"
        hF1="NULL"


        self.page3.Result11.SetLabel(fmin)
        self.page3.Result33.SetLabel(foF2)
        self.page3.Result88.SetLabel(foF1)
        self.page3.Result99.SetLabel(fxF2)
        self.page3.Result1414.SetLabel(hF2)
        self.page3.Result55.SetLabel(hF1)

        #RadioButton的重置。
        self.radio1.SetValue(true)

        #图片的重置。
        self.PicShow.Destroy()
        #重新生成空位图。
        self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(420, 65),size=(625,360))
        img = wx.Image('D:/DBS/FacePic/a.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
        self.PicShow.SetBitmap(wx.BitmapFromImage(img))

        #self.page3.PicShow.Destroy()
        img = wx.Image('D:/DBS/FacePic/a.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
        self.page3.PicShow.SetBitmap(wx.BitmapFromImage(img))

        
        #在page2中对page3的图片区（缓存区）进行重置。
        self.page3.memDC=wx.MemoryDC(wx.BitmapFromImage(img))

        self.page3.posCtrlX.Clear()
        self.page3.posCtrlY.Clear()


        for ResultPic in  [self.page3.Result11Pic,self.page3.Result22Pic,self.page3.Result33Pic,self.page3.Result44Pic,self.page3.Result55Pic,self.page3.Result66Pic,
                           self.page3.Result77Pic,self.page3.Result88Pic,self.page3.Result99Pic,self.page3.Result1010Pic,self.page3.Result1111Pic,
                           self.page3.Result1212Pic,self.page3.Result1313Pic,self.page3.Result1414Pic,]:
            ResultPic.SetBitmap(wxNullBitmap)

        #在page2中结束page3中的定时器事件。
            
        if timeFlag1==1 :
            self.page3.timer1.Stop()
            self.page3.timer11.Stop()
            self.page3.Result11Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag3==1 :
            self.page3.timer3.Stop()
            self.page3.timer33.Stop()
            self.page3.Result33Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag5==1 :
            self.page3.timer5.Stop()
            self.page3.timer55.Stop()
            self.page3.Result55Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag8==1 :
            self.page3.timer8.Stop()
            self.page3.timer88.Stop()
            self.page3.Result88Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag9==1 :
            self.page3.timer9.Stop()
            self.page3.timer99.Stop()
            self.page3.Result99Pic.SetBitmap(wxNullBitmap)

        
        if timeFlag14==1 :
            self.page3.timer14.Stop()
            self.page3.timer1414.Stop()
            self.page3.Result1414Pic.SetBitmap(wxNullBitmap)


#在page2中对page3中的图片输出区域进行重新绑定。
        self.page3.PicShow.Bind(wx.EVT_MOTION, self.page3.OnMove)
        self.page3.PicShow.Bind(wx.EVT_LEFT_UP, self.page3.OnClick)
        
     def OnShowPic(self,event):
         global Flag1,Flag2,Flag3
         global PicFlag  #此处也要注意列表的声明。
         if self.radio1.GetValue()==True:
            PicFlag[0]='radion1'
         elif self.radio2.GetValue()==True:
            PicFlag[0]='radion2'
         elif self.radio3.GetValue()==True:
            PicFlag[0]='radion3'
         elif self.radio4.GetValue()==True:
            PicFlag[0]='radion4'
         elif self.radio5.GetValue()==True:
            PicFlag[0]='radion5'
         elif self.radio6.GetValue()==True:
            PicFlag[0]='radion6'
         elif self.radio7.GetValue()==True:
            PicFlag[0]='radion7'
         else:
            PicFlag[0]='radion8'

         
         if Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion1':
            #源数据阈值处理后的图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\LabeledOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         elif Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion2':
            #分层以后E区图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\elimg.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         elif Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion3':
            #分层以后F区图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\limg.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         elif Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion4':
            #图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\elayer.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         elif Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion5':
            #图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\eslayer.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         elif Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion6':
            #图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\L_type.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         elif Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion7':
            #图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\m_nreflection.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         elif Flag1==1 and Flag2==1 and Flag3==1 and PicFlag[0]=='radion8':
            #图片的显示。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\Original.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

         else:
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:/DBS/FacePic/a.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))
         


     def OnFindMe(self,event):
        global Flag1,Flag2,Flag3,Flag4
        global foF1
        global foF2
        global fxF2
        global hF1
        global hF2
        global fmin
        global a
        global par_time
        global place
        unsure=['不确定'.decode('utf-8'),]
        nothing=['','提示：请点击上面按钮，选择您所要打开的文件。'.decode('utf-8'),]
        null=['无'.decode('utf-8'),]

        

        if self.Plateb.GetLabel()==nothing[1]:
            #下面新建空输入阈值的提示对话框并完成设置。
            dlg = wx.MessageDialog(None, "请您选择所要打开的文件".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                dlg.Destroy()
        else:
            Flag1=1

        if self.choice0.GetStringSelection()==nothing[0]:
             #下面新建空输入阈值的提示对话框并完成设置。
            dlg = wx.MessageDialog(None, "请您选择度量时间".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                dlg.Destroy()
        else:
            Flag2=1

        if self.choice2.GetStringSelection()==nothing[0]:
             #下面新建空输入阈值的提示对话框并完成设置。
            dlg = wx.MessageDialog(None, "请您选择观测站点".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                dlg.Destroy()
        else:
            Flag4=1
        
        if self.choice1.GetStringSelection()==nothing[0]:
            #下面新建空输入阈值的提示对话框并完成设置。
            dlg = wx.MessageDialog(None, "请您选择一个阈值".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                dlg.Destroy()
        else:
            Flag3=1
            threshold=self.choice1.GetStringSelection()
            
        if Flag1==1 and Flag2==1 and Flag3==1 and Flag4==1:

            global a
            global sqlitenumber
            global filename
            global place
            global par_time
            global ReadFileSeePara_main
            
            #subprocess.call('DBS\EXE\DBSoTOraw.exe %s %s %s' %(a[0].decode('utf-8'),'DBS\wu.raw',threshold))
            #subprocess.call('DBS\EXE\DBSrawTOjpg.exe')
            #subprocess.call('DBS\EXE\DBSprocess.exe')


            #os.startfile('explorer "DBS\DBSoriginalPicExe.exe"')

            os.popen('D:\DBS\EXE\DBSoTOraw.exe %s %s %s' %(a[0].decode('utf-8'),'D:\DBS\wu.raw',threshold))
            os.popen('D:\DBS\EXE\DBSoriginalPicExe.exe')
            os.popen('D:\DBS\EXE\DBSprocess.exe')


            #os.system的弊端在于不能在子进程完全结束后返回主线程。导致后面的主线程落后一拍。不可取。
            #os.system('cmd.exe /c start /B DBS\DBSoTOjpg.exe %s %s %s' %(a[0].decode('utf-8'),'DBS\wu.raw',threshold))
            #os.system('cmd.exe /c start /B DBS\DBSoriginalPicExe.exe')
            #os.system('cmd.exe /c start /B DBS\DBSprocess.exe')
 
            #读取参数。
            f=open('D:\DBS\parameter.txt','r')
            foF1 = f.readline()
            foF2 = f.readline()
            fxF2 = f.readline()
            hF1 = f.readline()
            hF2 = f.readline()
            fmin = f.readline()
            f.close()

            #显示参数。
            self.Result11.SetLabel(fmin)
            self.Result33.SetLabel(foF2)
            self.Result88.SetLabel(foF1)
            self.Result99.SetLabel(fxF2)
            self.Result1414.SetLabel(hF2)
            self.Result55.SetLabel(hF1)

            #ShellExecute(NULL, NULL,'start /b DBS\OPE\OriginalPicExe.exe', NULL, NULL, SW_SHOWNORMAL)
            #WinExec('start /b DBS\OriginalPicExe.exe',SW_HIDE)

            #RadioButton的重置。
            self.radio1.SetValue(true)
            #默认显示一副电离后的图片。
            self.PicShow.Destroy()
            self.PicShow=wx.StaticBitmap(self, -1, wxNullBitmap,pos=(420, 65),size=(625,360))
            img = wx.Image('D:\DBS\LabeledOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(625,360)
            self.PicShow.SetBitmap(wx.BitmapFromImage(img))

            #以下几行为page3的参数输出框和电离图显示框置参。
            self.page3.Result11.SetLabel(fmin)
            self.page3.Result33.SetLabel(foF2)
            self.page3.Result88.SetLabel(foF1)
            self.page3.Result99.SetLabel(fxF2)
            self.page3.Result1414.SetLabel(hF2)
            self.page3.Result55.SetLabel(hF1)
            

            #在page2中对page3的图片区进行赋值。
            img = wx.Image('D:/DBS/PaintedOriginal.jpg',wx.BITMAP_TYPE_ANY).Scale(820,400)
            self.page3.PicShow.SetBitmap(wx.BitmapFromImage(img))
            #self.page3.PicShow.SetBitmap(wx.BitmapFromImage(img))
            self.page3.memDC=wx.MemoryDC(wx.BitmapFromImage(img))
            
###############自动度量里面的数据库之数据保存####################################################
            ReadFileSeePara_main[:]=[]
            place=self.choice2.GetStringSelection()
##            if place1=="青岛站".decode('utf-8'):
##                place="QD"
##            if place1=="青海站".decode('utf-8'):
##                place="QH"
##            if place1=="新乡站".decode('utf-8'):
##                place="XX"
##            if place1=="济南站".decode('utf-8'):
##                place="JN"
## 
##            
            sqlitenumber=sqlitenumber+1
            sqlite_number=str(sqlitenumber)
            print sqlite_number
            print a[0]
            a2=a[0]
            a0=a2[16:42]
            par_time=a2[16:28]
            print a0

            filename_flag=0
            filename_flag1=0
            filename_flag2=0
            filename_flag3=0
            filename_flag4=0
            filename_flag5=0
            filename_flag6=0
            filename_flag7=0
            filename_flag8=0
            filename_flag9=0
            filename_flag10=0
            filename_flag11=0
            filename_flag12=0
            filename_flag13=0
            filename_flag14=0
        
            #filename.append("NULL")

            r1= self.Result11.GetValue()
            r2= self.Result22.GetValue()
            r3= self.Result33.GetValue()
            r4= self.Result44.GetValue()
            r5= self.Result55.GetValue()
            r6= self.Result66.GetValue()
            r7= self.Result77.GetValue()
            r8= self.Result88.GetValue()
            r9= self.Result99.GetValue()
            r10=self.Result1010.GetValue()
            r11=self.Result1111.GetValue()
            r12=self.Result1212.GetValue()
            r13=self.Result1313.GetValue()
            r14=self.Result1414.GetValue()
        
            r_flag1="0"
            r_flag2="0"
            r_flag3="0"
            r_flag4="0"
            r_flag5="0"
            r_flag6="0"
            r_flag7="0"
            r_flag8="0"
            r_flag9="0"
            r_flag10="0"
            r_flag11="0"
            r_flag12="0"
            r_flag13="0"
            r_flag14="0"

            con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
            cur=con.cursor()
            cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
            ReadFileSeePara_main=cur.fetchall()
            print len(ReadFileSeePara_main)#,ReadFileSeePara[0],"ReadFileSeePara,ReadFileSeePara[0]hahahahhahahhah"
            #if ReadFileSeePara[0]=="NULL"
            
        

            for i in range(0,len(filename)):
                if filename[i]==a0:
                    filename_flag=1
                else:
                    filename_flag=0

            if filename_flag==1 or len(ReadFileSeePara_main)!=0:
                  print "s--b"
                  #cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
                  con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
                  cur=con.cursor()
                  cur.execute("Select * From parameters where file_name=\'%s\'" %(a0))
                  ReadFileSeePara=cur.fetchall()
                  print ReadFileSeePara
                  print ReadFileSeePara[0][2]
                  if ReadFileSeePara[0][2]!=r1:
                      r_flag1="1"
                  if ReadFileSeePara[0][3]!=r2:
                      r_flag2="1"
                  if ReadFileSeePara[0][4]!=r3:
                      r_flag3="1"
                  if ReadFileSeePara[0][5]!=r4:
                      r_flag4="1"
                  if ReadFileSeePara[0][6]!=r5:
                      r_flag5="1"
                  if ReadFileSeePara[0][7]!=r6:
                      r_flag6="1"
                  if ReadFileSeePara[0][8]!=r7:
                      r_flag7="1"
                  if ReadFileSeePara[0][9]!=r8:
                      r_flag8="1"
                  if ReadFileSeePara[0][10]!=r9:
                      r_flag9="1"
                  if ReadFileSeePara[0][11]!=r10:
                      r_flag10="1"
                  if ReadFileSeePara[0][12]!=r11:
                      r_flag11="1"     
                  if ReadFileSeePara[0][13]!=r12:
                      r_flag12="1"      
                  if ReadFileSeePara[0][14]!=r13:
                      r_flag13="1"
                  if ReadFileSeePara[0][15]!=r14:
                      r_flag14="1"
      
                
                  cur.execute("update parameters set fmin='%s' where file_name=\'%s\'" %(r1,a0))
                  cur.execute("update parameters set fbEs='%s' where file_name=\'%s\'" %(r2,a0))
                  cur.execute("update parameters set foF2='%s' where file_name=\'%s\'" %(r3,a0))
                  cur.execute("update parameters set hE='%s' where file_name=\'%s\'" %(r4,a0))
                  cur.execute("update parameters set hF='%s' where file_name=\'%s\'" %(r5,a0))
                  cur.execute("update parameters set M3F2='%s' where file_name=\'%s\'" %(r6,a0))
                  cur.execute("update parameters set foE='%s' where file_name=\'%s\'" %(r7,a0))
                  cur.execute("update parameters set foF1='%s' where file_name=\'%s\'" %(r8,a0))
                  cur.execute("update parameters set fx1='%s' where file_name=\'%s\'" %(r9,a0))
                  cur.execute("update parameters set foEs='%s' where file_name=\'%s\'" %(r10,a0))
                  cur.execute("update parameters set M3F1='%s' where file_name=\'%s\'" %(r11,a0))
                  cur.execute("update parameters set hEs='%s' where file_name=\'%s\'" %(r12,a0))
                  cur.execute("update parameters set Es='%s' where file_name=\'%s\'" %(r13,a0))
                  cur.execute("update parameters set hF2='%s' where file_name=\'%s\'" %(r14,a0))
                  cur.execute("update parameters set Flag_1='%s' where file_name=\'%s\'" %(r_flag1,a0))
                  cur.execute("update parameters set Flag_2='%s' where file_name=\'%s\'" %(r_flag2,a0))
                  cur.execute("update parameters set Flag_3='%s' where file_name=\'%s\'" %(r_flag3,a0))
                  cur.execute("update parameters set Flag_4='%s' where file_name=\'%s\'" %(r_flag4,a0))
                  cur.execute("update parameters set Flag_5='%s' where file_name=\'%s\'" %(r_flag5,a0))
                  cur.execute("update parameters set Flag_6='%s' where file_name=\'%s\'" %(r_flag6,a0))
                  cur.execute("update parameters set Flag_7='%s' where file_name=\'%s\'" %(r_flag7,a0))
                  cur.execute("update parameters set Flag_8='%s' where file_name=\'%s\'" %(r_flag8,a0))
                  cur.execute("update parameters set Flag_9='%s' where file_name=\'%s\'" %(r_flag9,a0))
                  cur.execute("update parameters set Flag_10='%s' where file_name=\'%s\'" %(r_flag10,a0))
                  cur.execute("update parameters set Flag_11='%s' where file_name=\'%s\'" %(r_flag11,a0))
                  cur.execute("update parameters set Flag_12='%s' where file_name=\'%s\'" %(r_flag12,a0))
                  cur.execute("update parameters set Flag_13='%s' where file_name=\'%s\'" %(r_flag13,a0))
                  cur.execute("update parameters set Flag_14='%s' where file_name=\'%s\'" %(r_flag14,a0))
                  con.commit()####这一步很重要，关于提交的commit！务必谨记！！！
                  cur.close()
                  cur.close()
            elif len(ReadFileSeePara_main)==0 or filename_flag==0 :       

                  #以下部分为连接数据库并且插入。
                  con=lite.connect('D:\DBS\Data\ionogram_measure_parameters')
                  cur=con.cursor()

                  cur.execute("insert into parameters Values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                        %(sqlite_number,a0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r_flag1,r_flag2,r_flag3,r_flag4,r_flag5,r_flag6,r_flag7,r_flag8,r_flag9,r_flag10,r_flag11,r_flag12,r_flag13,r_flag14,par_time,place))
                  con.commit()
                  cur.close()
                  cur.close()
            filename.append(a0)
 

            
        else:
            PicFlag = ['radion1',]
            Flag1=0
            Flag2=0
            Flag3=0
            a=['FilesPath',]
            threshold=7
            foF1='NULL'
            foF2='NULL'
            fxF2='NULL'
            hF1='NULL'
            hF2='NULL'
            fmin='NULL'
    
           

if __name__ == '__main__':
     app = wx.PySimpleApp()
     frame = InFrame(parent=None, id=-1)
     frame.Show()
     app.MainLoop()
