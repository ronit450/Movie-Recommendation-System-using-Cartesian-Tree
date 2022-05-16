from tkinter import *
import time
# Create a tkinter window
root = Tk()
root.title("Label Slider")
root.geometry("500x200")
char_index = 0
text = " "
slide_text = "www.codershubb.com"
# function to display text characters with
# a particular time interval
def slide():
    global char_index , text, slide_text
    if char_index >= len(slide_text):
        char_index = 0
        text = " "
        slider.config(text = text)
    else:
        text = text + slide_text[char_index]
        slider.configure(text = text)
        char_index = char_index + 1
    slider.after(500, slide)
# place label on a window
slider = Label(root, text = text, font=("Arial", 25, "bold"), width=20)
slider.place(x = 30 , y = 60)
# call the function
slide()
root.mainloop()