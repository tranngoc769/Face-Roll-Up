"""
Code illustration: 1.11
A demonstration of tkinter Variable Class
IntVar, StringVar & BooleanVar

@Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
from tkinter import *
from tkinter import Frame
import sqlite3
root = tk.Tk()
ketNoiSql = sqlite3.connect("Database/Acc.db")
#define variable
class LoginGUI:
    frame = None
    password = tk.StringVar() # defines the widget state as string
    ID = tk.StringVar()
    remember_me = tk.BooleanVar()
    def __init__(self, root):
        self.root = root
        root.option_readfile('Appdata/option')
        root.title("Login to manage")
        self.frame = Frame(self.root,borderwidth=5)
        tk.Label(self.frame, text="    Adminstration:").grid(row=1, column=1)
        tk.Entry(self.frame, width=20, textvariable=self.ID).grid(row=1, column=2, columnspan=2)
        #Password
        tk.Label(self.frame, text="    Password:").grid(row=2, column=1, sticky='w')
        tk.Entry(self.frame, width=20, show="*",  textvariable=self.password).grid(row=2, column=2, columnspan=2)
        #Remember
        tk.Checkbutton(self.frame, text="Remember", variable=self.remember_me).grid(row=3, column=1)        
        self.remember_me.set(False)
        tk.Button(self.frame,text="Login", command=self.Login).grid(row=3, column=3)
        tk.Label(self.frame, text="    ").grid(row=2, column=4)
        tk.Label(self.frame, text="    ").grid(row=1, column=4)
        self.frame.pack()
    def getInfo(self):
        querry = "SELECT * FROM Acc"
        result = ketNoiSql.execute(querry)
        info = None
        for row in result:
            if (str(row[0]) == self.ID.get()):
                info = row
                break
        return info
    def Login(self):
        info = self.getInfo()
        if ((info == None or self.password.get()==None or self.ID.get()==None) or (str(info[0])!=self.ID.get() and str(info[1]) != self.password.get())):
            noti = Label(self.frame, text=" Sai", fg = 'red').grid(row=1, column=4)
            noti = Label(self.frame, text=" Sai", fg = 'red').grid(row=2, column=4)
        else :
            if str(info[0])==self.ID.get() and str(info[1]) != self.password.get():
                noti = Label(self.frame, text=" OK ", fg = 'blue').grid(row=1, column=4)
                noti = Label(self.frame, text=" Sai", fg = 'red').grid(row=2, column=4)
            if str(info[0])==self.ID.get() and str(info[1]) == self.password.get():
                noti = Label(self.frame, text=" OK ", fg = 'blue').grid(row=1, column=4)
                noti = Label(self.frame, text=" OK ", fg = 'blue').grid(row=2, column=4)
                ketNoiSql.close()
                self.frame.quit()
                self.destroy()
    def destroy(self):
        self.root.destroy() # close the current window