from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cx_Oracle as con


connString = 'FRAS/FRAS@localhost:1521/xe'
class Depart:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recoganization System")
        #=============variables========================
        self.var_depid=StringVar()
        self.var_depname=StringVar()
        self.var_descrip=StringVar()
        self.var_sem=StringVar()
        self.var_courseid=StringVar()
        self.var_coursename=StringVar()
        self.var_cdescrip=StringVar()
        self.var_cdepid=StringVar()
        self.var_status=StringVar()
        self.var_Cdepname=StringVar()

        img3=Image.open(r"D:\MCA_II\Project\IMG\img20.png")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lb=Label(bg_img,text="Department/Course Details",font=("times new roman",35,"bold"),bg="pink",fg="darkgreen")
        title_lb.place(x=0,y=5,width=1530,height=60)

        #===================frame and field=============

        D_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Department Info",font=("times new roman",15,"bold"))
        D_frame.place(x=100,y=120,width=625,height=600)

         #department Id
        dId_label=Label(D_frame,text="Depart Id:",font=("times new roman",13,"bold"),bg="white")
        dId_label.grid(row=0,column=1,padx=15,pady=15,sticky=W)

        dId_entry=ttk.Entry(D_frame, textvariable=self.var_depid,width=20,font=("times new roman",13,"bold"),state="readonly")
        dId_entry.grid(row=0,column=2,padx=15,pady=15,sticky=W)

        dname_label=Label(D_frame,text="Depart Name:",font=("times new roman",13,"bold"),bg="white")
        dname_label.grid(row=1,column=1,padx=15,pady=15,sticky=W)

        dname_entry=ttk.Entry(D_frame,textvariable=self.var_depname,width=20,font=("times new roman",13,"bold"))
        dname_entry.grid(row=1,column=2,padx=15,pady=15,sticky=W)

        descri_label=Label(D_frame,text="Description:",font=("times new roman",13,"bold"),bg="white")
        descri_label.grid(row=2,column=1,padx=15,pady=15,sticky=W)

        descri_entry=ttk.Entry(D_frame,textvariable=self.var_descrip,width=20,font=("times new roman",13,"bold"))
        descri_entry.grid(row=2,column=2,padx=15,pady=15,sticky=W)

        #buttons frame
        btn_frame=Frame(D_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=60,y=175,width=513,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.addD_data,width=16,font=("times new roman",13,"bold"),bg="pink",fg="black")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.updateD_data,width=16,font=("times new roman",13,"bold"),bg="pink",fg="black")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.ResetD_entrybx,width=16,font=("times new roman",13,"bold"),bg="pink",fg="black")
        reset_btn.grid(row=0,column=3)
        #==========table depart===================

        table_frame=Frame(D_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=225,width=615,height=340)

        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.stud_table=ttk.Treeview(table_frame,column=("id","name","des"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.stud_table.yview)

        self.stud_table.heading("id",text="Department ID")
        self.stud_table.heading("name",text="Department Name")
        self.stud_table.heading("des",text="Description")

        self.stud_table["show"]="headings"
        self.stud_table.column("id",width=180)
        self.stud_table.column("name",width=210)
        self.stud_table.column("des",width=225)

        self.stud_table.pack(fill=Y,expand=1)
        self.fetchD_data()
        self.stud_table.bind("<ButtonRelease>",self.getD_cursor)
#============================course details====================================================
        
        C_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Course Info",font=("times new roman",15,"bold"))
        C_frame.place(x=750,y=120,width=650,height=600)

         #course Id
        cId_label=Label(C_frame,text="course Id:",font=("times new roman",13,"bold"),bg="white")
        cId_label.grid(row=0,column=2,padx=15,pady=15,sticky=W)

        cId_entry=ttk.Entry(C_frame, textvariable=self.var_courseid,width=15,font=("times new roman",13,"bold"),state="readonly")
        cId_entry.grid(row=0,column=3,padx=15,pady=15,sticky=W)

        cname_label=Label(C_frame,text="course Name:",font=("times new roman",13,"bold"),bg="white")
        cname_label.grid(row=1,column=0,padx=15,pady=15,sticky=W)

        cname_entry=ttk.Entry(C_frame,textvariable=self.var_coursename,width=15,font=("times new roman",13,"bold"))
        cname_entry.grid(row=1,column=1,padx=15,pady=15,sticky=W)

        cescri_label=Label(C_frame,text="Description:",font=("times new roman",13,"bold"),bg="white")
        cescri_label.grid(row=2,column=2,padx=15,pady=15,sticky=W)

        cescri_entry=ttk.Entry(C_frame,textvariable=self.var_cdescrip,width=15,font=("times new roman",13,"bold"))
        cescri_entry.grid(row=2,column=3,padx=15,pady=15,sticky=W)

         #Semester   
        sem_label=Label(C_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        self.sem_combo=ttk.Combobox(C_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),width=13,state="readonly")
        self.sem_combo["values"]=("--Select--","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")   
        self.sem_combo.current(0)
        self.sem_combo.grid(row=1,column=3,padx=15,pady=10,sticky=W)
        #===============radio button====================

        radiobtn1=ttk.Radiobutton(C_frame,variable=self.var_status,text="Active",value="A")
        radiobtn1.grid(row=2,column=0)

       
        radiobtn2=ttk.Radiobutton(C_frame,variable=self.var_status,text="Deactive",value="D")
        radiobtn2.grid(row=2,column=1)
        self.var_status.set("Active")

        cdId_label=Label(C_frame,text="Depart Name:",font=("times new roman",13,"bold"),bg="white")
        cdId_label.grid(row=0,column=0,padx=15,pady=15,sticky=W)

        DCombo_val=self.bindDepart2()
        #cdId_entry=ttk.Entry(C_frame,textvariable=self.var_cdepid,width=15,font=("times new roman",13,"bold"))
        self.dep_combo=ttk.Combobox(C_frame ,textvariable=self.var_Cdepname,font=("times new roman",12,"bold"),width=15,state="readonly")
        self.dep_combo["values"]=DCombo_val
        self.dep_combo.current(0)
        self.dep_combo.grid(row=0,column=1,padx=15,pady=15,sticky=W)

        #buttons frame
        btn1_frame=Frame(C_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=60,y=165,width=513,height=35)

        save1_btn=Button(btn1_frame,text="Save", command=self.addC_data,width=16,font=("times new roman",13,"bold"),bg="pink",fg="black")
        save1_btn.grid(row=0,column=0)
        
        update1_btn=Button(btn1_frame,text="Update",command=self.updateC_data,width=16,font=("times new roman",13,"bold"),bg="pink",fg="black")
        update1_btn.grid(row=0,column=1)

        reset1_btn=Button(btn1_frame,text="Reset",command=self.ResetC_entrybx,width=16,font=("times new roman",13,"bold"),bg="pink",fg="black")
        reset1_btn.grid(row=0,column=3)
        #==========table course===================

        table1_frame=Frame(C_frame,bd=2,bg="white",relief=RIDGE)
        table1_frame.place(x=3,y=225,width=615,height=340)

        scroll_y=ttk.Scrollbar(table1_frame,orient=VERTICAL)

        self.stud1_table=ttk.Treeview(table1_frame,column=("id","name","des","sem","dep","st"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.stud_table.yview)

        self.stud1_table.heading("id",text="Course ID")
        self.stud1_table.heading("name",text="Course Name")
        self.stud1_table.heading("des",text="Description")
        self.stud1_table.heading("sem",text="semester")
        self.stud1_table.heading("dep",text="Depart Name")
        self.stud1_table.heading("st",text="Status")
        
        self.stud1_table["show"]="headings"
        self.stud1_table.column("id",width=100)
        self.stud1_table.column("name",width=100)
        self.stud1_table.column("des",width=100)
        self.stud1_table.column("sem",width=100)
        self.stud1_table.column("dep",width=100)
        self.stud1_table.column("st",width=100)
        

        self.stud1_table.pack(fill=Y,expand=1)
        self.fetchC_data()
        self.getmxD()
        self.getmxC()
        self.stud1_table.bind("<ButtonRelease>",self.getC_cursor)
       


#=============================database connection CRUD===================================================
#=============================Department insert ==========================================================
    def addD_data(self):
       if self.var_depid.get()=="" or self.var_depname.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
       if self.var_depid.get()=="":
            messagebox.showerror("Error","Enter departid",parent=self.root)
            return
       try:
           query2 = "INSERT INTO depart(DEPART_ID,DEPART_NAME,DESCRIP) VALUES ((select nvl(max(DEPART_ID),0)+1 from depart),'"+self.var_depname.get()+"','"+self.var_descrip.get()+"')"
       # implement query Sentence
           print("*******************")
           print(query2)
           db_connection = con.connect(connString)
           db_cursor = db_connection.cursor()
           db_cursor.execute(query2)
           
        # Submit to database for execution
           db_connection.commit()
           messagebox.showinfo('Information', "Department added Successfully")
           self.fetchD_data()
           self.ResetD_entrybx()
       except con.DatabaseError as e:
          print(e)
          db_connection.rollback()
          messagebox.showinfo('Information', "Data insertion failed!!!")
       finally:
          db_connection.close()
#================================Department fetching data to table=============================================

    def fetchD_data(self):
        try:
            self.stud_table.delete(*self.stud_table.get_children()) 
            query2="select DEPART_ID,DEPART_NAME,DESCRIP  from DEPART order by DEPART_ID"
            print("*-------**-------*")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                 print("**********Got Data Happy Na*********")
                 self.stud_table.insert("",'end',text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2])))
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()

