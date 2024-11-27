from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys
import subprocess

def insert():
    window.destroy()
    subprocess.run(['python', 'add_course.py'])
    sys.exit()
def delete():
    window.destroy()
    subprocess.run(['python', 'delete_course.py'])
    sys.exit()

def update ():
    window.destroy()
    subprocess.run(['python', 'update_course.py'])
    sys.exit()
def back():
    window.destroy()
    subprocess.run(['python', 'affairs_gui.py'])
    sys.exit()

window = Tk()
window.title('Course Management System')
window.geometry("1280x700+100+50")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file='Affairs_course_image/image_1.png')
image_1 = canvas.create_image(
    640.0,
    350.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file="Affairs_course_image/image_2.png")
image_2 = canvas.create_image(
    650.0,
    341.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file="Affairs_course_image/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=update,
    relief="flat"
)
button_1.place(
    x=721.0,
    y=467.0,
    width=413.0,
    height=64.0
)

button_image_2 = PhotoImage(
    file="Affairs_course_image/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=delete,
    relief="flat"
)
button_2.place(
    x=708.0,
    y=310.0,
    width=432.0,
    height=63.0
)

button_image_3 = PhotoImage(
    file="Affairs_course_image/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=insert,
    relief="flat"
)
button_3.place(
    x=702.0,
    y=153.0,
    width=432.0,
    height=63.0
)

canvas.create_text(
    139.0,
    312.0,
    anchor="nw",
    text="You can insert, delete, and update specific course’s details or \nsearch for any details you want",
    fill="#FFFFFF",
    font=("Perpetua", 19))

canvas.create_text(
    135.0,
    175.0,
    anchor="nw",
    text="Course\nManagement Section",
    fill="#FFFFFF",
    font=("Perpetua", 34, 'bold')
)
back_image = PhotoImage(
    file="Affairs_course_image/button_4.png")
back_button = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
back_button.place(
    x=241.0,
    y=476.0,
    width=233.0,
    height=63.0
)

window.resizable(False, False)
window.mainloop()
