from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
import tkinter as tk
from tkinter import filedialog
from firebase_admin import credentials, initialize_app, db , storage
import cv2
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



def crop_face(image_path, id, margin_factor=0.3):

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0 :
        messagebox.showerror('Error','No Detected faces')
        back()
    elif len(faces) > 1 :
        messagebox.showerror('Error','more than 1 face')
        back()
    else :
        x, y, w, h = faces[0]
        margin_x = int(margin_factor * w)
        margin_y = int(margin_factor * h)
        crop_x = max(0, x - margin_x)
        crop_y = max(0, y - margin_y)
        crop_w = min(image.shape[1] - crop_x, w + 2 * margin_x)
        crop_h = min(image.shape[0] - crop_y, h + 2 * margin_y)
        cropped_face = image[crop_y:crop_y + crop_h, crop_x:crop_x + crop_w]
        resized_image = cv2.resize(cropped_face, (195, 195))
        fileName = fr'{path}/images/{id}.png'
        cv2.imwrite(fileName, resized_image)

        bucket = storage.bucket()
        blob = bucket.blob(f'images/{id}.png')
        blob.upload_from_filename(fileName)


def back():
    window.destroy()
    subprocess.run(['python', 'affairs_student.py'])
    sys.exit()


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
        crop_face(entry_8.get(),student_id)
        ref.child(student_id).set(student_data)
        messagebox.showinfo('success','Student adedd successfully')
    except :
        messagebox.showerror('Error' , 'can not add student')

def browse_photo():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        entry_8.delete(0, tk.END)
        entry_8.insert(0, file_path)


window = Tk()
window.title('Insert New Student')
window.geometry("832x484+340+190")
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

browse_image = PhotoImage(
    file='add_stu_image/button_1.png')
browse_button = Button(
    image=browse_image,
    borderwidth=0,
    highlightthickness=0,
    command=browse_photo,
    relief="flat"
)
browse_button.place(
    x=686.0,
    y=376.0,
    width=86.0,
    height=46.0
)

canvas.create_text(
    44.0,
    225.0,
    anchor="nw",
    text="Fill student's details to add him to \ncollege system",
    fill="#FFFFFF",
    font=("Perpetua", 16)
)

canvas.create_text(
    41.0,
    112.0,
    anchor="nw",
    text="Insert \nNew Student",
    fill="#FFFFFF",
    font=('Perpetua', 33, 'bold')
)

button_image_2 = PhotoImage(
    file='add_stu_image/button_2.png')
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=add_student,
    relief="flat"
)
button_2.place(
    x=486.0,
    y=429.0,
    width=287.0,
    height=49.0
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
    397.0,
    385.0,
    anchor="nw",
    text="Photo:",
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



entry_image_8 = PhotoImage(
    file='add_stu_image/entry_8.png')
entry_bg_8 = canvas.create_image(
    584.0,
    395.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("rockwell", 12)
)
entry_8.place(
    x=492.0,
    y=380.0,
    width=180.0,
    height=30
)
button_1_image = PhotoImage(
    file="add_stu_image/button3.png")
button_1 = Button(
    image=button_1_image,
    borderwidth=0,
    highlightthickness=0,
    command= back,
    relief="flat"
)
button_1.place(
    x=95.0,
    y=403.0,
    width=203.0,
    height=54.0
)


window.mainloop()
