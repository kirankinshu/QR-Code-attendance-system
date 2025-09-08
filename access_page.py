from tkinter import*
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox
from detail_page import detail

def access():
    t=Toplevel()
    t.geometry("1920x1200")

    def reset():
        t1.delete(0,END)
        t2.delete(0,END)

#--------Background Image---------
    img=Image.open("img/access_bg.jpg")
    img=img.resize((1533,790))
    img=ImageTk.PhotoImage(img)
    l=Label(t)
    l.config(image=img)
    l.image=img
    l.place(x=0,y=0)
    
#--------------Page Title---------
    title=Label(t,text="Access Your Information",bg="black",fg="white", font=('arial',35,'bold'))
    title.place(x=485,y=100)

#----------------Form-----------
        
    l1=Label(t,text="Employee ID *",bg="silver",font=('arial',12))
    l1.place(x=590,y=352)
    t1=Entry(t,font="bold",bg="silver")
    t1.place(x=710,y=350)

    l2=Label(t,text="Password *",bg="silver",font=('arial',12))
    l2.place(x=590,y=402)
    t2=Entry(t,font="bold",show="*",bg="silver")
    t2.place(x=710,y=400)
    
#-------------login Section---------
    def log():
        mydb=mysql.connector.connect(host="127.0.0.1", user="root", passwd="")
        my=mydb.cursor()
        my.execute("use facial_database")
        my.execute("select * from employee where emp_id="+"'"+t1.get()+"'"+" and pass="+"'"+t2.get()+"'"+"")
        log=my.fetchall()
        f=0
        for x in log:
            name=x[1]
            f=f+1
        mydb.commit()
        if f==0:
            messagebox.showinfo("Login Message...","Invailid Employee Id or Password!")
        else:
            messagebox.showinfo("Login Message...","Login Successful")
            detail(name) # page detail and blink admin Name in that page
        
#-------------Buttons-------------
    img7=Image.open("img/next.jpg")
    img7=img7.resize((180,57))
    img7=ImageTk.PhotoImage(img7)
    b=Button(t,)
    b.config(image=img7, command=log)
    b.image=img7
    b.place(x=1275,y=250)

    img8=Image.open("img/reset.jpg")
    img8=img8.resize((180,57))
    img8=ImageTk.PhotoImage(img8)
    b=Button(t)
    b.config(image=img8, command=reset)
    b.image=img8
    b.place(x=1275,y=350)

    img10=Image.open("img/exit.jpg")
    img10=img10.resize((180,57))
    img10=ImageTk.PhotoImage(img10)
    b=Button(t)
    b.config(image=img10, command=t.destroy)
    b.image=img10
    b.place(x=1275,y=450)


