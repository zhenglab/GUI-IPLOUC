#!/usr/bin/env python
#coding=utf-8

import sqlite3 as lite
import wx,os,sys,string
import wx.lib.buttons
import wx.lib.buttons as buttons
import os
from wxPython.wx import *


#界面############################主页############################################
class InFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id,'人机交互检索界面'.decode('utf-8')
                            ,size=(800,730), style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        panel = wx.Panel(self)
        self.tb  = TestTB(panel,id)
        self.tb.Bind(wx.EVT_TOOLBOOK_PAGE_CHANGED, self.OnPageChanged)
        
        menubar = wx.MenuBar(wx.MB_DOCKABLE)
        
        file = wx.Menu()
        manage=wx.MenuItem(file, 1, "&管理(M)\tCtrl+M".decode('utf-8'))
        imgManage = wx.Image('FacePic/manage.png',wx.BITMAP_TYPE_ANY).Scale(22,22)
        manage.SetBitmap(wx.BitmapFromImage(imgManage))
        quit = wx.MenuItem(file, 2, "&退出(Q)\tCtrl+Q".decode('utf-8'))
        imgQuit = wx.Image('FacePic/quit.png',wx.BITMAP_TYPE_ANY).Scale(17,17)
        quit.SetBitmap(wx.BitmapFromImage(imgQuit))        
        file.AppendItem(manage)
        file.AppendItem(quit)
        self.Bind(wx.EVT_MENU, self.OnLoad, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
        menubar.Append(file, "&文件(F)".decode('utf-8'))        

        help = wx.Menu()
        helps=wx.MenuItem(help, 3,"&帮助(H)\tCtrl+H".decode('utf-8'))
        about=wx.MenuItem(help, 4,"&关于(A)\tCtrl+A".decode('utf-8'))
        imgHelps = wx.Image('FacePic/help.png',wx.BITMAP_TYPE_ANY).Scale(19,19)
        helps.SetBitmap(wx.BitmapFromImage(imgHelps))
        imgabout = wx.Image('FacePic/about.png',wx.BITMAP_TYPE_ANY).Scale(22,22)
        about.SetBitmap(wx.BitmapFromImage(imgabout))
        help.AppendItem(helps)
        help.AppendItem(about)
        menubar.Append(help, "&帮助(H)".decode('utf-8'))
        self.Bind(wx.EVT_MENU, self.OnHelp, id=3)
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
        os.system("start /B notepad 'Help.txt'")
        
    def OnAbout(self,event):
        os.system("start /B notepad 'About.txt'")

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
        wx.Toolbook.__init__(self, parent, id,size=(800,700),pos=(0,2),style=wx.BK_DEFAULT)

        panel = wx.Panel(self)
        
        img1 = wx.Image('FacePic/1.png',wx.BITMAP_TYPE_ANY).Scale(50,50)
        img2 = wx.Image('FacePic/2.png',wx.BITMAP_TYPE_ANY).Scale(50,50)
        img3 = wx.Image('FacePic/3.png',wx.BITMAP_TYPE_ANY).Scale(50,50)
        
        il = wx.ImageList(50,50)
        bmp1 =img1.ConvertToBitmap()
        bmp2 =img2.ConvertToBitmap()
        bmp3 =img3.ConvertToBitmap()
        index1 = il.Add(bmp1)
        index2 = il.Add(bmp2)
        index3 = il.Add(bmp3)
        self.AssignImageList(il)

        page1 = PageOne(self)
        self.AddPage(page1, "    使用说明    ".decode('utf-8'), imageId = index1)
        page3 = PageThree(self);
        page2 = PageTwo(self, page3);
        self.AddPage(page2, "    选择检索    ".decode('utf-8'), imageId = index2)
        self.AddPage(page3, "    查看结果    ".decode('utf-8'), imageId = index3)

        
        
        page1.SetFocus() 
        
     
###########################使用说明######################################
class PageOne(wx.Panel):
     def __init__(self, parent):
         wx.Panel.__init__(self, parent)         
         panel = wx.Panel(self)
         colour = [(255,255,255),(153,204,255),(151,253,225),]
         self.SetBackgroundColour(colour[0])
         #下面几句设置“使用说明”的显示图片。
         self.title=wx.Image('FacePic/11.png',wx.BITMAP_TYPE_ANY).Scale(100,25)
         self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.title),pos=(345,30))         
         Font= wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
         self.Introduction1=wx.StaticText(self, -1, "1：本检索软件的核心功能是“选择检索”，也就是当您输入相应的检索信息（完整或".decode('utf-8'), (90, 92),(200,-1),wx.ALIGN_LEFT)
         self.Introduction11=wx.StaticText(self, -1,"不完整）的时候，软件系统会给出几项藻种供您参考比较。".decode('utf-8'), (115, 117),(200,-1),wx.ALIGN_LEFT)  
         self.Introduction2=wx.StaticText(self, -1, "2：在您进入“选择检索”模块的时候，随着您检索信息的输入，系统会自动匹配出对".decode('utf-8'), (90, 152),(200,-1),wx.ALIGN_LEFT)
         self.Introduction22=wx.StaticText(self, -1, "应的图例以引导您进行较为准确的检索。".decode('utf-8'), (115, 177),(200,-1),wx.ALIGN_LEFT)
         self.Introduction3=wx.StaticText(self, -1, "3：在“选择检索”模块中我们根据您输入的信息提供给您三种藻，其后分别列举了与".decode('utf-8'), (90, 212),(200,-1),wx.ALIGN_LEFT)
         self.Introduction33=wx.StaticText(self, -1, "您的目的藻种的相似程度。".decode('utf-8'), (115, 237),(200,-1),wx.ALIGN_LEFT)
         self.Introduction4=wx.StaticText(self, -1, "4：在“选择检索”模块中，设置有重置功能，方便用户多次检索。同时设“查看详情”".decode('utf-8'), (90, 272),(200,-1),wx.ALIGN_LEFT)
         self.Introduction44=wx.StaticText(self, -1, "按钮，以查看对应藻种的详细信息，默认的“查看结果”选项卡显示最相似藻种。".decode('utf-8'), (115, 297),(200,-1),wx.ALIGN_LEFT)
         self.Introduction5=wx.StaticText(self, -1, "5：在“文件”-->“管理”选项中设置了管理员登陆对话框，这是为了以后的数据库管".decode('utf-8'), (90, 332),(200,-1),wx.ALIGN_LEFT)
         self.Introduction55=wx.StaticText(self, -1, "理方便（目前还未开发完全），普通用户可忽略此功能。".decode('utf-8'), (115, 357),(200,-1),wx.ALIGN_LEFT)
         self.Introduction6=wx.StaticText(self, -1, "6：具体使用方法请参阅“Help.txt”或点击菜单栏中的“帮助(H)”(Ctrl+H)。".decode('utf-8'), (90,392),(200,-1),wx.ALIGN_LEFT)
         self.Introduction7=wx.StaticText(self, -1, "7：如有疑问请联系我们：wugengkun@126.com。".decode('utf-8'), (90,432),(200,-1),wx.ALIGN_LEFT)
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


