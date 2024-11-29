import os
import tempfile
from tkinter import *
from tkinter import ttk, messagebox
import Home
from Qpaper import newClass
import sqlite3
import random


class questionClass:

    def __init__(self, root):
        self.root = root
        self.root.title("Question Paper Generator")
        self.root.geometry("1370x900+0+0")
        self.root.config(bg="#87CEEb")
        self.root.focus_force()

        self.var_type = StringVar()
        self.var_name = StringVar()
        self.var_branch = StringVar()
        self.var_sem = StringVar()
        self.var_mark = StringVar()
        self.var_time=StringVar()
        self.var_total = StringVar()
        self.int_given = IntVar()
        self.var_sub = StringVar()
        self.sub_list = []
        self.fetch_sub()

        self.var_desc=StringVar()

        title = Label(self.root, text="                Question Paper Generator               ", font=("comic sens ms", 20), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=30)
        lbl = Label(self.root, text="                  Set Question Paper                   ",font=("times new roman", 20), bg="black", fg="white")
        lbl.place(x=0, y=30, relwidth=1, height=30)

        frame1 = Frame(self.root, bd=5, relief=RIDGE)
        frame1.place(x=10, y=120, width=520, height=420)

        lbl1=Label(frame1,text="Subject",font=("times new roman",20))
        lbl1.place(x=30,y=70)
        cmb_sub = ttk.Combobox(frame1, textvariable=self.var_sub, values=self.sub_list, state="readonly",
                               justify=CENTER, font=("times new roman", 18))
        cmb_sub.place(x=220, y=70, width=250, height=30)
        cmb_sub.current(0)

        lbl2=Label(frame1,text="Marks",font=("times new roman",20))
        lbl2.place(x=30,y=120)
        cmb_mark = ttk.Combobox(frame1,textvariable=self.var_mark,values=("Select", "two", "five", "ten"),
                                state="readonly", justify=CENTER, font=("times new roman", 18))
        cmb_mark.place(x=220, y=125, width=220, height=30)
        cmb_mark.current(0)


        lbl3 = Label(frame1, text="Total Question", font=("times new roman", 20))
        lbl3.place(x=30, y=170)
        self.lbl_given = Label(frame1,text="", font=("times new roman", 15), bg="lightgrey")
        self.lbl_given.place(x=220, y=170, width=220, height=30)
        lbl4= Label(frame1, text="Given Question", font=("times new roman",20))
        lbl4.place(x=30, y=220)
        txt_mark2 = Entry(frame1,textvariable=self.int_given ,font=("times new roman", 15),bg="lightgrey")
        txt_mark2.place(x=220, y=220, width=220, height=30)

        frame2 = LabelFrame(self.root, bd=5, relief=RIDGE)
        frame2.place(x=550, y=120, width=800, height=530)

        scrolly = Scrollbar(frame2, orient=VERTICAL)
        scrollx = Scrollbar(frame2, orient=HORIZONTAL)
        self.Paper = Text(frame2, yscrollcommand=scrolly.set, xscrollcommand=scrollx.set ,font=("times new roman", 15))
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Paper.yview)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.Paper.xview)
        self.Paper.pack(fill=BOTH, expand=1)

        btn_submit=Button(self.root,text="Print",command=self.save ,bd=5,relief=RIDGE,font=("times new roman", 15), bg="red")
        btn_submit.place(x=10,y=600,width=150,height=60)
        btn_clear = Button(self.root, text="Exit",command=self.add_Home, bd=5, relief=RIDGE, font=("times new roman", 15), bg="grey")
        btn_clear.place(x=170, y=600, width=150, height=60)

        btn_add = Button(frame1, text="Add",command=self.add_subject, bd=5, relief=RIDGE, font=("times new roman", 15), bg="red")
        btn_add.place(x=10, y=300, width=150, height=60)
        btn_clear = Button(frame1,command=self.clear, text="Clear", bd=5, relief=RIDGE, font=("times new roman", 15), bg="grey")
        btn_clear.place(x=180, y=300, width=150, height=60)
        btn_ok = Button(frame1, text="Ok",command=self.view, bd=5, relief=RIDGE, font=("times new roman", 10), bg="grey")
        btn_ok.place(x=450, y=170, width=60, height=30)

        self.Title()

        #======================Question paper=====

    def fetch_sub(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("Select name from Shruti")
            sub = cur.fetchall()
            self.sub_list.append("Empty")
            if len(sub) > 0:
                del self.sub_list[:]
                self.sub_list.append("Select")
            for i in sub:
                self.sub_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def view(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sub.get() =="Select" or self.var_mark.get() =="Select":
                messagebox.showinfo("info", "All fields are required")
            else:
                cur.execute("select Count(*) from bharati where sub=? AND mark=?",(self.var_sub.get(), self.var_mark.get()), )
                rows = cur.fetchall()
                length = rows [0] [0]
                if length != 0:
                    self.lbl_given.config(text=f"{str(int(length))}")
                else:
                    messagebox.showerror("error", "NO records found")
        except Exception as ex:
            messagebox.showerror("Error", f"Error dur to{str(ex)}", parent=self.root)

    def add_subject(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sub.get() == "Select" or self.var_mark.get() == "Select":
                messagebox.showinfo("info", "All fields are required")

            else:
                cur.execute(f"SELECT name FROM bharati WHERE sub=? AND mark=?  ORDER By random() LIMIT {self.int_given.get()}",
                        (self.var_sub.get(), self.var_mark.get()), )
                no = cur.fetchall()
                no = [('\n\n' + n[0]) for n in no]
                t = no
                no = list()
                for x in t:
                    no.extend(x)
                no="".join(no)
                self.Paper.insert(END, no)
        except Exception as ex:
            messagebox.showerror("Error", f"Error dur to{str(ex)}", parent=self.root)

    def clear(self):
        self.var_sub.set("Select")
        self.var_mark.set("Select")
        self.var_total.set("")
        self.int_given.set(0)
        self.show()

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from bharati")
            rows = cur.fetchall()
        except Exception as ex:
            messagebox.showerror("Error", f"error due to:{str(ex)}", parent=self.root)







    def save(self):
        opt=messagebox.askyesno("Question Paper","Do you want to save?")
        if opt==TRUE:
            q = self.Paper.get(1.0, 'end-1c')
            filename = tempfile.mktemp('.txt')
            open(filename, 'w').write(q)
            os.startfile(filename, "print")








    def Title(self):
        self.Paper.insert(END,f"\n")
        self.Paper.insert(END,f"\n Branch\t\t\t\t\tSemester")
        self.Paper.insert(END,f"\n Subject\t\t\tTotal Mark\t\t\tTotal Time")
        self.Paper.insert(END,f"\n____________________________________________________________________________")









        # =========================================================================================================



        # =======================================================================================================








    def add_Home(self):
        self.root.destroy()
        self.new_win2 = Tk()
        self.new_obj2 = Home.HomeClass(self.new_win2)



if __name__ == "__main__":
    root = Tk()
    obj = questionClass(root)
    root.mainloop()