#============================Department get cursor=========================================================================
        
    def getD_cursor(self,event=""):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]
        self.var_depid.set(data[0]),
        self.var_depname.set(data[1]),
        self.var_descrip.set(data[2]);
        
#=============================Department update depart=============================================================================
    def updateD_data(self):
        if self.var_depid.get()=="" or self.var_depname.get()=="" or self.var_descrip.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
        if self.var_depid.get()=="":
            messagebox.showerror("Error","Enter departid",parent=self.root)
            return
        
        try:
            update=messagebox.askyesno("update","Do you want to update this depart details",parent=self.root)
            if update>0:
                print("Hello Maau")
                db_connection = con.connect(connString)
                db_cursor = db_connection.cursor()
                QueryString="update depart set DEPART_ID='"+self.var_depid.get()+"',DEPART_NAME='"+self.var_depname.get()+"',DESCRIP='"+self.var_descrip.get()+"' "+" where DEPART_ID="+self.var_depid.get()+""
                db_cursor.execute(QueryString)
                print(QueryString)
            else:
                if not update:
                    return
            messagebox.showinfo("success","Depart details successfully  updated",parent=self.root)
            db_connection.commit()
            #self.Reset_entrybx()
            self.fetchD_data()
            self.ResetD_entrybx()
            db_connection.close()
                
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
#==================================Depart Reset================================================
    def ResetD_entrybx(self):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]
        self.var_depid.set(""),
        self.var_depname.set(""),
        self.var_descrip.set("")
        
        self.getmxD()
        