############################查看结果#####################################
class PageThree(wx.Panel):
     def __init__(self, parent):          
        wx.Panel.__init__(self, parent)

        self.toolkit = parent
        global flag1
        panel = wx.Panel(self)
        
        self.Bind(wx.EVT_PAINT, self.Paint1)
        
        colour = [(255,255,204),(255,204,255),(255, 255, 255),(0,123,167)]
        self.SetBackgroundColour(colour[2])
        #下面几句设置“结果详情”的显示图片。
        self.title=wx.Image('FacePic/33.png',wx.BITMAP_TYPE_ANY).Scale(100,25)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.title),pos=(345,30))
        self.result1 = wx.StaticText(self, -1, "", (43, 100), (100, -1),
                                  wx.ALIGN_CENTER)
        Font= wx.Font(11, wx.MODERN, wx.NORMAL, wx.BOLD)
        self.result1.SetFont(Font)
        
        #下面设置空位图图框和与它对应的文本提示框，同时新建”门纲目科属“的信息文本框。
        self.show1=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(90, 375),size=(450,180))        
        self.TiShiMap1=wx.StaticText(self, -1, "", (90, 342),(200,-1),wx.ALIGN_CENTER)
        
        Font= wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL)
        self.Phylum=wx.StaticText(self, -1, "", (122, 127),(50,-1),wx.ALIGN_CENTER)
        self.Class=wx.StaticText(self, -1, "", (244, 127),(50,-1),wx.ALIGN_CENTER)
        self.Order=wx.StaticText(self, -1, "", (364, 127),(50,-1),wx.ALIGN_CENTER)
        self.Family=wx.StaticText(self, -1, "", (486, 127),(50,-1),wx.ALIGN_CENTER)
        self.Genus=wx.StaticText(self, -1, "", (611, 127),(50,-1),wx.ALIGN_CENTER)

        self.Phylum.SetFont(Font)
        self.Class.SetFont(Font)
        self.Order.SetFont(Font)
        self.Family.SetFont(Font)
        self.Genus.SetFont(Font)

        #下面生成位图类型的返回按钮。
        img = wx.Image('FacePic/back.jpg',wx.BITMAP_TYPE_ANY).Scale(85,45)
        bmp = img.ConvertToBitmap()
        self.button = wx.BitmapButton(self, -1, bmp, pos=(610, 500))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        #下面设置多行输入的文本以显示细胞详细信息。

        colour = [(160,255,204),(153,204,255),(151,253,225),]

        Font= wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL)
        colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167)]
      
        self.multiText = wx.StaticText(self,-1,'', 
                pos = (90,153),size = (610,160), 
                                style = wx.ST_NO_AUTORESIZE)
        self.multiText.SetFont(Font)
        self.multiText.SetBackgroundColour(colour[1])       


     def OnClick(self,event):
        self.toolkit.SetSelection(1)

#绘画Paint1。
     def Paint1(self,event):
        dc = wx.PaintDC(self)
        
        dc.SetPen(wx.Pen((192,192,192),1))
        rect1 = wx.Rect(10,40,765,550)
        self.paintMain=dc.DrawRoundedRectangleRect(rect1, 10)
        rect2 = wx.Rect(83,314,633,250)
        self.paint2=dc.DrawRoundedRectangleRect(rect2, 10)
        rect3 = wx.Rect(83,330,173,39)
        self.paint3=dc.DrawRoundedRectangleRect(rect3, 10)
        rect4 = wx.Rect(83,144,633,170)
        self.paint4=dc.DrawRoundedRectangleRect(rect4, 10)
        rect5 = wx.Rect(85,122,125,22)
        self.paint5=dc.DrawRoundedRectangleRect(rect5, 10)
        rect6 = wx.Rect(210,122,125,22)
        self.paint6=dc.DrawRoundedRectangleRect(rect6, 10)
        rect7 = wx.Rect(335,122,125,22)
        self.paint7=dc.DrawRoundedRectangleRect(rect7, 10)
        rect8 = wx.Rect(460,122,125,22)
        self.paint8=dc.DrawRoundedRectangleRect(rect8, 10)
        rect9 = wx.Rect(585,122,125,22)
        self.paint9=dc.DrawRoundedRectangleRect(rect9, 10)
        rect10 = wx.Rect(83,369,464,191)
        self.paint10=dc.DrawRoundedRectangleRect(rect10, 10)
        

#生成详细结果。    
     def SeeResult1(self,text):
        colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167)]
        self.result1.SetLabel(text)

        
        if text=='强壮前沟藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('强壮前沟藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'1\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'强壮前沟藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='赤潮异弯藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('赤潮异弯藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'2\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'赤潮异弯藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='多纹膝沟藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('多纹膝沟藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'3\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'多纹膝沟藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='反曲原甲藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('反曲原甲藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'4\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'反曲原甲藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='三角棘原甲藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('三角棘原甲藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'5\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'三角棘原甲藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='微小原甲藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('微小原甲藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'6\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'微小原甲藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='具刺膝沟藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('具刺膝沟藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'7\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'具刺膝沟藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='锥状斯氏藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('锥状斯氏藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'8\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'锥状斯氏藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='血红哈卡藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('血红阿卡藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'9\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'血红哈卡藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='条纹环沟藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('条纹环沟藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'10\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'条纹环沟藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='叉状角藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('叉状角藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'11\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'叉状角藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='新月筒柱藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('新月筒柱电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'12\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'新月筒柱藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='梭角藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('梭角藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'13\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'梭角藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='东海原甲藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('东海原甲藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'14\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'东海原甲藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='海洋原甲藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('海洋原甲藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'15\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'海洋原甲藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='米氏凯伦藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('米氏凯伦藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'16\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'米氏凯伦藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='利玛原甲藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('利玛原甲藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'17\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'利玛原甲藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='海洋卡盾藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('海洋卡盾藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'18\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'海洋卡盾藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='盐生卡盾藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('盐生卡盾藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'19\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'盐生卡盾藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='链状亚历山大藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('链状亚历山大藻电镜与光镜图：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'20\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'链状亚历山大藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='奇异棍形藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('奇异棍形藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'21\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'奇异棍形藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='球形棕囊藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('球形棕囊藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'22\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'球形棕囊藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='萎软海链藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('萎软海链藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'23\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'萎软海链藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='聚生角毛藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('聚生角毛藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'24\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'聚生角毛藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='旋链角毛藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('旋链角毛藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'25\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'旋链角毛藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='柔弱角毛藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('柔弱角毛藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'26\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'柔弱角毛藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='日本星杆藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('日本星杆藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'27\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'日本星杆藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='菱形海线藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('菱形海线藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'28\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'菱形海线藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='热带骨条藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('热带骨条藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'29\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'热带骨条藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='玛氏骨条藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('玛氏骨条藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'30\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'玛氏骨条藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='圆海链藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('圆海链藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'31\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'圆海链藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='旋转海链藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('旋转海链藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'32\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'旋转海链藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='尖刺拟菱形藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('尖刺拟菱形藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'33\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'尖刺拟菱形藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='多列拟菱形藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('多列拟菱形藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'34\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'多列拟菱形藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='链状裸甲藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('链状裸甲藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'35\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'链状裸甲藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='塔玛亚历山大藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('塔玛亚历山大藻电镜与光镜图：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'36\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'塔玛亚历山大藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='双胞旋沟藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('双胞旋沟藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'37\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'双胞旋沟藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='窄隙角毛藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('窄隙角毛藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'38\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'窄隙角毛藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='洛氏角毛藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('洛氏角毛藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'39\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'洛氏角毛藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='双胞角毛藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('双胞角毛藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'40\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'双胞角毛藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='卡氏角毛藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('卡氏角毛藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'41\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'卡氏角毛藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])
        elif text=='丹麦细柱藻'.decode('utf-8'):
            self.TiShiMap1.SetLabel('丹麦细柱藻电镜与光镜图像：'.decode('utf-8'))
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'42\'')
            ReadFileSeePic=cur.fetchall()
            cur.close()
            cur.close()
            con=lite.connect('Data0')
            cur1=con.cursor()
            cur1.execute('Select * From DataDetails where cell_name=\'丹麦细柱藻\'')
            ReadFileSeeDetails=cur1.fetchall()
            cur1.close()
            cur1.close() 
            img = wx.Image(ReadFileSeePic[0][8],wx.BITMAP_TYPE_ANY).Scale(450,180)
            self.show1.SetBitmap(wx.BitmapFromImage(img))
            self.multiText.SetLabel(ReadFileSeeDetails[0][15])
            self.Phylum.SetLabel(ReadFileSeeDetails[0][3])
            self.Class.SetLabel(ReadFileSeeDetails[0][5])
            self.Order.SetLabel(ReadFileSeeDetails[0][7])
            self.Family.SetLabel(ReadFileSeeDetails[0][9])
            self.Genus.SetLabel(ReadFileSeeDetails[0][11])

        else:
            self.TiShiMap1.SetLabel('')
            self.show1.SetBackgroundColour(colour[2])
            #下面一行销毁位图框。
            self.show1.Destroy()
            #下面一行销毁位图框后重新生成之。
            self.show1=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(90, 375),size=(400,180))
            #下面对多行文本框及”门纲目科属“进行置空。
            self.multiText.SetLabel('')
            self.Phylum.SetLabel('')
            self.Class.SetLabel('')
            self.Order.SetLabel('')
            self.Family.SetLabel('')
            self.Genus.SetLabel('')
           
        
  


