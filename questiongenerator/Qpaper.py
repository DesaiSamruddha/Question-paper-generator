from tkinter import *
from tkinter import ttk,messagebox

class newClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Question Paper Generator")
        self.root.geometry("1000x750+200+0")
        self.root.config(bg="#0b5377")

        self.var_type = StringVar()
        self.var_name = StringVar()
        self.var_branch = StringVar()
        self.var_sem = StringVar()
        self.var_sub = StringVar()
        self.sub_list = []
        self.fetch_sub()
        self.var_total = StringVar()
        self.var_given = StringVar()
        self.var_desc = StringVar()

    def generate(self):
        if self.var_name.get()=="" or  self.var_branch.get()=="":
            messagebox.showerror("Error",f"Question paper details are required",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=newClass(root)
    root.mainloop()