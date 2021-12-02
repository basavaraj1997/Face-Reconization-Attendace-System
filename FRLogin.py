from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from FRWindo import face_recoganization
import cx_Oracle as con
import DAL
connString = 'FRAS/FRAS@localhost:1521/xe'
connString = DAL.getDbConn()


class Login_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry('400x400+0+0')
        self.root.title("Face Recoganization System Login")

    #==========variables================

        #self.var_uname=StringVar()
        #self.var_pass=StringVar()
          #back img3
        img3=Image.open(r"IMG\Grey.jpg")
        img3=img3.resize((380,380),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=380,height=380)

        title_lb=Label(bg_img,text="Login Here",font=("times new roman",15,"bold"),bg="white",fg="red")
        title_lb.place(x=130,y=15,width=105,height=35)

        #main frame for stud details
        main_frame =Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=65,width=355,height=300)

        user_label=Label(main_frame,text="Username:",font=("times new roman",13,"bold"),bg="white")
        user_label.grid(row=0,column=0,padx=10,pady=20,sticky=W)

        self.user_entry=ttk.Entry(main_frame,width=20,font=("times new roman",13,"bold"))
        self.user_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)

        pass_label=Label(main_frame,text="Password:",font=("times new roman",13,"bold"),bg="white")
        pass_label.grid(row=1,column=0,padx=10,pady=20,sticky=W)

        self.pass_entry=ttk.Entry(main_frame,width=20,font=("times new roman",13,"bold"))
        self.pass_entry.grid(row=1,column=1,padx=0,pady=5,sticky=W)

        but=Button(main_frame,text="Login",command=self.Face,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="black")
        but.place(x=110,y=150,width=150,height=30)

    def Face(self): #this function called in sysytem login button
        if self.user_entry.get()=="":
           messagebox.showerror("Error","Enter username",parent=self.root)
           return
        if self.pass_entry.get()=="":
            messagebox.showerror("Error","Enter password",parent=self.root)
            return
        try:
           query2 ="SELECT UNM , UPW FROM USERMST WHERE  EMAIL='"+str(self.user_entry.get())+"' AND UPW='"+str(self.pass_entry.get())+"'"

           # implement query Sentence
           print("*******************")
           print(query2)
           db_connection = con.connect(connString)
           db_cursor = db_connection.cursor()
           db_cursor.execute(query2)
           rows=db_cursor.fetchall()
           if db_cursor.rowcount>0:              
               self.new_window=Toplevel(self.root)
               self.SD=face_recoganization(self.new_window)
               root.destroy()
               
           else:
                messagebox.showinfo('Information', "Invalid Credential")
                self.user_entry.focus()
                return ""
        except con.DatabaseError as e:
            print(e)
          
            messagebox.showinfo('Information', "connection failed!!!")
        finally:
          db_connection.close()
           
        

if __name__ == "__main__":
    root=Tk()
    obj=Login_page(root)
    root.mainloop()