############################选择检索######################################
class PageTwo(wx.Panel):
     #在PageTwo中设置全局变量以便于进行结果输出中新生成的按钮进行清空处理。
     flag=0

     def __init__(self, parent,page3):
        wx.Panel.__init__(self, parent)
        
        self.toolkit = parent

        panel = wx.Panel(self)
        colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167)]
        global flag
        flag=0
        global flag1
        flag1=0
        self.SetBackgroundColour(colour[1])
        self.page3=page3
        self.Last1='无输出结果'.decode('utf-8')
        self.page3.SeeResult1(self.Last1)
        #绑定画板的边线底纹绘制（Paint0部分）。
        self.Bind(wx.EVT_PAINT, self.Paint0)

        #下面几句设置“选择检索”的显示图片。
        self.title=wx.Image('FacePic/22.png',wx.BITMAP_TYPE_ANY).Scale(100,25)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.title),pos=(345,30))

        #下面一句设置下拉菜单引导检索的空位图提示图框和与它对应的文本提示框。
        FontTishiMap1 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL)
        self.show=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(240, 460),size=(100,120))
        self.TiShiMap1=wx.StaticText(self, -1, "", (260, 415),(200,-1),wx.ALIGN_CENTER)
        self.TiShiMap1.SetFont(FontTishiMap1)
        
        self.TiShiMapLS=wx.StaticText(self, -1, "", (130, 415),(200,-1),wx.ALIGN_CENTER)
        self.TiShiMapLS.SetFont(FontTishiMap1)
        self.showLS=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(110, 460),size=(100,120))

        self.TiShiMap5=wx.StaticText(self, -1, "", (367, 415),(200,-1),wx.ALIGN_CENTER)
        self.TiShiMap5.SetFont(FontTishiMap1)
        self.show5=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(375, 460),size=(100,120))

        self.TiShiMap6=wx.StaticText(self, -1, "", (528, 415),(200,-1),wx.ALIGN_CENTER)
        self.TiShiMap6.SetFont(FontTishiMap1)
        self.show6=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(510, 460),size=(100,120))
    
        self.show4=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(195,242),size=(35,31))
        

        #下面几句设置图例引导的显示图片。
        self.guide=wx.Image('FacePic/guide.png',wx.BITMAP_TYPE_ANY).Scale(25,125)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.guide),pos=(25,440))
        
        #下面几句设置静态文本显示框。（空）
        
        FontResult = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)   
        
        self.result1 = wx.StaticText(self, -1, "", (433, 217), (100, -1),
                                  wx.ALIGN_CENTER)
        self.result1.SetFont(FontResult)
        self.result11 = wx.StaticText(self, -1, "", (565, 217), (50, -1),
                                  wx.ALIGN_CENTER)
        self.result11.SetFont(FontResult)

        self.result2 = wx.StaticText(self, -1, "", (433, 262), (100, -1),
                                  wx.ALIGN_CENTER)
        self.result2.SetFont(FontResult)
        self.result22 = wx.StaticText(self, -1, "", (565, 262), (50, -1),
                                  wx.ALIGN_CENTER)
        self.result22.SetFont(FontResult)

        self.result3 = wx.StaticText(self, -1, "", (433, 307), (100, -1),
                                  wx.ALIGN_CENTER)
        self.result3.SetFont(FontResult)
        self.result33 = wx.StaticText(self, -1, "", (565, 307), (50, -1),
                                  wx.ALIGN_CENTER)
        self.result33.SetFont(FontResult)

        #设置细胞大小和图例引导提示语的虚拟文本提示框。
        self.choice2Text=wx.StaticText(self, -1, "", (190, 150), (60, -1),
                                  wx.ALIGN_CENTER)
        self.choice3Text=wx.StaticText(self, -1, "", (215, 200), (80, -1),
                                  wx.ALIGN_CENTER)

        
        #设置显示结果的颜色。
        self.result1.SetForegroundColour('blue')
        self.result11.SetForegroundColour('blue')
        self.result2.SetForegroundColour('blue')
        self.result22.SetForegroundColour('blue')
        self.result3.SetForegroundColour('blue')
        self.result33.SetForegroundColour('blue')
                

        centerFont1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        
        self.center1 = wx.StaticText(self, -1,"",(430,100),
            (140,-1),wx.ALIGN_CENTER)
        self.center2 = wx.StaticText(self, -1,"",(425,120),
            (300,-1),wx.ALIGN_CENTER)
        self.center3 = wx.StaticText(self, -1,"",(432,160),
            (300,-1),wx.ALIGN_CENTER)
        self.center1.SetFont(centerFont1)
        
