from distutils.command import register
from doctest import master
from tkinter import *
from tkinter import messagebox


class User():
    def __init__(self, username, password, hobbies):
        self.username = username
        self.password = password
        self.hobbies = []
        for i in hobbies:
            self.hobbies.append(i)
class Authentication():

    def __init__(self):
        self.list_of_record = dict()

    def click(self, username, password, hobbies):
        user1 = User(username, password, hobbies)
        self.list_of_record[user1.username] = user1

    def check(self, username, password):
        found = self.list_of_record.get(username, False)

        if found:
            # print(found.password)
            if password == found.password:
                return ("Password is correct..... Login Successful", found)
            else:
                return ("Incorrect password", found)

        else:
            return ("No username of this ID was foud", found)


authentication = Authentication()
authentication.click("oqba", "abdul", ["fishing", "farming"])
class loginpage(Frame):  # login page
    def __init__(self, root):
        Frame.__init__(self, root)
        # this will create a window and between this and main loop we have to work for GUI
        self.root = root

        self.authentication = Authentication()
        self.authentication.click("oqba", "abdul", ["fishing", "farming"])
        self.root.title("Login Page")
        self.root.geometry('1280x720')
        self.root.resizable(False, False)
        # register_frame=Frame(self.root, borderwidth=2, relief='sunken', bg="white", bd='10')
        # register_frame.place(x=0, y=0,height = 720, width =1280 )
        # self.b = PhotoImage(file = "login.png")
        # Label(register_frame, image=self.b).place(x=0, y=0, relwidth = 1, relheight = 1)

        def Message(Text):
            messagebox.showinfo("Message", Text)

        # canvas1 = Canvas(self.root, width = 1280, height = 720)
        # self.b = PhotoImage(file = "login.png")
        # canvas1.create_image( 0, 0, image = self.b)
        # Label(self.root, image=self.b, width='2000', height='4000').pack()

        login_frame = Frame(self.root, borderwidth=2,
                            relief='sunken', bg="white", bd='2')
        login_frame.place(x=0, y=0, height=720, width=1280)

        canvas1 = Canvas(login_frame, width=1280, height=720)
        self.b = PhotoImage(file="loginpg_1366x720.png")
        canvas1.create_image(0, 0, image=self.b)
        Label(login_frame, image=self.b, width='1280', height='720').pack()

        # label = Label(login_frame,text="Login Here", font=("Bebas Neue", 35, "bold"), fg='#405898', bg="white").place(x=125, y=0)
        # label1 = Label(login_frame,text="Username", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=120)
        # --> create an Entry for user to write his name
        self.E1 = Entry(login_frame, bd=0, bg="white")
        self.E1.place(x=780, y=280, width=245, height=30)

        # label2 = Label(login_frame,text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=50, y=170)
        # --> create an Entry for user to write his name
        self.E2 = Entry(login_frame, bd=0, bg="white")
        self.E2.place(x=780, y=377, width=245, height=30)

        self.b1 = PhotoImage(file="registershape.png")
        signup_button = Button(login_frame, text='SignUp', command='c', image=self.b1, relief='sunken', padx=5, pady=5,
                               activebackground='white', activeforeground='red', bg='white', fg='black', font=('Bebas Neue', 15), bd=0, height='30', width='120')
        signup_button.place(x=837, y=507)

        def _login():
            user = self.E1.get()
            password = self.E2.get()
            if self.authentication.check(user, password)[0] == "Password is correct..... Login Successful":

                print(self.authentication.check(user, password)[1])
                login_frame.destroy()
                self.post_frame = Frame(
                    self.root, borderwidth=2, relief='sunken', bg="white", bd='10')
                self.post_frame.place(x=0, y=0, height=720, width=1280)
                # back_button=Button(self.post_frame, text='Back',command=goback, padx=5, pady=5,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('Bebas Neue', 15, 'bold'), bd=5)
                # back_button.place(x=170, y=300)

                # currentData = Data()
                BG_GRAY = "#ABB2B9"
                BG_COLOR = "#17202A"
                TEXT_COLOR = "#EAECEE"


                FONT = "Helvetica 14"
                FONT_BOLD = "Helvetica 13 bold"

main_root = Tk()
main_root.title ('HU Movie Akinator')
main_root.geometry ("1366x720")
main_root.config (bg='White')
obj1 = loginpage(main_root)
main_root.mainloop()
