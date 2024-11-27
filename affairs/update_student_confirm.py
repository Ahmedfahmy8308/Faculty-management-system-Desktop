from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
from tkinter import filedialog
from firebase_admin import credentials, initialize_app, db , storage
import cv2
import os


cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recognition-94cf6.appspot.com"
})

path = os.getcwd()
path = path.split('affairs')[0]


ref = db.reference('Students')




def back():
    window.destroy()
    from affairs import affairs_student


def add_student():
    try:
        student_id = entry_2.get()
        student_data = {
            "name": entry_1 .get(),
            "id": int(entry_2.get()),
            "email": entry_3.get(),
            "level": int(entry_4.get()),
            "department": entry_5.get(),
            "gpa": int(entry_6.get()),
            "gender": entry_7.get(),
        }
        ref.child(student_id).set(student_data)
        messagebox.showinfo('success','your student adedd')
    except :
        messagebox.showerror('Error' , 'can not add student')


window = Tk()
window.title("Updating Student's Data")
window.geometry("832x474+340+190")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 484,
    width = 832,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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

back_button = Button(
    bg ='#89228A',
    fg ='white',
    font=('times', 18, 'italic'),
    text= 'Back',
    borderwidth=1.5,
    highlightthickness=0,
    command=add_student,
     relief="flat"
)
back_button.place(
    x=95.0,
    y=403.0,
    width=150.0,
    height=45.0
)



confirm_button = Button(
    bg ='#89228A',
    fg ='white',
    font=('times', 18, 'italic'),
    text= 'Confirm',
    borderwidth=1.5,
    highlightthickness=0,
    command=add_student,
     relief="flat"
)
confirm_button.place(
    x=555.0,
    y=400.0,
    width=150.0,
    height=45.0
)

window.mainloop()




# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
#

# window.geometry("530x422+480+170")
# window.configure(bg = "#FFFFFF")
#
# canvas = Canvas(
#     window,
#     bg = "#FFFFFF",
#     height = 422,
#     width = 530,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge"
# )
#
# canvas.place(x = 0, y = 0)
# image_image_1 = PhotoImage(
#     file="update_student_confirm_image/image_1.png")
# image_1 = canvas.create_image(
#     283.0,
#     235.0,
#     image=image_image_1
# )
#
# canvas.create_text(
#     51.0,
#     290.0,
#     anchor="nw",
#     text="Click Confirm to update student’s data\n in the system",
#     fill="#FFFFFF",
#     font=("perpetua", 21)
# )
#
# canvas.create_text(
#     117.0,
#     111.0,
#     anchor="nw",
#     text="Level:",
#     fill="#FFFFFF",
#     font=("perpetua", 20)
# )
#
# canvas.create_text(
#     124.0,
#     168.0,
#     anchor="nw",
#     text="GPA:",
#     fill="#FFFFFF",
#     font=("perpetua", 20)
# )
#
# canvas.create_text(
#     62.0,
#     229.0,
#     anchor="nw",
#     text="Departement:",
#     fill="#FFFFFF",
#     font=("perpetua", 20)
# )
#
# button_image_1 = PhotoImage(
#     file="update_student_confirm_image/button_1.png")
# button_1 = Button(
#     image=button_image_1,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_1 clicked"),
#     relief="flat"
# )
# button_1.place(
#     x=150.0,
#     y=358.0,
#     width=276.0,
#     height=36.0
# )
#
# canvas.create_text(
#     20.0,
#     13.0,
#     anchor="nw",
#     text="Student’s Data that can be\n updated",
#     fill="#FFFFFF",
#     font=("Perpetua", 30, 'bold')
# )
#
# entry_image_1 = PhotoImage(
#     file="update_student_confirm_image/entry_1.png")
# entry_bg_1 = canvas.create_image(
#     344.0,
#     123.5,
#     image=entry_image_1
# )
# entry_1 = Entry(
#     bd=0,
#     bg="#D9D9D9",
#     fg="#000716",
#     highlightthickness=0,
#     font=("rockwell", 12)
# )
# entry_1.place(
#     x=214.0,
#     y=107.0,
#     width=260.0,
#     height=37.0
# )
#
# entry_image_2 = PhotoImage(
#     file="update_student_confirm_image/entry_2.png")
# entry_bg_2 = canvas.create_image(
#     344.0,
#     181.5,
#     image=entry_image_2
# )
# entry_2 = Entry(
#     bd=0,
#     bg="#D9D9D9",
#     fg="#000716",
#     highlightthickness=0,
#     font=("rockwell", 12)
# )
# entry_2.place(
#     x=214.0,
#     y=165.0,
#     width=260.0,
#     height=37.0
# )
#
# entry_image_3 = PhotoImage(
#     file="update_student_confirm_image/entry_3.png")
# entry_bg_3 = canvas.create_image(
#     344.0,
#     241.5,
#     image=entry_image_3
# )
# entry_3 = Entry(
#     bd=0,
#     bg="#D9D9D9",
#     fg="#000716",
#     highlightthickness=0,
#     font=("rockwell", 12)
# )
# entry_3.place(
#     x=214.0,
#     y=225.0,
#     width=260.0,
#     height=37.0
# )
# window.resizable(False, False)
# window.mainloop()
