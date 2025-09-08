from tkinter import *
from PIL import ImageTk, Image
import cv2
import time
import os
import mysql.connector
from datetime import datetime

def mark():
    t = Toplevel()
    t.geometry("1920x1200")
    t.title("Mark Attendance")

    #--------Background Image---------
    try:
        img11 = Image.open("img/mark_bg.jpg")
        img11 = img11.resize((1533, 790))
        img11 = ImageTk.PhotoImage(img11)
        l = Label(t, image=img11)
        l.image = img11
        l.place(x=0, y=0)
    except Exception as e:
        print("Error loading background:", e)

    #----------Frame for Captured Image-------
    frm1 = Frame(t, bg="silver")
    frm1.place(x=80, y=125, width=550, height=380)

    cam_label = Label(frm1)
    cam_label.pack()

    #---------Label to show QR code data---------
    qr_msg = StringVar()
    qr_msg.set("Scan a QR Code...")
    qr_label = Label(t, textvariable=qr_msg, font=("Arial", 16), fg="green", bg="white")
    qr_label.place(x=700, y=450)

    #------------Camera and QR Logic------------
    cap = cv2.VideoCapture(0)
    qr_detector = cv2.QRCodeDetector()
    current_frame = [None]
    captured_once = [False]
    captured_filename = [None]
    is_updating = [True]
    last_qr_data = [""]  # ✅ Store actual QR content

    os.makedirs("Captured", exist_ok=True)

    def update_frame():
        if not is_updating[0] or captured_once[0]:
            return

        ret, frame = cap.read()
        if ret:
            current_frame[0] = frame.copy()
            data, bbox, _ = qr_detector.detectAndDecode(frame)
            if data:
                last_qr_data[0] = data.strip()  # ✅ Store QR code
                qr_msg.set(f"QR Code Detected: {data}")
            else:
                qr_msg.set("Scan a QR Code...")

            # Show camera frame
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            img = img.resize((550, 380))
            imgtk = ImageTk.PhotoImage(image=img)
            cam_label.imgtk = imgtk
            cam_label.configure(image=imgtk)

        cam_label.after(10, update_frame)

    def capture_image():
        if current_frame[0] is not None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"Captured/attendance_{timestamp}.jpg"
            try:
                cv2.imwrite(filename, current_frame[0])
                captured_once[0] = True
                captured_filename[0] = filename
                mark_btn.config(state=DISABLED)
                is_updating[0] = False
                if cap.isOpened():
                    cap.release()

                # ✅ Get QR name data
                qr_data = last_qr_data[0].strip()
                now = datetime.now()

                if qr_data:
                    # ✅ Save to MySQL
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="attendance_db"
                    )
                    cursor = conn.cursor()

                    # Optional auto-create
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS records (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            datetime DATETIME
                        )
                    """)

                    insert_query = "INSERT INTO records (name, datetime) VALUES (%s, %s)"
                    cursor.execute(insert_query, (qr_data, now))
                    conn.commit()
                    cursor.close()
                    conn.close()

                    qr_msg.set(f"Attendance marked:\n{qr_data} at {now.strftime('%Y-%m-%d %H:%M:%S')}")
                    print("Saved:", qr_data, now)
                else:
                    qr_msg.set("QR data not found. Try again.")
            except Exception as e:
                qr_msg.set(f"Error: {e}")
        else:
            qr_msg.set("No image to capture!")

    def retake_image():
        if captured_once[0]:
            captured_once[0] = False
            mark_btn.config(state=NORMAL)
            if captured_filename[0] and os.path.exists(captured_filename[0]):
                os.remove(captured_filename[0])
                qr_msg.set("Previous image deleted. Ready to recapture.")
            else:
                qr_msg.set("Ready to recapture.")

            if not cap.isOpened():
                cap.open(0)
            is_updating[0] = True
            update_frame()

    def on_closing():
        if cap.isOpened():
            cap.release()
        t.destroy()

    t.protocol("WM_DELETE_WINDOW", on_closing)

    update_frame()

    #------------Buttons--------------
    retake_img = Image.open("img/retake.jpg").resize((180, 45))
    retake_img = ImageTk.PhotoImage(retake_img)
    retake_btn = Button(t, image=retake_img, command=retake_image)
    retake_btn.image = retake_img
    retake_btn.place(x=160, y=530)

    mark_img = Image.open("img/mark.jpg").resize((180, 45))
    mark_img = ImageTk.PhotoImage(mark_img)
    mark_btn = Button(t, image=mark_img, command=capture_image)
    mark_btn.image = mark_img
    mark_btn.place(x=360, y=530)

    exit_img = Image.open("img/exit.jpg").resize((180, 45))
    exit_img = ImageTk.PhotoImage(exit_img)
    exit_btn = Button(t, image=exit_img, command=lambda: [cap.release() if cap.isOpened() else None, t.destroy()])
    exit_btn.image = exit_img
    exit_btn.place(x=260, y=600)
