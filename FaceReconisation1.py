from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import numpy as np
import os
from datetime import date
import cx_Oracle as con

connString = 'FRAS/FRAS@localhost:1521/xe'
class faceReco:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600")
        self.root.title("Face Reconization")
        heading_lbl=Label(self.root,text="Attendace", font=("times new roman",36,"bold"),bg="orange",fg="black")
        heading_lbl.place(x=0,y=0,width=1000,height=48)
        img_btn=Button(self.root,text="Attend", cursor="hand2",command=self.Face_recgni, bg="green")
        img_btn.place(x=500,y=450)

    def Face_recgni(self):
        def Draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            cordnt=[]
            lastSrno=""
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)                
                srno_id, predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                try:
                    rollno=""
                    Stud_Name=""
                    if str(lastSrno)!= str(srno_id):
                        query2="select srno, ROLLNO, FULLNAME from student_mst where srno="+str(srno_id)
                        print("*******************")
                        print(query2)
                        db_connection = con.connect(connString)
                        db_cursor = db_connection.cursor()
                        db_cursor.execute(query2)
                        rows=db_cursor.fetchall()
                                               
                        for row in rows:
                            rollno=(row[1])
                            Stud_Name=(row[2])
                    
                    lastSrno=srno_id
                    if confidence>77:
                        cv2.putText(img,f"Roll:"+str(rollno)+"",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:"+str(Stud_Name)+"",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        #Add Attendace to Database....
                        today = date.today()
                        db_connection = con.connect(connString)
                        db_cursor = db_connection.cursor()
                        db_cursor.execute("select srno cnt from attendace where ODT=(select to_char(sysdate,'dd-mon-yyyy')  from dual) and rollno="+str(rollno)+" ")
                        rows=db_cursor.fetchall()
                        if db_cursor.rowcount==0:                                     
                            todayDate=str(today.day)+"-"+str(today.month)+"-"+str(today.year)
                            Query3=" insert into attendace(SRNO,ODT,ROLLNO,SUB_CODE,FACULTY_ID,FRTIME,TOTIME,ISPRESENT) "
                            Query3=Query3+" values((select nvl(max(srno),0)+1 from attendace), (select to_char(sysdate,'dd-mon-yyyy')  from dual) , "
                            Query3=Query3+ str(rollno)+ ", null, null, (select to_char(sysdate,'HH:mi') from dual),null,'Y')"
                            print("==>"+Query3)
                            db_cursor.execute(Query3)
                            db_connection.commit()
                    else:
                        cv2.putText(img,f"Unkonw Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cordnt=[x,y,w,y]
                except con.DatabaseError as e:
                     print(e)
                     db_connection.rollback()
                     messagebox.showinfo('Information', "Attedance Not Submitted!!!")
                finally:
                    db_connection.close()                    
            return cordnt
        def reconise(img,clf,faceCasecade):
            cordnt=Draw_boundray(img,faceCasecade,(1.1),10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cam=cv2.VideoCapture(0)
        while True:
            ret,img=video_cam.read()
            img=reconise(img,clf,faceCascade)
            cv2.imshow("Wel Come Your Attendace Recorded",img)
            if(cv2.waitKey(13)==13):
                break
        video_cam.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    root=Tk()
    obj=faceReco(root)
    root.mainloop()
