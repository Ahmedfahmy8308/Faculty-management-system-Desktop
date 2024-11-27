from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
from firebase_admin import credentials, initialize_app, db
import os
import sys
import subprocess



cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-94cf6.appspot.com"
})

path = os.getcwd()
path = path.split('affairs')[0]


ref = db.reference('Doctors')






def back():
    window.destroy()
    subprocess.run(['python', 'affairs_doctors.py'])
    sys.exit()

def add_doctor():
    try:
        username = entry_3.get()
        doctor_data = {
            "name": entry_1 .get(),
            "id": int(entry_2.get()),
            "username": entry_3.get(),
            "email": entry_4.get(),
            "password": entry_5.get(),
        }
        ref.child(username).set(doctor_data)
        messagebox.showinfo('success','Doctor added successfully')
        window.destroy()
        subprocess.run(['python', 'affairs_doctors.py'])
        sys.exit()
    except:
        messagebox.showerror('Error', 'can not add doctor')

window = Tk()
window.title('Insert New Doctor')
window.geometry("754x414+300+150")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 414,
    width = 754,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file="add_doc_image/image_1.png")
image_1 = canvas.create_image(
    377.0,
    207.0,
    image=image_image_1
)

canvas.create_text(
    44.0,
    225.0,
    anchor="nw",
    text="Fill doctor details to add him to \ncollege system",
    fill="#FFFFFF",
    font=("Perpetua", 16)
)

canvas.create_text(
    41.0,
    90.0,
    anchor="nw",
    text="Insert \nNew Doctor",
    fill="#FFFFFF",
    font=('Perpetua', 33, 'bold')
)

button_image_1 = PhotoImage(
    file="add_doc_image/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_doctor,
    relief="flat"
)
button_1.place(
    x=452.0,
    y=349.0,
    width=287.0,
    height=49.0
)

canvas.create_text(
    353.0,
    31.0,
    anchor="nw",
    text="Name:",
    fill="#FFFFFF",
    font=("perpetua", 19)
)

canvas.create_text(
    332.0,
    154.0,
    anchor="nw",
    text="Username:",
    fill="#FFFFFF",
    font=("perpetua", 19)
)

canvas.create_text(
    332.0,
    289.0,
    anchor="nw",
    text="Password:",
    fill="#FFFFFF",
    font=("perpetua", 19)
)

canvas.create_text(
    377.0,
    95.0,
    anchor="nw",
    text="ID:",
    fill="#FFFFFF",
    font=("perpetua", 19)
)

canvas.create_text(
    359.0,
    227.0,
    anchor="nw",
    text="E-mail:",
    fill="#FFFFFF",
    font=("perpetua", 19)
)

entry_image_1 = PhotoImage(
    file="add_doc_image/entry_1.png")
entry_bg_1 = canvas.create_image(
    590.5,
    42.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("rockwell", 12)
)
entry_1.place(
    x=461.0,
    y=25.0,
    width=259.0,
    height=37.0
)

entry_image_2 = PhotoImage(
    file="add_doc_image/entry_2.png")
entry_bg_2 = canvas.create_image(
    590.5,
    106.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("rockwell", 12)
)
entry_2.place(
    x=461.0,
    y=89.0,
    width=259.0,
    height=37.0
)

entry_image_3 = PhotoImage(
    file="add_doc_image/entry_3.png")
entry_bg_3 = canvas.create_image(
    590.5,
    170.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("rockwell", 12)
)
entry_3.place(
    x=461.0,
    y=153.0,
    width=259.0,
    height=37.0
)

entry_image_4 = PhotoImage(
    file="add_doc_image/entry_4.png")
entry_bg_4 = canvas.create_image(
    593.5,
    238.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("rockwell", 12)
)
entry_4.place(
    x=464.0,
    y=221.0,
    width=259.0,
    height=37.0
)

entry_image_5 = PhotoImage(
    file="add_doc_image/entry_5.png")
entry_bg_5 = canvas.create_image(
    592.5,
    300.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("rockwell", 12)
)
entry_5.place(
    x=463.0,
    y=283.0,
    width=259.0,
    height=37.0
)

back_image = PhotoImage(
    file="add_doc_image/button_2.png")
back_button = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
back_button.place(
    x=83.0,
    y=352.0,
    width=249.0,
    height=36.0
)
window.resizable(False, False)
window.mainloop()