#生成下拉菜单选项，并设置字体格式。
        DownFont1 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)

        self.Plate1=wx.StaticText(self,-1,"输入操作".decode('utf-8'),(35,68))
        self.Plate1.SetFont(DownFont1)

        self.Plate2=wx.StaticText(self,-1,"输出结果".decode('utf-8'),(705,68))
        self.Plate2.SetFont(DownFont1)
        
        self.sampleList1 = ['不确定'.decode('utf-8'),'单细胞'.decode('utf-8'), '群体'.decode('utf-8'),]
        self.guide1=wx.Image('FacePic/111.png',wx.BITMAP_TYPE_ANY).Scale(59,27)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.guide1),pos=(37,92))
        self.choice1 = wx.Choice(self, -1, (110, 98), choices=self.sampleList1,style=wx.SL_VERTICAL,
                                 name="LifeStyle")


        self.sampleList2 = ['不确定'.decode('utf-8'),'小'.decode('utf-8'), '较大'.decode('utf-8'),'大'.decode('utf-8'),]
        self.guide2=wx.Image('FacePic/222.png',wx.BITMAP_TYPE_ANY).Scale(59,27)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.guide2),pos=(37,142))
        self.choice2 = wx.Choice(self, -1, (110, 148), choices=self.sampleList2,
                                 name="size")


        self.sampleList3 = ['不确定'.decode('utf-8'),'二叉形'.decode('utf-8'),
                            '新月形'.decode('utf-8'),'心形或卵形'.decode('utf-8'),
                            '圆形'.decode('utf-8'),'近圆形'.decode('utf-8'),
                            '卵圆形'.decode('utf-8'),'椭圆形'.decode('utf-8'),
                            '圆球状'.decode('utf-8'),'披针形'.decode('utf-8'),
                            '梭形'.decode('utf-8'),'齿形'.decode('utf-8'),
                            '梨形'.decode('utf-8'),'尖椒形'.decode('utf-8'),
                            '五边近圆形'.decode('utf-8'),'棍形'.decode('utf-8'),
                            '方形'.decode('utf-8'),'三角形'.decode('utf-8'),
                            '菱形'.decode('utf-8'),'纽扣形'.decode('utf-8'),]
        self.guide3=wx.Image('FacePic/333.png',wx.BITMAP_TYPE_ANY).Scale(59,27)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.guide3),pos=(37,192))
        self.choice3 = wx.Choice(self, -1, (110, 198), choices=self.sampleList3,style=wx.SL_VERTICAL,
                                 name="CellsForm")

        
                                
        self.sampleList4 = ['不确定'.decode('utf-8'),'绿色'.decode('utf-8'), '橘黄色'.decode('utf-8'),
                            '黄褐色'.decode('utf-8'),'黄绿色'.decode('utf-8'),]
        self.guide4=wx.Image('FacePic/444.png',wx.BITMAP_TYPE_ANY).Scale(66,27)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.guide4),pos=(37,242))
        self.choice4 = wx.Choice(self, -1, (110, 248), choices=self.sampleList4,style=wx.SL_VERTICAL,
                                 name="colour")

 
        self.sampleList5 = ['不确定'.decode('utf-8'),'光滑'.decode('utf-8'),
                            '布满小刺'.decode('utf-8'), '前端具钩状突起'.decode('utf-8'),
                            '具角毛'.decode('utf-8'),
                            '角毛向不同角度伸出'.decode('utf-8'),'具角毛自链两侧伸出'.decode('utf-8'),
                            '细胞底部有小刺'.decode('utf-8'),
                            '细胞顶部有小刺'.decode('utf-8'),'细胞扁平'.decode('utf-8'),
                            '细胞圆球状'.decode('utf-8'),'中央膨大区向两端平滑无凹陷过渡'.decode('utf-8'),
                            '中央膨大区向两端有凹陷地过渡'.decode('utf-8'),'细胞前宽后尖'.decode('utf-8'),
                            '藻体中央有横沟'.decode('utf-8'),
                            '藻体中央有蛋白核'.decode('utf-8'),'有鞭毛'.decode('utf-8'),
                            '膨大三角形基部和细长长柄'.decode('utf-8'),
                            '相邻细胞借许多突起连成链'.decode('utf-8'),'相邻细胞借中间丝连成链'.decode('utf-8')]
                            

        self.guide5=wx.Image('FacePic/555.png',wx.BITMAP_TYPE_ANY).Scale(59,27)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.guide5),pos=(37,292))    
        self.choice5 = wx.Choice(self, -1, (110, 298), choices=self.sampleList5,style=wx.SL_VERTICAL,
                                 name="character")
        #下面两行为绑定“生活形态”的下拉选择框同时显示静态文本“群体特征”。
        self.choice1.Bind(wx.EVT_CHOICE,self.OnChoice1)
        self.guide6=wx.Image('FacePic/666.png',wx.BITMAP_TYPE_ANY).Scale(59,27)
        self.GuideShow=wx.StaticBitmap(self,-1,wx.BitmapFromImage(self.guide6),pos=(192,92))


        #下面一行为绑定“细胞大小”的下拉选择框。
        self.choice2.Bind(wx.EVT_CHOICE,self.OnChoice2)
        #下面一行为绑定“细胞形态”的下拉选择框。
        self.choice3.Bind(wx.EVT_CHOICE,self.OnChoice3)
        #下面一行为绑定“色素体颜色“的下拉选择框。
        self.choice4.Bind(wx.EVT_CHOICE,self.OnChoice4)
        #下面一行为绑定“细胞特征”的下拉选择框。
        self.choice5.Bind(wx.EVT_CHOICE,self.OnChoice5)


        #下面两行为群体特征创造下拉框。
        self.sampleList6 = ['',]
        self.choice6 = wx.Choice(self, -1, (265,98),wx.Size(110,50),choices=self.sampleList6,
                                 name="Group characteristics")

        #下面一行为绑定“群体特征”的下拉选择框。
        self.choice6.Bind(wx.EVT_CHOICE,self.OnChoice6)

        
        self.str1=[]
        self.str2=[]
        self.str3=[]
        self.str4=[]
        self.str5=[]
        self.str6=[]
        ReadFile=[]
        
#生成“重置”“检索”按钮，并绑定鼠标单击事件。
        
        self.resetButton = buttons.GenButton(self, -1,'重置'.decode('utf-8'),size=(80,25),pos=(68, 350))
        self.resetButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.resetButton.SetBezelWidth(1000)
        self.resetButton.SetBackgroundColour(colour[3])
        self.resetButton.SetForegroundColour("white")
        self.resetButton.SetToolTipString("点击以清屏...".decode('utf-8'))
        
        self.resetButton.Bind(wx.EVT_BUTTON, self.OnClearMe)

        self.findButton = buttons.GenButton(self, -1,'检索'.decode('utf-8'),size=(80,25),pos=(223, 350))
        self.findButton.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        self.findButton.SetBezelWidth(1000)
        self.findButton.SetBackgroundColour(colour[3])
        self.findButton.SetForegroundColour("white")
        self.findButton.SetToolTipString("点击以检索符合输入条件的藻种...".decode('utf-8'))

        self.findButton.Bind(wx.EVT_BUTTON, self.OnFindMe)
        
        
        

#绘画Paint0。
     def Paint0(self,event):
        dc = wx.PaintDC(self)
        
        dc.SetPen(wx.Pen((192,192,192),1))
        rect3 = wx.Rect(10,40,765,360)
        dc.DrawRoundedRectangleRect(rect3, 10)        
        rect4 = wx.Rect(20,75,375,315)
        dc.DrawRoundedRectangleRect(rect4, 10)        
        rect5 = wx.Rect(395,75,372,315)
        dc.DrawRoundedRectangleRect(rect5, 10)
        rect6 = wx.Rect(35,400,715,192)
        dc.DrawRoundedRectangleRect(rect6, 10)
        
        dc.SetPen(wx.Pen('black',1))
        rect1 = wx.Rect(66, 348, 84, 29) 
        dc.DrawRoundedRectangleRect(rect1, 1)
        rect2 = wx.Rect(221, 348, 84, 29) 
        dc.DrawRoundedRectangleRect(rect2, 1)

        
