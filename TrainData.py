from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import numpy as np
import os
import DAL

connString = 'FRAS/FRAS@localhost:1521/xe'
connString = DAL.getDbConn()


class TrainData:
    def __init__(self,root):
        self.root=root
        width= self.root.winfo_screenwidth() 
        height= self.root.winfo_screenheight()
        
        self.root.geometry("%dx%d" % (width-1, height-20))
        self.root.title("Attendace System") 
        self.root.configure(bg='#e5ebeb')
        #=================label============================
        heading_lbl=Label(self.root,text="Trainig Images", font=("times new roman",36,"bold"),bg="skyblue",fg="black")
        heading_lbl.place(x=0,y=10,width=(width-2),height=60)        
        img_top=Image.open(r"Img\FaceRecoIcon.ico")
        img_top=img_top.resize((200,150,),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        b1=Button(self.root,image=self.photoimg_top,command=self.traingData_classifier,cursor="hand2")
        b1.place(x=width/2-120,y=170,width=250,height=250)

        lbl_note=Label(self.root,text="---Click Above Image button to Train Image Data---", cursor="hand2")
        lbl_note.place(x=width/2-120,y=450)    
        
    def traingData_classifier(self):
        data_directory=("DataImgs")
        path=[os.path.join(data_directory,file) for file in os.listdir(data_directory)]
        faces=[]
        rollno=[]
        for image in path:
            img=Image.open(image).convert('L') #grey scale image
            imgNP=np.array(img,'uint8')
            id=str(os.path.split(image)[1].split('_')[1]).split('.')[0]
            faces.append(imgNP)
            rollno.append(int(id))
            cv2.imshow("Training",imgNP)
            cv2.waitKey(1)==13
            print(rollno)
        rollno=np.array(rollno)        
        print("Currect...")
        print(rollno)
        #classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,rollno)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result"," ALl Images Data Trainig Completed..")
        root.destroy()
        
if __name__ == "__main__":
    root=Tk()
    obj=TrainData(root)
    root.mainloop()
