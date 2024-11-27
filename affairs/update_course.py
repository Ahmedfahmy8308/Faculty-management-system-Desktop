from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,messagebox
from firebase_admin import credentials, initialize_app, db
import sys
import subprocess

cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-94cf6.appspot.com"
})

ref = db.reference('Courses')


def update_confirm():
    def back1():
        window.destroy()
        subprocess.run(['python', 'affairs_course.py'])
        sys.exit()
    def confirm1():
        try:
            course_data = {
                "course name": entry_1.get(),
                "id": int(entry_2.get()),
                "credit hours": int(entry_3.get()),
                "level": int(entry_4.get()),
                "department": entry_5.get(),

            }
            ref.child(name).set(course_data)
            messagebox.showinfo('success', 'your student updated')
            back1()
        except:
            messagebox.showerror('Error', 'can not add student')
    window = Tk()
    window.title("Updating Course's Data")
    window.geometry("754x414+340+190")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=414,
        width=754,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file='add_course_image/image_1.png')
    image_1 = canvas.create_image(
        377.0,
        207.0,
        image=image_image_1
    )

    canvas.create_text(
        24.0,
        225.0,
        anchor="nw",
        text="Click Confirm to update student’s data\n in the system",
        fill="#FFFFFF",
        font=("Perpetua", 16)
    )

    canvas.create_text(
        18.0,
        120.0,
        anchor="nw",
        text="Course’s Data\nthat can be updated",
        fill="#FFFFFF",
        font=('Perpetua', 26, 'bold')
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
    entry_1.insert(0,coursedata['course name'])

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
    entry_2.insert(0,coursedata['credit hours'])

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
    entry_3.insert(0,coursedata['level'])

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
    entry_4.insert(0,coursedata['level'])

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
    entry_5.insert(0,coursedata['department'])

    back_button = Button(
        bg='#89228A',
        fg='white',
        font=('times', 18, 'italic'),
        text='Back',
        borderwidth=1.5,
        highlightthickness=0,
        command=back1,
        relief="flat"
    )
    back_button.place(
        x=95.0,
        y=350.0,
        width=150.0,
        height=35.0
    )

    confirm_button = Button(
        bg='#89228A',
        fg='white',
        font=('times', 18, 'italic'),
        text='Confirm',
        borderwidth=1.5,
        highlightthickness=0,
        command=confirm1,
        relief="flat"
    )
    confirm_button.place(
        x=515.0,
        y=350.0,
        width=150.0,
        height=35.0
    )

    window.resizable(False, False)
    window.mainloop()


def back():
    window.destroy()
    subprocess.run(['python', 'affairs_course.py'])
    sys.exit()

def confirm():
    global coursedata, name
    name = entry_1.get()
    if name == "":
        messagebox.showerror('Error', 'Enter name')
    else:
        try:
            coursedata = db.reference(f'Courses/{name}').get()
        except:
            pass
        if not coursedata:
            messagebox.showerror('Error', 'invalid name')
        if coursedata:
            window.destroy()
            update_confirm()





window = Tk()
window.title('Course ID to Update')
window.geometry("517x403+470+200")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 403,
    width = 517,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file='update_course_image/image_1.png')
image_1 = canvas.create_image(
    259.0,
    219.0,
    image=image_image_1
)

canvas.create_text(
    34.0,
    148.0,
    anchor="nw",
    text="Enter course’s Name :",
    fill="#FFFFFF",
    font=("perpetua", 22)
)

canvas.create_text(
    19.0,
    18.0,
    anchor="nw",
    text="Update Course’s Data in\n our System",
    fill="#FFFFFF",
    font=("Perpetua", 30, 'bold')
)


entry_image_1 = PhotoImage(
    file=("update_course_image/entry_1.png"))
entry_bg_1 = canvas.create_image(
    162.5,
    211.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font= ("perpetua", 14)
)
entry_1.place(
    x=46.0,
    y=191.0,
    width=233.0,
    height=38.0
)


back_image = PhotoImage(
    file="update_course_image/button_1.png")
back_button = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back ,
    relief="flat"
)
back_button.place(
    x=40.0,
    y=293.0,
    width=208.0,
    height=51.0
)

search_image = PhotoImage(
    file="update_course_image/button_2.png")
search_button = Button(
    image=search_image,
    borderwidth=0,
    highlightthickness=0,
    command=confirm,
    relief="flat"
)
search_button.place(
    x=276.0,
    y=300.0,
    width=206.1134033203125,
    height=44.0
)

window.resizable(False, False)
window.mainloop()
