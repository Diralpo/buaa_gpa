#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/9/5 13:30
# @Author  : Diralpo (diralpo@163.com)
# @Link    : https://github.com/Diralpo/
# @Desc    :


import tkinter as tk

from cookie import *

from src import signin
from src import kbcx
from src import savefile
from src import gpa


class App:
    def __init__(self, root):
        # 初始化值
        self.username = tk.StringVar()  # 储存用户名
        self.pwd = tk.StringVar()  # 储存密码
        self.initVal()
        # 初始化GUI
        self.root = root
        # root.iconbitmap("test1.ico")
        root.title("查询GPA及课表")
        root.geometry("380x280")
        root.resizable(width=False, height=False)
        self.initGui()

    def initVal(self):
        self.username.set('')
        self.pwd.set('')
        self.loadDefault()

    def logIn(self):
        user_data = [self.username.get(), self.pwd.get()]
        try:
            if not signin.sign_in(user_data):
                self.username.set('error')
                self.pwd.set('error')
            else:
                # 成功登陆
                self.initCxGui()
        except BaseException:
            self.username.set('error')
            self.pwd.set('error')

    def logOut(self):
        signin.logout()
        self.logInFrame.destroy()
        # sys.exit(0)
        self.initVal()
        self.initGui()

    def cxgpa(self):
        user_data = [self.username.get(), self.pwd.get()]
        gpa.gpa(user_data)

    def cxkb(self):
        user_data = [self.username.get(), self.pwd.get()]
        kbcx.kbcx(user_data)

    def saveUser(self):
        user_data = [self.username.get(), self.pwd.get()]
        savefile.save_user(user_data,
                           path="save/user/{}.p".format(self.username.get()))

    def loadUser(self):
        the_path = "save/user/{}.p".format(self.username.get())
        if os.path.exists(the_path):
            user_data = savefile.load_user(path=the_path)
            # print(user_data)
            self.username.set(user_data[0])
            self.pwd.set(user_data[1])
        else:
            pass
            # print(the_path, " not found")

    def loadDefault(self):
        the_path = "save/user/user.p"
        if os.path.exists(the_path):
            user_data = savefile.load_user(path=the_path)
            self.username.set(user_data[0])
            self.pwd.set(user_data[1])

    def setAsDefault(self):
        user_data = [self.username.get(), self.pwd.get()]
        savefile.save_user(user_data, path="save/user/user.p")

    def initLogInGui(self):
        self.logInFrame = tk.Frame(self.root)
        self.logInFrame.grid(row=0, column=0, sticky=tk.N)

        self.logInFrame1 = tk.Frame(self.logInFrame)
        self.logInFrame1.grid(row=0, column=0, sticky=tk.N)

        self.logInFrame2 = tk.Frame(self.logInFrame)
        self.logInFrame2.grid(row=1, column=0, sticky=tk.N)

        tk.Label(
            self.logInFrame1,
            text='用户名',
            width=6).grid(
            row=0,
            column=0,
            sticky=tk.N)
        tk.Label(
            self.logInFrame1,
            text='密码',
            width=6).grid(
            row=1,
            column=0,
            sticky=tk.N)
        tk.Entry(
            self.logInFrame1,
            width=40,
            textvariable=self.username).grid(
            row=0,
            column=1,
            sticky=tk.N)
        tk.Entry(
            self.logInFrame1,
            width=40,
            textvariable=self.pwd, show="*").grid(
            row=1,
            column=1,
            sticky=tk.N)

        tk.Button(
            self.logInFrame2,
            text='保存用户',
            width=8,
            fg="blue",
            command=self.saveUser).grid(
            row=2,
            column=0,
            sticky=tk.N)
        tk.Button(
            self.logInFrame2,
            text='设为默认',
            width=8,
            fg="blue",
            command=self.setAsDefault).grid(
            row=2,
            column=1,
            sticky=tk.N)
        tk.Button(
            self.logInFrame2,
            text='登录',
            width=8,
            fg="blue",
            command=self.logIn).grid(
            row=2,
            column=2,
            sticky=tk.N)
        tk.Button(
            self.logInFrame2,
            text='加载用户',
            width=8,
            fg="blue",
            command=self.loadUser).grid(
            row=2,
            column=3,
            sticky=tk.N)

    def initCxGui(self):
        self.logInFrame.destroy()
        self.logInFrame = tk.Frame(self.root)
        self.logInFrame.place(x=70, y=80, anchor='nw')

        tk.Button(
            self.logInFrame,
            text='GPA',
            width=8,
            fg="blue",
            command=self.cxgpa).grid(
            row=3,
            column=0,
            sticky=tk.N)
        tk.Button(
            self.logInFrame,
            text='logout&quit',
            width=14,
            fg="blue",
            command=self.logOut).grid(
            row=3,
            column=1,
            sticky=tk.N)
        tk.Button(
            self.logInFrame,
            text='schedule',
            width=8,
            fg="blue",
            command=self.cxkb).grid(
            row=3,
            column=2,
            sticky=tk.N)

    def initGui(self):
        self.initLogInGui()


if __name__ == "__main__":
    main()
