from tkinter import*
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox
import io
import qrcode
import cv2, time
from pyzbar.pyzbar import decode

def detail(name):
    t=Toplevel()
    t.geometry("1920x1200")

#--------Background Image---------
    img=Image.open("img/detail_bg.jpg")
    img=img.resize((1533,790))
    img=ImageTk.PhotoImage(img)
    l=Label(t)
    l.config(image=img)
    l.image=img
    l.place(x=0,y=0)

#---------Frame---------
    frm=Frame(t,bg="white")
    frm.place(x=370,y=120,width=750,height=560)

#---------------Frame for Image-------
    frm1=Frame(frm,bg="silver")
    frm1.place(x=520,y=100,width=220,height=150)

#---------User Name Show--------
    l=Label(frm,text="Welcome, "+str(name),bg="white",fg="blue", font=('arial',25,'italic'))
    l.place(x=1,y=5)

#------------Registered Data Showing-------
    mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="")
    my=mydb.cursor()
    my.execute("use facial_database")
    my.execute("select * from employee where emp_name=%s", (name,))
    log=my.fetchall()
    path1=""
    f=0
    for x in log:
        employee=x[1]
        path1=x[7]
        f=f+1
    l1=Label(frm,text="Your Registered Data",bg="white",font=('arial',20,'bold'))
    l1.place(x=210,y=50)
    l2=Label(frm,text="Employee Id: ",bg="white",font=('arial',15,'bold'))
    l2.place(x=10,y=100)
    d1=Label(frm,text=x[0],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d1.place(x=140,y=100)
    l3=Label(frm,text="Full Name:",bg="white",font=('arial',15,'bold'))
    l3.place(x=10,y=150)
    d2=Label(frm,text=x[1],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d2.place(x=120,y=150)
    l4=Label(frm,text="Contact Number:",bg="white",font=('arial',15,'bold'))
    l4.place(x=10,y=200)
    d3=Label(frm,text=x[2],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d3.place(x=180,y=200)
    l5=Label(frm,text="Department:",bg="white",font=('arial',15,'bold'))
    l5.place(x=10,y=250)
    d4=Label(frm,text=x[3],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d4.place(x=140,y=250)
    l6=Label(frm,text="Designation:",bg="white",font=('arial',15,'bold'))
    l6.place(x=10,y=300)
    d5=Label(frm,text=x[4],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d5.place(x=140,y=300)
    l7=Label(frm,text="Email Id:",bg="white",font=('arial',15,'bold'))
    l7.place(x=10,y=350)
    d6=Label(frm,text=x[5],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d6.place(x=100,y=350)
    l8=Label(frm,text="Gender:",bg="white",font=('arial',15,'bold'))
    l8.place(x=10,y=400)
    d7=Label(frm,text=x[8],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d7.place(x=100,y=400)
    l9=Label(frm,text="Password:",bg="white",font=('arial',15,'bold'))
    l9.place(x=10,y=450)
    d8=Label(frm,text=x[6],bg="white",fg='green',font=('arial',17,'italic','bold'))
    d8.place(x=110,y=450)

#-------------Image----------
    l9=Label(frm1,bg="white",font=('arial',15,'bold'))
    img=Image.open(path1)
    img=img.resize((220,150))
    img=ImageTk.PhotoImage(img)
    l9.config(image=img)
    l9.image=img
    l9.place(x=0,y=0)

#--------------Change Password Only--------
    def dfs():
        p1=Toplevel()
        p1.geometry("500x200")
        l1=Label(p1,text="Enter old password",font="bold")
        l1.place(x=40,y=20)
        l2=Label(p1,text="Enter new password",font="bold")
        l2.place(x=40,y=72)
        t2=Entry(p1,font="bold")
        t2.place(x=240,y=20)
        t3=Entry(p1,font="bold")
        t3.place(x=240,y=72)
        def change():
            mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="")
            my=mydb.cursor()
            my.execute("use facial_database")
            my.execute("update employee set pass=%s where pass=%s", (t3.get(), t2.get()))
            messagebox.showinfo("CONFIRMATION!!!","Password Changed Successfully!")
            mydb.commit()
        b=Button(p1,text="Change Password",command=change)
        b.place(x=200,y=130)

#--------------Export Attendance Report--------
    def att():
        name=""
        v=cv2.VideoCapture(0)
        while True:
            rect,frame=v.read()
            d=decode(frame)
            for obj in d:
                name=d[0].data.decode()
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,name,(50,50),font,1,(0,0,225),2)
            cv2.imshow("MY FRAME",frame)
            key=cv2.waitKey(1)
            if key==ord('q'):
                break
        v.release()
        cv2.destroyAllWindows()

#--------------Edit Info--------
    def open_edit_window():
        edit_win = Toplevel()
        edit_win.title("Edit Information")
        edit_win.geometry("400x300")

        Label(edit_win, text="Contact No:", font=("arial", 12)).place(x=20, y=30)
        Label(edit_win, text="Department:", font=("arial", 12)).place(x=20, y=70)
        Label(edit_win, text="Designation:", font=("arial", 12)).place(x=20, y=110)
        Label(edit_win, text="Email ID:", font=("arial", 12)).place(x=20, y=150)

        e1 = Entry(edit_win, font=("arial", 12))
        e1.place(x=150, y=30)
        e2 = Entry(edit_win, font=("arial", 12))
        e2.place(x=150, y=70)
        e3 = Entry(edit_win, font=("arial", 12))
        e3.place(x=150, y=110)
        e4 = Entry(edit_win, font=("arial", 12))
        e4.place(x=150, y=150)

        e1.insert(0, x[2])  # cont
        e2.insert(0, x[3])  # dept
        e3.insert(0, x[4])  # design
        e4.insert(0, x[5])  # email

        def update_info():
            try:
                mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="", database="facial_database")
                my = mydb.cursor()
                my.execute("""
                    UPDATE employee 
                    SET cont=%s, dept=%s, design=%s, email=%s 
                    WHERE emp_name=%s
                """, (e1.get(), e2.get(), e3.get(), e4.get(), name))
                mydb.commit()
                messagebox.showinfo("Success", "Information Updated Successfully!")
                edit_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        Button(edit_win, text="Update", command=update_info, bg="green", fg="white", font=("arial", 12)).place(x=150, y=210)

#-----------Buttons------------
    img1=Image.open("img/attendance.jpg")
    img1=img1.resize((180,57))
    img1=ImageTk.PhotoImage(img1)
    b1=Button(t)
    b1.config(image=img1,command=att)
    b1.image=img1
    b1.place(x=1275,y=300)

    img2=Image.open("img/edit.jpg")
    img2=img2.resize((180,57))
    img2=ImageTk.PhotoImage(img2)
    b2=Button(t)
    b2.config(image=img2, command=open_edit_window)
    b2.image=img2
    b2.place(x=1275,y=400)

    img3=Image.open("img/exit.jpg")
    img3=img3.resize((180,57))
    img3=ImageTk.PhotoImage(img3)
    b3=Button(t)
    b3.config(image=img3, command=t.destroy)
    b3.image=img3
    b3.place(x=1275,y=500)

    b6=Button(frm,text="Change Your Password",fg="red",font=('arial',10,'italic'),command=dfs)
    b6.place(x=300,y=500)
