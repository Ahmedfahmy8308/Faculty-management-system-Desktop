from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import sys
import subprocess


path = os.getcwd()

def student_cliked():
    window.destroy()
    subprocess.run(['python', 'affairs_student.py'])
    sys.exit()

def dotor_cliked():
    window.destroy()
    subprocess.run(['python', 'affairs_doctors.py'])
    sys.exit()

def courses_cliked():
    window.destroy()
    subprocess.run(['python', 'affairs_course.py'])
    sys.exit()






window = Tk()
window.title('Affairs Management System')
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
    file='affairs_image/image_1.png')
image_1 = canvas.create_image(
    640.0,
    350.0,
    image=image_image_1
)

bg_image = PhotoImage(
    file='affairs_image/image_2.png')
image_2 = canvas.create_image(
    628.0,
    350.0,
    image=bg_image
)

courses_image = PhotoImage(
    file='affairs_image/button_1.png')
courses_button = Button(
    image=courses_image,
    borderwidth=0,
    highlightthickness=0,
    command=courses_cliked,
    relief="flat"
)
courses_button.place(
    x=700.0,
    y=464.0,
    width=413.0,
    height=64.0
)

canvas.create_text(
    120.0,
    190.0,
    anchor="nw",
    text="Hi!\nWelcome back to the\nAffairs Management System",
    fill="#FFFFFF",
    font=('Perpetua', 33, 'bold')
)

canvas.create_text(
    126.0,
    367.0,
    anchor="nw",
    text="Go on and click on any button you want to edit its details",
    fill="#FFFFFF",
    font=("Perpetua", 19)
)

student_image = PhotoImage(
    file='affairs_image/button_2.png')
student_button = Button(
    image=student_image,
    borderwidth=0,
    highlightthickness=0,
    command= student_cliked ,
    relief="flat"
)
student_button.place(
    x=685.0,
    y=319.0,
    width=432.0,
    height=63.0
)

doc_image = PhotoImage(
    file='affairs_image/button_3.png')
doc_button = Button(
    image=doc_image,
    borderwidth=0,
    highlightthickness=0,
    command=dotor_cliked,
    relief="flat"
)
doc_button.place(
    x=686.0,
    y=165.0,
    width=432.0,
    height=63.0
)
window.resizable(False, False)
window.mainloop()