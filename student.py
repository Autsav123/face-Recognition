from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import  mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION  SYSTEM")
        
        
    #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
      #  self.var_address = "Default Address"
        self.var_teacher=StringVar()
        
        
        
        

    # first Image
        img=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\stu1.jpeg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\stu2.jpeg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        # third image
        img2=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\stu3.webp")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
       #bg img
        img3=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\backgroud1.jpeg")
        img3=img3.resize((1500,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="White",fg="darkgreen")
        title_lbl.place(x=0,y=1,width=1510,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1485,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=750,height=580)

        img_left=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\stu2.jpeg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current Course information
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Technolgy","Electronics","Mechnical","Civil","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","B.E./B.Tech","BCA","MCA","M.Tech","MBA","Other")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        Semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=720,height=300)
        
        #Student Id
        Student_ID_label=Label(Class_Student_frame,text="StudentID",font=("times new roman",12,"bold"))
        Student_ID_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.va_std_id,width=18,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        

        #Student name
        StudentName_label=Label(Class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"))
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(Class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

      #  class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=18,font=("times new roman",13,"bold"))
       # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("A","B","C","Other")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        #Roll No
        Roll_No_label=Label(Class_Student_frame,text="Roll no:",font=("times new roman",13,"bold"))
        Roll_No_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_No_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=18,font=("times new roman",13,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        Gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",13,"bold"))
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #Gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=18,font=("times new roman",13,"bold"))
        #Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        Gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=2,pady=8,sticky=W)

        #DOB
        dob_label=Label(Class_Student_frame,text="DOB:",font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=18,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #Email

        email_label=Label(Class_Student_frame,text="Email:",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
      
      # phone
        phone_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=18,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
    
    # ADRESS
        address_label=Label(Class_Student_frame,text="Address:",font=("times new roman",13,"bold"))
        address_label.grid(row=4,column=0,padx=8,pady=5,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=18,font=("times new roman",13,"bold"))                                    
        address_entry.grid(row=4,column=1,padx=8,pady=5)
    
    #Teacher Name
        teacher_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"))
        teacher_label.grid(row=4,column=2,padx=8,pady=5,sticky=W)

        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=18,font=("times new roman",13,"bold"))                                    
        teacher_entry.grid(row=4,column=3,padx=8,pady=5)
    #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Class_Student_frame,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        #buttons frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=650,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=650,height=40)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        
        update_btn_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn_photo_btn.grid(row=0,column=1)

         # Right Label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=780,height=580)

        img_right=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\student right.jpeg")
        img_right=img_right.resize((720,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=770,height=130)

        #Search System
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=700,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        self.var_search_combo=StringVar()
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No","Other")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        self.var_search=StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=18,font=("times new roman",13,"bold"))                                    
        search_entry.grid(row=0,column=2,padx=8,pady=5)

        search_btn=Button(Search_frame,command=self.search_data,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,command=self.fetch_data,text="ShowAll",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
#table frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher",),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Set column headings
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        
        self.student_table.heading("roll", text="Roll NO")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")  # Fixed typo here
        self.student_table.heading("teacher", text="Teacher")
        
        self.student_table["show"] = "headings"
       
        # Set column widths
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)

        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        
        self.student_table.column("teacher", width=100)
      

# Set widths for other columns as needed...

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
#function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Aspn@123456",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                
                                                                                                             #7  self.var_radio1.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get()
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aspn@123456",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for  i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
       # self.var_radio1.set(data[14])

# update function
    def update_data(self):
        print(self)
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.va_std_id.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Aspn@123456",database="face_recognizer")
                    my_cursor=conn.cursor()
                   # my_cursor = conn.cursor()
                    update_query = (
    "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s, Gender=%s, "
    "Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s WHERE Student_id=%s"
)
                    data = (
                                   self.var_dep.get(),
                                   self.var_course.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.var_std_name.get(),
                                   self.var_div.get(),
                                   self.var_roll.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_email.get(),
                                   self.var_phone.get(),
                                   self.var_address.get(),
                                   self.var_teacher.get(),
                                   #self.var_radio1.get(),  # Include this line to update var_radio1
                                   self.va_std_id.get()
                                   )

                    my_cursor.execute(update_query, data)
                    conn.commit()

                                                                                           
                                                                                                                                                                               
                else: 
                    if not Update:
                         return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                           
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                              
# delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)           
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                   conn=mysql.connector.connect(host="localhost",username="root",password="Aspn@123456",database="face_recognizer")
                   my_cursor=conn.cursor()
                   sql="delete from student where Student_id=%s"
                   val=(self.va_std_id.get(),)
                   my_cursor.execute(sql,val)
                else:
                    if not delete:
                       return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")     
        self.var_course.set("Select Course")  
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
       # self.var_radio1.set("")
    #search data
    def search_data(self):
        if  self.var_search_combo.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Aspn@123456",database="face_recognizer")
                
                my_cursor=conn.cursor()
                my_cursor.execute("select *from student where "+str(self.var_search_combo.get())+" LIKE '% "+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END , values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
# generate data set or take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Aspn@123456",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select* from Student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where Student_id=%s",(
                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                   # self.var_radio1.get(),
                                                                                                                                                                    self.va_std_id.get()==id+1                   
                                                                                                                                                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
              #  ========LOad predefined data on face drontals fromopencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scalling factor=1.3
                    #Minimum Neighbour=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)        
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         

if __name__=="__main__":
   root=Tk()
   obj=Student(root)
  
   

   root.mainloop()