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

        # frame = Frame(self.main_root)
        # frame.pack()

        self.main_image = ImageTk.PhotoImage (Image.open (
            self.AbsolutePath('pictures_used/loginpg_1366x720.png')))
        temp_label = Label (main_root,
                            image=self.main_image)
        temp_label.place (x=0,y=0, relwidth=1,relheight=1)

        text_for_name = Text(self.main_root, bg = "#292B37", width = 30, font="Verdana 18",  height = 2)
        # text_for_name.grid (padx=830,pady=310)
        text_for_password = Text(self.main_root, bg = "#292B37", width = 31, font="Verdana 18",  height = 2)
        # text_for_password.grid(padx = 40, pady = 430)

        Button (main_root,
                text = "Login",
                height=2,
                width = 35,
                bg='#1C1C1C',
                command = lambda: self.homepage(),
                borderwidth=2).grid (padx = 870, pady = 550)

    def homepage(self):
        homepage = Toplevel ()
        homepage.title ('HU Movie Akinator')
        homepage.geometry ("1366x720")
        homepage.config (bg='White')
        homepage_obj = Homepage(homepage)
        homepage.mainloop ()




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
            self.AbsolutePath('pictures_used/finalhomepage.png')))
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
                                 fg='black',
                                 height=2,
                                 width=35,
                                 command= self.shifting_to_movie_data,
                                 bg='light green')
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
        self.parameter = "Duratiom"
    def Genre(self):
        self.parameter = "Genre"

    def genre_selctor (self):
        self.myframe1 = Frame (self.homepage, padx= 40, pady = 10,bg='#151718', borderwidth=0)
        self.myframe1.place (x=40,y=200)
        menue_items = [('Name'),('Genre'), ('IMDB Rating'), ('Year'), ('Duration')]
        self.lbl = Label (self.myframe1,text="Select the Category",fg='Black',font=("Helvetica", 14))
        self.lbl.grid(padx = 10, pady = 10)
        self.v0 = IntVar ()
        self.v0.set (1)
        self.r1 = Radiobutton (self.myframe1,
                               text="Name",
                               variable=self.v0,
                               value=1,
                               command=self.name)
        self.r2 = Radiobutton (self.myframe1,
                               text="Genre",
                               variable=self.v0,
                               value=2,
                               command=self.Genre)
        self.r3 = Radiobutton (self.myframe1,
                               text="ImDB Rating",
                               variable=self.v0,
                               value=3,
                               command=self.imdb)
        self.r4 = Radiobutton (self.myframe1,
                               text="Year",
                               variable=self.v0,
                               value=4,
                               command=self.year)
        self.r5 = Radiobutton (self.myframe1,
                               text="Duration",
                               variable=self.v0,
                               value=5,
                               command=self.Duration)
        self.r1.grid()
        self.r2.grid()
        self.r3.grid()
        self.r4.grid()
        self.r5.grid()





    def maxtomin(self):
        self.max = True

    def mintomax(self):
        self.max = False

    def select_order_of_data(self):
        self.frame_for_order_of_data = Frame(self.homepage, padx= 40, pady = 20,bg='#151718', borderwidth=0)
        self.frame_for_order_of_data.place (x=40,y=420)
        self.lbl = Label (self.frame_for_order_of_data,
                          text="Select the Order of Data",
                          fg='Black',
                          font=("Helvetica", 14))
        self.lbl.grid(padx = 10, pady = 2)
        self.v = IntVar ()
        self.v.set (1)
        self.r1 = Radiobutton (self.frame_for_order_of_data,text="Max to Min",variable=self.v,value=1,command=self.maxtomin)
        self.r2 = Radiobutton (self.frame_for_order_of_data,text="Min to Max",variable=self.v,value=2,command=self.mintomax)
        self.r1.grid()
        self.r2.grid()

    def combobox(self, x):
        self.top = self.cb.get()
        self.top = self.top[4:]
        self.top = int(self.top)

    def selct_range_of_data(self):
        self.range_data_frame = Frame(self.homepage,  padx= 40, pady = 20,bg='#151718', borderwidth=0)
        self.range_data_frame.place (x=350,y=420)
        self.lbl = Label (self.range_data_frame,
                          text="Select the Range of Data",
                          fg='Black',
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
        application_obj = Application(parameter, max_or_min, top_range)
        self.movie_lst = application_obj.data_processing()
        self.displaying_movie_data()
    def displaying_movie_data(self):
        table = PrettyTable ()
        movie_data_frame = Frame (self.third_window,
                                    bg='#1C1C1C')
        movie_data_frame.grid ()
        label = Text (movie_data_frame,
                      bg='#1C1C1C',
                      fg='white',
                      height=50,
                      width=100,
                      borderwidth=0)
        label.config (font=("Courier", 15))
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
