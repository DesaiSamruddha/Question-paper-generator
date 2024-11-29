from tkinter import*
from unit import unitClass
from quepaper import QuepaperClass
from que import questionClass
from exit import exitClass
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class HomeClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Question Paper Generator")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#87CEEB")

        title=Label(self.root,text="                               Question Paper Generator                              ",font=("comic sens ms",40),bg="#033054",fg="white")
        title.place(x=0,y=0,relwidth=1,height=70)
        title.pack()

        frame1=LabelFrame(self.root,text="Home",font=("times new roman",15),bg="white")
        frame1.place(x=0,y=70,width=1370,height=100)

        btn_unit=Button(frame1,text="Subject",font=("times new roman",15),bg="#0b3357",fg="white",cursor="hand2",command=self.add_unit)
        btn_unit.place(x=30,y=10,width=200,height=50)
        btn_gene=Button(frame1,text="Add Questions",font=("times new roman",15),bg="#0b3357",fg="white",cursor="hand2",command=self.add_quepaper)
        btn_gene.place(x=290,y=10,width=270,height=50)
        btn_pre=Button(frame1,text="Set Question Paper",font=("times new roman",15),bg="#0b3357",fg="white",cursor="hand2",command=self.add_que)
        btn_pre.place(x=620,y=10,width=250,height=50)
        btn_back=Button(frame1,text="Exit",font=("times new roman",15),bg="#0b3357",fg="white",cursor="hand2",command=self.add_exit)
        btn_back.place(x=930,y=10,width=170,height=50)

        self.img1=Image.open("download.png")
        resized=self.img1.resize((1300,500))
        self.bg=ImageTk.PhotoImage(resized)

        self.bg_label1=Label(self.root,image=self.bg)
        self.bg_label1.place(x=10,y=220,width=800,height=400)

        self.lbl_sub=Label(self.root,text="Total Subjects\n[0]",bd=10,relief=RIDGE,font=("times new roman",20),bg="yellow",fg="black")
        self.lbl_sub.place(x=960,y=250,width=200,height=100)

        self.lbl_que=Label(self.root,text="Total Questions\n[0]",bd=10,relief=RIDGE,font=("Times new roman",20),bg="yellow",fg="black")
        self.lbl_que.place(x=950,y=370,width=220,height=100)

        self.update_content()


    def add_unit(self):
        self.new_win6=Toplevel(self.root)
        self.new_obj6=unitClass(self.new_win6)

    def add_quepaper(self):
        self.new_win7=Toplevel(self.root)
        self.new_obj7=QuepaperClass(self.new_win7)

    def add_que(self):
        self.new_win8=Toplevel(self.root)
        self.new_obj8=questionClass(self.new_win8)

    def add_exit(self):
        self.new_win9=Toplevel(self.root)
        self.new_win9=exitClass(self.new_win9)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from Title")
            Title=cur.fetchall()
            self.lbl_sub.config(text=f"Total Subjects\n[{str(len(Title))}]")

            cur.execute("select * from bharati")
            bharati = cur.fetchall()
            self.lbl_que.config(text=f"Total Questions\n[{str(len(bharati))}]")

        except Exception as ex:
            messagebox.showerror("Error", f"error due to:{str(ex)}", parent=self.root)




if  __name__=="__main__":
    root=Tk()
    obj=HomeClass(root)
    root.mainloop()