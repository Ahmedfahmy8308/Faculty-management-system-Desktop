from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,messagebox
from firebase_admin import credentials, initialize_app, db 

import  sys
import subprocess


cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-94cf6.appspot.com"
})

def conf_del():

    def back1():
        window.destroy()
        subprocess.run(['python', 'affairs_doctors.py'])
        sys.exit()
    def yes():
        ref = db.reference(f'Doctors/{username}')
        ref.delete()
        messagebox.showinfo('Success','Student deleted successfully')
        back1()
    def no():
        back1()

    window = Tk()
    window.title('Confirm to Delete Doctor')
    window.geometry("530x397+480+170")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=397,
        width=530,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file="conf_del_doctor_image/image_1.png")
    image_1 = canvas.create_image(
        265.0,
        198.0,
        image=image_image_1
    )

    canvas.create_text(
        87.0,
        92.0,
        anchor="nw",
        text="Name:",
        fill="#FFFFFF",
        font=("perpetua", 20)
    )

    canvas.create_text(
        72.0,
        260.0,
        anchor="nw",
        text="Are you sure you want to delete this \ndoctor?!",
        fill="#FFFFFF",
        font=("perpetua", 22)
    )

    canvas.create_text(
        64.0,
        190.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("perpetua", 20)
    )

    canvas.create_text(
        87.0,
        141.0,
        anchor="nw",
        text="E-mail:",
        fill="#FFFFFF",
        font=("perpetua", 20)
    )

    button_image_1 = PhotoImage(
        file="conf_del_doctor_image/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=yes,
        relief="flat"
    )
    button_1.place(
        x=78.0,
        y=332.0,
        width=199.0,
        height=37.0
    )

    button_image_2 = PhotoImage(
        file=r"conf_del_doctor_image/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=no,
        relief="flat"
    )
    button_2.place(
        x=283.0,
        y=332.0,
        width=199.0,
        height=47.0
    )

    canvas.create_text(
        28.0,
        22.0,
        anchor="nw",
        text="Doctor’s Data",
        fill="#FFFFFF",
        font=("Perpetua", 30, 'bold')
    )

    entry_image_1 = PhotoImage(
        file=r"conf_del_doctor_image/entry_1.png")
    entry_bg_1 = canvas.create_image(
        329.5,
        103.5,
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
        x=200.0,
        y=87.0,
        width=259.0,
        height=37.0
    )
    entry_1.insert(0,doctor_date['name'])

    entry_image_2 = PhotoImage(
        file="conf_del_doctor_image/entry_2.png")
    entry_bg_2 = canvas.create_image(
        329.5,
        152.5,
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
        x=200.0,
        y=136.0,
        width=259.0,
        height=37.0
    )
    entry_2.insert(0,doctor_date['email'])

    entry_image_3 = PhotoImage(
        file="conf_del_doctor_image/entry_3.png")
    entry_bg_3 = canvas.create_image(
        329.5,
        201.5,
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
        x=200.0,
        y=185.0,
        width=259.0,
        height=37.0
    )
    entry_3.insert(0,doctor_date['username'])
    window.mainloop()




def confirm():
    global doctor_date, username
    username = entry_1.get()
    if username == "":
        messagebox.showerror('Error', 'Enter username')
    else:
        try:
            doctor_date = db.reference(f'Doctors/{username}').get()
        except:
            pass
        if not doctor_date:
            messagebox.showerror('Error', 'invalid username')
        if doctor_date:
            print(doctor_date)
            window.destroy()
            conf_del()

def back():
    window.destroy()
    subprocess.run(['python', 'affairs_doctors.py'])
    sys.exit()


window = Tk()
window.title('Doctor ID to Delete')
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
    file="del_doctor_image/image_1.png")
image_1 = canvas.create_image(
    259.0,
    219.0,
    image=image_image_1
)

canvas.create_text(
    34.0,
    148.0,
    anchor="nw",
    text="Enter Doctor username :",
    fill="#FFFFFF",
    font=("Perpetua", 20 )
)

canvas.create_text(
    19.0,
    18.0,
    anchor="nw",
    text="Delete Doctor from\nour System",
    fill="#FFFFFF",
    font=("Perpetua", 30 , 'bold')
)
entry_image_1 = PhotoImage(
    file="del_doctor_image/entry_1.png")
entry_bg_1 = canvas.create_image(
    159.0,
    210.5,
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
    y=193.0,
    width=226.0,
    height=37.0
)
button_image_1 = PhotoImage(
    file="del_doctor_image/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_1.place(
    x=37.0,
    y=310.0,
    width=208.0,
    height=48.0
)

confirm_image = PhotoImage(
    file="del_doctor_image/button_2.png")
confirm_button = Button(
    image=confirm_image,
    borderwidth=0,
    highlightthickness=0,
    command=confirm,
    relief="flat"
)
confirm_button.place(
    x=273.0,
    y=314.0,
    width=209.0,
    height=44.0
)
window.resizable(False, False)
window.mainloop()
