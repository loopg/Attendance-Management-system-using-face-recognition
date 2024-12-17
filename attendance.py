# import tkinter as tk
# from tkinter import *
# import os,cv2
# import shutil
# import csv
# import numpy as np
# from PIL import ImageTk, Image
# import pandas as pd
# import datetime
# import time
# import tkinter.font as font
# import pyttsx3 

# # project module
# import show_attendance
# import takeImage
# import trainImage
# import automaticAttedance

# # engine = pyttsx3.init()
# # engine.say("Welcome!")
# # engine.say("Please browse through your options..")
# # engine.runAndWait()


# def text_to_speech(user_text):
#     engine = pyttsx3.init()
#     engine.say(user_text)
#     engine.runAndWait()


# haarcasecade_path = "haarcascade_frontalface_default.xml"
# trainimagelabel_path = (
#     "/TrainingImageLabel/Trainner.yml"
# )
# trainimage_path = "TrainingImage"
# if not os.path.exists(trainimage_path):
#     os.makedirs(trainimage_path)

# studentdetail_path = (
#     "/StudentDetails/studentdetails.csv"
# )
# attendance_path = "Attendance"


# window = Tk()
# window.title("Face recognizer")
# window.geometry("1280x720")
# dialog_title = "QUIT"
# dialog_text = "Are you sure want to close?"
# window.configure(background="black")


# # to destroy screen
# def del_sc1():
#     sc1.destroy()


# # error message for name and no
# def err_screen():
#     global sc1
#     sc1 = tk.Tk()
#     sc1.geometry("400x110")
#     sc1.iconbitmap("AMS.ico")
#     sc1.title("Warning!!")
#     sc1.configure(background="black")
#     sc1.resizable(0, 0)
#     tk.Label(
#         sc1,
#         text="Enrollment & Name required!!!",
#         fg="yellow",
#         bg="black",
#         font=("times", 20, " bold "),
#     ).pack()
#     tk.Button(
#         sc1,
#         text="OK",
#         command=del_sc1,
#         fg="yellow",
#         bg="black",
#         width=9,
#         height=1,
#         activebackground="Red",
#         font=("times", 20, " bold "),
#     ).place(x=110, y=50)


# def testVal(inStr, acttyp):
#     if acttyp == "1":  # insert
#         if not inStr.isdigit():
#             return False
#     return True


# logo = Image.open("UI_Image/0001.png")
# logo = logo.resize((50, 47), Image.Resampling.LANCZOS)
# logo1 = ImageTk.PhotoImage(logo)
# titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
# titl.pack(fill=X)
# l1 = tk.Label(window, image=logo1, bg="black",)
# l1.place(x=470, y=10)

# titl = tk.Label(
#     window, text="Smart College!!", bg="black", fg="green", font=("arial", 27),
# )
# titl.place(x=525, y=12)

# a = tk.Label(
#     window,
#     text="Welcome to the Face Recognition Based\nAttendance Management System",
#     bg="black",
#     fg="yellow",
#     bd=10,
#     font=("arial", 35),
# )
# a.pack()

# ri = Image.open("UI_Image/register.png")
# r = ImageTk.PhotoImage(ri)
# label1 = Label(window, image=r)
# label1.image = r
# label1.place(x=100, y=270)

# ai = Image.open("UI_Image/attendance.png")
# a = ImageTk.PhotoImage(ai)
# label2 = Label(window, image=a)
# label2.image = a
# label2.place(x=980, y=270)

# vi = Image.open("UI_Image/verifyy.png")
# v = ImageTk.PhotoImage(vi)
# label3 = Label(window, image=v)
# label3.image = v
# label3.place(x=600, y=270)


# def TakeImageUI():
#     ImageUI = Tk()
#     ImageUI.title("Take Student Image..")
#     ImageUI.geometry("780x480")
#     ImageUI.configure(background="black")
#     ImageUI.resizable(0, 0)
#     titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
#     titl.pack(fill=X)
#     # image and title
#     titl = tk.Label(
#         ImageUI, text="Register Your Face", bg="black", fg="green", font=("arial", 30),
#     )
#     titl.place(x=270, y=12)

