from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cx_Oracle as con


connString = 'FRAS/FRAS@localhost:1521/xe'
class ReportBut:
    def __init__(self,root):
        self.root=root
        self.root.geometry('600x600+0+0')
        self.root.title("Face Recoganization System")


        img3=Image.open(r"IMG\img18.JFIF")
        img3=img3.resize((1500,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1500,height=790)

        title_lb=Label(bg_img,text="Reports",font=("times new roman",20,"bold"),bg="white",fg="black")
        title_lb.place(x=0,y=0,width=600,height=60)

        # report table frame
        R_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Report Details",font=("times new roman",10,"bold"))
        R_frame.place(x=5,y=45,width=590,height=550)

        search_label=Label(R_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=40,pady=40,sticky=W)

        

        search_btn=Button(R_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="pink",fg="black")
        search_btn.grid(row=0,column=17,padx=10)

        graph_btn=Button(R_frame,text="Graph",width=12,font=("times new roman",12,"bold"),bg="pink",fg="black")
        graph_btn.grid(row=0,column=18,padx=5)

        ex_btn=Button(R_frame,text="Export",width=12,font=("times new roman",12,"bold"),bg="pink",fg="black")
        ex_btn.grid(row=0,column=19,padx=5)

        



if __name__ == "__main__":
    root=Tk()
    obj=ReportBut(root)
    root.mainloop()

