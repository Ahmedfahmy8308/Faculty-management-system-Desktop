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

ref = db.reference('Doctors')
def update_confirm():
    
    def back1():
        window.destroy()
        subprocess.run(['python', 'affairs_doctors.py'])
        sys.exit()
    def confirm1():
        try:
            doctor_data = {
                "name": entry_1.get(),
                "id": int(entry_2.get()),
                "username": entry_3.get(),
                "email": entry_4.get(),
                "password": entry_5.get(),
            }
            ref.child(username).set(doctor_data)
            messagebox.showinfo('success', 'your student updated')
            back1()
        except:
            messagebox.showerror('Error', 'can not add student')

    window = Tk()
    window.title("Updating Doctor's Data")
    window.geometry("754x414+380+150")
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
        file="add_doc_image/image_1.png")
    image_1 = canvas.create_image(
        377.0,
        207.0,
        image=image_image_1
    )

    canvas.create_text(
        20.0,
        225.0,
        anchor="nw",
        text="Click Confirm to update doctor’s data\n in the system",
        fill="#FFFFFF",
        font=("Perpetua", 16)
    )

    canvas.create_text(
        20.0,
        112.0,
        anchor="nw",
        text="Doctor’s data\nthat can be updated",
        fill="#FFFFFF",
        font=('Perpetua', 27, 'bold')
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
    entry_1.insert(0,doctor_data['name'])

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
    entry_2.insert(0,doctor_data['id'])

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
    entry_3.insert(0,doctor_data['username'])

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
    entry_4.insert(0,doctor_data['email'])


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
    entry_5.insert(0,doctor_data['password'])

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
        y=349.0,
        width=140.0,
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
        y=349.0,
        width=140.0,
        height=35.0
    )
    window.resizable(False, False)
    window.mainloop()


def confirm ():
    global doctor_data , username
    username = entry_1.get()
    if username =="":
        messagebox.showerror('Error', 'Enter username')
    else:
        try :
            doctor_data = db.reference(f'Doctors/{username}').get()
        except :
            pass
        if not doctor_data :
            messagebox.showerror('Error' , 'invalid username')
        if doctor_data :
            window.destroy()
            update_confirm()


def back():
    window.destroy()
    subprocess.run(['python', 'affairs_doctors.py'])
    sys.exit()



window = Tk()
window.title('Doctor ID to Update')
window.geometry("517x403+470+200")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 403,
    width = 517,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x=0, y=0)
bg_image = PhotoImage(
    file='id_update_doctor_image/image_1.png')
image_1 = canvas.create_image(
    259.0,
    219.0,
    image=bg_image
)

entry_image_1 = PhotoImage(
    file='id_update_doctor_image/entry_1.png')
entry_bg_1 = canvas.create_image(
    159.0,
    207.5,
    image=entry_image_1
)
entry_1= Entry(
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
    height=37.0
)

canvas.create_text(
    34.0,
    148.0,
    anchor="nw",
    text="Enter Doctor username:",
    fill="#FFFFFF",
    font=("perpetua", 22)
)

canvas.create_text(
    19.0,
    18.0,
    anchor="nw",
    text="Update Doctor’s Data in \nour System",
    fill="#FFFFFF",
    font=("Perpetua", 30, 'bold')
)

back_image = PhotoImage(
    file=("id_update_doctor_image/button_1.png"))
back_button = Button(
    image=back_image,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
back_button.place(
    x=26.0,
    y=295.0,
    width=227.0,
    height=64.0
)

search_image = PhotoImage(
    file=("id_update_doctor_image/button_2.png"))
search_button =Button(
image = search_image,
    borderwidth=0,
    highlightthickness=0,
    command=confirm,
    relief="flat"
)
search_button.place(
    x=270.0,
    y=302.0,
    width=212.0,
    height=44.0
)

window.mainloop()
