# face recoganization Student Page
from tkinter import*
from tkcalendar import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cx_Oracle as con
from tkcalendar import Calendar, DateEntry
from datetime import date,timedelta
import cv2
import os
import io
import base64
import DAL

connString = 'FRAS/FRAS@localhost:1521/xe'
connString = DAL.getDbConn()

filename="DataImgs/"
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
if not os.path.exists(filename):
    os.makedirs(filename)
imageFullPath=""
connString = 'FRAS/FRAS@localhost:1521/xe'
class Student:
    def __init__(self,root):
        self.root=root
        width= self.root.winfo_screenwidth() 
        height= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height-20))

        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoganization System")
    #=================variables============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_studid=StringVar()
        self.var_studname=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_AdmissionDate=StringVar()         
        self.search_combo=StringVar()
        self.search_entry=StringVar()
       
         #back img3
        img3=Image.open(r"IMG\Grey.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lb=Label(bg_img,text="Student Management",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lb.place(x=0,y=0,width=1530,height=60)

        #main frame for stud details
        main_frame =Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1510,height=670)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        left_frame.place(x=5,y=0,width=730,height=650)

        img_left=Image.open(r"IMG\img14.JFIF")
        img_left=img_left.resize((700,200),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        flb=Label(left_frame,image=self.photoimg_left)
        flb.place(x=5,y=0,width=700,height=200)
        
        

        #current_course
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Info",font=("times new roman",15,"bold"))
        current_frame.place(x=3,y=190,width=700,height=115)
        
        #Department 
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=1,padx=10)

        DCombo_val=self.bindDepart()
        dep_combo=ttk.Combobox(current_frame ,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        #dep_combo["values"]=("-Select Department-","MCA","MBA","Computer","IT","Civil","Mechanical")
        dep_combo["values"]=DCombo_val
        dep_combo.current(0)
        dep_combo.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        #Course     
        

        #Year    
        year_label=Label(current_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)        
        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=20,state="readonly")
        
        
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")   
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester   
        sem_label=Label(current_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")   
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Stud Info
        class_stud_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Stud Info",font=("times new roman",15,"bold"))
        class_stud_frame.place(x=3,y=310,width=700,height=300)

        #StudId
        studId_label=Label(class_stud_frame,text="Student Id:",font=("times new roman",13,"bold"),bg="white")
        studId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studId_entry=ttk.Entry(class_stud_frame,textvariable=self.var_studid,state="readonly",width=20,font=("times new roman",13,"bold"))
        studId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #stud name
        studName_label=Label(class_stud_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studName_entry=ttk.Entry(class_stud_frame,textvariable=self.var_studname,width=20,font=("times new roman",13,"bold"))
        studName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_stud_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(class_stud_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=18,state="readonly")
        class_div_combo["values"]=("select div","A","B","C")   
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no_label=Label(class_stud_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_stud_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_stud_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_stud_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=18,state="readonly")
        gender_combo["values"]=("select gender","Male","Female")   
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_stud_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #dob_entry=ttk.Entry(class_stud_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        #dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        todays_date = date.today()
        # fetching the current year, month and day of today
        curnt_yr=todays_date.year
        cmnth=todays_date.month
        dob_entry = DateEntry(class_stud_frame, width=15,background='darkblue',textvariable=self.var_dob,font=("times new roman",13,"bold"),bg="white", foreground='white', borderwidth=1,month=1, year=int(curnt_yr)-20,locale='en_US', date_pattern='dd-mm-y')
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        

        #Email
        email_label=Label(class_stud_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_stud_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        phone_label=Label(class_stud_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_stud_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_stud_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_stud_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #admission date
        teacher_label=Label(class_stud_frame,text="AdmissionDate:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #teacher_entry=ttk.Entry(class_stud_frame,textvariable=self.var_AdmissionDate,width=20,font=("times new roman",13,"bold"))
        #teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        teacher_entry = DateEntry(class_stud_frame, width=15,background='darkblue',textvariable=self.var_AdmissionDate, font=("times new roman",13,"bold"),bg="white", foreground='white', borderwidth=1,month=1, year=int(curnt_yr),locale='en_US',date_pattern='dd-mm-y')
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

       
        radiobtn2=ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

         #buttons frame
        btn_frame=Frame(class_stud_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=25,y=205,width=645,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="pink",fg="black")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="pink",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="pink",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.Reset_entrybx,width=15,font=("times new roman",13,"bold"),bg="pink",fg="black")
        reset_btn.grid(row=0,column=3)

        #buttons
        btn_frame1=Frame(class_stud_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=25,y=235,width=645,height=35)

        take_photo_btn=Button(btn_frame1,text="Take photo Sample",command=self.Stud_sample,width=31,font=("times new roman",13,"bold"),bg="pink",fg="black")
        take_photo_btn.grid(row=0,column=0)
    
        update_photo_btn=Button(btn_frame1,text="Update photo Sample",width=31,font=("times new roman",13,"bold"),bg="pink",fg="black")
        update_photo_btn.grid(row=0,column=2)
        
         #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"),bg="white")
        right_frame.place(x=720,y=0,width=700,height=700)

        #Studet Img Smpl
        Studt_smpl=Image.open(r"IMG\img12.png")
        Studt_smpl=Studt_smpl.resize((220,220),Image.ANTIALIAS)
        self.Stud_Smplimg=ImageTk.PhotoImage(Studt_smpl)
        std_smpllb=Label(right_frame,image=self.Stud_Smplimg)
        std_smpllb.place(x=235,y=0,width=225,height=225)
        
        #================Search System===============

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        search_frame.place(x=3,y=225,width=615,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=8,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.search_combo,font=("times new roman",13,"bold"),width=10,state="readonly")
        search_combo["values"]=("Roll_No","Phone_No")  
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        search_entry=ttk.Entry(search_frame,width=10,textvariable=self.search_entry, font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,command=self.fetch_dataByRollNoPhon, font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="ShowAll",width=12,command=self.fetch_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #================Table Frame==============

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=300,width=615,height=315)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.stud_table=ttk.Treeview(table_frame,column=("id","roll","name","dep","div","sem","phone","email","year","gender","dob","address","AdmissionDate","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)
        
        self.stud_table.heading("id",text="StudentID")
        self.stud_table.heading("roll",text="RollNo")
        self.stud_table.heading("name",text="Name")
        self.stud_table.heading("dep",text="Department")
        self.stud_table.heading("div",text="Division")
        self.stud_table.heading("sem",text="Semester")
        self.stud_table.heading("phone",text="PhoneNo")
        self.stud_table.heading("email",text="Email")
        self.stud_table.heading("year",text="Year")
        
        self.stud_table.heading("gender",text="Gender")
        self.stud_table.heading("dob",text="DOB")       
        self.stud_table.heading("address",text="Address")
        self.stud_table.heading("AdmissionDate",text="AdmissionDate")
        self.stud_table.heading("photo",text="PhotoStatus")
        self.stud_table["show"]="headings"
        self.stud_table.column("id",width=100)
        self.stud_table.column("roll",width=100)
        self.stud_table.column("name",width=100)
        self.stud_table.column("dep",width=100)    
        self.stud_table.column("div",width=100)
        self.stud_table.column("sem",width=100)   
        
        self.stud_table.column("phone",width=100)
        self.stud_table.column("email",width=100)
        self.stud_table.column("year",width=100)
             
        self.stud_table.column("gender",width=100)
        self.stud_table.column("dob",width=100)
        self.stud_table.column("address",width=100)
        self.stud_table.column("AdmissionDate",width=100)
        self.stud_table.column("photo",width=150)
        
        self.stud_table.pack(fill=BOTH,expand=1)
        self.getmxsrno()
        self.fetch_data()
        
        self.stud_table.bind("<ButtonRelease>",self.get_cursor)
    #======================function declaration====================================


    #=======================Student (Photo) Sample Saving==========================
    def Stud_sample(self):
        
        if self.var_dep.get()=="-Select Department-" or self.var_studname.get()=="" or self.var_studid.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Enter roll no",parent=self.root)
            return
        if self.var_radio1.get()!="Yes":
            messagebox.showerror("Error","Select Take Sample",parent=self.root)
            return  

        if self.var_studid.get()=="":
            messagebox.showerror("Error"," Student Id Not Found ",parent=self.root)
            return
        faceCascde = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        webcam = cv2.VideoCapture(0)
        #webcam.set(3,240) # set Width
        #webcam.set(4,250) # set Height
        Img_ID=0
        Studnt_ID = self.var_studid.get()
        def face_croped(f_img):
            gray = cv2.cvtColor(f_img, cv2.COLOR_BGR2GRAY)
            C_face=faceCascde.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in C_face:
                #cv2.rectangle(my_frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = f_img[y:y+h, x:x+w]
                return roi_gray
        while True:
            try:
                ret,my_frame=webcam.read()
                if (face_croped(my_frame) is not None):
                    print("imgae croping beging")
                    Img_ID+=1
                print(face_croped(my_frame).shape)
                #face=roi_gray
                imageFullPath=str(filename+'img_'+Studnt_ID+'_'+str(Img_ID)+'.jpg')
                #print(face.shape)
                face=cv2.resize(face_croped(my_frame),(400,400))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) #####
                cv2.imwrite(imageFullPath,face)
                #cv2.putText(face,str(Img_ID),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) ######
                cv2.imshow("Image Sample",face)
                print(str(Img_ID))
                if cv2.waitKey(1)==13 or int(Img_ID)==30:
                    break
            except Exception as ex:
                webcam.release()
                print(ex)
                cv2.destroyAllWindows()
                break
            
        webcam.release()
        print('Cam Released...')
        cv2.destroyAllWindows()




        #cv2.imshow("Sample Image",my_frame)
        #==== BIND IMG TO===
        try:
            Studt_smpl=Image.open(r"DataImgs\img_"+str(self.var_studid.get())+"_1.jpg")
            Studt_smpl=Studt_smpl.resize((200,200),Image.ANTIALIAS)
            self.Stud_Smplimg=ImageTk.PhotoImage(Studt_smpl)
            std_smpllb=Label(root,image=self.Stud_Smplimg)
            std_smpllb.place(x=270,y=80,width=200,height=200)
        except Exception as es:
            messagebox.showinfo("Info","Sample Image Not Found",parent=self.root)
        ###==============        
                
        #Database Save And Display on Screen...
        if my_frame is None:
            messagebox.showerror("Error","Sample Not Saved In Database Retake Sample....",parent=self.root)
            return
        #Check Is RollNOExist Or Not On Same Sem?
        #
        
      
        update=1
        try:
             if update>0:
                print("Hello"+str(self.var_studid.get()))
                db_connection = con.connect(connString)
                db_cursor = db_connection.cursor()
                db_cursor.execute("update student_mst set IsPhSmplIsAvail='Y' where srno="+str(self.var_studid.get())+"")
                db_connection.commit()
                messagebox.showinfo("Success","Student Sample Successfully Updated.",parent=self.root)
                self.Reset_entrybx()                 
                db_connection.close()
                self.fetch_data()
        except Exception as es:
            print('errro-----'+str(es))
            #messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
 
    #================= Save =======================
    def add_data(self):
       if self.var_dep.get()=="Select Department" or self.var_studname.get()=="" or self.var_studid.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
       if self.var_roll.get()=="":
            messagebox.showerror("Error","Enter roll no",parent=self.root)
            return         
       else:
           #messagebox.showinfo("success","Welcome To Zeal Institute Of Management,Narhe,Pune")
        gender="M"
        db_connection1 = con.connect(connString)
        db_cursor1 = db_connection1.cursor()
        db_cursor1.execute(" select srno from student_mst where sem='"+self.var_sem.get()+"' and rollno="+self.var_roll.get()+"")
        print(" select srno from student_mst where sem='"+self.var_sem.get()+"' and rollno="+self.var_roll.get()+"")
        rows=db_cursor1.fetchall()
        if(db_cursor1.rowcount>0):
            messagebox.showerror("Error","Roll No Already Regisaterd... !!")
            db_connection1.close()
            return
        db_connection1.close()
       
        try:
            if self.var_gender.get()=="Male":
                gender="M"
            else:
                gender="F"
            query2 = "INSERT INTO student_mst (SRNO,ROLLNO,FULLNAME,MOBILE1,EMAIL,DEPART,SEM,dob,EDUYEAR,REGDATE,ADMISIONDATE,GENDER,address,div)"
            query2 = query2 +" VALUES ((select nvl(max(srno),0)+1 from student_mst),"+self.var_roll.get()+", '"+self.var_studname.get()+"','"+self.var_phone.get()+"' "
            query2=query2+",'"+ self.var_email.get()+"','"+ self.var_dep.get()+"','"+self.var_sem.get()+"',to_char(to_date('"+self.var_dob.get()+"','dd-mm-yyyy'),'dd-MON-yyyy'),"
            query2=query2+"'"+self.var_year.get()+"',(select to_char(sysdate,'dd-mon-yyyy')  from dual),to_char(to_date('"+self.var_AdmissionDate.get()+"','dd-mm-yyyy'),'dd-MON-yyyy'),'"+gender+"','"+self.var_address.get()+"','"+self.var_div.get()+"')"
    # implement query Sentence
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
           
        # Submit to database for execution
            db_connection.commit()
            messagebox.showinfo('Information', "Student Registration Successfully")
            self.fetch_data()
           
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data insertion failed!!!")
        finally:
            db_connection.close()

     #fetching data to table
    def fetch_data(self):
        try:
            self.stud_table.delete(*self.stud_table.get_children())# 
            query2="select SRNO,ROLLNO,FULLNAME,DEPART,div,SEM,MOBILE1,EMAIL,EDUYEAR,(case when GENDER='M' then 'Male' when GENDER='F' then 'Female' else GENDER end) GENDER,to_char(dob,'dd-mm-yyyy') dob,address,to_char(ADMISIONDATE,'dd-mm-yyyy') ADMISIONDATE, (case when IsPhSmplIsAvail='Y' then 'Yes' else 'No' end) IsPhSmplIsAvail from student_mst"
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                 print("**********Got Data Happy Na*********")
                 self.stud_table.insert("",'end',text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2]), str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]),str(row[10]),str(row[11]),str(row[12]),str(row[13])))
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()

    #===============Get Search By Id or Phone================================  ["values"]=("Roll_No","Phone_No")  
    def fetch_dataByRollNoPhon(self):
        try:
            self.stud_table.delete(*self.stud_table.get_children())# 
            query2=" Select SRNO,ROLLNO,FULLNAME,DEPART,div,SEM,MOBILE1,EMAIL,EDUYEAR, "
            query2=query2+" (case when GENDER='M' then 'Male' when GENDER='F' then 'Female' else GENDER end) GENDER,to_char(dob,'dd-mm-yyyy') dob,"
            query2=query2+" address,to_char(ADMISIONDATE,'dd-mm-yyyy') ADMISIONDATE, (case when IsPhSmplIsAvail='Y' then 'Yes' else 'No' end) IsPhSmplIsAvail "
            query2=query2+" from student_mst "
            print("***<--SEARCH-->****")
            print(self.search_combo.get())
            if(self.search_combo.get()=="Roll_No"):
                 query2=query2+" where rollno LIKE '%"+self.search_entry.get()+"%'"
            
            if(self.search_combo.get()=="Phone_No"):
                query2=query2+" where MOBILE1 LIKE '%"+self.search_entry.get()+"%'"
        
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                 print("**********Got Data Happy Na*********")
                 self.stud_table.insert("",'end',text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2]), str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]),str(row[10]),str(row[11]),str(row[12]),str(row[13])))
        except con.DatabaseError as e:
             print(e)
            
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()


            


    #===============max Studetn ID===========================================================
    def getmxsrno(self):
        try:
            self.stud_table.delete(*self.stud_table.get_children()) 
            query2="select (nvl(max(SRNO),0)+1) srno from student_mst"
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                self.var_studid.set(row[0])
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()

    #===Reset===============================================================================

    def Reset_entrybx(self):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]
        self.var_studid.set(""),
        self.var_roll.set(""),
        self.var_studname.set(""),
        self.var_dep.set("-Select Department-"),
        self.var_div.set("-Select division-"),
        self.var_sem.set("-Select Semester-"),
        self.var_course.set("-Select Course-"),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_year.set("-Select Year-"),
        self.var_gender.set("-Select Gender-"),
        self.var_dob.set(""),
        self.var_address.set(""),
        self.var_AdmissionDate.set(""),
        self.var_radio1.set("")
        self.getmxsrno()

    #=============get cursor=========================================================================
        
    def get_cursor(self,event=""):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]
        self.var_studid.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_studname.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_div.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_phone.set(data[6]),
        self.var_email.set(data[7]),
        self.var_year.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_address.set(data[11]),
        self.var_AdmissionDate.set(data[12])
        self.var_radio1.set(data[13])
        
        #==== BIND IMG TO===
        try:
            print("DataImgs\img_"+str(self.var_studid.get())+"_1.jpg")
            Studt_smpl=Image.open(r"DataImgs\img_"+str(self.var_studid.get())+"_1.jpg")
            Studt_smpl=Studt_smpl.resize((200,200),Image.ANTIALIAS)
            self.Stud_Smplimg=ImageTk.PhotoImage(Studt_smpl)
            std_smpllb=Label(self.root,image=self.Stud_Smplimg)
            std_smpllb.place(x=990,y=80,width=200,height=200)
        except Exception as es:
            print(es)
            messagebox.showinfo("success","Sample Image Not Found",parent=self.root)
        ###==============        
         
    
    #=====update_function======================================================================================
    def update_data(self):
        if self.var_dep.get()=="-Select Department-" or self.var_studname.get()=="" or self.var_studid.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return 
        else:
            try:
                gender="M"
                if self.var_gender.get()=="Male":
                    gender="M"
                else:
                    gender="F"
                db_connection1 = con.connect(connString)
                db_cursor1 = db_connection1.cursor()
                db_cursor1.execute(" select srno from student_mst where sem='"+self.var_sem.get()+"' and rollno="+self.var_roll.get()+"")
                print(" select srno from student_mst where sem='"+self.var_sem.get()+"' and rollno="+self.var_roll.get()+"")
                rows=db_cursor1.fetchall()
                if(db_cursor1.rowcount>0):
                    messagebox.showerror("Error","Roll No Already Regisaterd... !!")
                    db_connection1.close()
                    return
                db_connection1.close()
        
                
                update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                if update>0:
                    print("Hello")
                    db_connection = con.connect(connString)
                    db_cursor = db_connection.cursor()
                    QueryString="update student_mst set ROLLNO='"+self.var_roll.get()+"',FULLNAME='"+self.var_studname.get()+"',MOBILE1='"+self.var_phone.get()+"', EMAIL='"+self.var_email.get()+"',DEPART='"+self.var_dep.get()+"',SEM='"+self.var_sem.get()+"',"+ "dob=to_char(to_date('"+self.var_dob.get()+"','dd-mm-yyyy'),'dd-mon-yyyy'), EDUYEAR='"+self.var_year.get()+"',"+"ADMISIONDATE=to_char(to_date('"+self.var_AdmissionDate.get()+"','dd-mm-yyyy'),'dd-mon-yyyy'),"+"GENDER='"+gender+"',address='"+self.var_address.get()+"',div='"+self.var_div.get()+"',co_name='"+self.var_course.get()+"' "+" where srno="+self.var_studid.get()+""
                    db_cursor.execute(QueryString)
                    print(QueryString)            
                else:
                    if not update:
                        return  
                messagebox.showinfo("success","student details successfully updated",parent=self.root)
                db_connection.commit()
                self.Reset_entrybx()
                self.fetch_data()
                db_connection.close()                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #========================delete data====================================================================

    def delete_data(self):
        if self.var_studid.get()=="":        
            messagebox.showerror("Error","student id must be require",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","Do You want to delete this student",parent=self.root)
                if delete>0:
                    db_connection = con.connect(connString)
                    db_cursor = db_connection.cursor()
                    QueryString="delete from student_mst where srno="+self.var_studid.get()+""
                    db_cursor.execute(QueryString)
                    print(QueryString)
                else:
                    if not delete:
                        return                        
                db_connection.commit()
                self.fetch_data()
                db_connection.close()
                messagebox.showinfo("Delete","student details successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #============================binding depart============================================================

    def bindDepart(self):
        retDepart=()
        try:
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            Query="select '--select--'  DEPART_NAME from dual union all select DEPART_NAME from depart"
            db_cursor.execute(Query)
            print(Query)
            rows=db_cursor.fetchall()
            if db_cursor.rowcount>1:
                retDepart=rows
            else:
                retDepart=["--select--","MCA"]
            return retDepart
            
            db_connection.close()
        except Exception as es:
                messagebox.showerror("Error","department binding error",parent=self.root)
            
    
            
 
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

