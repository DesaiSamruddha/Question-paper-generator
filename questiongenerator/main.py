from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

import Home
from signup import SignUpClass
from Aboutus import AboutusClass
from Home import HomeClass
import sqlite3
import os



class QPG:
    def __init__(self,root):
        self.root=root
        self.root.title("Question Paper Generator")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#0b5377")
                

        self.username=StringVar()
        self.password=StringVar()

        title=Label(self.root,text="                          Question Paper Generator                           ",font=("comic sens ms",40),bg="#033054",fg="white")
        title.place(x=0,y=0,relwidth=1,height=70)
        title.pack()

        M_Frame=LabelFrame(self.root,text="",font=("times new roman",15),bg="white")
        M_Frame.place(x=0,y=70,width=1370,height=60)

        btn_aboutus=Button(M_Frame,text="AboutUs",font=("times new roman",15),bg="#0b5377",fg="white",cursor="hand2",command=self.add_Aboutus)
        btn_aboutus.place(x=880,y=5,width=200,height=40)
        btn_sign=Button(M_Frame,text="SignUp",font=("times new roman",15),bg="#0b5377",fg="white",cursor="hand2",command=self.add_signup)
        btn_sign.place(x=1100,y=5,width=200,height=40)

        self.img=Image.open("download1.png")
        resized=self.img.resize((1300,500))
        self.bg=ImageTk.PhotoImage(resized)

        self.bg_label=Label(self.root,image=self.bg)
        self.bg_label.place(x=0,y=130,width=700,height=700)

        frame_login=Frame(self.root,bg="white")
        frame_login.place(x=790,y=220,width=500,height=420)

        name=Label(frame_login,text="Login Here",font=("comic sens ms",35,"bold"),bg="#d77337",fg="white")
        name.place(x=130)
        user_label=Label(frame_login,text="Username",font=("times new roman",30),fg="grey",bg="white")
        user_label.place(x=0,y=110)
        txt_user=Entry(frame_login,font=("times new roman",15),textvariable=self.username,bg="lightgrey")
        txt_user.place(x=10,y=160,width=450,height=40)
        warn_label=Label(frame_login,text="(Username must be email)",font=("times new roman",12),fg="#d77337",bd=0)
        warn_label.place(x=170,y=130)
        pass_label=Label(frame_login,text="Password",font=("times new roman",30),fg="grey",bg="white")
        pass_label.place(x=0,y=220)
        txt_pass=Entry(frame_login,font=("times new roman",15),textvariable=self.password,show="*",bg="lightgrey")
        txt_pass.place(x=10,y=270,width=450,height=40)


        login_btn=Button(self.root,text="Login",bg="#d77337",fg="white",font=("Times new roman",30),command=self.login)
        login_btn.place(x=970,y=610,width=150,height=60)

    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from Login2 where eid=? AND pass=?",(self.username.get(),self.password.get(),))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("error","Invalid Username/Password",parent=self.root)
                else:
                    messagebox.showinfo('info',"Login successful")
                    self.root.destroy()
                    root1=Tk()
                    obj=Home.HomeClass(root1)

                    # self.new_win2 = Toplevel(self.root)
                    # self.new_obj2 = HomeClass(self.new_win)

        except Exception as ex:
           messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)


    def add_signup(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SignUpClass(self.new_win)




    def add_Aboutus(self):
        self.new_win1=Toplevel(self.root)
        self.new_obj1=AboutusClass(self.new_win1)




if  __name__=="__main__":
    root=Tk()
    obj=QPG(root)
    root.mainloop()
