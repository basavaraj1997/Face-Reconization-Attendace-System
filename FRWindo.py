# face recoganization
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from FRStud import Student
from FRFaculty import Faculty
from FRDepart import Depart
from TrainData import TrainData
from FaceReconisation import faceReco
from FRProfile import Profile
from CourseWiseAttendace import CourseWiseAttendace
from FRReport_ClassWise import FRReport_ClassWise
import DAL
#reports ...

from FRReport_StudWise import FRReport_StudWise
from FRReport_Course import FRReport_Course
from FRReport_Per import FRReport_Per


connString = 'FRAS/FRAS@localhost:1521/xe'
connString = DAL.getDbConn()

class face_recoganization:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        TittleStr=str(DAL.GetToDayDate()) #+"  "+str(DAL.GetCollgeNameText)
        print(str(DAL.GetCollgeNameText))
        self.root.title("Face Recoganization System  "+str(TittleStr))

        #back img3
        img3=Image.open(r"IMG\Grey.jpg")  
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=20,width=1530,height=710)

        title_lb=Label(bg_img,text="Face Recoganization Attendance System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb.place(x=0,y=0,width=1530,height=60)

        #Student button img4
        img4=Image.open(r"IMG\img12.PNG")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.stud_details,cursor="hand2")
        b1.place(x=200,y=120,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.stud_details,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_1.place(x=200,y=299,width=220,height=40)


        #Reports face button img5 --  
        img5=Image.open(r"IMG\imgR.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b3=Button(bg_img,image=self.photoimg5,command=self.FR_RprClsWise, cursor="hand2")
        b3.place(x=500,y=120,width=220,height=220)

        b1_2=Button(bg_img,text="Class Report",command=self.FR_RprClsWise, cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_2.place(x=500,y=130, width=220,height=40)
        
        b1_Coursewise=Button(bg_img,text="Course Wise",command=self.FR_RprCourseWse, cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_Coursewise.place(x=500,y=175,width=220,height=40)

        b1_Stud=Button(bg_img,text="Student Wise",command=self.FR_RptStudWise,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_Stud.place(x=500,y=220,width=220,height=40)
        
        b1_Per=Button(bg_img,text="Percentage",command=self.FR_RptStudPer,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_Per.place(x=500,y=265,width=220,height=40)


        # Attendace button img6
        img6=Image.open(r"IMG\img9.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.FR_details)
        b6.place(x=800,y=120,width=220,height=220)

        b1_12=Button(bg_img,text="Attendace",command=self.FR_details,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_12.place(x=800,y=300,width=220,height=40)


        # Help button img7
        img7=Image.open(r"IMG\img15.PNG")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b8=Button(bg_img,image=self.photoimg7,command=self.faculty_details,cursor="hand2")
        b8.place(x=1100,y=120,width=220,height=220)

        b1_14=Button(bg_img,text="Faculty",command=self.faculty_details,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_14.place(x=1100,y=300,width=220,height=40)


        # Train button img8
        img8=Image.open(r"IMG\img16.JFIF")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b9=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.TD_details)
        b9.place(x=200,y=400,width=220,height=220)

        b1_16=Button(bg_img,text="Train Data",command=self.TD_details,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_16.place(x=200,y=600,width=220,height=40)


        # photoes button img9
        img9=Image.open(r"IMG\img7.JFIF")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        #COURSE WISE ATTENCE
        b10=Button(bg_img,image=self.photoimg9,command=self.FR_CourseWiseAttendace,cursor="hand2")
        b10.place(x=500,y=400,width=220,height=220)

        b1_18=Button(bg_img,text="Course Wise Attendace",command=self.FR_CourseWiseAttendace,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_18.place(x=500,y=600,width=220,height=40)

    
        # Course and Departments
        img10=Image.open(r"IMG\imgC8.JFIF")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b122=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.DC_details)
        b122.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Depart/Course",command=self.DC_details,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        b1_1.place(x=800,y=600,width=220,height=40)

        # Exit button img11
        img11=Image.open(r"IMG\img17.PNG")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b121=Button(bg_img,image=self.photoimg11,command=self.FR_Profile,cursor="hand2")
        b121.place(x=1100,y=400,width=220,height=220)

        b1_120=Button(bg_img,text="Profile",cursor="hand2",command=self.FR_Profile, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_120.place(x=1100,y=600,width=220,height=40)

        #============function=========================

    def stud_details(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=Student(self.new_window)
    def faculty_details(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=Faculty(self.new_window)
    def DC_details(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=Depart(self.new_window)
    def TD_details(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=TrainData(self.new_window)
    def FR_details(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=faceReco(self.new_window)
    def FR_Profile(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=Profile(self.new_window)
    def FR_CourseWiseAttendace(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=CourseWiseAttendace(self.new_window)
        #rpt.... , 
    def FR_RprClsWise(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=FRReport_ClassWise(self.new_window)

    def FR_RptStudWise(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=RptStudWise(self.new_window)

    def FR_RprCourseWse(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=FRReport_Course(self.new_window)

    def FR_RptStudPer(self): #this function called in studentDetails button
        self.new_window=Toplevel(self.root)
        self.SD=FRReport_Per(self.new_window)
    

if __name__ == "__main__":
    root=Tk()
    obj=face_recoganization(root)
    root.mainloop()
    
