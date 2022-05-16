# Libraries used
from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk
# from tkSliderWidget import Slider
from RangeSlider.RangeSlider import RangeSliderH

class frontend():
    def  __init__(self, main_root):
        self.main_root = main_root

        self.main_image = ImageTk.PhotoImage (Image.open (
            self.AbsolutePath('pictures_used/background1.png')))
        temp_label = Label (main_root,
                            image=self.main_image)
        temp_label.place (x=0,y=0, relwidth=1,relheight=1)
        self.asking_parameter()

    def slider_of_text(self):
        pass

    def asking_parameter(self):


        self.genre_selctor()
        self.imdb_slider()
    def genre_selctor(self):
        combostyle = ttk.Style ()

        combostyle.theme_create ('combostyle',
                                 parent='alt',
                                 settings={'TCombobox':
                                               {'configure':
                                                    {
                                                     'fieldbackground': '#292B37',

                                                     }}}
                                 )
        # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
        combostyle.theme_use ('combostyle')

        myframe1 = Frame(self.main_root)
        myframe1.grid(padx = 146, pady = 440)
        menue_items = [ ('Comedy'), ('Action'), ('Love'), ('Thriller')]
        mycombo = ttk.Combobox(myframe1, value= menue_items, state = 'readonly', font="Verdana 18",  height=60,
                               width=30,)
        mycombo.current(0)

        mycombo.pack()

    def imdb_slider(self):
        myslider2 = Scale (self.main_root,
                           from_=0,
                           to=100,
                           orient=HORIZONTAL,
                           width= '40')
        # myslider2.set(34)
        myslider2.grid ()




    def AbsolutePath (self, dir):
        AbsoluteDirectory = os.path.dirname (os.path.abspath (__file__))
        returnDir = os.path.join (AbsoluteDirectory,dir)
        return returnDir


main_root = Tk()
main_root.title ('HU Movie Akinator')
main_root.geometry ("1366x720")
main_root.config (bg='White')
obj1 = frontend(main_root)
main_root.mainloop()
