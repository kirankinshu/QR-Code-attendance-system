from tkinter import*
import qrcode
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import filedialog
import math
import argparse
gender1=""
path=""
def reg():
    t=Toplevel()
    t.geometry("1920x1200")

    def reset():
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        t5.delete(0,END)
        t6.delete(0,END)
        t7.delete(0,END)
        t8.delete(0,END)
        
#--------Background Image---------
    img11=Image.open("img/reg_bg.jpg")
    img11=img11.resize((1440,900))
    img11=ImageTk.PhotoImage(img11)
    l=Label(t)
    l.config(image=img11)
    l.image=img11
    l.place(x=0,y=0)
    
#--------------Frame--------------
    frm=Frame(t,bg="white")
    frm.place(x=400,y=40,width=665,height=720)
    
#--------------Page Title---------
    title=Label(frm,text="Employee Registration Form",bg="white",fg="blue", font=('arial',35,'bold','underline'))
    title.place(x=5,y=5)

#--------------Form--------------  
    l1=Label(frm,text="Employee ID*",bg="white",font=('arial',12))
    l1.place(x=150,y=252)
    t1=Entry(frm,font="bold",bg="white")
    t1.place(x=300,y=250)

    l2=Label(frm,text="Employee Name*",bg="white",font=('arial',12))
    l2.place(x=150,y=302)
    t2=Entry(frm,font="bold",bg="white")
    t2.place(x=300,y=300)

    l3=Label(frm,text="Contact Number*",bg="white",font=('arial',12))
    l3.place(x=150,y=352)
    t3=Entry(frm,font="bold",bg="white")
    t3.place(x=300,y=350)

    l4=Label(frm,text="Department*",bg="white",font=('arial',12))
    l4.place(x=150,y=452)
    t4=Entry(frm,font="bold",bg="white")
    t4.place(x=300,y=450)

    l5=Label(frm,text="Designation*",bg="white",font=('arial',12))
    l5.place(x=150,y=502)
    t5=Entry(frm,font="bold",bg="white")
    t5.place(x=300,y=500)

    l6=Label(frm,text="Email ID*",bg="white",font=('arial',12))
    l6.place(x=150,y=552)
    t6=Entry(frm,font="bold",bg="white")
    t6.place(x=300,y=550)

    l7=Label(frm,text="Create Password*",bg="white",font=('arial',12))
    l7.place(x=150,y=602)
    t7=Entry(frm,font="bold",bg="white")
    t7.place(x=300,y=600)

    l8=Label(frm,text="Confirm Password*",bg="white",font=('arial',12))
    l8.place(x=150,y=652)
    t8=Entry(frm,font="bold",show= '*',bg="white")
    t8.place(x=300,y=650)

    l9=Label(frm,text="Gender*",bg="white",font=('arial',12))
    l9.place(x=150,y=402)
    t9=Entry(frm,font="bold",bg="white")
    t9.place(x=300,y=400)
    t9.config(state='disable')

    l10=Label(frm,text="---- If all infromation are correct, just click on submit button ----",bg="white",fg="red",font=('arial',10))
    l10.place(x=160,y=682)
 
#--------------Connecting and Save------------
    def save():
        name = t2.get().strip()
        contact = t3.get().strip()

        # ✅ Name validation
        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Employee name must contain only letters.")
            return

        # ✅ Contact validation
        if not contact.isdigit() or len(contact) != 10:
            messagebox.showerror("Invalid Input", "Contact number must be exactly 10 digits.")
            return

        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
            my = mydb.cursor()
            my.execute("use facial_database")
            count = 1
            my.execute("select * from employee")
            res = my.fetchall()
            for x in res:
                count += 1

            my.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                t1.get(), name, contact, t4.get(), t5.get(), t6.get(), t7.get(), path, t9.get()
            ))
            mydb.commit()

            img = qrcode.make(name)
            img.save("qrcode/" + str(count) + ".jpg")
            messagebox.showinfo("FACIAL DATABASE!!!", "You are Registered Successfully. Click Picture Of Your QR Code!!!")

            qr = Toplevel()
            qr.geometry("300x300")
            l = Label(qr)
            img21 = Image.open("qrcode/" + str(count) + ".jpg")
            img21 = img21.resize((300, 300))
            img21 = ImageTk.PhotoImage(img21)
            l.config(image=img21)
            l.image = img21
            l.place(x=0, y=0)

        except Exception as e:
            messagebox.showerror("Database Error", str(e))


#---------------Frame for Capture Image-------
    frm1=Frame(t,bg="silver")
    frm1.place(x=572,y=120,width=240,height=150)