#     # heading
#     a = tk.Label(
#         ImageUI,
#         text="Enter the details",
#         bg="black",
#         fg="yellow",
#         bd=10,
#         font=("arial", 24),
#     )
#     a.place(x=280, y=75)

#     # ER no
#     lbl1 = tk.Label(
#         ImageUI,
#         text="Enrollment No",
#         width=10,
#         height=2,
#         bg="black",
#         fg="yellow",
#         bd=5,
#         relief=RIDGE,
#         font=("times new roman", 12),
#     )
#     lbl1.place(x=120, y=130)
#     txt1 = tk.Entry(
#         ImageUI,
#         width=17,
#         bd=5,
#         validate="key",
#         bg="black",
#         fg="yellow",
#         relief=RIDGE,
#         font=("times", 25, "bold"),
#     )
#     txt1.place(x=250, y=130)
#     txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

#     # name
#     lbl2 = tk.Label(
#         ImageUI,
#         text="Name",
#         width=10,
#         height=2,
#         bg="black",
#         fg="yellow",
#         bd=5,
#         relief=RIDGE,
#         font=("times new roman", 12),
#     )
#     lbl2.place(x=120, y=200)
#     txt2 = tk.Entry(
#         ImageUI,
#         width=17,
#         bd=5,
#         bg="black",
#         fg="yellow",
#         relief=RIDGE,
#         font=("times", 25, "bold"),
#     )
#     txt2.place(x=250, y=200)

#     lbl3 = tk.Label(
#         ImageUI,
#         text="Notification",
#         width=10,
#         height=2,
#         bg="black",
#         fg="yellow",
#         bd=5,
#         relief=RIDGE,
#         font=("times new roman", 12),
#     )
#     lbl3.place(x=120, y=270)

#     message = tk.Label(
#         ImageUI,
#         text="",
#         width=32,
#         height=2,
#         bd=5,
#         bg="black",
#         fg="yellow",
#         relief=RIDGE,
#         font=("times", 12, "bold"),
#     )
#     message.place(x=250, y=270)

#     def take_image():
#         l1 = txt1.get()
#         l2 = txt2.get()
#         takeImage.TakeImage(
#             l1,
#             l2,
#             haarcasecade_path,
#             trainimage_path,
#             message,
#             err_screen,
#             text_to_speech,
#         )
#         txt1.delete(0, "end")
#         txt2.delete(0, "end")

#     # take Image button
#     # image
#     takeImg = tk.Button(
#         ImageUI,
#         text="Take Image",
#         command=take_image,
#         bd=10,
#         font=("times new roman", 18),
#         bg="black",
#         fg="yellow",
#         height=2,
#         width=12,
#         relief=RIDGE,
#     )
#     takeImg.place(x=130, y=350)

#     def train_image():
#         trainImage.TrainImage(
#             haarcasecade_path,
#             trainimage_path,
#             trainimagelabel_path,
#             message,
#             text_to_speech,
#         )

#     # train Image function call
#     trainImg = tk.Button(
#         ImageUI,
#         text="Train Image",
#         command=train_image,
#         bd=10,
#         font=("times new roman", 18),
#         bg="black",
#         fg="yellow",
#         height=2,
#         width=12,
#         relief=RIDGE,
#     )
#     trainImg.place(x=360, y=350)


# r = tk.Button(
#     window,
#     text="Register a new student",
#     command=TakeImageUI,
#     bd=10,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=100, y=520)


# def automatic_attedance():
#     automaticAttedance.subjectChoose(text_to_speech)


# r = tk.Button(
#     window,
#     text="Take Attendance",
#     command=automatic_attedance,
#     bd=10,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=600, y=520)


# def view_attendance():
#     show_attendance.subjectchoose(text_to_speech)


# r = tk.Button(
#     window,
#     text="View Attendance",
#     command=view_attendance,
#     bd=10,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=1000, y=520)
# r = tk.Button(
#     window,
#     text="EXIT",
#     bd=10,
#     command=quit,
#     font=("times new roman", 16),
#     bg="black",
#     fg="yellow",
#     height=2,
#     width=17,
# )
# r.place(x=600, y=660)

# window.mainloop()