#=================================Course Insert==================================================
    def addC_data(self):
       if self.var_courseid.get()=="" or self.var_coursename.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
       if self.var_courseid.get()=="":
            messagebox.showerror("Error","Enter departid",parent=self.root)
            return
       try:
           query2 = "INSERT INTO course(CO_ID,CO_NAME,DESCRIP,DEPART_ID,SEM,STATUS) VALUES ((select nvl(max(CO_ID),0)+1 from course),'"+self.var_coursename.get()+"','"+self.var_cdescrip.get()+"',(select depart_id from depart where depart_name='"+self.var_Cdepname.get()+"'),'"+self.var_sem.get()+"','"+self.var_status.get()+"')"
       # implement query Sentence
           print("*******************")
           print(query2)
           db_connection = con.connect(connString)
           db_cursor = db_connection.cursor()
           db_cursor.execute(query2)
           
        # Submit to database for execution
           db_connection.commit()
           messagebox.showinfo('Information', "Course added Successfully")
           self.fetchC_data()
           self.ResetC_entrybx()
       except con.DatabaseError as e:
          print(e)
          db_connection.rollback()
          messagebox.showinfo('Information', "Data insertion failed!!!")
       finally:
          db_connection.close()
#===================================Course fetching data to table===================================
    def fetchC_data(self):
        try:
            self.stud1_table.delete(*self.stud1_table.get_children()) 
            query2=" Select C.CO_ID,C.CO_NAME,C.DESCRIP,C.SEM,D.DEPART_NAME,C.STATUS,D.DEPART_ID  from DEPART D ,COURSE C WHERE D.DEPART_ID=C.DEPART_ID order by C.CO_ID " 
            print("*-------**-------*")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                 print("**********Got Data Happy Na*********")
                 self.stud1_table.insert("",'end',text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5])))
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()
#============================Department get cursor=========================================================================
        
    def getC_cursor(self,event=""):
        cursor_focus=self.stud1_table.focus()
        content=self.stud1_table.item(cursor_focus)
        data=content["values"]
        self.var_courseid.set(data[0]),
        self.var_coursename.set(data[1]),
        self.var_cdescrip.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_Cdepname.set(data[4]),
        self.var_status.set(data[5]);
        self.var_status.set("Active")
        
