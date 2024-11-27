from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import os
import sys
import subprocess

from firebase_admin import credentials, initialize_app, db , storage


cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-94cf6.appspot.com"
})

path = os.getcwd()
path = path.split('login')[0]




def on_radio_button_click(event):
    global cliked
    cliked = event

def submit():
    if pass_entry.get() == '' or email_entry.get() == '' or cliked == '':
        messagebox.showerror('Error!', 'Fields can not be empty!')
    elif cliked == 'Doctor' :
        try :
            doctorinfo = db.reference(f'Doctors/{email_entry.get()}').get()
            if  doctorinfo['password'] == pass_entry.get() :
                messagebox.showinfo("Success", f'Welcome : DR / {doctorinfo["name"]}')
                window.destroy()
                os.chdir(fr'{path}\doctor')
                from doctor import doctor_gui
            else :
                messagebox.showerror("Error", 'invalid password')

        except:
            messagebox.showerror("Error", 'invalid username')
    elif cliked == 'Affairs' :
        if  email_entry.get() == 'Affairs' and pass_entry.get() == '123' :
            messagebox.showinfo("Success", 'Welcome')
            window.destroy()
            os.chdir(fr'{path}\affairs')
            from affairs import affairs_gui

        else :
            messagebox.showerror("Error", 'invalid username or password')

window = Tk()

window.title("Attendance System Log In")
window.geometry("1280x700+100+50")
window.configure(bg = "")
window.resizable(False, False)



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
image_image_1 = PhotoImage( file='login_gui_image/image_1.png')
image_1 = canvas.create_image(
    640.0,
    350.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("login_gui_image/image_2.png"))
image_2 = canvas.create_image(
    640.0,
    350.0,
    image=image_image_2
)

passentry_image = PhotoImage(
    file=("login_gui_image/entry_1.png"))
entry_bg_1 = canvas.create_image(
    916.5,
    376.0,
    image=passentry_image
)
pass_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font= ('Rockwell', 14)
)
pass_entry.place(
    x=768.0,
    y=352.0,
    width=297.0,
    height=46.0
)

# submit button
submit_image = PhotoImage( file='login_gui_image/button_1.png' )
submit_button = Button(
    image= submit_image,
    borderwidth=0,
    highlightthickness=0,
    command= submit,
    relief="groove",
    cursor='hand2'
)
submit_button.place(
    x=786.0,
    y=529.0,
    width=286.0,
    height=58.0
)

canvas.create_text(
    134.0,
    353.0,
    anchor="nw",
    text="  Log in and join our Attendance with Face-Recognition System",
    fill="#FFFFFF",
    font=("Perpetua", 17)
)

canvas.create_text(
    740.0,
    100.0,
    anchor="nw",
    text=" Hello!\n Welcome back",
    fill="#FFFFFF",
    font= ('Rockwell', 26, 'bold')
)

canvas.create_text(
    134.0,
    206.0,
    anchor="nw",
    text="Attendance\nSystem\n\n",
    fill="#FFFFFF",
    font=('Perpetua', 37, 'bold')
)

canvas.create_text(
    779.0,
    214.0,
    anchor="nw",
    text="Username : ",
    fill="#FFFFFF",
    font=("Rockwell", 16)
)

emailentry_image = PhotoImage(
    file='login_gui_image/entry_2.png')
entry_bg_2 = canvas.create_image(
    916.5,
    269.0,
    image=emailentry_image
)
email_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font= ('Rockwell', 14)
)
email_entry.place(
    x=768.0,
    y=245.0,
    width=297.0,
    height=46.0
)

canvas.create_text(
    779.0,
    320.0,
    anchor="nw",
    text="Password : ",
    fill="#FFFFFF",
    font=("Rockwell", 16)
)

email_icon = PhotoImage(
    file='login_gui_image/image_3.png')
image_3 = canvas.create_image(
    761.0,
    229.0,
    image=email_icon
)

pass_icon = PhotoImage(
    file='login_gui_image/image_4.png')
image_4 = canvas.create_image(
    761.0,
    330.0,
    image=pass_icon
)

user_icon = PhotoImage(
    file='login_gui_image/user.png')
image_3 = canvas.create_image(
    761.0,
    429.0,
    image=user_icon
)
canvas.create_text(
    779.0,
    420.0,
    anchor="nw",
    text="Select Your Role:",
    fill="#FFFFFF",
    font=("Rockwell", 16)
)

style = ttk.Style()
style.configure("TRadiobutton", background ='#9C2795' ,foreground = 'white',relief="flat", font=("Rockwell", 15, 'bold'),cursor='hand2')
doctor_button = ttk.Radiobutton(window,
                                text="Doctor",
                                value="Doctor",
                                compound="right",
                                command=lambda: on_radio_button_click("Doctor"),
                                cursor='hand2'
)

affairs_button = ttk.Radiobutton(window,
                                text="Affairs",
                                value="Affairs",
                                compound="right",
                                command=lambda: on_radio_button_click("Affairs"),
                                padding=0,
                                cursor='hand2'
)
doctor_button.place(
    x=780.0,
    y=470.0,
    width=88.0,
    height=32.0
)
affairs_button.place(
    x=968.0,
    y=470.0,
    width=88.0,
    height=32.0
)
window.mainloop()