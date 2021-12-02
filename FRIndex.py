from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from FRWindo import face_recoganization
from FRLogin import Login_page
from FaceReconisation import faceReco
from CourseWiseAttendace import CourseWiseAttendace
import DAL

class Main_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        TittleStr=str(DAL.GetToDayDate())#+"  "+str(DAL.GetCollgeNameText)
        print(str(DAL.GetCollgeNameText))

        self.root.title("Face Recoganization System " +TittleStr)

        img3=Image.open(r"IMG\img2.jpg")  
        img3=img3.resize((1530,775),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=775)

        title_lb=Label(bg_img,text="Zeal Institute of Management",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb.place(x=0,y=0,width=1530,height=60)

        b1_1=Button(bg_img,text="Syatem Login",command=self.Login,cursor="hand2",font=("times new roman",18,"bold"),bg="#ffb3fe",fg="black")
        b1_1.place(x=1200,y=120,width=230,height=50)

        b2_1=Button(bg_img,text="Student Attendance",command=self.FR_details,cursor="hand2",font=("times new roman",18,"bold"),bg="#ffb3fe",fg="black")
        b2_1.place(x=1200,y=200,width=230,height=50)
        
        b2_1=Button(bg_img,text="Course Wise",command=self.CourseWiseAtendace,cursor="hand2",font=("times new roman",18,"bold"),bg="#ffb3fe",fg="black")
        b2_1.place(x=1200,y=280,width=230,height=50)

    def F_R(self): #this function called in sysytem login button
        self.new_window=Toplevel(self.root)
        self.SD=face_recoganization(self.new_window)

    def Login(self): #this function called in sysytem login button
        self.new_window=Toplevel(self.root)
        self.SD=Login_page(self.new_window)

    def FR_details(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=faceReco(self.new_window)

    def CourseWiseAtendace(self): #this function called in CourseWiseAttendace button
        self.new_window=Toplevel(self.root)
        self.SD=CourseWiseAttendace(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Main_page(root)
    root.mainloop()