#==================================Depart Reset==================================================
    def ResetC_entrybx(self):
        cursor_focus=self.stud1_table.focus()
        content=self.stud1_table.item(cursor_focus)
        data=content["values"]
        self.dep_combo.current(0),
        self.var_courseid.set(""),
        self.var_coursename.set(""),
        self.var_cdescrip.set(""),
        self.var_cdepid.set(""),
        self.sem_combo.current(0),
        self.var_status.set("")
        self.getmxC()
#====================================Course update===============================================
    def updateC_data(self):
        if self.var_courseid.get()=="" or self.var_coursename.get()=="" or self.var_cdescrip.get()=="" or self.var_Cdepname.get()=="--Select--" or self.var_sem.get()=="" or self.var_status.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
           return
        if self.var_courseid.get()=="":
            messagebox.showerror("Error","Enter courseid",parent=self.root)
            return
        
        try:
            update=messagebox.askyesno("update","Do you want to update this course details",parent=self.root)
            if update>0:
                print("Hello Maau")
                db_connection = con.connect(connString)
                db_cursor = db_connection.cursor()
                QueryString="update course set CO_ID='"+self.var_courseid.get()+"',CO_NAME='"+self.var_coursename.get()+"',DESCRIP='"+self.var_cdescrip.get()+"',DEPART_ID=(select depart_id from depart where depart_name='"+self.var_Cdepname.get()+"'),SEM='"+self.var_sem.get()+"',STATUS='"+self.var_status.get()+"' "+" where CO_ID="+self.var_courseid.get()+""
                db_cursor.execute(QueryString)
                print(QueryString)
            else:
                if not update:
                    return
            messagebox.showinfo("success","course details successfully  updated",parent=self.root)
            db_connection.commit()
            self.ResetC_entrybx()
            self.fetchC_data()
            db_connection.close()
                
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
#==============================
    def getmxD(self):
        try:
            query2="select (nvl(max(DEPART_ID),0)+1) srno from depart"
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                self.var_depid.set(row[0])
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()
#===============================
    def getmxC(self):
        try:
            query2="select (nvl(max(CO_ID),0)+1) srno from course"
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            for row in rows:
                self.var_courseid.set(row[0])
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Data fetching error!!!")
        finally:
            db_connection.close()
    #=============================================================

    def bindDepart2(self):
        retDepart=()
        try:
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            Query="select '--Select--'  DEPART_NAME from dual union all select DEPART_NAME from depart"
            db_cursor.execute(Query)
            print(Query)
            rows=db_cursor.fetchall()
            if db_cursor.rowcount>1:
                retDepart=rows
            else:
                retDepart=["--Select--","MCA"]
            return retDepart
            
            db_connection.close()
        except Exception as es:
                messagebox.showerror("Error","department binding error",parent=self.root)
            

            

        
       

       





if __name__ == "__main__":
    root=Tk()
    obj=Depart(root)
    root.mainloop()