#重置事件。
     def OnClearMe(self,event):

        unsure=['不确定'.decode('utf-8'),]
        nothing=['',]
        global flag
        if flag==42 :
            self.detailButton1.Destroy()
            self.detailButton2.Destroy()
            self.detailButton3.Destroy()
        flag=0

        #选项卡的重置清零。
        self.choice = [self.choice1, self.choice2, self.choice3,
                       self.choice4, self.choice5,self.choice6]
        self.sampleList = ['', self.sampleList1, self.sampleList2,
                    self.sampleList3, self.sampleList4, self.sampleList5,self.sampleList6]
        for i in range(1, 7):
            self.choice[i-1].Clear()
            self.choice[i-1].SetItems(self.sampleList[i])
        #结果显示框和文本提示框的重置清零以及第三界面的结果重置。
        colour = [(160,255,204),(153,204,255),(151,253,225),(0,123,167)]
        self.center1.SetLabel('')
        self.center2.SetLabel('')
        self.center3.SetLabel('')
        self.result1.SetLabel('')
        self.result11.SetLabel('')
        self.result2.SetLabel('')
        self.result22.SetLabel('')
        self.result3.SetLabel('')
        self.result33.SetLabel('')
        self.choice2Text.SetLabel('')
        self.choice3Text.SetLabel('')
        self.TiShiMap1.SetLabel('')
        self.TiShiMap5.SetLabel('')
        self.TiShiMap6.SetLabel('')
        self.TiShiMapLS.SetLabel('')
        self.showLS.SetBackgroundColour(colour[1])
        self.show.SetBackgroundColour(colour[1])
        #为了从page3返回page2时候不再看见位图，下面一行销毁位图框。
        self.show.Destroy()
        self.showLS.Destroy()
        #下面一行销毁位图框后重新生成之。
        self.show=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(240, 460),size=(100,120))
        self.showLS=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(110, 460),size=(100,120))
        self.show4.SetBackgroundColour(colour[1])
        self.show4.Destroy()
        self.show4=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(195,242),size=(35,31))
        self.show5.SetBackgroundColour(colour[1])
        self.show5.Destroy()
        self.show5=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(375, 460),size=(100,120))
        self.show6.SetBackgroundColour(colour[1])
        self.show6.Destroy()
        self.show6=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(510, 460),size=(100,120))
        
        self.Last1='无输出结果'.decode('utf-8')
        self.page3.SeeResult1(self.Last1)
        
        #被按下的检索键的恢复未选择状态重置。
        self.findButton.SetBackgroundColour(colour[3])
        self.findButton.SetForegroundColour("white")
#“群体特征：”事件,"生活形态"的提示事件。。
     def OnChoice1(self,event):

        if self.choice1.GetStringSelection()=='不确定'.decode('utf-8') or self.choice1.GetStringSelection()=='':
            self.choice6.Clear()
            self.choice6.Append('不确定'.decode('utf-8'))
            self.choice6.Append('锯齿状群体群体'.decode('utf-8'))
            self.choice6.Append('螺旋状群体'.decode('utf-8'))
            self.choice6.Append('膨松团状群体'.decode('utf-8'))
            self.choice6.Append('平行排列群体'.decode('utf-8'))
            self.choice6.Append('群体链弯曲'.decode('utf-8'))
            self.choice6.Append('球形群体'.decode('utf-8'))
            self.choice6.Append('团块状群体'.decode('utf-8'))
            self.choice6.Append('直链状群体'.decode('utf-8'))

            self.TiShiMapLS.SetLabel('')
            colour = [(160,255,204),(153,204,255),(151,253,225),]
            self.showLS.Destroy()
            self.showLS=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(110, 460),size=(100,120))
            self.TiShiMapLS.SetLabel('')
            self.TiShiMap6.SetLabel('')
            self.show6.Destroy()
            self.show6=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(510, 460),size=(100,120))
            
        else:            
            if self.choice1.GetStringSelection()=='单细胞'.decode('utf-8'):
                
                self.TiShiMap6.SetLabel('')
                self.show6.Destroy()
                self.show6=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(510, 460),size=(100,120))
                
                self.choice6.Clear()
                self.choice6.Append("无".decode('utf-8'))
                self.choice6.SetSelection(0)
                self.TiShiMapLS.SetLabel('单细胞图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'1\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][12],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.showLS.SetBitmap(wx.BitmapFromImage(img))
            if self.choice1.GetStringSelection()=='群体'.decode('utf-8'):
                self.TiShiMapLS.SetLabel('群体图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'20\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][12],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.showLS.SetBitmap(wx.BitmapFromImage(img))
                self.choice6.Clear()
                self.choice6.Append('不确定'.decode('utf-8'))
                self.choice6.Append('锯齿状群体群体'.decode('utf-8'))
                self.choice6.Append('螺旋状群体'.decode('utf-8'))
                self.choice6.Append('膨松团状群体'.decode('utf-8'))
                self.choice6.Append('平行排列群体'.decode('utf-8'))
                self.choice6.Append('群体链弯曲'.decode('utf-8'))
                self.choice6.Append('球形群体'.decode('utf-8'))
                self.choice6.Append('团块状群体'.decode('utf-8'))
                self.choice6.Append('直链状群体'.decode('utf-8'))
#“细胞大小”的提示事件。
     def OnChoice2(self,event):
        if self.choice2.GetStringSelection()=='小'.decode('utf-8'):
            self.choice2Text.SetLabel('细胞长度在10μm~20μm之间'.decode('utf-8'))
        if self.choice2.GetStringSelection()=='较大'.decode('utf-8'):
            self.choice2Text.SetLabel('细胞长度在20μm~150μm之间'.decode('utf-8'))
        if self.choice2.GetStringSelection()=='大'.decode('utf-8'):
            self.choice2Text.SetLabel('细胞长度在150μm~550μm之间'.decode('utf-8'))
        if self.choice2.GetStringSelection()=='不确定'.decode('utf-8'):
            self.choice2Text.SetLabel('')
