# Libraries used
from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.ttk import Combobox
from application import Application
from prettytable import PrettyTable

class Login():
    def  __init__(self, main_root):
        self.main_root = main_root
        self.username = "m"

        self.main_image = ImageTk.PhotoImage (Image.open (
            self.AbsolutePath('pictures_used/loginpg_1366x720.png')))
        temp_label = Label (self.main_root,
                            image=self.main_image)
        temp_label.place (x=0,y=0, relwidth=1,relheight=1)
        self.login_username()
        self.login_password()



        Button (self.main_root,
                text = "Login",
                height=2,
                width = 25,
                font=("Helvetica", 14),
                bg='#B52840',
                fg = 'white',
                command =  self.homepage,
                borderwidth=2).grid (padx = 850, pady = 550)
    def homepage(self):
        print(self.username)
        homepage = Toplevel ()
        homepage.title ('HU Movie Akinator')
        homepage.geometry ("1366x720")
        homepage.config (bg='White')
        homepage_obj = Homepage(homepage)
        homepage.mainloop ()

    def login_username (self):
        self.login_frame = Frame(self.main_root,padx=0, pady = 0,bg='#B52840', borderwidth=0 )
        self.login_frame.place(x = 820, y = 290)
        text_for_name = Entry(self.login_frame, bg = "#B52840", width = 20, fg='white', font="Verdana 18")
        text_for_name.grid (padx=0,pady=0)




    def login_password(self):
        self.password_frame = Frame(self.main_root,padx=0 , pady = 0,bg='#B52840', borderwidth=0 )
        self.password_frame.place(x = 820, y = 440)
        text_for_password = Entry(self.password_frame,show = '*', fg='white', bg = "#B52840", width = 20,
                                font="Verdana 18",)
        text_for_password.grid(padx=0,pady=0)

    def AbsolutePath (self, dir):
        AbsoluteDirectory = os.path.dirname (os.path.abspath (__file__))
        returnDir = os.path.join (AbsoluteDirectory,dir)
        return returnDir





