# import LoginMenu as login
# login.LoginGUI(login.root)
# login.root.mainloop()
import cv2
import time
import datetime
import os
import numpy as np
import tkinter as tk
from tkinter import ttk,Tk,Menu,Button, messagebox
from PIL import Image, ImageTk
import CSDL
import xlsxwriter
fontface = cv2.FONT_HERSHEY_TRIPLEX
fontscale = 0.7
fontcolor = (0,0,0)
count = 0
stt = 0
source = "ClassList"
saveDir = "FaceData"
try:
    Classlist = next(os.walk('ClassList/'))[1]
except:
    Classlist = ["Trống"]
try:
    os.mkdir(source)
except:
    pass
PROGRAM_NAME = "Face Detecting"
class FaceMachine:
    panel = None
    button = None
    button2 = None
    key = True
    vs  = cv2.VideoCapture(0)
    camera1 = False
    camera_1 = False

    HinhThuc = None
    detector=cv2.CascadeClassifier("C:\\Users\erenb\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
    def __init__(self, root):
        self.root = root
        self.root.title(PROGRAM_NAME)
        self.init_gui()
    def create_top_menu(self):
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load Project", command=self.load)
        self.file_menu.add_command(label="Save Project", command=self.load)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.root.config(menu=self.menu_bar)        
    def exit_app(self):
        if messagebox.askokcancel("Quit", "Really quit?"):
            self.root.destroy()
    def load():

    	return
    def init_gui(self):
        self.create_top_menu()
        self.create_tab()
    def show_about(self):

        messagebox.showinfo(PROGRAM_NAME,"Roll up class by detecting face\nDevelope by Tran Ngoc")
    def create_tab(self):
        TabLayout = ttk.Notebook(self.root)     
        #2 tab   
        TAB1 = ttk.Frame(TabLayout)         
        TAB2 = ttk.Frame(TabLayout)        
        TAB3 = ttk.Frame(TabLayout)          
        TabLayout.add(TAB1, text='Nhận Diện Học Viên Theo Lớp')         
        TabLayout.add(TAB2, text='Lưu Thông Tin Nhận Diện')         
        TabLayout.add(TAB3, text='Điểm Danh')  
        #button = tk.Button(TAB1, text="Forward")
        #button.grid(row=5, column=5, padx=5, pady=5)
        #TAB1
        self.TAB1(TAB1)
        self.TAB2(TAB2)
        self.TAB3(TAB3)

        #Pack
        TabLayout.pack(expand=1, fill='both')
        # 3 TAB
    def TAB1(self,TAB1):
        MSSV = tk.StringVar() # defines the widget state as string
        HoTen = tk.StringVar()
        Lop = tk.StringVar()
        Nam = tk.BooleanVar()
        Nu = tk.BooleanVar()
        #self.Confirm(MSSV,HoTen,Lop,Nam,Nu)
        #Panel Camera
        self.panel = tk.Label(TAB1, bd = 10,height = 450, width = 512,  relief= 'sunken')
        self.panel.place(x = 20, y = 15)
        self.MatDo = tk.Scale(TAB1, from_=1, to=5,width = 18,length = 340,orient="horizontal")

        self.MatDo.set(1)
        self.MatDoLabel = tk.Label(TAB1,text="ĐỘ CHÍNH XÁC : ",font = (10))
        self.MatDoLabel.place(x = 20, y = 495)                
        self.MatDo.place(x = 200, y = 480)
        imgtk = ImageTk.PhotoImage(Image.open("Appdata/webcam.png"))  # convert image for tkinter
        self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        self.panel.config(image=imgtk)
        #Header
        textFrame = tk.Frame(TAB1, height = 40,width = 480)
        tk.Label(textFrame, text="NHẬP THÔNG TIN HỌC VIÊN", font=("Helvetica", 22,'bold')).pack()
        textFrame.place(x = 570, y = 20)
        #Nhap Thong Tin
        inputFrame = tk.Frame(TAB1, height = 480,width = 480, bd = 1, relief= 'ridge')
        tk.Label(inputFrame, text="MSSV  ",font=("Times",14)).grid(row=2, column=1,pady = 3,padx = 3,sticky ='W')
        tk.Entry(inputFrame, width=25, textvariable=MSSV,font=("Times",14,'bold')).grid(row=2, column=2,pady = 3,padx = 3,sticky ='NW')
        tk.Label(inputFrame, text="Họ Tên  ",font=("Times",14)).grid(row=3, column=1,pady = 3,padx = 3,sticky ='W')
        tk.Entry(inputFrame, width=25, textvariable=HoTen,font=("Times",14,'bold')).grid(row=3, column=2,pady = 3,padx = 3,sticky ='NW')
        tk.Label(inputFrame, text="Lớp  ",font=("Times",14)).grid(row=4, column=1,pady = 3,padx = 3,sticky ='W')
        tk.Entry(inputFrame, width=25, textvariable=Lop,font=("Times",14,'bold')).grid(row=4, column=2,pady = 3,padx = 3,sticky ='NW')        
        tk.Label(inputFrame, text="Giới Tính  ",font=("Times",14)).grid(row=5, column=1,pady = 3,padx = 3,sticky ='W')
        GT = None
        tk.Checkbutton(inputFrame, text="Nam", variable=Nam, command= lambda arg1 = Nam, arg2 = Nu ,arg3 = GT: self.checkGT(arg1,arg2,arg3)).grid(row=5, column=2)
        tk.Checkbutton(inputFrame, text="Nữ   ", variable=Nu,command= lambda arg1 = Nu, arg2 = Nam ,arg3 = GT: self.checkGT(arg1,arg2,arg3)).grid(row=6, column=2)
        inputFrame.place(x = 600, y = 70)
        #Button Quét Dữ Liệu
        btframe = tk.Frame(TAB1)
        self.QuetBtn = tk.Button(btframe,text="QUÉT DỮ LIỆU", fg="blue",command = lambda arg1 = MSSV,arg2 = HoTen,arg3 = Lop,arg4 = Nam,arg5=Nu :self.Confirm(arg1,arg2,arg3,arg4,arg5),font=(22))
        self.QuetBtn.pack()      
        btframe.place(x = 788,y = 234)
        btframe2 = tk.Frame(TAB1)
        self.NgungQuetbtn = tk.Button(btframe2,text="HIỆN CAMERA", fg="blue",command = self.ShowHideCamera,font=(22))
        self.NgungQuetbtn.pack()    
        btframe2.place(x = 605,y = 234)
        #Log
        logFrame = tk.Frame(TAB1, height = 15,width = 50, bd = 1, relief= 'ridge')
        self.log = tk.Text(logFrame, wrap='word', height = 14,width = 50)
        logFrame.pack()
        self.log.pack(expand='yes', fill='both')
        self.log.insert("end", 'Chú ý : Có thể quét ngay, camera tự động mở\n')
        logFrame.place(x = 570, y = 280)
        #Start
    def TAB2(self,TAB2):
        #Panel Avatar
        self.imagePanel = tk.Label(TAB2, bd = 10,height = 340, width = 300,  relief= 'sunken')
        self.imagePanel.place(x = 20, y = 25)
        avatar = ImageTk.PhotoImage(Image.open("Appdata/Avatar.png"))
        self.imagePanel.imgtk = avatar
        self.imagePanel.config(image=avatar)
        self.Name = "TRẦN NGỌC QUANG"
        self.Khoa = "CNTT"
        self.BoMon = "THỊ GIÁC MÁY TÍNH"
        self.Truong = "ĐẠI HỌC BÔN BA"


        tk.Label(TAB2,text="Giảng Viên : ",font=(16)).place(x=20,y = 400+2)
        tk.Label(TAB2,text=self.Name,font=('Helvetica',15,'bold')).place(x=120,y = 400)
        tk.Label(TAB2,text="Khoa           : ",font=(16)).place(x=20,y = 425+2)
        tk.Label(TAB2,text=self.Khoa,font=('Helvetica',15,'bold')).place(x=120,y = 425)
        tk.Label(TAB2,text="Bộ Môn       : ",font=(15)).place(x=20,y = 450+2)
        tk.Label(TAB2,text=self.BoMon,font=('Helvetica',15,'bold')).place(x=120,y = 450)
        tk.Label(TAB2,text="Trường       : ",font=(15)).place(x=20,y = 475+2)
        tk.Label(TAB2,text=self.Truong,font=('Helvetica',15,'bold')).place(x=120,y = 475)


        #Lớp
        self.dataFrame = tk.Frame(TAB2,bd = 1,height = 80, width = 580,  relief= 'groove')
        self.dataFrame.place(x = 380,y=70)
        #Chọn Lớp
        tk.Label(TAB2,text="Chọn Lớp : ",font=(15)).place(x= 380,y=30)
        self.chooseLop = ttk.Combobox(TAB2, values=(Classlist))
        self.chooseLop.bind('<<ComboboxSelected>>',lambda event, y = TAB2:self.MaHoaHocVien(event,y))
        self.chooseLop.place(x= 500,y=25)
        self.chooseLop.config(width=14,font=(14))
        #Thông Tin Học Viên Frame
        self.tthv = tk.Frame(TAB2,bd = 1,height = 340, width = 580,  relief= 'groove')
        self.tthv.place(x = 380,y=160)
    def TAB3(self,TAB3):
        self.DiemDanhMode = False
        self.FModule = cv2.CascadeClassifier("C:\\Users\erenb\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        self.detectMachine = cv2.face.LBPHFaceRecognizer_create();
        #Camera Panel
        self.cameraPanel = tk.Label(TAB3, bd = 10,height = 428, width = 428,  relief= 'sunken')
        self.cameraPanel.place(x = 20, y = 15)
        imgtk = ImageTk.PhotoImage(Image.open("Appdata/webcam.png"))  # convert image for tkinter
        self.cameraPanel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        self.cameraPanel.config(image=imgtk)
        #Button Show/hide,Button Điểm Danh và Log
        buttonFrame = tk.Frame(TAB3,bd = 0,relief='groove',width = 450,height = 55)
        buttonFrame.place(x=20,y=470)
        self.camera3 = False
        self.button3 = tk.Button(buttonFrame,text  ="HIỆN CAMERA",width = 12,font=('Consolas',14),command = self.ShowHideCamera3)
        self.button3.place(x=0,y=8)
        self.Start = tk.Button(buttonFrame,text  ="ĐIỂM DANH",width = 12,font=('Consolas',14),command =self.DiemDanh)
        self.Start.place(x=312,y=8)

        self.log3 = tk.Text(buttonFrame, wrap='word', height = 2,width = 16, relief="groove")
        self.log3.tag_configure("center", justify='center')
        vscroll = tk.Scrollbar(buttonFrame, orient="vertical", command=self.log3.yview)
        self.log3['yscroll'] = vscroll.set
        vscroll.place(x=280,y = 4) 
        self.log3.insert("1.0","LOG\n")
        self.log3.insert("1.0","Nhập bên phải\n")
        self.log3.insert("1.0","Chưa đủ chi tiết\n")
        self.log3.tag_add("center", "1.0", "end")
        self.log3.config(state='disabled')   
        self.log3.place(x = 146, y = 9) 
        #
        self.DiemDanhMode = False
        #Chọn Lớp/Tiết
        tkbFrame = tk.Frame(TAB3,bd= 2,relief='sunken',width=500,height = 100)
        tkbFrame.place(x = 482,y=420)
        self.EnoughCondition = 0
        self.TKBbox(tkbFrame)
        #Header
        tk.Label(TAB3,bd= 2,relief='groove',text="HỌC VIÊN ĐÃ ĐIỂM DANH",font = ('Helvetica',20,'bold'),padx=75,pady=10).place(x = 485,y=15)
        #Điểm Danh Frame
        self.diemDanhFrame = tk.Frame(TAB3,width=497,height = 330,bd=3,relief="groove")
        self.diemDanhFrame.place(x = 485, y = 80)
        self.ThongTinDiemDanh(self.diemDanhFrame)
    #TAB3 Function
    def ThongTinDiemDanh(self,diemDanhFrame):
        self.HocVienGanNhat = []
        self.ListCC = {}
        self.Last = ""
        self.BangDiemDanh(diemDanhFrame)
        self.GanDay(diemDanhFrame)
        self.LuuDanhSach(diemDanhFrame)
    def LuuDanhSach(self,diemDanhFrame):        
        LuuBtn = tk.Button(diemDanhFrame,text="Lưu Danh Sách",height = 1, width = 12,font =(12),command = self.XacNhanLuuDanhSachHocVien)#command = lambda arg1 = MSSV,arg2 = HoTen,arg3 = Lop,arg4 = GioiTinh ,arg5= confirmWD:self.ConfirmOK(arg1,arg2,arg3,arg4,arg5)).place(x=220,y=200)
        LuuBtn.place(x = 55, y = 279)
    def XacNhanLuuDanhSachHocVien(self):
        DSHV = tk.Tk()
        DSHV.title("Xác Nhận Lưu Học Viên Đã Điểm Danh")
        DSHV.geometry('370x500')
        data = self.HocVienDiemDanhLog.get("1.0",'end-1c')
        box = tk.Text(DSHV, wrap='word', height = 18,width = 25, bd = 2,relief="groove",font=(14),padx = 10)
        vscroll = tk.Scrollbar(DSHV, orient="vertical", command=box.yview)
        box['yscroll'] = vscroll.set
        vscroll.place(x=335,y = 10)
        box.insert("1.0",data.replace("lúc","vào lớp lúc"))
        box.place(x = 10, y = 10)
        box.config(state='disabled')
        #Button
        confirm = tk.Button(DSHV,width = 10, text ="Xác Nhận",font =(8),command =lambda x = DSHV, y = data: self.LuuHVDiemDanh(x,y))
        cancel = tk.Button(DSHV,width = 10, text ="Hủy",font =(8),command =lambda x = DSHV: self.HuyLuuHVDiemDanh(x))
        confirm.place(x = 200, y = 450)
        cancel.place( x= 10, y = 450)       
        DSHV.mainloop()
    def HuyLuuHVDiemDanh(self,DSHV):
        DSHV.destroy()
    def LuuHVDiemDanh(self,DSHV,data):
        try:
            os.mkdir("KetQuaDiemDanh")
        except:
            pass
        filename = "KetQuaDiemDanh\\" +str(self.chonLop.get())+ str(self.chonNam.get()) + "_"+str(self.chonThang.get()) + "_"+str(self.chonNgay.get())
        workbook = xlsxwriter.Workbook("KetQuaDiemDanh\\" +str(self.chonLop.get())+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Hello')
        workbook.close()
        f = open(filename+'.txt','w')
        f.write(data)
        f.close()
        messagebox.showinfo("Hoàn Thành","Đã Lưu Danh Sách Điểm Danh")
        self.HuyLuuHVDiemDanh(DSHV)
    def GanDay(self,diemDanhFrame):
        tk.Label(diemDanhFrame, text ="GẦN ĐÂY",font=(14)).place(x = 315, y = 10)
        self.GanDayImage = tk.Label(diemDanhFrame, bd = 2,height = 12, width = 24,  relief= 'sunken')        
        self.GanDayImage.place(x = 275, y = 38)
    def BangDiemDanh(self,diemDanhFrame):        
        self.HocVienDiemDanhLog = tk.Text(diemDanhFrame, wrap='word', height = 14,width = 23, relief="groove",bd = 2,font=(12))
        self.HocVienDiemDanhLog.tag_configure("center", justify='center')
        vscroll = tk.Scrollbar(diemDanhFrame, orient="vertical", command=self.HocVienDiemDanhLog.yview)
        self.HocVienDiemDanhLog['yscroll'] = vscroll.set
        vscroll.place(x=232,y = 10) 
        self.HocVienDiemDanhLog.config(state='disabled')   
        self.HocVienDiemDanhLog.place(x = 10, y = 7)    
    def TKBbox(self,tkbFrame):
        self.cClass = next(os.walk('ClassList/'))[1]
        self.Month = []
        self.Year  = []
        self.Date =[]
        ttk.Label(tkbFrame,text = "LỚP", width = "8",anchor="center",font=('Arial',14)).grid(column =1,row = 1,padx = 1,columnspan = 2)        
        ttk.Label(tkbFrame,text = "NĂM", width = "6",anchor="center",font=('Arial',14)).grid(column =3,row = 1,padx = 1)
        ttk.Label(tkbFrame,text = "THÁNG", width = "6",anchor="center",font=('Arial',14)).grid(column =4,row = 1,padx = 1)
        ttk.Label(tkbFrame,text = "NGÀY", width = "7",anchor="center",font=('Arial',14)).grid(column =5,row = 1,padx = 1,columnspan = 2)
        ttk.Label(tkbFrame,text = "THỨ", width = "9",anchor="center",font=('Arial',14)).grid(column =7,row = 1,padx = 1)
        #
        ttk.Label(tkbFrame,text = "Số Tiết : ", width = "8",anchor="w",font=('Arial',14)).grid(column =1,row = 4,padx = 1,pady = 2)
        ttk.Label(tkbFrame,text = "BĐ:", width = "3",anchor="w",font=('Arial',14)).place(x = 140, y = 62)
        ttk.Label(tkbFrame,text = "KT : ", width = "3",anchor="w",font=('Arial',14)).place(x = 330, y = 62)
        ttk.Label(tkbFrame,text = ":", width = "1",anchor="w",font=('Arial',13)).place(x = 240-5, y = 62)        #Chọn Lớp
        self.chonLop = ttk.Combobox(tkbFrame, values=(self.cClass), width = "8",font=('Arial',14))
        self.chonLop.grid(column =1,row = 2,padx = 1,pady = 3,sticky='nw',rowspan = 2,columnspan = 2) 
        self.chonLop.set("Lớp")

        self.chonLop.bind('<<ComboboxSelected>>', self.UpdateLop)        
        #Số tiết        
        self.soTiet = ttk.Combobox(tkbFrame, width = "3",font=('Arial',13))
        self.soTiet.grid(column =2,row = 3,padx = 1,pady = 3,sticky='nw')
        self.soTiet.set("Tiết") 
        self.soTiet.set(5) #Xoa
        self.soTiet.place(x = 85, y = 62)
        self.soTiet.bind('<<ComboboxSelected>>', self.UpdateLNTN)
        #Giờ Bắt Đầu                      
        self.batDauH = ttk.Combobox(tkbFrame, width = "3",font=('Arial',13))
        self.batDauH.place(x = 190-5, y = 62)
        self.batDauH.set("HH")
        self.batDauH.set(6)
        self.batDauH.bind('<<ComboboxSelected>>', self.UpdateLNTN)
        self.batDauM = ttk.Combobox(tkbFrame, width = "3",font=('Arial',13))
        self.batDauM.place(x = 250-5, y = 62)
        self.batDauM.set("MM")
        self.batDauM.set(5)
        self.batDauM.bind('<<ComboboxSelected>>', self.UpdateLNTN)
        #Giờ Kết Thúc                    
        self.ketThucH = ttk.Label(tkbFrame, width = "7",font=('Arial',15))
        self.ketThucH.place(x = 380, y = 61)
        self.ketThucH.configure(text=" -- : --")
        #Năm
        self.chonNam = ttk.Combobox(tkbFrame, values=(self.Year), width = "6",font=('Arial',14))
        self.chonNam.grid(column =3,row = 2,padx = 1,pady = 3,sticky='nw',rowspan = 2) 
        self.chonNam.set("Năm")
        self.chonNam.bind('<<ComboboxSelected>>', self.UpdateLNTN)
        #Tháng
        self.chonThang = ttk.Combobox(tkbFrame, values=(self.Month), width = "6",font=('Arial',14))
        self.chonThang.grid(column =4,row = 2,padx = 1,pady = 3,sticky='nw',rowspan = 2) 
        self.chonThang.set("Tháng")
        self.chonThang.bind('<<ComboboxSelected>>',self.UpdateLNTN)
        # #Ngày
        self.chonNgay = ttk.Combobox(tkbFrame, values=(self.Date), width = "5",font=('Arial',14))
        self.chonNgay.grid(column =5,row = 2,padx = 1,pady = 3,sticky='nw',columnspan = 2,rowspan = 2) 
        self.chonNgay.set("Ngày")        
        self.chonNgay.bind('<<ComboboxSelected>>', self.UpdateLNTN)
        #Thứ
        self.chonThu = ttk.Combobox(tkbFrame, width = "9",font=('Arial',14))
        self.chonThu.grid(column =7,row = 2,padx = 1,pady = 3,sticky='nw') 
        self.chonThu.set("Thứ")        
        self.chonThu.bind('<<ComboboxSelected>>', self.UpdateLNTN)
    def UpdateLop(self,event = None):
        lop = str(self.chonLop.get())
        messagebox.showinfo("Chọn Lớp","Tải dữ liệu khuôn mặt lớp "+lop)
        self.detectMachine.read("FaceData\\" + lop +".yml")

        messagebox.showinfo("Hoàn thành","Đã tải dữ liệu khuôn mặt lớp "+lop)
        currentDT = datetime.datetime.now()
        self.chonNam.set(str(currentDT.year))
        self.chonThang.set(str(currentDT.month)) 
        self.chonNgay.set(str(currentDT.day))
        self.UpdateLNTN()
    def UpdateLNTN(self,event=None):
        if self.chonLop.get() !="Lớp":
        # self.Day = ["Thứ 2","Thứ 3","Thứ 4","Thứ 5","Thứ 6","Thứ 7","Chủ Nhật"]
            self.Year  = [str(datetime.datetime.now().year-1),str(datetime.datetime.now().year),str(datetime.datetime.now().year+1)]
            self.chonNam.configure(values=self.Year)
            self.EnoughCondition = 1
        if self.chonNam.get() != "Năm":
            self.Month = ["1","2","3","4","5","6","7","8","9","10","11","12"]
            self.chonThang.configure(values=self.Month)
            self.EnoughCondition = 2
        if self.chonThang.get() != "Tháng":
            self.Day = []
            #self.chonNgay.set("Ngày")
            if self.chonThang.get() =="2":
                if (int(self.chonNam.get()) %4 == 0 and int(self.chonNam.get()) % 100 != 0):                    
                    for x in range(1,30):
                        self.Day.append(str(x))
                else:
                    for x in range(1,29):
                        self.Day.append(str(x))
            else:
                if self.chonThang.get() in ["4","6","9","11"]:
                    for x in range(1,31):
                        self.Day.append(str(x))
                else:
                    for x in range(1,32):
                        self.Day.append(str(x))
            self.chonNgay.configure(values=self.Day)
            self.EnoughCondition = 3
        if self.chonNgay.get() !="Ngày":
            temp = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
            thu = datetime.date(int(self.chonNam.get()),int(self.chonThang.get()),int(self.chonNgay.get())).strftime("%A")
            Day = ["Chủ Nhật","Thứ Hai","Thứ Ba","Thứ Tư","Thứ Năm","Thứ Sáu","Thứ Bảy"]
            self.chonThu.set(Day[temp.index(thu)])
            self.EnoughCondition = 5
        if self.chonLop.get() !="Lớp":
            self.soTiet.configure(values=(1,2,3,4,5,6))
        if self.soTiet.get()!= "Tiết":
            self.EnoughCondition = 6
            self.batDauH.configure(values=(6,7,8,9,10,11,12,13,14,15,16,17,18,19))
        if(self.batDauH.get()!= "HH"):
            self.EnoughCondition = 7
            self.batDauM.configure(values=(0,5,10,15,20,25,30,35,40,45,50,55,60))
        if (self.batDauM.get()!="MM"):
            if self.EnoughCondition == 7:
                thoiluong = int(self.soTiet.get()) * 45 + int(self.batDauM.get())+(int(int(self.soTiet.get())/2)-1) * 15 + (int(self.soTiet.get())-1)*5
                ktH = int(self.batDauH.get()) + int(thoiluong / 60)
                if (ktH < 10):
                    ktH = "0" + str(ktH)
                ktH = str(ktH)
                ktM = int(thoiluong % 60)
                if (ktM < 10):
                    ktM = "0" + str(ktM)
                ktM = str(ktM)
                self.ketThucH.configure(text = ktH+ " : "+ ktM)      
            self.EnoughCondition = 8
    def ShowHideCamera3(self):
        if self.camera3 == False:
            self.DiemDanhMode == True
            self.camera3 = True
            self.button3.configure(text="ẨN CAMERA")
            self.log3.config(state='normal')   
            self.log3.insert("1.0","CAMERA : ON\n")
            self.log3.tag_add("center", "1.0", "end")
            self.log3.config(state='disabled')         
        else:
            self.DiemDanhMode == False
            self.camera3 = False 
            self.button3.configure(text="HIỆN CAMERA")
            self.log3.config(state='normal')   
            self.log3.insert("1.0","CAMERA : OFF\n")
            self.log3.tag_add("center", "1.0", "end")
            self.log3.config(state='disabled')  
        self.showcamera3()
    def showcamera3(self):
        if (self.camera3 == False):
            imgtk = ImageTk.PhotoImage(Image.open("Appdata/webcam.png"))  # convert image for tkinter
            self.cameraPanel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.cameraPanel.config(image=imgtk)
            #self.root.update
            return
        ok, frame = self.vs.read()
        if ok:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            self.current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
            self.cameraPanel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.cameraPanel.config(image=imgtk)
            # show the image
        self.root.after(50, self.showcamera3)
    def DiemDanh(self):
        if self.EnoughCondition ==8: # Sua cho nay    
            if self.camera3 == False:
                self.camera3 = True
                self.button3.configure(text="ẨN CAMERA")
                self.log3.config(state='normal')   
                self.log3.insert("1.0","CAMERA : ON\n")
                self.log3.tag_add("center", "1.0", "end")
                self.log3.config(state='disabled')         
            else:
                self.camera3 = False 
                self.button3.configure(text="HIỆN CAMERA")            

                self.log3.config(state='normal')   
                self.log3.insert("1.0","CAMERA : OFF\n")
                self.log3.tag_add("center", "1.0", "end")
                self.log3.config(state='disabled')
            if (self.DiemDanhMode == False):
                self.DiemDanhMode = True
                self.log3.config(state='normal')   
                self.log3.insert("1.0","Đang Điểm Danh\n")
                self.log3.tag_add("center", "1.0", "end")
                self.log3.config(state='disabled')
                self.Start.configure(text="NGỪNG")
            else:
                self.DiemDanhMode = False
                self.log3.config(state='normal')   
                self.log3.insert("1.0","Ngừng Điểm Danh\n")
                self.log3.tag_add("center", "1.0", "end")
                self.log3.config(state='disabled')
                self.Start.configure(text="ĐIỂM DANH")
            self.DiemDanhCamera()
        else:
            if (self.EnoughCondition == 0):
                messagebox.showinfo("Thông báo","Chưa chọn lớp")
            if (self.EnoughCondition == 5):
                messagebox.showinfo("Thông báo","Chưa chọn số tiết")
            if (self.EnoughCondition == 6):
                messagebox.showinfo("Thông báo","Chưa chọn giờ bắt đầu")
            if (self.EnoughCondition == 7):
                messagebox.showinfo("Thông báo","Chưa chọn giờ bắt đầu")

            self.log3.config(state='normal') 
            self.log3.insert("1.0","Nhập bên phải\n")
            self.log3.insert("1.0","Chưa đủ chi tiết\n")
            self.log3.tag_add("center", "1.0", "end")
            self.log3.config(state='disabled') 
        return
    def XuatHocVienGanNhat(self,frame,MSSV,HoTen,Lop,Tuoi):
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2.imwrite(saveDir+'\\temp.jpg', frame)
        pil_image = Image.open(saveDir+'\\temp.jpg')
        image200x100 = pil_image.resize((180, 180), Image.ANTIALIAS)
        tk_image2 = ImageTk.PhotoImage(image200x100)
        self.GanDayImage.imgtk = tk_image2
        self.GanDayImage.config(image=tk_image2,height = 180, width = 180)
        os.remove(saveDir+'\\temp.jpg')
        tk.Label(self.diemDanhFrame,text=str(MSSV),width = 18, font =('Consolas',14)).place(x = 270, y = 230)
        tk.Label(self.diemDanhFrame,text=str(HoTen),width = 18, font =('Consolas',14)).place(x = 270, y = 252)
        tk.Label(self.diemDanhFrame,text=str(Lop) + " - " + str(Tuoi),width = 20, font =('Consolas',14)).place(x = 260, y = 274)
        #Ghi Danh
        currentDT = datetime.datetime.now()
        self.HocVienDiemDanhLog.config(state='normal')
        self.HocVienDiemDanhLog.insert("1.0",str(MSSV) + " lúc " +str(currentDT.hour)+":"+str(currentDT.minute)+"\n")
        self.HocVienDiemDanhLog.config(state='disabled')
    def DiemDanhCamera(self):
        # if (self.camera3 == True):
        #     self.camera3 == False
        #     self.showcamera3()
        #     return
        ok, frame = self.vs.read()
        if ok:
            if self.DiemDanhMode == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.FModule.detectMultiScale(gray, 1.3, 4);
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    id, conf = self.detectMachine.predict(gray[y:y + h, x:x + w])
                    person = CSDL.getData(id)
                    if person != None and str(person[0]) not in self.HocVienGanNhat:
                        print(self.HocVienGanNhat)
                        print(str(person[0]))
                        self.HocVienGanNhat.append(str(person[0]))
                        self.ListCC[str(person[0])] = 1
                        self.XuatHocVienGanNhat(gray[y-30:y + h+30, x-30:x + w+30],person[0],person[1],person[2],person[3])
                        if (str(person[0]) != self.Last):
                            if (self.ListCC[str(person[0])] == 1):
                                print("vo")
                            else:
                                print("ra")
                            self.Last =str(person[0]) 
                        else:
                            pass
                    if person != None and str(person[0]) in self.HocVienGanNhat:
                        if (str(person[0]) != self.Last):
                            if (self.ListCC[str(person[0])] == 1):
                                self.ListCC[str(person[0])] = 0
                                print("Ra")
                            else:
                                self.ListCC[str(person[0])] = 1
                                print("Vo")                        
                            self.Last =str(person[0])
                            
                    if person != None:
                        # cv2.PutText(cv2.fromarray(img),str(id),(x+y+h),font,(0,0,255),2);
                        cv2.putText(frame, str(person[1]),(x, y + h + 30), fontface, fontscale, fontcolor, 2)
                        cv2.putText(frame, str(person[2]), (x, y + h + 50), fontface, fontscale, fontcolor, 2)
                        #Show Camera
                    else:
                        pass
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        self.current_image = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=self.current_image)
        self.cameraPanel.imgtk = imgtk
        self.cameraPanel.config(image=imgtk)
            # show the image
        self.root.update()
        self.root.after(50, self.DiemDanhCamera)
    #TAB1_Function
    def DetectClick(self,MSSV,HoTen,Lop,GioiTinh):             
        self.NhanDien(MSSV,HoTen,Lop,GioiTinh)
    def checkGT(self,GTclick,GTkoclick,GioiTinh):
        if (GTclick.get() == True and GTkoclick.get()== True):
            GTkoclick.set(False)
    def showcamera(self):
        if (self.camera_1 == False):
            imgtk = ImageTk.PhotoImage(Image.open("Appdata/webcam.png"))  # convert image for tkinter
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=imgtk)
            #self.root.update
            return
        ok, frame = self.vs.read()
        if ok:
            self.log.config(state='normal')
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            self.current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=imgtk)
            # show the image
        self.root.after(50, self.showcamera)  # call the same function after 30 milliseconds
    def NhanDien(self,MSSV,HoTen,Lop,GioiTinh):
        global stt
        global count
        #isZe = False
        try:
            os.mkdir(source + "/"+ str(Lop.get()))
        except:
            pass
        if (self.camera_1 == True):
            self.camera_1 = False
            self.showcamera()  
        if (self.camera1 == False):        
            #imgtk = ImageTk.PhotoImage(Image.open("webcam.png"))  # convert image for tkinter
            #self.showcamera()
            self.log.insert("1.0","Đã quét và lưu vào CSDL xong\n")
            self.log.config(state='disabled')
            messagebox.showinfo("Hoàn Thành","Đã Lưu Thông Tin Học Viên Xong")
            Classlist = next(os.walk('ClassList/'))[1]
            self.chooseLop.configure(values =Classlist)
            self.camera_1 = False
            self.ShowHideCamera()            
            Classlist = next(os.walk('ClassList/'))[1]
            return        
        ok, frame = self.vs.read()
        if ok:
            cv2.putText(frame, "XOAY XUNG QUANH", (220,40), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 3)
            cv2.putText(frame, str(stt+1)+"/40", (70,40), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 3)
            self.log.config(state='normal')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            dochinhxac = 6 - int(self.MatDo.get())
            faces = self.detector.detectMultiScale(gray, 1.3, dochinhxac)
            for rect in faces:
                (x, y, w, h) = rect
                framegray = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                count = count + 1
                if count % 2 == 0:
                    stt = stt + 1
                    path = source + "/"+str(Lop.get())+"/" + str(MSSV.get()) + '_' + str(Lop.get()) + '_' + str(stt) + ".jpg"
                    logpath = path[10:]
                    if stt !=40:
                        status = "    Còn "+ str(40-stt)+"\n"
                    else:
                        status = "    Đã xong"+"\n"
                    self.log.insert("1.0","Đã lưu "+logpath +status)
                    cv2.putText(framegray, "Captured", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,0), 2)
                    cv2.imwrite(path, gray[y:y + h, x:x + w])
                if stt == 40:
                    break
            #cv2.imshow("KhungHinh", frame)
            self.current_image = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)
            if stt == 40:
                self.camera1 = False #Gioi han 40 data khuon mat
                self.QuetBtn.configure(text="QUÉT DỮ LIỆU")
                count = 0
                stt = 0

        self.root.after(50, lambda arg1 = MSSV,arg2 = HoTen,arg3 = Lop,arg4 = GioiTinh :self.NhanDien(arg1,arg2,arg3,arg4))
        
        #cv2.destroyAllWindows()
    def Confirm(self,MSSV,HoTen,Lop,Nam,Nu):
        confirmWD = tk.Tk()
        confirmWD.title("Xác Nhận")
        confirmFrame = tk.Frame(confirmWD,width = 400,height = 300)
        dataFrame = tk.Frame(confirmWD, relief="groove", borderwidth=2)
        GioiTinh = ""
        if (Nam.get() == True):
            GioiTinh = "Nam"
        else:
            GioiTinh = "Nữ"
        self.HinhThuc = "Thêm Mới"
        if (CSDL.checkExist(str(MSSV.get()))==True):
            self.HinhThuc = "Cập Nhật"
        tk.Label(confirmWD, text='Xác Nhận Thông Tin',font=('Consolas',18,'bold')).place(x = 100, y = 15,anchor="w")
        tk.Label(dataFrame, text="Hình thức : " +self.HinhThuc,font=('Consolas',14),width=30,anchor='w').grid(row = 0,padx = 15,sticky='w')
        tk.Label(dataFrame, text="MSSV      : "+MSSV.get(),font=('Consolas',14),width=30,anchor='w').grid(row = 1,padx = 15)
        tk.Label(dataFrame, text="Họ Tên    : "+HoTen.get(),font=('Consolas',14),width=30,anchor='w').grid(row = 2,padx = 15)
        tk.Label(dataFrame, text="Lớp       : "+Lop.get(),font=('Consolas',14),width=30,anchor='w').grid(row = 3,padx = 15)
        tk.Label(dataFrame, text="Giới Tính : "+GioiTinh,font=('Consolas',14),width=30,anchor='w').grid(row = 4,padx = 15)
        dataFrame.place(x = 30, y = 50)
        confirmFrame.pack()
        #Button
        cfmBtn = tk.Button(confirmWD,text="Xác Nhận",font =(15),command = lambda arg1 = MSSV,arg2 = HoTen,arg3 = Lop,arg4 = GioiTinh ,arg5= confirmWD:self.ConfirmOK(arg1,arg2,arg3,arg4,arg5)).place(x=220,y=200)
        cancelCfm = tk.Button(confirmWD,text="Hủy Bỏ",font =(15),command = lambda arg1=confirmWD:self.CancelConfirm(arg1)).place(x=70,y=200)
        confirmWD.mainloop()
    def CancelConfirm(self,frame):

        frame.destroy()
    def ConfirmOK(self,MSSV,HoTen,Lop,GioiTinh,frame):
        if self.camera1 == False:
            self.camera1 = True
            self.QuetBtn.configure(text="NGỪNG QUÉT")  
        else:
            self.camera1 = False 
            self.QuetBtn.configure(text="QUÉT DỮ LIỆU") 
        frame.destroy()
        CSDL.Insert_UpdateStudent(str(MSSV.get()),str(HoTen.get()),str(Lop.get()),GioiTinh)
        self.DetectClick(MSSV,HoTen,Lop,GioiTinh)
    def ShowHideCamera(self):   #Còn bug bất đồng bộ
        if self.camera_1 == False:
            self.camera_1 = True
            self.NgungQuetbtn.configure(text="ẨN CAMERA")
            self.log.insert("1.0","Hiện camera\n")              
        else:
            self.camera_1 = False 
            self.NgungQuetbtn.configure(text="HIỆN CAMERA")
            self.log.insert("1.0","Ẩn camera\n")
        self.showcamera()
    #TAB2_Function
    def ClassChoose(self,event,Class,TAB2,temp):
        soLuong = CSDL.soLuongHV(Class)
        siSo = tk.Label(TAB2,text = "Sỉ Số : "+str(soLuong) +"   ",font=(14))
        siSo.place(x=750+temp,y = 30)
    def MaHoaHocVien(self,event,TAB2):
        Class = str(self.chooseLop.get())
        if Class == "Trống":
            messagebox.showinfo("Lỗi","Không có lớp này")
            return
        self.ClassChoose(event,Class,TAB2,0)
        Header1 = tk.Label(TAB2,text = "ĐANG MÃ HÓA THÔNG TIN CÁC HỌC VIÊN",font=("Helvetica",16,'italic'),anchor='center')
        Lop = tk.Label(TAB2,text = "LỚP : "+str(Class)+"   ",font=("Helvetica",16,'bold'),anchor='center')
        Lop.place(x=600,y=110)
        Header1.place(x=460,y=80)
        ListFace, ListID= self.FaceShow(Class)
        try:
            os.mkdir(saveDir)
        except:
            pass
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(ListFace,np.array(ListID))
        recognizer.save(saveDir+"/"+Class+".yml")
        Classlist = next(os.walk('ClassList/'))[1]
        self.chonLop.configure(values =Classlist)
        messagebox.showinfo("Hoàn Thành","Đã lưu thông tin mã hóa")
    def FaceShow(self,Class):
        ListFace = []
        ListID = []
        path = source +"/"+ Class
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        progress = ttk.Progressbar(self.tthv, orient = 'horizontal',length = 460, mode = 'determinate') 
        progress.place(x=105,y=304)
        size = len(imagePaths)
        lv = 100/size
        encrease = lv
        for imagePath in imagePaths:
            MS = imagePath.split("_")[0].split("\\")[1]
            maHoaAnh = Image.open(imagePath).convert('L')            
            chuanHoaAnh  = np.array(maHoaAnh,'uint8')
            ListFace.append(chuanHoaAnh)
            mssv,ten,lop,gt,ID = CSDL.ThongTinHV(MS)
            ListID.append(ID)
            #Show thông đa
            dataBox = tk.Frame(self.tthv,bd = 5,height = 265, width = 285,relief= 'groove')
            dataBox.place(x = 10, y = 25)            
            header1 = tk.Label(dataBox,text="THÔNG TIN HỌC VIÊN",anchor = 'center',font=('Helvetica',15,'bold'))
            header1.place(x = 25,y = 8)
            tk.Label(dataBox,text="MSSV : "+str(mssv),font = (14)).place(x = 5,y = 50)
            tk.Label(dataBox,text="TÊN  : "+str(ten),font = (14)).place(x = 5,y = 90)
            tk.Label(dataBox,text="LỚP  : "+str(lop),font = (14)).place(x = 5,y = 130)
            tk.Label(dataBox,text="GIỚI : "+str(gt),font = (14)).place(x = 5,y = 170)
            tk.Label(dataBox,text="STT  : "+str(ID),font = (14)).place(x = 5,y = 210)
            #Show hình ảnh
            frameImagePanel = tk.Label(self.tthv, bd = 5,height = 255, width = 255,  relief= 'sunken')
            frameImagePanel.place(x = 300, y = 25)
            pil_image = Image.open(imagePath)
            image255x255 = pil_image.resize((255, 255), Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image255x255)
            frameImagePanel.config(image=imgtk)
            tk.Label(self.tthv,text =" "+str(encrease)+"%",font =('Consolas','18','bold'),width = 7,anchor = 'center').place(x=0,y=298)
            progress['value'] = encrease         
            encrease = encrease + lv
            self.root.update()
        return ListFace,ListID
        #cv2.destroyAllWindows()
if __name__ == '__main__':
    root = Tk()
    root.geometry('1000x550')
    FaceMachine(root)
    root.mainloop()