#“细胞形态”的提示事件。
     def OnChoice3(self,event):
        if self.choice3.GetStringSelection()=='不确定'.decode('utf-8'):
            self.choice3Text.SetLabel('')
            colour = [(160,255,204),(153,204,255),(151,253,225),]
            self.show.Destroy()
            self.show=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(240, 460),size=(100,120))
            self.TiShiMap1.SetLabel('')
        else:
            self.choice3Text.SetLabel('请您参照图例引导区的图例'.decode('utf-8'))
            if self.choice3.GetStringSelection()=='二叉形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('二叉形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'11\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='新月形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('新月形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'1\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='五边近圆形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('五边近圆形：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'3\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='尖椒形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('尖椒形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'4\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='披针形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('披针形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'5\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='心形或卵形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('心形或卵形：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'6\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='梭形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('梭形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'12\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='齿形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('齿形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'14\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='梨形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('梨形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'15\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='近圆形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('近圆形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'16\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='卵圆形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('卵圆形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'17\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='椭圆形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('椭圆形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'18\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='圆球状'.decode('utf-8'):
                self.TiShiMap1.SetLabel('圆球状图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'20\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='棍形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('棍形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'21\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='圆形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('圆形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'22\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='方形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('方形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'24\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='三角形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('三角形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'27\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='菱形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('菱形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'28\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))
            if self.choice3.GetStringSelection()=='纽扣形'.decode('utf-8'):
                self.TiShiMap1.SetLabel('纽扣形图例：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'29\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][9],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show.SetBitmap(wx.BitmapFromImage(img))

#“色素体颜色”的提示事件。
     def OnChoice4(self,event):
        if self.choice4.GetStringSelection()=='不确定'.decode('utf-8'):
            colour = [(160,255,204),(153,204,255),(151,253,225),]
            self.show4.Destroy()
            self.show4=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(195,242),size=(35,31))
        else:
            if self.choice4.GetStringSelection()=='绿色'.decode('utf-8'):
                img = wx.Image('FacePic/lvse.png',wx.BITMAP_TYPE_ANY).Scale(35,31)
                self.show4.SetBitmap(wx.BitmapFromImage(img))
            if self.choice4.GetStringSelection()=='黄褐色'.decode('utf-8'):
                img = wx.Image('FacePic/huanghese.png',wx.BITMAP_TYPE_ANY).Scale(35,31)
                self.show4.SetBitmap(wx.BitmapFromImage(img))
            if self.choice4.GetStringSelection()=='黄绿色'.decode('utf-8'):
                img = wx.Image('FacePic/huanglvse.png',wx.BITMAP_TYPE_ANY).Scale(35,31)
                self.show4.SetBitmap(wx.BitmapFromImage(img))
            if self.choice4.GetStringSelection()=='橘黄色'.decode('utf-8'):
                img = wx.Image('FacePic/juhuangse.png',wx.BITMAP_TYPE_ANY).Scale(35,31)
                self.show4.SetBitmap(wx.BitmapFromImage(img))
        
     def OnChoice5 (self,event):
        if self.choice5.GetStringSelection()=='不确定'.decode('utf-8'):
            colour = [(160,255,204),(153,204,255),(151,253,225),]
            self.show5.Destroy()
            self.show5=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(375, 460),size=(100,120))
            self.TiShiMap5.SetLabel('')
        else:
            if self.choice5.GetStringSelection()=='藻体中央有横沟'.decode('utf-8'):
                self.TiShiMap5.SetLabel('藻体中央有横沟：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'16\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][10],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show5.SetBitmap(wx.BitmapFromImage(img))
            if self.choice5.GetStringSelection()=='藻体中央有蛋白核'.decode('utf-8'):
                self.TiShiMap5.SetLabel('藻体中央有蛋白核：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'17\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][10],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show5.SetBitmap(wx.BitmapFromImage(img))
            if self.choice5.GetStringSelection()=='膨大三角形基部和细长长柄'.decode('utf-8'):
                self.TiShiMap5.SetLabel('膨大三角基和细长柄：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'27\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][10],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show5.SetBitmap(wx.BitmapFromImage(img))
            if self.choice5.GetStringSelection()=='相邻细胞借中间丝连成链'.decode('utf-8'):
                self.TiShiMap5.SetLabel('细胞借中间丝连成链：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'31\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][10],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show5.SetBitmap(wx.BitmapFromImage(img))
            if self.choice5.GetStringSelection()=='具角毛自链两侧伸出'.decode('utf-8'):
                self.TiShiMap5.SetLabel('具角毛自链两侧伸出：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'38\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][10],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show5.SetBitmap(wx.BitmapFromImage(img))

     def OnChoice6(self,event):
        if self.choice6.GetStringSelection()=='不确定'.decode('utf-8')or self.choice6.GetStringSelection()=='':
            colour = [(160,255,204),(153,204,255),(151,253,225),]
            self.show6.Destroy()
            self.show6=wx.StaticBitmap(self, -1, wxNullBitmap, pos=(510, 460),size=(100,120))
            self.TiShiMap6.SetLabel('')
        else:
            if self.choice6.GetStringSelection()=='直链状群体'.decode('utf-8'):
                self.TiShiMap6.SetLabel('直链状群体：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'20\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][11],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show6.SetBitmap(wx.BitmapFromImage(img))
            if self.choice6.GetStringSelection()=='平行排列群体'.decode('utf-8'):
                self.TiShiMap6.SetLabel('平行排列群体：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'21\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][11],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show6.SetBitmap(wx.BitmapFromImage(img))
            if self.choice6.GetStringSelection()=='膨松团状群体'.decode('utf-8'):
                self.TiShiMap6.SetLabel('膨松团状群体：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'24\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][11],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show6.SetBitmap(wx.BitmapFromImage(img))
            if self.choice6.GetStringSelection()=='螺旋状群体'.decode('utf-8'):
                self.TiShiMap6.SetLabel('螺旋状群体：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'25\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][11],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show6.SetBitmap(wx.BitmapFromImage(img))
            if self.choice6.GetStringSelection()=='锯齿状群体群体'.decode('utf-8'):
                self.TiShiMap6.SetLabel('锯齿状群体群体：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'28\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][11],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show6.SetBitmap(wx.BitmapFromImage(img))
            if self.choice6.GetStringSelection()=='群体链弯曲'.decode('utf-8'):
                self.TiShiMap6.SetLabel('群体链弯曲：'.decode('utf-8'))
                con=lite.connect('Data0')
                cur=con.cursor()
                cur.execute('Select * From DataCharacters where CellId=\'30\'')
                ReadFileCF=cur.fetchall()
                cur.close()
                cur.close()
                img = wx.Image(ReadFileCF[0][11],wx.BITMAP_TYPE_ANY).Scale(100,120)
                self.show6.SetBitmap(wx.BitmapFromImage(img))
#设置PageChange的内容，切换时候显示详细信息。
            
     def PageChange1(self,event):
        self.page3.SeeResult1(self.Last1)
        self.toolkit.SetSelection(2)


     def PageChange2(self,event):
        self.page3.SeeResult1(self.Last2)
        self.toolkit.SetSelection(2)

     def PageChange3(self,event):
        self.page3.SeeResult1(self.Last3)
        self.toolkit.SetSelection(2)
        
        
     def OnFindMe(self,event):        
        unsure=['不确定'.decode('utf-8'),]
        nothing=['',]
        null=['无'.decode('utf-8'),]

        global flag
        if flag==42:
            self.detailButton1.Destroy()
            self.detailButton2.Destroy()
            self.detailButton3.Destroy()
            self.result1.SetLabel('')
            self.result11.SetLabel('')
            self.result2.SetLabel('')
            self.result22.SetLabel('')
            self.result3.SetLabel('')
            self.result33.SetLabel('')



        colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167),(51,204,255)]

        self.findButton.SetBackgroundColour(colour[4])
        self.findButton.SetForegroundColour("white")
        self.choice = [self.choice1, self.choice2, self.choice3,
                       self.choice4, self.choice5,self.choice6]
        self.str = [self.str1,self.str2,self.str3,self.str4,self.str5,self.str6]

        
        for i in range(1, 7):
            self.str[i-1]=self.choice[i-1].GetStringSelection()
        if flag!=42 and (self.str[0]==unsure[0] or self.str[0]==nothing[0]) and (self.str[1]==unsure[0] or self.str[1]==nothing[0])and (self.str[2]==unsure[0] or self.str[2]==nothing[0]) and (self.str[3]==unsure[0] or self.str[3]==nothing[0])and (self.str[4]==unsure[0] or self.str[4]==nothing[0]) and (self.str[5]==unsure[0] or self.str[5]==nothing[0]) :

            self.result1.SetLabel('')
            self.result11.SetLabel('')
            self.result2.SetLabel('')
            self.result22.SetLabel('')
            self.result3.SetLabel('')
            self.result33.SetLabel('')
            
            #下面重置检索按钮到未选中状态。
            self.findButton.SetBackgroundColour(colour[3])
            self.findButton.SetForegroundColour("white")

            #下面新建对话框并完成设置。
            dlg = wx.MessageDialog(None, "请您输入检索信息".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                dlg.Destroy()

        elif flag==42 and (self.str[0]==unsure[0] or self.str[0]==nothing[0]) and (self.str[1]==unsure[0] or self.str[1]==nothing[0])and (self.str[2]==unsure[0] or self.str[2]==nothing[0]) and (self.str[3]==unsure[0] or self.str[3]==nothing[0])and (self.str[4]==unsure[0] or self.str[4]==nothing[0]) and (self.str[5]==unsure[0] or self.str[5]==nothing[0]) :

            self.center1.SetLabel('')
            self.center2.SetLabel('')
            self.center3.SetLabel('')
            self.result1.SetLabel('')
            self.result11.SetLabel('')
            self.result2.SetLabel('')
            self.result22.SetLabel('')
            self.result3.SetLabel('')
            self.result33.SetLabel('')

            self.Last1='无输出结果'.decode('utf-8')
            self.page3.SeeResult1(self.Last1)
            
            #下面重置检索按钮到未选中状态。
            self.findButton.SetBackgroundColour(colour[3])
            self.findButton.SetForegroundColour("white")

            #下面新建对话框并完成设置。
            dlg = wx.MessageDialog(None, "请您输入检索信息".decode('utf-8'),'提示'.decode('utf-8'),
                                  wx.OK| wx.ICON_EXCLAMATION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):
                dlg.Destroy()
            flag=0
            

        else :

            flag=1

            colour = [(255,255,204),(255, 255, 255),(151,253,225),(0,123,167),(51,204,255)]

            self.detailButton1 = wx.Button(self, label="查看详细信息".decode('utf-8'), pos=(643, 214),
                size=(90,25))
            self.detailButton1.Bind(wx.EVT_BUTTON, self.PageChange1)

            self.detailButton2 = wx.Button(self, label="查看详细信息".decode('utf-8'), pos=(643, 259),
                size=(90,25))
            self.detailButton2.Bind(wx.EVT_BUTTON, self.PageChange2)

            self.detailButton3 = wx.Button(self, label="查看详细信息".decode('utf-8'), pos=(643, 304),
                size=(90,25))
            self.detailButton3.Bind(wx.EVT_BUTTON, self.PageChange3)
        

        #输出提示文本事件。
            self.center1.SetLabel('检索结果如下：'.decode('utf-8'))
            self.center2.SetLabel('（其中右侧数值为此藻类与目的藻类的相似程度）'.decode('utf-8'))
            self.center3.SetLabel('最接近目的藻种的前三种藻类及各自近似程度依次如下：'.decode('utf-8'))

        #文件事件。
            #文件事件中匹配特征字符的函数。
            def compare():
                if self.str[0]==ReadFile[0][2] or self.str[0]==unsure[0]or self.str[0]==nothing[0]:
                        LifeStyle=1
                else:
                        LifeStyle=0
                if self.str[1]==ReadFile[0][3] or self.str[1]==unsure[0]or self.str[1]==nothing[0]:
                        size=1
                else:
                        size=0
                if self.str[2]==ReadFile[0][4] or self.str[2]==unsure[0]or self.str[2]==nothing[0]:
                        CellsForm=1
                else:
                        CellsForm=0
                if self.str[3]==ReadFile[0][5] or self.str[3]==unsure[0]or self.str[3]==nothing[0]:
                        colour=1
                else:
                        colour=0
                if self.str[4]==ReadFile[0][6] or self.str[4]==unsure[0]or self.str[4]==nothing[0]:
                        character=1
                else:
                        character=0

                #群体特征不确定时。
                if self.str[5]==unsure[0] or self.str[5]==nothing[0]:
                        GroupCharacteristics1=1
                        GroupCharacteristics2=1
                else:
                    #群体特征"无"（进入单细胞情况）时。
                    if self.str[5]==null[0]:
                            GroupCharacteristics1=1
                            GroupCharacteristics2=0
                    else:
                            #群体特征和多细胞匹配时候。
                            if self.str[5]==ReadFile[0][7]:
                                GroupCharacteristics1=0
                                GroupCharacteristics2=1
                            else:
                                GroupCharacteristics1=0
                                GroupCharacteristics2=0
                list1=[LifeStyle,size,CellsForm,colour,character,GroupCharacteristics1,GroupCharacteristics2]
                return list1
            #访问并计算文件中第一行的藻种的匹配概率。
            Possibility=[0,]
            
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'1\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility1=0.05*data[0]+0.05*data[1]+0.1*data[2]+0.05*data[3]+0.45*data[4]+0.3*data[5]
            Possibility.append(Possibility1)
            cur.close()
            cur.close()
            
            

            #访问并计算文件中第二行的藻种的匹配概率。

            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'2\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility2=0.05*data[0]+0.05*data[1]+0.40*data[2]+0.05*data[3]+0.15*data[4]+0.3*data[5]
            Possibility.append(Possibility2)
            cur.close()
            cur.close()

            #访问并计算文件中第三行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'3\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility3=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.05*data[3]+0.35*data[4]+0.3*data[5]
            Possibility.append(Possibility3)
            cur.close()
            cur.close()

            #访问并计算文件中第四行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'4\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility4=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.05*data[3]+0.35*data[4]+0.3*data[5]
            Possibility.append(Possibility4)
            cur.close()
            cur.close()
            
            #访问并计算文件中第五行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'5\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility5=0.05*data[0]+0.05*data[1]+0.4*data[2]+0.05*data[3]+0.15*data[4]+0.3*data[5]
            Possibility.append(Possibility5)
            cur.close()
            cur.close()
            
            #访问并计算文件中第六行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'6\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility6=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[5]
            Possibility.append(Possibility6)
            cur.close()
            cur.close()
            
            #访问并计算文件中第七行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'7\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility7=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.05*data[3]+0.35*data[4]+0.3*data[5]
            Possibility.append(Possibility7)
            cur.close()
            cur.close()
            
            #访问并计算文件中第八行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'8\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility8=0.05*data[0]+0.05*data[1]+0.1*data[2]+0.05*data[3]+0.45*data[4]+0.3*data[5]
            Possibility.append(Possibility8)
            cur.close()
            cur.close()
            
            #访问并计算文件中第九行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'9\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility9=0.05*data[0]+0.05*data[1]+0.1*data[2]+0.05*data[3]+0.45*data[4]+0.3*data[5]
            Possibility.append(Possibility9)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'10\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility10=0.05*data[0]+0.05*data[1]+0.1*data[2]+0.05*data[3]+0.45*data[4]+0.3*data[5]
            Possibility.append(Possibility10)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十一行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'11\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility11=0.05*data[0]+0.05*data[1]+0.4*data[2]+0.05*data[3]+0.15*data[4]+0.3*data[5]
            Possibility.append(Possibility11)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十二行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'12\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility12=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[5]
            Possibility.append(Possibility12)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十三行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'13\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility13=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[5]
            Possibility.append(Possibility13)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十四行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'14\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility14=0.05*data[0]+0.05*data[1]+0.35*data[2]+0.05*data[3]+0.2*data[4]+0.3*data[5]
            Possibility.append(Possibility14)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十五行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'15\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility15=0.05*data[0]+0.05*data[1]+0.15*data[2]+0.05*data[3]+0.4*data[4]+0.3*data[5]
            Possibility.append(Possibility15)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十六行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'16\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility16=0.05*data[0]+0.05*data[1]+0.1*data[2]+0.05*data[3]+0.45*data[4]+0.3*data[5]
            Possibility.append(Possibility16)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十七行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'17\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility17=0.025*data[0]+0.025*data[1]+0.025*data[2]+0.025*data[3]+0.6*data[4]+0.3*data[5]
            Possibility.append(Possibility17)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十八行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'18\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility18=0.025*data[0]+0.025*data[1]+0.025*data[2]+0.025*data[3]+0.6*data[4]+0.3*data[5]
            Possibility.append(Possibility18)
            cur.close()
            cur.close()
            
            #访问并计算文件中第十九行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'19\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility19=0.05*data[0]+0.05*data[1]+0.05*data[2]+0.4*data[3]+0.15*data[4]+0.3*data[5]
            Possibility.append(Possibility19)
            cur.close()
            cur.close()
            
            #访问并计算文件中第20行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'20\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility20=0.05*data[0]+0.05*data[1]+0.3*data[2]+0.05*data[3]+0.25*data[4]+0.3*data[6]
            Possibility.append(Possibility20)
            cur.close()
            cur.close()
            
            #访问并计算文件中第21行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'21\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility21=0.05*data[0]+0.05*data[1]+0.3*data[2]+0.05*data[3]+0.25*data[4]+0.3*data[6]
            Possibility.append(Possibility21)
            cur.close()
            cur.close()
            
            #访问并计算文件中第22行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'22\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility22=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.05*data[3]+0.35*data[4]+0.3*data[6]
            Possibility.append(Possibility22)
            cur.close()
            cur.close()
            
            #访问并计算文件中第23行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'23\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility23=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.05*data[3]+0.35*data[4]+0.3*data[6]
            Possibility.append(Possibility23)
            cur.close()
            cur.close()
            
            #访问并计算文件中第24行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'24\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility24=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.1*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility24)
            cur.close()
            cur.close()
            
            #访问并计算文件中第25行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'25\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility25=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.1*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility25)
            cur.close()
            cur.close()
            
            #访问并计算文件中第26行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'26\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility26=0.05*data[0]+0.05*data[1]+0.15*data[2]+0.05*data[3]+0.4*data[4]+0.3*data[6]
            Possibility.append(Possibility26)
            cur.close()
            cur.close()
            
            #访问并计算文件中第27行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'27\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility27=0.05*data[0]+0.05*data[1]+0.2*data[2]+0.1*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility27)
            cur.close()
            cur.close()
            
            #访问并计算文件中第28行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'28\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility28=0.05*data[0]+0.05*data[1]+0.35*data[2]+0.05*data[3]+0.2*data[4]+0.3*data[6]
            Possibility.append(Possibility28)
            cur.close()
            cur.close()
            
            #访问并计算文件中第29行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'29\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility29=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility29)
            cur.close()
            cur.close()
            
            #访问并计算文件中第30行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'30\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility30=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility30)
            cur.close()
            cur.close()
            
            #访问并计算文件中第31行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'31\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility31=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility31)
            cur.close()
            cur.close()
            
            #访问并计算文件中第32行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'32\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility32=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility32)
            cur.close()
            cur.close()
            
            #访问并计算文件中第33行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'33\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility33=0.05*data[0]+0.05*data[1]+0.3*data[2]+0.1*data[3]+0.2*data[4]+0.3*data[6]
            Possibility.append(Possibility33)
            cur.close()
            cur.close()
            
            #访问并计算文件中第34行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'34\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility34=0.05*data[0]+0.05*data[1]+0.35*data[2]+0.05*data[3]+0.2*data[4]+0.3*data[6]
            Possibility.append(Possibility34)
            cur.close()
            cur.close()
            
            #访问并计算文件中第35行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'35\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility35=0.0*data[0]+0.05*data[1]+0.25*data[2]+0.1*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility35)
            cur.close()
            cur.close()
            
            #访问并计算文件中第36行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'36\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility36=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility36)
            cur.close()
            cur.close()
            
            #访问并计算文件中第37行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'37\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility37=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility37)
            cur.close()
            cur.close()
            
            #访问并计算文件中第38行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'38\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility38=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility38)
            cur.close()
            cur.close()
            
            #访问并计算文件中第39行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'39\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility39=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility39)
            cur.close()
            cur.close()
            
            #访问并计算文件中第40行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'40\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility40=0.05*data[0]+0.05*data[1]+0.15*data[2]+0.25*data[3]+0.2*data[4]+0.3*data[6]
            Possibility.append(Possibility40)
            cur.close()
            cur.close()
            
            #访问并计算文件中第41行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'41\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility41=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility41)
            cur.close()
            cur.close()
            
            #访问并计算文件中第42行的藻种的匹配概率。
            con=lite.connect('Data0')
            cur=con.cursor()
            cur.execute('Select * From DataCharacters where CellId=\'42\'')
            ReadFile=cur.fetchall()
            data=compare()
            Possibility42=0.05*data[0]+0.05*data[1]+0.25*data[2]+0.05*data[3]+0.3*data[4]+0.3*data[6]
            Possibility.append(Possibility42)
            cur.close()
            cur.close()

            flag=42
            

        
            #计算寻找最接近目的藻种的前三种藻类的概率值和行号事件。
            def Max():
                Max=Possibility[1]
                LineNumber=1
                for i in range(1,43):
                  if Max<Possibility[i]:
                      Max=Possibility[i]
                      LineNumber=i
                return [Max,LineNumber]
            Biggest=Max()
            Possibility[Biggest[1]]=0
            Bigger=Max()
            Possibility[Bigger[1]]=0
            Big=Max()



      #输出最接近的三种藻类的名字和接近程度（概率）。       
            #访问并计算文件中最相似行的藻种，提取藻种名字和概率值。并显示在界面上。
            con=lite.connect('Data0')
            cur=con.cursor()
            Biggest1=Biggest[1]
            cur.execute('Select * From DataCharacters where CellId=:Biggest1',{"Biggest1":Biggest1})
            ReadFile=cur.fetchall()
            #为page3中的查看结果做参数传递准备。
            self.Last1=ReadFile[0][1]
            self.result1.SetLabel(ReadFile[0][1])
            self.result11.SetLabel(str(Biggest[0]))
            cur.close()
            cur.close()
            
            
            #访问并计算文件中第二相似行的藻种，提取藻种名字和概率值。并显示在界面上。
            con=lite.connect('Data0')
            cur=con.cursor()
            Bigger1=Bigger[1]
            cur.execute('Select * From DataCharacters where CellId=:Bigger1',{"Bigger1":Bigger1})
            ReadFile=cur.fetchall()
            #为page3中的查看结果做参数传递准备。
            self.Last2=ReadFile[0][1]
            self.result2.SetLabel(ReadFile[0][1])
            self.result22.SetLabel(str(Bigger[0]))
            cur.close()
            cur.close()
            


            #访问并计算文件中第三相似行的藻种，提取藻种名字和概率值。并显示在界面上。
            con=lite.connect('Data0')
            cur=con.cursor()
            Big1=Big[1]
            cur.execute('Select * From DataCharacters where CellId=:Big1',{"Big1":Big1})
            ReadFile=cur.fetchall()
            #为page3中的查看结果做参数传递准备。
            self.Last3=ReadFile[0][1]
            self.result3.SetLabel(ReadFile[0][1])
            self.result33.SetLabel(str(Big[0]))
            cur.close()
            cur.close()
            



        self.page3.SeeResult1(self.Last1)


if __name__ == '__main__':
     app = wx.PySimpleApp()
     frame = InFrame(parent=None, id=-1)
     frame.Show()
     app.MainLoop()
