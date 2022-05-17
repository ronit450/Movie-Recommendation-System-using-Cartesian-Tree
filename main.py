# Libraries used
from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.ttk import Combobox
# from tkSliderWidget import Slider
from RangeSlider.RangeSlider import RangeSliderH

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
        self.parameter = "Name"
        self.main_image = ImageTk.PhotoImage (Image.open (
            self.AbsolutePath('pictures_used/finalhomepage.png')))
        temp_label = Label (self.homepage,
                            image=self.main_image)
        temp_label.place (x=0,y=0, relwidth=1,relheight=1)
        self.asking_parameter()
        self.select_order_of_data()
        self.selct_range_of_data()
        self.proceed_button()
        proceed_button = Button (self.homepage,
                                 text="Proceed",
                                 fg='black',
                                 height=2,
                                 width=35,
                                 command=lambda: self.proceed_button(),
                                 bg='light green')
        proceed_button.place(x = 400, y = 600)


    def proceed_button(self):
        max_or_min = self.max
        top_range = self.top
        print(top_range)
        print(max_or_min)
        print(self.parameter)



    def AbsolutePath (self,dir):
            AbsoluteDirectory = os.path.dirname (os.path.abspath (__file__))
            returnDir = os.path.join (AbsoluteDirectory,dir)
            return returnDir

    def asking_parameter (self):
        value = self.genre_selctor ()
        # self.imdb_slider ()

    def genre_selctor (self):
        combostyle = ttk.Style ()
        combostyle.theme_create ('combostyle',parent='alt',settings={'TCombobox':{'configure':{'fieldbackground': '#292B37',}}})

        combostyle.theme_use ('combostyle')
        self.current_table = tk.StringVar ()
        self.myframe1 = Frame (self.homepage, padx= 40, pady = 10,bg='#151718', borderwidth=0)
        self.myframe1.place (x=40,y=200)
        menue_items = [('Name'),('Genre'), ('IMDB Rating'), ('Year'), ('Duration')]
        self.lbl = Label (self.myframe1,
                          text="Select the Range of Data",
                          fg='Black',
                          font=("Helvetica", 14))
        self.lbl.grid(padx = 10, pady = 10)
        self.var = StringVar ()
        self.var.set ("All")
        self.cb = Combobox (self.myframe1,values=menue_items)
        self.cb.bind ("<<ComboboxSelected>>",self.parameter_combo)
        self.cb.grid()

        btn = Button(self.myframe1,
                          text="Get the Parameters")
        btn.grid(padx = 50, pady = 10)

        choice = self.current_table.get()
    def parameter_combo(self,x):
        self.parameter = self.cb.get()


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


main_root = Tk()
main_root.title ('HU Movie Akinator')
main_root.geometry ("1366x720")
main_root.config (bg='White')
obj1 = Login(main_root)
main_root.mainloop()