#---------------Camera------------------
    def cam():
        global path
        count=1
        mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="")
        my=mydb.cursor()
        my.execute("use facial_database")
        my.execute("select * from employee");
        res=my.fetchall()
        for x in res:
            count=count+1;
        cap=cv2.VideoCapture(0)
        while True:
            rect,frame=cap.read()
            cv2.imshow("Click Photo:Press-'x'",frame)
            cv2.imwrite("user_img/emp"+str(count)+".jpg",frame)
            if cv2.waitKey(1)& 0xff==ord('x'):
                break
        cap.release()
        cv2.destroyAllWindows()
        path="user_img/emp"+str(count)+".jpg"
        img20=Image.open("user_img/emp"+str(count)+".jpg")
        img20=img20.resize((240,150))
        img20=ImageTk.PhotoImage(img20)
        l=Label(frm1)
        l.config(image=img20)
        l.image=img20
        l.place(x=0,y=0)
#--------------Uploading a picture from file-----------
    def upload():
        filename=filedialog.askopenfilename(title='open')
        img21=Image.open(filename)
        img21=img21.resize((120,150))
        img21=ImageTk.PhotoImage(img21)
        l=Label(frm1)
        l.config(image=img21)
        l.image=img21
        l.place(x=60,y=0)
        
#---------------camera for gender detecting--------
    def cam_g():
        def g_detect(net, frame):
            global gender1
            frameOpencvDnn=frame.copy()
            frameHeight=frameOpencvDnn.shape[0]
            frameWidth=frameOpencvDnn.shape[1]
            blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123],True,False)

            net.setInput(blob)
            detections=net.forward()
            faceBoxes=[]
            for i in range(detections.shape[2]):
                confidence=detections[0,0,i,2]
                if confidence>0.7:
                    x1=int(detections[0,0,i,3]*frameWidth)
                    y1=int(detections[0,0,i,4]*frameHeight)
                    x2=int(detections[0,0,i,5]*frameWidth)
                    y2=int(detections[0,0,i,6]*frameHeight)
                    faceBoxes.append([x1,y1,x2,y2])
                    cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (155,0,0),2, int(round(frameHeight/150)))
            return frameOpencvDnn,faceBoxes

        parser=argparse.ArgumentParser()
        parser.add_argument('--image')
        args=parser.parse_args()

        faceProto="opencv_face_detector.pbtxt"
        faceModel="opencv_face_detector_uint8.pb"
        genderProto="gender_deploy.prototxt"
        genderModel="gender_net.caffemodel"

        MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
        genderList=['Male','Female']

        faceNet=cv2.dnn.readNet(faceModel,faceProto)
        genderNet=cv2.dnn.readNet(genderModel,genderProto)

        vid=cv2.VideoCapture(0)
        #padding=20

        while True:
            hasFrame,frame=vid.read()
            resultImg,faceBoxes=g_detect(faceNet,frame)

            for faceBox in faceBoxes:
                face=frame[faceBox[1]:faceBox[3],faceBox[0]:faceBox[2]]
                #face=frame[max(0,faceBox[1]-padding):min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding):min(faceBox[2]+padding, frame.shape[1]-1)]
                blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
                genderNet.setInput(blob)
                genderPreds=genderNet.forward()
                gender=genderList[genderPreds[0].argmax()]

                cv2.putText(resultImg, f'{gender}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, cv2.LINE_AA)
                cv2.imshow("Detecting gender", resultImg)
                gender1=gender

            if cv2.waitKey(1)& 0xff==ord('x'):
                break
        vid.release()
        cv2.destroyAllWindows()
        t9.config(state='normal')
        t9.insert(0,gender1)
        t9.config(state='disable')

#-------------Buttons-------------
    img7=Image.open("img/submit.jpg")
    img7=img7.resize((180,57))
    img7=ImageTk.PhotoImage(img7)
    b=Button(t,command=save)
    b.config(image=img7)
    b.image=img7
    b.place(x=1200,y=300)

    img13=Image.open("img/gender.jpg")
    img13=img13.resize((180,57))
    img13=ImageTk.PhotoImage(img13)
    b=Button(t, command=cam_g)
    b.config(image=img13)
    b.image=img13
    b.place(x=1200,y=400)

    img8=Image.open("img/reset.jpg")
    img8=img8.resize((180,57))
    img8=ImageTk.PhotoImage(img8)
    b=Button(t)
    b.config(image=img8, command=reset)
    b.image=img8
    b.place(x=1200,y=500)

    img10=Image.open("img/exit.jpg")
    img10=img10.resize((180,57))
    img10=ImageTk.PhotoImage(img10)
    b=Button(t)
    b.config(image=img10, command=t.destroy)
    b.image=img10
    b.place(x=1200  ,y=600)

    img11=Image.open("img/capture.jpg")
    img11=img11.resize((80,30))
    img11=ImageTk.PhotoImage(img11)
    b=Button(frm)
    b.config(image=img11, command=cam)
    b.image=img11
    b.place(x=420,y=120)

    img12=Image.open("img/upload.jpg")
    img12=img12.resize((80,30))
    img12=ImageTk.PhotoImage(img12)
    b=Button(frm)
    b.config(image=img12, command=upload)
    b.image=img12
    b.place(x=420,y=160)

