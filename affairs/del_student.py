from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,messagebox
from firebase_admin import credentials, initialize_app, db ,storage
import os
import  sys
import subprocess


cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-94cf6.appspot.com"
})

path = os.getcwd()
path = path.split('affairs')[0]


def conf_del():
    def back1():
        window.destroy()
        subprocess.run(['python', 'affairs_student.py'])
        sys.exit()
    def yes():
        ref = db.reference(f'Students/{id}')
        ref.delete()
        os.remove(f'{path}/images/{id}.png')

        bucket = storage.bucket()
        blob = bucket.blob(f'images/{id}.png')
        blob.delete()
        messagebox.showinfo('Success','Student deleted successfully')
        back1()
    def no():
        back1()

    window = Tk()
    window.title('Confirm to Delete Student')
    window.geometry("530x422+480+170")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=422,
        width=530,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file="conf_del_student_image/image_1.png")
    image_1 = canvas.create_image(
        265.0,
        211.0,
        image=image_image_1
    )

    canvas.create_text(
        102.0,
        73.0,
        anchor="nw",
        text="Name:",
        fill="#FFFFFF",
        font=("perpetua", 19)
    )

    canvas.create_text(
        46.0,
        306.0,
        anchor="nw",
        text="Are you sure you want to delete this\nstudent?!",
        fill="#FFFFFF",
        font=("perpetua", 22))

    canvas.create_text(
        110.0,
        165.0,
        anchor="nw",
        text="Level:",
        fill="#FFFFFF",
        font=("perpetua", 19)
    )

    canvas.create_text(
        115.0,
        210.0,
        anchor="nw",
        text="GPA:",
        fill="#FFFFFF",
        font=("perpetua", 19)
    )

    canvas.create_text(
        56.0,
        258.0,
        anchor="nw",
        text="Departement:",
        fill="#FFFFFF",
        font=("perpetua", 19)
    )

    canvas.create_text(
        102.0,
        118.0,
        anchor="nw",
        text="E-mail:",
        fill="#FFFFFF",
        font=("perpetua", 19)
    )

    button_image_1 = PhotoImage(
        file="conf_del_student_image/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=yes,
        relief="flat"
    )
    button_1.place(
        x=66.0,
        y=372.0,
        width=199.0,
        height=37.0
    )

    button_image_2 = PhotoImage(
        file="conf_del_student_image/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=no,
        relief="flat"
    )
    button_2.place(
        x=277.0,
        y=373.0,
        width=199.0,
        height=36.0
    )

    canvas.create_text(
        20.0,
        13.0,
        anchor="nw",
        text="Student’s Data",
        fill="#FFFFFF",
        font=("Perpetua", 30, 'bold')
    )

    entry_image_1 = PhotoImage(
        file="conf_del_student_image/entry_1.png")
    entry_bg_1 = canvas.create_image(
        344.5,
        84.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("rockwell", 12)
    )
    entry_1.insert(0,studentdata['name'])
    entry_1.place(
        x=215.0,
        y=68.0,
        width=259.0,
        height=37.0
    )

    entry_image_2 = PhotoImage(
        file="conf_del_student_image/entry_2.png")
    entry_bg_2 = canvas.create_image(
        344.5,
        131.5,
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
        x=215.0,
        y=115.0,
        width=259.0,
        height=37.0
    )
    entry_2.insert(0,studentdata['email'])

    entry_image_3 = PhotoImage(
        file="conf_del_student_image/entry_3.png")
    entry_bg_3 = canvas.create_image(
        344.5,
        178.5,
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
        x=215.0,
        y=162.0,
        width=259.0,
        height=37.0
    )
    entry_3.insert(0,studentdata['level'])

    entry_image_4 = PhotoImage(
        file="conf_del_student_image/entry_4.png")
    entry_bg_4 = canvas.create_image(
        344.5,
        225.5,
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
        x=215.0,
        y=209.0,
        width=259.0,
        height=37.0
    )
    entry_4.insert(0,studentdata['gpa'])

    entry_image_5 = PhotoImage(
        file="conf_del_student_image/entry_5.png")
    entry_bg_5 = canvas.create_image(
        344.5,
        275.5,
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
        x=215.0,
        y=259.0,
        width=259.0,
        height=37.0
    )
    entry_5.insert(0,studentdata['department'])

    window.mainloop()


def confirm():
    global studentdata, id
    id = entry_1.get()
    if id == "":
        messagebox.showerror('Error', 'Enter id')
    else:
        try:
            studentdata = db.reference(f'Students/{id}').get()
        except:
            pass
        if not studentdata:
            messagebox.showerror('Error', 'invalid id')
        if studentdata:
            window.destroy()
            conf_del()

def back():
    window.destroy()
    subprocess.run(['python', 'affairs_student.py'])
    sys.exit()


window = Tk()
window.title('Student ID to Delete')
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
    file="del_student_image/image_1.png")
image_1 = canvas.create_image(
    259.0,
    219.0,
    image=image_image_1
)

canvas.create_text(
    34.0,
    148.0,
    anchor="nw",
    text="Enter Student’s ID :",
    fill="#FFFFFF",
    font=("Perpetua", 20 )
)

canvas.create_text(
    19.0,
    18.0,
    anchor="nw",
    text="Delete Student from \nour System",
    fill="#FFFFFF",
    font=("Perpetua", 30 , 'bold')
)

entry_image_1 = PhotoImage(
    file="del_student_image/entry_1.png")
entry_bg_1 = canvas.create_image(
    159.0,
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
    width=226.0,
    height=38.0
)
confirm_image = PhotoImage(
    file="del_student_image/button_2.png")
confirm_button = Button(
    image=confirm_image,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
confirm_button.place(
    x=34.0,
    y=304.0,
    width=215.0,
    height=57.0
)

back_image = PhotoImage(
    file="del_student_image/button_1.png")
back_button = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=confirm,
    relief="flat"
)
back_button.place(
    x=274.0,
    y=311.0,
    width=206.1134033203125,
    height=44.0
)
window.resizable(False, False)
window.mainloop()
