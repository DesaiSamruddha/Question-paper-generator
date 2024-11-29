from tkinter import *
from PIL import Image,ImageTk
from Home import HomeClass
from tkinter import ttk,messagebox
import sqlite3

class SignUpClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Question Paper Generator")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#0b5377")

        self.var_Fname = StringVar()
        self.var_Lname = StringVar()
        self.var_ContNo = IntVar()
        self.var_Emailid = StringVar()
        self.var_Password = StringVar()
        self.var_confiPass = StringVar()




        title=Label(self.root,text="                          Question Paper Generator                       ",font=("comic sens ms",40),bg="#033054",fg="white")
        title.place(x=0,y=0,relwidth=1,height=70)
        title.pack()

        self.img1=Image.open("registration.jpeg")
        self.reg=ImageTk.PhotoImage(self.img1)

        self.reg_label=Label(self.root,image=self.reg,bg="#0b5377")
        self.reg_label.place(x=0,y=120,width=638,height=500)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=660,y=120,width=640,height=500)

        f_name=Label(frame1,text="First Name",font=("times new roman",20,"bold"),bg="white",fg="black")
        f_name.place(x=30,y=50,)
        txt_name=Entry(frame1,textvariable=self.var_Fname,font=("times new roman",15),bg="lightgrey")
        txt_name.place(x=30,y=90,width=270,height=35)


        f_name1=Label(frame1,text="Last Name",font=("times new roman",20,"bold"),bg="white")
        f_name1.place(x=340,y=50)
        txt_name1=Entry(frame1,textvariable=self.var_Lname,font=("times new roman",20),bg="lightgrey")
        txt_name1.place(x=340,y=90,width=270,height=35)

        f_contact=Label(frame1,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        f_contact.place(x=30,y=140)
        txt_contact=Entry(frame1,textvariable=self.var_ContNo,font=("times new roman",20),bg="lightgrey")
        txt_contact.place(x=30,y=180,width=270,height=35)

        f_email=Label(frame1,text="Email id",font=("times new roman",20,"bold"),bg="white")
        f_email.place(x=340,y=140)
        txt_email=Entry(frame1,textvariable=self.var_Emailid,font=("times new roman",20),bg="lightgrey")
        txt_email.place(x=340,y=180,width=270,height=35)

        f_pass=Label(frame1,text="Password",font=("times new roman",20,"bold"),bg="white")
        f_pass.place(x=30,y=230)
        txt_pass=Entry(frame1,textvariable=self.var_Password,font=("times new roman",20),bg="lightgrey",show="*")
        txt_pass.place(x=30,y=270,width=270,height=35)

        f_cpass=Label(frame1,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        f_cpass.place(x=340,y=230)
        txt_cpass=Entry(frame1,textvariable=self.var_confiPass,font=("times new roman",20),bg="lightgrey",show="*")
        txt_cpass.place(x=340,y=270,width=270,height=35)

        reg_Button=Button(frame1,text="Register Now",command=self.signup,bg="#0b5377",fg="white",font=("times new roman",30))
        reg_Button.place(x=200,y=370,width=270,height=60)
        sign_Button=Button(frame1,text="Sign In",bg="#0b5367",fg="white",font=("times new roman",30),command=self.add_)
        sign_Button.place(x=230,y=440,width=220,height=50)

    def signup(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_Fname.get() == "" or self.var_Lname.get() =="" or self.var_ContNo.get()=="" or self.var_Emailid.get()=="" or self.var_Password.get()=="" or self.var_confiPass.get()=="":
                messagebox.showerror("Error", "All fields must be required", parent=self.root)
            elif self.var_Password.get()!=self.var_confiPass.get():
                messagebox.showerror("Error","Password and confirm password should be same",parent=self.root)
            else:
                cur.execute("Select * from Login2  where eid=?", (self.var_Emailid.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already present,try different", parent=self.root)
                else:
                    cur.execute("Insert into Login2(fname,lname,contact,eid,pass) Values(?,?,?,?,?)", (self.var_Fname.get(),self.var_Lname.get(),self.var_ContNo.get(),self.var_Emailid.get(),self.var_Password.get(),))
                con.commit()
                messagebox.showinfo("success", "User added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def add_Home(self):
        self.new_win3=Toplevel(self.root)
        self.new_obj3=HomeClass(self.new_win3)

    def add_main(self):
        self.new_win9=Toplevel(self.root)
        self.new_obj9=QPG(self.new_win9)

if  __name__=="__main__":
    root=Tk()
    obj=SignUpClass(root)
    root.mainloop()