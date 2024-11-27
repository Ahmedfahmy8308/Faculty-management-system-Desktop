from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
from firebase_admin import credentials, initialize_app, db
import sys
import subprocess


cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-94cf6.appspot.com"
})
window = Tk()
window.title('Insert New Student')
window.geometry("754x414+340+190")
window.configure(bg = "#FFFFFF")
ref = db.reference('Courses')
def back():
    window.destroy()
    subprocess.run(['python', 'affairs_course.py'])
    sys.exit()
def add_course():
        try:
            coursename = entry_1.get()
            course_data = {
                "course name": entry_1.get(),
                "id": int(entry_2.get()),
                "credit hours":int(entry_3.get()),
                "level": int(entry_4.get()),
                "department": entry_5.get(),

            }
            ref.child(coursename).set(course_data)
            messagebox.showinfo('success', 'Course added successfully')
            window.destroy()
            subprocess.run(['python', 'affairs_course.py'])
            sys.exit()
        except:
            messagebox.showerror('Error', 'can not add course')

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
    file= 'add_course_image/image_1.png')
image_1 = canvas.create_image(
    377.0,
    207.0,
    image=image_image_1
)

canvas.create_text(
    44.0,
    225.0,
    anchor="nw",
    text="Fill course details to add him to \ncollege system ",
    fill="#FFFFFF",
    font=("Perpetua", 16)
)

canvas.create_text(
    27.0,
    106.0,
    anchor="nw",
    text="Insert \nNew Course",
    fill="#FFFFFF",
    font=('Perpetua', 33, 'bold'))

button_image_1 = PhotoImage(
    file="add_course_image/button_1.png")
add = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_course,
    relief="flat"
)
add.place(
    x=452.0,
    y=349.0,
    width=287.0,
    height=49.0
)

canvas.create_text(
    306.0,
    31.0,
    anchor="nw",
    text="Course Name:",
    fill="#FFFFFF",
    font=("perpetua", 19))

canvas.create_text(
    362.0,
    84.0,
    anchor="nw",
    text="ID:",
    fill="#FFFFFF",
    font=("perpetua", 19)
)

canvas.create_text(
    356.0,
    211.0,
    anchor="nw",
    text="Level:",
    fill="#FFFFFF",
    font=("perpetua", 19)

)

canvas.create_text(
    314.0,
    152.0,
    anchor="nw",
    text="Credit Hours:",
    fill="#FFFFFF",
    font=("perpetua", 19)

)

canvas.create_text(
    323.0,
    283.0,
    anchor="nw",
    text="Department:",
    fill="#FFFFFF",
    font=("perpetua", 19)

)

entry_image_1 = PhotoImage(
    file="add_course_image/entry_1.png")
entry_bg_1 = canvas.create_image(
    590.5,
    42.0,
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
    y=22.0,
    width=259.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file="add_course_image/entry_2.png")
entry_bg_2 = canvas.create_image(
    590.5,
    103.0,
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
    y=83.0,
    width=259.0,
    height=38.0
)

entry_image_3 = PhotoImage(
    file="add_course_image/entry_3.png")
entry_bg_3 = canvas.create_image(
    590.5,
    167.0,
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
    y=147.0,
    width=259.0,
    height=38.0
)

entry_image_4 = PhotoImage(
    file="add_course_image/entry_4.png")
entry_bg_4 = canvas.create_image(
    593.5,
    233.0,
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
    y=213.0,
    width=259.0,
    height=38.0
)

entry_image_5 = PhotoImage(
    file="add_course_image/entry_5.png")
entry_bg_5 = canvas.create_image(
    590.5,
    299.0,
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
    x=461.0,
    y=279.0,
    width=259.0,
    height=38.0
)
back_image = PhotoImage(
    file="add_course_image/button_2.png")
back = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
back.place(
    x=69.0,
    y=354.0,
    width=219.0,
    height=44.0
)
window.resizable(False, False)
window.mainloop()