import tkinter as tk
from tkinter import *
import os, cv2
import pyttsx3
from PIL import ImageTk, Image
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# Function for text-to-speech
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# Paths
haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "TrainingImageLabel/Trainner.yml"
trainimage_path = "TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)
studentdetail_path = "StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

# Initialize main window
window = Tk()
window.title("Face Recognition Attendance System")
window.geometry("1280x720")
window.configure(bg="#f0f5f9")  # Light grey-blue background

# Header Styling
header = tk.Label(window, text="Smart Attendance System", 
                  bg="#2f5597", fg="white", font=("Helvetica", 28, "bold"), 
                  relief=RAISED, bd=5, pady=10)
header.pack(fill=X)

# Helper functions
def del_sc1():
    sc1.destroy()

def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.title("Warning")
    sc1.configure(bg="#f7d7d7")
    tk.Label(sc1, text="Enrollment & Name required!", fg="red", bg="#f7d7d7", font=("Helvetica", 14, "bold")).pack()
    tk.Button(sc1, text="OK", command=del_sc1, bg="#d9534f", fg="white", font=("Helvetica", 12)).place(x=150, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1" and not inStr.isdigit():
        return False
    return True

# Button Styling
def style_button(text, command, x, y):
    return tk.Button(window, text=text, command=command, 
                     font=("Helvetica", 14, "bold"), bg="#007bff", fg="white", 
                     activebackground="#0056b3", activeforeground="white",
                     width=20, height=2, relief=RAISED, bd=4).place(x=x, y=y)

# Logo
logo = Image.open("UI_Image/0001.png").resize((60, 60), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
tk.Label(window, image=logo1, bg="#f0f5f9").place(x=10, y=10)

# Main UI Images
images = {"register": "UI_Image/register.png", "attendance": "UI_Image/attendance.png", "verify": "UI_Image/verifyy.png"}
positions = {"register": (150, 250), "attendance": (950, 250), "verify": (550, 250)}

for key, path in images.items():
    img = ImageTk.PhotoImage(Image.open(path).resize((200, 200), Image.LANCZOS))
    tk.Label(window, image=img, bg="#f0f5f9").place(x=positions[key][0], y=positions[key][1])
    window.__dict__[f"{key}_img"] = img  # Prevent garbage collection

# Buttons
style_button("Register Student", lambda: TakeImageUI(), 150, 500)
style_button("Take Attendance", lambda: automatic_attedance(), 550, 500)
style_button("View Attendance", lambda: view_attendance(), 950, 500)
style_button("Exit", window.quit, 550, 620)

# Register UI
def TakeImageUI():
    image_ui = Toplevel(window)
    image_ui.title("Register Student")
    image_ui.geometry("600x400")
    image_ui.configure(bg="#f0f5f9")

    tk.Label(image_ui, text="Register Face", bg="#2f5597", fg="white",
             font=("Helvetica", 20, "bold"), pady=10).pack(fill=X)

    tk.Label(image_ui, text="Enrollment No:", bg="#f0f5f9", font=("Helvetica", 14)).place(x=50, y=100)
    txt1 = tk.Entry(image_ui, bg="#e6f7ff", font=("Helvetica", 14), width=20)
    txt1.place(x=200, y=100)

    tk.Label(image_ui, text="Name:", bg="#f0f5f9", font=("Helvetica", 14)).place(x=50, y=150)
    txt2 = tk.Entry(image_ui, bg="#e6f7ff", font=("Helvetica", 14), width=20)
    txt2.place(x=200, y=150)

    message = tk.Label(image_ui, text="", bg="#f0f5f9", fg="green", font=("Helvetica", 12, "italic"))
    message.place(x=200, y=200)

    def take_image():
        takeImage.TakeImage(txt1.get(), txt2.get(), haarcasecade_path, trainimage_path, message, err_screen, text_to_speech)
        txt1.delete(0, END)
        txt2.delete(0, END)

    def train_image():
        trainImage.TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message, text_to_speech)

    tk.Button(image_ui, text="Capture Image", command=take_image, bg="#28a745", fg="white", font=("Helvetica", 14), width=15).place(x=100, y=250)
    tk.Button(image_ui, text="Train Model", command=train_image, bg="#ffc107", fg="white", font=("Helvetica", 14), width=15).place(x=300, y=250)

# Function bindings
def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

window.mainloop()
