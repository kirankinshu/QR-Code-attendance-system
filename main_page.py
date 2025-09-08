from tkinter import*
from PIL import ImageTk,Image
from reg_page import reg
from access_page import access
from mark_page import mark

t=Tk()
t.geometry("1920x1200")

#-------BackGround-------
img=Image.open("img/main_bg.jpg")
img=img.resize((1510,900))
img=ImageTk.PhotoImage(img)
l=Label(t,image=img)
l.place(x=0,y=0)

#===================== Sliding Project Title Start =====================
title_text = "  QR Code Recognition-Based Attendance System  "
x = 0

slide_label = Label(t, text="", font=("arial", 28, "bold"), fg="white", bg="black")
slide_label.place(relx=0.5, y=10, anchor="n")  # Centered horizontally
slide_label.lift()  # Bring to front

def slide():
    global x
    slide_label.config(text=title_text[:x])
    x += 1
    if x > len(title_text):
        x = 0
    t.after(150, slide)

slide()
#====================== Sliding Project Title End ======================

#-------Calling Next Pages------
def next3():
    reg()
def next4():
    mark()
def next5():
    access()

#----------Text----------
frm1=Frame(t,bg="black")
frm1.place(x=5,y=145,width=455,height=150)

line1=Label(frm1,text=" This is a QR CODE Base Attendance\nSystem for Employees. Here Employee\ncan mark Their attendance with time and date\nby their face.",font=("arial",14,"bold"),bg="black",fg="white").place(x=0,y=10)
line2=Label(frm1,text="Do not forget to mark Attendance!!!",font=("arial",19,"bold"),bg="black",fg="red").place(x=17,y=115)

#===============================================Introduction Page Start================================================
def intro():
    t=Toplevel()
    t.geometry("1920x1200")

    img11=Image.open("img/intro_bg.jpg")
    img11=img11.resize((700,800))
    img11=ImageTk.PhotoImage(img11)
    l=Label(t)
    l.config(image=img11)
    l.image=img11
    l.place(x=0,y=0)

    frm=Frame(t,bg="silver")
    frm.place(x=700,y=2,width=765,height=900)

    intro=Label(frm,text="INTRODUCTION",font=("arial",30,"bold"),bg="silver",fg="red").place(x=250,y=10)

    intro_text = '''
Traditional method of attendance marking is a tedious task in many schools or
colleges and organizations. It is also an extra burden to the faculties or
department who should mark attendance by manually calling the names of
students or employees which might take about 5 minutes of entire session.
This is time consuming. There are some chances of proxy attendance. Therefore,
many institutes or organization started deploying many other techniques for
recording attendance like use of Radio Frequency Identification(RFID), iris
recognition, fingerprint recognition, and so on. However, these systems are
queue based which might consume more time and are intrusive in nature. Face
recognition has set an important biometric feature, which can be easily
acquirable and is non-intrusive. Face recognition based systems are relatively
oblivious to various facial expression. Face recognition system consists of two
categories: verification and face identification. Face verification is a
matching process, it compares face image against the registered face images and
whereas is a problem that compares a query face image. The purpose of this
system is to build an attendance system which is based on face recognition
techniques. Here face of an individual will be considered for marking attendance.
Nowadays, face recognition is gaining more popularity and has been widely used.
In this paper, we proposed a system which detects the faces of students or
employee from live streaming video of classroom and work location and attendance
will be marked if the detected face is found in the database. This new system will
consume less time than compared to traditional methods.
'''
    line1 = Label(frm, text=intro_text, font=("arial",15), bg="silver", fg="black", justify="left")
    line1.place(x=0, y=70)

    img18=Image.open("img/exit.jpg")
    img18=img18.resize((180,57))
    img18=ImageTk.PhotoImage(img18)
    b=Button(t)
    b.config(image=img18, command=t.destroy)
    b.image=img18
    b.place(x=1080,y=700)

#====================================================Introduction Page End==================================================

#====================================================How To Use Page Start==============================================
def use():
    t=Toplevel()
    t.geometry("1920x1200")

    img11=Image.open("img/use_bg.WEBP")
    img11=img11.resize((1510,900))
    img11=ImageTk.PhotoImage(img11)
    l=Label(t)
    l.config(image=img11)
    l.image=img11
    l.place(x=0,y=0)

    step1=Label(t,text="STEP1: Click on Register Button and Fill All details with Photo, click Submit.",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=50)
    step2=Label(t,text="STEP2: After Submit You Can Mark Your Attendance From Main Screen Menu.",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=100)
    step3=Label(t,text="STEP3: For Mark Attendance Choose Mark Attendance Button.",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=150)
    step4=Label(t,text="STEP4: Click your clear photo or you can retake photo if not clear.",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=200)
    step5=Label(t,text="STEP5: Then click mark attendence given that screen.",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=250)
    step6=Label(t,text="STEP6: If you want to access your account and Modify any Information.",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=300)
    step7=Label(t,text="STEP7: Click Access you information in Main Menu and fill instruction. ",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=350)
    step8=Label(t,text="STEP8: After successful login you can modify you profile data with edit Button. ",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=400)
    step9=Label(t,text="STEP9: And you can also change your password and see and export your Attendance Report.",font=("arial",15,"bold"),bg="black",fg="white").place(x=10,y=450)

    img15=Image.open("img/exit.jpg")
    img15=img15.resize((180,57))
    img15=ImageTk.PhotoImage(img15)
    b=Button(t)
    b.config(image=img15, command=t.destroy)
    b.image=img15
    b.place(x=1200,y=550)

#=====================================================How To Use Page End=================================================

#---------Button---------
img1=Image.open("img/intro.jpg")
img1=img1.resize((185,63))
img1=ImageTk.PhotoImage(img1)
b=Button(t,image=img1,command=intro)
b.place(x=1200,y=175)

img2=Image.open("img/how.jpg")
img2=img2.resize((185,63))
img2=ImageTk.PhotoImage(img2)
b=Button(t,image=img2, command=use)
b.place(x=1200,y=255)

img3=Image.open("img/reg.jpg")
img3=img3.resize((185,63))
img3=ImageTk.PhotoImage(img3)
b=Button(t,image=img3, command=next3)
b.place(x=1200,y=385)

img4=Image.open("img/mark.jpg")
img4=img4.resize((185,63))
img4=ImageTk.PhotoImage(img4)
b=Button(t,image=img4, command=next4)
b.place(x=1200,y=500)

img5=Image.open("img/access.jpg")
img5=img5.resize((185,63))
img5=ImageTk.PhotoImage(img5)
b=Button(t,image=img5,command=next5)
b.place(x=1200,y=635)

img6=Image.open("img/exit.jpg")
img6=img6.resize((185,63))
img6=ImageTk.PhotoImage(img6)
b=Button(t,image=img6,command=t.destroy)
b.place(x=1200,y=735)

#---------Video---------
s=1
def picture():
    global s
    try:
        img1=Image.open(r"img/img"+str(s)+".jpg")
        img2=img1.resize((600,420))
        img2=ImageTk.PhotoImage(img2)
        l1=Label(t)
        l1.config(image=img2)
        l1.image=img2
        l1.place(x=440,y=370)
        s=s+1
        if s==132:
            s=1
        t.after(100,picture)
    except:
        s = 1
        picture()

picture()
