from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class unitClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Question Paper Generator")
        self.root.geometry("1200x550+100+100")
        self.root.config(bg="#87CEEb")
        self.root.focus_force()

        self.var_sub_id = StringVar()
        self.var_name = StringVar()

        title = Label(self.root, text="                       Question Paper Generator                     ",
                      font=("comic sens ms", 20), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=40)

        label_sub = Label(self.root, text="                     Subject                    ",
                          font=("times new roman", 20, "bold"), bg="black", fg="white")
        label_sub.place(x=0, y=40, relwidth=1, height=40)

        label_name = Label(self.root, text="Enter Subject Name", font=("goudy old style", 30, "bold"), bg="#87CEEb",
                           fg="black")
        label_name.place(x=70, y=100)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 25), bg="Lightyellow")
        txt_name.place(x=70, y=160, width=350, height=40)

        btn_add = Button(self.root, text="ADD", command=self.add, font=("times new roman", 15), bg="black", fg="white",
                         cursor="hand2")
        btn_add.place(x=430, y=160, width=150, height=40)

        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("times new roman", 15, "bold"),
                            bg="red", fg="black", cursor="hand2")
        btn_delete.place(x=430, y=210, width=150, height=40)

        sub_frame = Frame(self.root, bd=3, relief=RIDGE)
        sub_frame.place(x=600, y=120, width=500, height=350)

        scrolly = Scrollbar(sub_frame, orient=VERTICAL)
        scrollx = Scrollbar(sub_frame, orient=HORIZONTAL)

        self.SubTable = ttk.Treeview(sub_frame, columns=("sid", "name"), yscrollcommand=scrolly.set,
                                     xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SubTable.xview)
        scrolly.config(command=self.SubTable.yview)
        self.SubTable.heading("sid", text="Subject ID")
        self.SubTable.heading("name", text="Subject Name")
        self.SubTable["show"] = "headings"
        self.SubTable.column("sid", width=70)
        self.SubTable.column("name", width=100)
        self.SubTable.pack(fill=BOTH, expand=1)
        self.SubTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        # ==================================================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Subject name must be required", parent=self.root)
            else:
                cur.execute("Select * from Shruti  where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Question already present,try different", parent=self.root)
                else:
                    cur.execute("Insert into Shruti(name) Values(?)", (self.var_name.get(),))
                con.commit()
                messagebox.showinfo("success", "subject added successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from Shruti")
            rows = cur.fetchall()
            self.SubTable.delete(*self.SubTable.get_children())
            for row in rows:
                self.SubTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.SubTable.focus()
        content = (self.SubTable.item(f))
        row = content['values']
        # print(row)
        self.var_sub_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please enter subject name from the list", parent=self.root)
            else:
                cur.execute("Select * from Shruti where sid=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Error, Please try again!!!", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from Shruti where name=?", (self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Subject deleted succesfully", parent=self.root)
                        self.show()
                        self.var_sub_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if  __name__=="__main__":
    root=Tk()
    obj=unitClass(root)
    root.mainloop()