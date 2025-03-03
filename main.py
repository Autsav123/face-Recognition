from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self .root.title("face  Recognition System")

        img=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\face 4.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\face recog1.webp")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        # third image
        img2=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\college.jpg")
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

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=1,width=1510,height=45)
         #student button
        img4=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\student.jpg")
        img4=img4.resize((220,220))
        self. photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4, command =self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=200,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=200,height=40)
        #Detect Face
        img5=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\face detector.png")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=200,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=200,height=40)
             #attendance
        img6=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\attendance face_recognization.png")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=200,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=200,height=40)
       #help
        img7=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\help.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=200,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=200,height=40)
       #train
        img8=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\training.jpeg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=350,width=200,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.train_data)
        b1_1.place(x=200,y=550,width=200,height=40)
#photo
        img9=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\photo.jpeg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=350,width=200,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=550,width=200,height=40)
# Devloper
        img10=Image.open(r"C:\Users\UTSAV DUBEY\Desktop\final face recog\face recog img\dev.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=350,width=200,height=220)

        b1_1=Button(bg_img,text="Devloper",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=550,width=200,height=40)
#Exit
        img11=Image.open(r"face recog img/exit.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=350,width=200,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=550,width=200,height=40)

    def open_img(self):
        os.startfile("data")
        # function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()