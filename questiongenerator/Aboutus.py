from tkinter import*
from PIL import Image,ImageTk

class AboutusClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Question Paper Generator")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#87CEEB")

        title=Label(self.root,text="                        Question Paper Generator                         ",font=("comic sens ms",40),bg="#033054",fg="white")
        title.place(x=0,y=0,relwidth=1,height=70)
        title.pack()

        self.img2=Image.open("aboutus.png")
        self.abt=ImageTk.PhotoImage(self.img2)

        self.abt_label=Label(self.root,image=self.abt,bg="#033054")
        self.abt_label.place(x=0,y=70,width=1370,height=200)

        txt_frame=Frame(self.root,bg="#87CEEb")
        txt_frame.place(x=0,y=350,width=1300,height=200)

        text_label=Label(txt_frame,text="Hey Folks! Welcome to “Question Paper Generator” , We are here to Provide You best and efficient services.\n We are hereby hoping that “Question Paper Generator” will less your stress and burden of making question paper. \n   Our main aim is to reduce time of creating IDLE question paper based on covering important topics ,whole syllabus and \noverall difficulty as per your desire .We Genuinely think that this project will help you a lot.\nWe also hope You enjoyed this project as much as we enjoy to offering you!\nIf u have any query , without any hesitation contact us...….",bg="#87CEEB",font=("times new roman",20,),fg="#033054")
        text_label.place(x=0,y=1200,width=900,height=800)
        text_label.pack()








if  __name__=="__main__":
    root=Tk()
    obj=AboutusClass(root)
    root.mainloop()
