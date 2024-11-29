from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class QuepaperClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Question Paper Generator")
        self.root.geometry("1200x550+100+100")
        self.root.config(bg="#87CEEb")
        self.root.focus_force()

        self.var_Qid = StringVar()
        self.var_sub = StringVar()
        self.var_mark = StringVar()
        self.var_name = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.sub_list = []
        self.fetch_sub()

        title = Label(self.root, text="                  Question Paper Generator                     ",font=("comic sens ms", 20), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=40)

        label = Label(self.root, text="                    ADD Question                   ", font=("comic sens ms", 20),bg="black", fg="white")
        label.place(x=0, y=40, relwidth=1, height=40)

        frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        frame1.place(x=20, y=100, width=570, height=410)

        lbl = Label(frame1, text="Add Question Here", font=("times new roman", 15), bg="#0f4d7d", fg="white")
        lbl.pack(side=TOP, fill=X)

        lbl_sub = Label(frame1, text="Question Id", font=("times new roman", 18), bg="white")
        lbl_sub.place(x=20, y=50)
        lbl_type = Label(frame1, text="Subject", font=("times new roman", 18), bg="white")
        lbl_type.place(x=20, y=100)
        lbl_diff = Label(frame1, text="Marks", font=("times new roman", 18), bg="white")
        lbl_diff.place(x=20, y=200)
        lbl_add = Label(frame1, text="Enter Question Here", font=("times new roman", 18), bg="white")
        lbl_add.place(x=20, y=250)


        txt_id = Entry(frame1, textvariable=self.var_Qid, font=("times new roman", 12), bg="lightgrey")
        txt_id.place(x=270, y=50, width=250, height=30)

        txt_add = Entry(frame1, textvariable=self.var_name,font=("times new roman", 18), bg="lightgrey")
        txt_add.place(x=20, y=290, width=500, height=80)

        cmb_sub = ttk.Combobox(frame1, textvariable=self.var_sub, values=self.sub_list, state="readonly",justify=CENTER, font=("times new roman", 18))
        cmb_sub.place(x=270, y=90, width=250, height=30)
        cmb_sub.current(0)

        cmb_mark = ttk.Combobox(frame1, textvariable=self.var_mark, values=("Select", "two", "five", "ten"),state="readonly", justify=CENTER, font=("times new roman", 18))
        cmb_mark.place(x=270, y=200, width=250, height=30)
        cmb_mark.current(0)

        btn_add = Button(self.root, text="Save", command=self.add, font=("times new roman", 15), bg="blue")
        btn_add.place(x=40, y=490, width=120, height=40)
        btn_update = Button(self.root, text="Update", command=self.update,font=("times new roman", 15), bg="green")
        btn_update.place(x=170, y=490, width=120, height=40)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("times new roman", 15), bg="Red")
        btn_delete.place(x=300, y=490, width=120, height=40)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("times new roman", 15), bg="grey")
        btn_clear.place(x=430, y=490, width=120, height=40)

        searchframe = LabelFrame(self.root, text="Search Question", font=("times new roman", 15))
        searchframe.place(x=630, y=100, width=560, height=80)

        cmb_search = ttk.Combobox(searchframe, textvariable=self.var_searchby, values=("select", "Sub", "Mark"),state="readonly", justify=CENTER, font=("times new roman", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(searchframe, textvariable=self.var_searchtxt, font=("times new roman", 12))
        txt_search.place(x=200, y=10, width=250, height=25)
        btn_search = Button(searchframe, text="Search", command=self.search, font=("times new roman", 12), bg="green")
        btn_search.place(x=460, y=10, width=90, height=25)

        frame2 = Frame(self.root, bd=3, relief=RIDGE)
        frame2.place(x=630, y=180, width=560, height=350)

        scrolly = Scrollbar(frame2, orient=VERTICAL)
        scrollx = Scrollbar(frame2, orient=HORIZONTAL)

        self.table = ttk.Treeview(frame2, columns=("qid", "name", "Sub", "marks"), yscrollcommand=scrolly.set,
                                  xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)
        self.table.heading("qid", text="Que id")
        self.table.heading("name", text="Question")
        self.table.heading("Sub", text="Subject")
        self.table.heading("marks", text="Marks")
        self.table["show"] = "headings"

        self.table.column("qid", width=50)
        self.table.column("name", width=400)
        self.table.column("Sub", width=150)
        self.table.column("marks", width=70)
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("ButtonRelease-1>", self.get_data)
        self.show()

        # ======================================================================================

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

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sub.get() == "Select" or self.var_mark.get() == "Select" or self.var_name.get()=="Empty":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select * from bharati where name=? ", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Question Already exists,try different", parent=self.root)
                else:
                    #print(self.var_name.get(), self.var_sub.get(), self.var_mark.get(),)
                    cur.execute("Insert into bharati(name,sub,mark) Values(?,?,?)",(self.var_name.get(), self.var_sub.get(),  self.var_mark.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Question added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dur to{str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from bharati")
            rows = cur.fetchall()
            self.table.delete(*self.table.get_children(),)
            for row in rows:
                self.table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        print(self.var_name.get(), self.var_Qid.get())
        try:
            if self.var_Qid.get()=="" :
                messagebox.showerror("Error", "Please enter question", parent=self.root)
            else:
                cur.execute("Select * from bharati where qid=?", (self.var_Qid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Pleas try again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        print("yes")
                        cur.execute("delete from bharati where qid=?", (self.var_Qid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Subject Deleted successfully", parent=self.root)
                        self.show()
                        self.var_Qid.set("")
                        self.var_name.set("")
                        self.var_sub.set("")
                        self.var_mark.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}", parent=self.root)



    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sub.get() == "Select" or self.var_mark.get() == "Select" or self.var_name.get()=="Empty":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select * from bharati where name=? ", (self.var_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Question ID", parent=self.root)
                else:
                    #print(self.var_name.get(), self.var_sub.get(), self.var_mark.get(),)
                    cur.execute("Update bharati set name=?,sub=?,mark=? where qid=?",(self.var_name.get(), self.var_sub.get(),  self.var_mark.get(),self.var_Qid.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Question updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dur to{str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Searchby option",parent=self.root)
            elif self.var_searchtxt.get()=="Select":
                messagebox.showerror("Error","Search input must required",parent=self.root)
            else:
                cur.execute("select * from bharati where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%' ")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.table.delete(*self.table.get_children(), )
                    for row in rows:
                        self.table.insert('', END, values=row)
                else:
                    messagebox.showerror("Erroe","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to:{str(ex)}", parent=self.root)


    def clear(self):
        self.var_Qid.set("")
        self.var_name.set("")
        self.var_sub.set("Select")
        self.var_mark.set("Select")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()

    def get_data(self, ev):
        f = self.table.focus()
        content = (self.table.item(f))
        row = content['values']
        self.var_Qid.set(row[0])
        self.var_name.set(row[1])
        self.var_sub.set(row[2])
        self.var_mark.set(row[3])


if __name__ == "__main__":
    root = Tk()
    obj = QuepaperClass(root)
    root.mainloop()