from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
from firebase_admin import credentials, initialize_app, db , storage
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


ref = db.reference('Students')


def update_confirm():

    def back1():
        window.destroy()
        subprocess.run(['python', 'affairs_student.py'])
        sys.exit()
    def confirm1():
        try:
            student_data = {
                "name": entry_1.get(),
                "id":entry_2.get(),
                "email": entry_3.get(),
                "level":entry_4.get(),
            "department": entry_5.get() ,
            "gpa": entry_6.get(),
            "gender": entry_7.get(),
            }
            ref.child(id).set(student_data)
            messagebox.showinfo('success', 'your student updated')
            back1()
        except:
            messagebox.showerror('Error', 'can not update student')

    window = Tk()
    window.title("Updating Student's Data")
    window.geometry("832x474+340+190")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=484,
        width=832,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file='add_stu_image/image_1.png')
    image_1 = canvas.create_image(
        416.0,
        245.0,
        image=image_image_1
    )

    canvas.create_text(
        44.0,
        225.0,
        anchor="nw",
        text="Click Confirm to update student’s data\n in the system",
        fill="#FFFFFF",
        font=("Perpetua", 16)
    )

    canvas.create_text(
        41.0,
        112.0,
        anchor="nw",
        text="Student’s Data\nthat can be updated",
        fill="#FFFFFF",
        font=('Perpetua', 29, 'bold')
    )

    canvas.create_text(
        394.0,
        32.0,
        anchor="nw",
        text="Name:",
        fill="#FFFFFF",
        font=("perpetua", 19))

    canvas.create_text(
        418.0,
        84.0,
        anchor="nw",
        text="ID:",
        fill="#FFFFFF",
        font=("perpetua", 19))

    canvas.create_text(
        394.0,
        187.0,
        anchor="nw",
        text="Level:",
        fill="#FFFFFF",
        font=("perpetua", 19))

    canvas.create_text(
        402.0,
        287.0,
        anchor="nw",
        text="GPA:",
        fill="#FFFFFF",
        font=("perpetua", 19))

    canvas.create_text(
        387.0,
        337.0,
        anchor="nw",
        text="Gender:",
        fill="#FFFFFF",
        font=("perpetua", 19)
    )

    canvas.create_text(
        370.0,
        235.0,
        anchor="nw",
        text="Department:",
        fill="#FFFFFF",
        font=("perpetua", 19)
    )

    canvas.create_text(
        393.0,
        134.0,
        anchor="nw",
        text="E-mail:",
        fill="#FFFFFF",
        font=("perpetua", 19))

    entry_image_1 = PhotoImage(
        file='add_stu_image/entry_1.png')
    entry_bg_1 = canvas.create_image(
        630.5,
        46.5,
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
        x=501.0,
        y=29.0,
        width=259.0,
        height=37.0
    )
    entry_1.insert(0,studentdata['name'])

    entry_image_2 = PhotoImage(
        file='add_stu_image/entry_2.png')
    entry_bg_2 = canvas.create_image(
        628.5,
        95.5,
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
        x=499.0,
        y=79.0,
        width=259.0,
        height=37.0
    )
    entry_2.insert(0,studentdata['id'])


    entry_image_3 = PhotoImage(
        file='add_stu_image/entry_3.png')
    entry_bg_3 = canvas.create_image(
        628.5,
        144.5,
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
        x=499.0,
        y=128.0,
        width=259.0,
        height=37.0
    )
    entry_3.insert(0,studentdata['email'])

    entry_image_4 = PhotoImage(
        file='add_stu_image/entry_4.png')
    entry_bg_4 = canvas.create_image(
        628.5,
        196.5,
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
        x=499.0,
        y=179.0,
        width=259.0,
        height=37.0
    )
    entry_4.insert(0,studentdata['level'])

    entry_image_5 = PhotoImage(
        file='add_stu_image/entry_5.png')
    entry_bg_5 = canvas.create_image(
        629.5,
        246.5,
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
        x=500.0,
        y=229.0,
        width=259.0,
        height=37.0
    )
    entry_5.insert(0,studentdata['department'])

    entry_image_6 = PhotoImage(
        file='add_stu_image/entry_6.png')
    entry_bg_6 = canvas.create_image(
        630.5,
        295.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("rockwell", 12)
    )
    entry_6.place(
        x=501.0,
        y=279.0,
        width=259.0,
        height=37.0
    )
    entry_6.insert(0,studentdata['gpa'])

    entry_image_7 = PhotoImage(
        file='add_stu_image/entry_7.png')
    entry_bg_7 = canvas.create_image(
        630.5,
        345.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("rockwell", 12)
    )
    entry_7.place(
        x=500.0,
        y=329.0,
        width=261.0,
        height=37.0
    )
    entry_7.insert(0,studentdata['gender'])

    button_1 = Button(
        bg='#89228A',
        fg='white',
        font=('times', 18, 'italic'),
        text='Back',
        borderwidth=1.5,
        highlightthickness=0,
        command=back1,
        relief="flat"
    )
    button_1.place(
        x=95.0,
        y=403.0,
        width=150.0,
        height=45.0
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
        x=555.0,
        y=400.0,
        width=150.0,
        height=45.0
    )

    window.mainloop()

def confirm ():
    global studentdata , id
    id = entry_1.get()
    if id =="":
        messagebox.showerror('Error', 'Enter id')
    else:
        try :
            studentdata = db.reference(f'Students/{id}').get()
        except :
            pass
        if not studentdata :
            messagebox.showerror('Error' , 'invalid id')
        if studentdata :
            window.destroy()
            update_confirm()


def back():
    window.destroy()
    subprocess.run(['python', 'affairs_student.py'])
    sys.exit()






window = Tk()

window.title('Student ID to Update')
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
    file="id_update_student_image/image_1.png")
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
    font=("perpetua", 22)
)

canvas.create_text(
    19.0,
    18.0,
    anchor="nw",
    text="Update Student’s Data in\nour System",
    fill="#FFFFFF",
    font=("Perpetua", 30, 'bold')
)

entry_image_1 = PhotoImage(
    file="id_update_student_image/entry_1.png")
entry_bg_1 = canvas.create_image(
    159.0,
    211.5,
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
    y=194.0,
    width=226.0,
    height=37.0
)
back_image = PhotoImage(
    file=("id_update_student_image/button_1.png"))
back_button = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
back_button.place(
    x=40.0,
    y=303.0,
    width=208.0,
    height=47.0
)

search_image = PhotoImage(
    file=("id_update_student_image/button_2.png"))
search_button = Button(
    image=search_image,
    borderwidth=0,
    highlightthickness=0,
    command=confirm,
    relief="flat"
)
search_button.place(
    x=276.0,
    y=306.0,
    width=206.1134033203125,
    height=44.0
)
window.resizable(False, False)
window.mainloop()
