from tkinter import*

class exitClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Question Paper Generator")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="#87CEEb")

if __name__=="__main__":
    root=Tk()
    obj=exitClass(root)
    root.mainloop()