class Homepage():
    def __init__(self, homepage):
        self.homepage = homepage
        self.max = True
        self.top = 45
        self.parameter = "Film Name"
        self.main_image = ImageTk.PhotoImage (Image.open (
            self.AbsolutePath('pictures_used/final-changes_1366x720.png')))
        temp_label = Label (self.homepage,
                            image=self.main_image)
        temp_label.place (x=0,y=0, relwidth=1,relheight=1)
        self.asking_parameter()
        self.select_order_of_data()
        self.selct_range_of_data()
        self.proceed_button()



    def proceed_button(self):
        proceed_button = Button (self.homepage,
                                 text="Proceed",
                                 fg='white',
                                 bg = "#B52840",
                                 height=2,
                                 width=20,
                                 font=("Helvetica", 14),
                                 command= self.shifting_to_movie_data,
                                 )
        proceed_button.place(x = 400, y = 600)
        max_or_min = self.max
        top_range = self.top
        parameter = self.parameter
        print(parameter, max_or_min, top_range)
        # self.shifting_to_movie_data()


    def shifting_to_movie_data(self):
        results = Toplevel ()
        results.title ('HU Movie Akinator')
        results.geometry ("1366x720")
        results.config (bg='#1C1C1C')
        movie_obj = Movie_Data (results,
                                self.parameter,
                                self.top,
                                self.max)
        results.mainloop ()




    def AbsolutePath (self,dir):
            AbsoluteDirectory = os.path.dirname (os.path.abspath (__file__))
            returnDir = os.path.join (AbsoluteDirectory,dir)
            return returnDir

    def asking_parameter (self):
        value = self.genre_selctor ()
        # self.imdb_slider ()
    def name(self):
        self.parameter = "Film Name"
    def imdb(self):
        self.parameter = "Rating"
    def year(self):
        self.parameter = "Year"
    def Duration(self):
        self.parameter = "Duration"
    def Genre(self):
        self.parameter = "Genre"

    def genre_selctor (self):
        self.myframe1 = Frame (self.homepage, padx= 40, pady = 10,bg='#151718', borderwidth=0)
        self.myframe1.place (x=40,y=250)
        menue_items = [('Name'),('Genre'), ('IMDB Rating'), ('Year'), ('Duration')]
        self.lbl = Label (self.myframe1,text="Select the Category", fg='white',
                          bg = '#151718',font=("Helvetica", 14))
        self.lbl.grid(padx = 10, pady = 13)
        self.v0 = IntVar ()
        self.v0.set (1)
        self.r1 = Radiobutton (self.myframe1,
                               text="Name",
                               variable=self.v0,
                               value=1,
                               bg = "#151718",
                               fg = 'white',
                               height = 1,
                               width = 10,
                               selectcolor = 'red',
                               font=("Helvetica", 14),
                               command=self.name)
        self.r2 = Radiobutton (self.myframe1,
                               text="Genre",
                               variable=self.v0,
                               value=2,
                               selectcolor='red',
                               bg="#151718",
                               fg='white',
                               height=1,
                               width=10,

                               font=("Helvetica", 14),
                               command=self.Genre)
        self.r3 = Radiobutton (self.myframe1,
                               text="ImDB Rating",
                               variable=self.v0,
                               value=3,
                               bg="#151718",
                               fg='white',
                               selectcolor='red',
                               height=1,
                               width=10,
                               font=("Helvetica", 14),
                               command=self.imdb)
        self.r4 = Radiobutton (self.myframe1,
                               text="Year",
                               variable=self.v0,
                               value=4,
                               selectcolor='red',
                               bg="#151718",
                               fg='white',
                               height=1,
                               width=10,
                               font=("Helvetica", 14),
                               command=self.year)
        self.r5 = Radiobutton (self.myframe1,
                               text="Duration",
                               variable=self.v0,
                               value=5,
                               selectcolor='red',
                               height=1,
                               bg="#151718",
                               fg='white',
                               width=10,
                               font=("Helvetica", 14),
                               command=self.Duration)
        self.r1.grid(row = 1, column = 0)
        self.r2.grid(row = 1, column = 1)
        self.r3.grid(row = 2,column = 0)
        self.r4.grid(row = 2, column = 1)
        # self.r5.grid(row = 3, column = 1)





    def maxtomin(self):
        self.max = True

    def mintomax(self):
        self.max = False

    def select_order_of_data(self):
        self.frame_for_order_of_data = Frame(self.homepage, padx= 40, pady = 20,bg='#151718', borderwidth=0)
        self.frame_for_order_of_data.place (x=40,y=430)
        self.lbl = Label (self.frame_for_order_of_data,
                          text="Select the Order of Data",
                          fg='white',
                          bg = '#151718',

                          font=("Helvetica", 14))
        self.lbl.grid(padx = 10, pady = 2)
        self.v = IntVar ()
        self.v.set (1)
        self.r1 = Radiobutton (self.frame_for_order_of_data,text="Max to Min",selectcolor='red',
                               bg="#151718",
                               fg='white', variable=self.v,value=1,command=self.maxtomin)
        self.r2 = Radiobutton (self.frame_for_order_of_data,text="Min to Max",selectcolor='red',
                               bg="#151718",
                               fg='white', variable=self.v,value=2,command=self.mintomax)
        self.r1.grid()
        self.r2.grid()

    def combobox(self, x):
        self.top = self.cb.get()
        self.top = self.top[4:]
        self.top = int(self.top)

    def selct_range_of_data(self):
        self.range_data_frame = Frame(self.homepage,  padx= 40, pady = 20,bg='#151718', borderwidth=0)
        self.range_data_frame.place (x=350,y=430)
        self.lbl = Label (self.range_data_frame,
                          text="Select the Range of Data",
                          fg='white',
                          bg='#151718',
                          font=("Helvetica", 14))
        self.lbl.grid(padx = 10, pady = 10)
        self.var = StringVar ()
        self.var.set ("All")
        self.data = ("top 5", "top 15", "top 30")
        self.cb = Combobox (self.range_data_frame,values=self.data)
        self.cb.bind ("<<ComboboxSelected>>",self.combobox)
        self.cb.grid()

    def imdb_slider (self):
        myslider2 = Scale (self.homepage,
                           from_=0,
                           to=100,
                           orient=HORIZONTAL,
                           width='40')
        # myslider2.set(34)
        myslider2.grid ()

class Movie_Data():
    def __init__(self, third_window, parameter, top_range, max_or_min):
        self.third_window = third_window
        self.main_image = ImageTk.PhotoImage (Image.open (
            self.AbsolutePath('pictures_used/resultss_1366x720.png')))
        temp_label = Label (self.third_window,
                            image=self.main_image)
        temp_label.place (x=0,y=0, relwidth=1,relheight=1)
        application_obj = Application(parameter, max_or_min, top_range)
        self.movie_lst = application_obj.data_processing()
        self.displaying_movie_data()

    def AbsolutePath (self,dir):
            AbsoluteDirectory = os.path.dirname (os.path.abspath (__file__))
            returnDir = os.path.join (AbsoluteDirectory,dir)
            return returnDir
    def displaying_movie_data(self):
        table = PrettyTable ()
        movie_data_frame = Frame (self.third_window,
                                    bg='#1C1C1C')
        movie_data_frame.place(x = 0, y = 70)
        label = Text (movie_data_frame,
                      bg='#1C1C1C',
                      fg='white',
                      height=50,
                      width=100,
                      borderwidth=0)
        label.config (font=("Courier", 12))
        table.field_names = ["Name", "Year", "Duration", "Genre", "Rating"]
        for i in range (len (self.movie_lst)):
            table.add_rows ([self.movie_lst[i]], )
        label.insert (INSERT,
                      table)
        label.config (state=DISABLED)
        label.grid (padx=200,
                    pady=10,
                    sticky=E + W)


main_root = Tk()
main_root.title ('HU Movie Akinator')
main_root.geometry ("1366x720")
main_root.config (bg='White')
obj1 = Login(main_root)
main_root.mainloop()
