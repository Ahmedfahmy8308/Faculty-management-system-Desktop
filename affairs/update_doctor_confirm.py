from pathlib import Path
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
# ده functionality الي كانت موجوده في ال insert doctor

# path = os.getcwd()
# path = path.split('affairs')[0]
#
#
# ref = db.reference('Students')
#
#
#
# def crop_face(image_path, id, margin_factor=0.3):
#
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
#
#     if len(faces) == 0 :
#         pass  # can not load file
#     elif len(faces) > 1 :
#         pass  # more than face
#     else :
#         x, y, w, h = faces[0]
#         margin_x = int(margin_factor * w)
#         margin_y = int(margin_factor * h)
#         crop_x = max(0, x - margin_x)
#         crop_y = max(0, y - margin_y)
#         crop_w = min(image.shape[1] - crop_x, w + 2 * margin_x)
#         crop_h = min(image.shape[0] - crop_y, h + 2 * margin_y)
#         cropped_face = image[crop_y:crop_y + crop_h, crop_x:crop_x + crop_w]
#         fileName = fr'{path}/images/{id}.png'
#         cv2.imwrite(fileName, cropped_face)
#
#         bucket = storage.bucket()
#         blob = bucket.blob(f'images/{id}.png')
#         blob.upload_from_filename(fileName)
#
#
# def back():
#     window.destroy()
#     from affairs import affairs_student

# دي انت كنت عاملها كومنت
# def add_student():
#     try:
#         student_id = entry_2.get()
#         student_data = {
#             "name": entry_1 .get(),
#             "id": int(entry_2.get()),
#             "email": entry_3.get(),
#             "level": int(entry_4.get()),
#             "department": entry_5.get(),
#             "gpa": int(entry_6.get()),
#             "gender": entry_7.get(),
#         }
#         crop_face(entry_8.get(),student_id)
#         ref.child(student_id).set(student_data)
#         messagebox.showinfo('success','your student adedd')

window = Tk()
window.title("Updating Doctor's Data")
window.geometry("754x414+380+150")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 414,
    width = 754,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
back_button = Button(
    bg ='#89228A',
    fg ='white',
    font=('times', 18, 'italic'),
    text= 'Back',
    borderwidth=1.5,
    highlightthickness=0,
    # command=add_student,
     relief="flat"
)
back_button.place(
    x=95.0,
    y=349.0,
    width=140.0,
    height=35.0
)

confirm_button = Button(
    bg ='#89228A',
    fg ='white',
    font=('times', 18, 'italic'),
    text= 'Confirm',
    borderwidth=1.5,
    highlightthickness=0,
    # command=add_student,
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



# from pathlib import Path
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
#
# window = Tk()
# window.title("Updating Doctor's Data")
# window.geometry("530x422+480+170")
# window.configure(bg = "#FFFFFF")
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
# background_image = PhotoImage(
#     file="update_doctor_confirm_image/image_1.png")
# image_1 = canvas.create_image(
#     282.0,
#     243.0,
#     image=background_image
# )
#
# canvas.create_text(
#     51.0,
#     290.0,
#     anchor="nw",
#     text="Click Confirm to update doctor’s data\n in the system",
#     fill="#FFFFFF",
#     font=("perpetua", 21))
#
# canvas.create_text(
#     87.0,
#     143.0,
#     anchor="nw",
#     text="E-mail:",
#     fill="#FFFFFF",
#     font=("perpetua", 21)
# )
#
# canvas.create_text(
#     70.0,
#     215.0,
#     anchor="nw",
#     text="Username:",
#     fill="#FFFFFF",
#     font=("perpetua", 21)
# )
#
# button_image_1 = PhotoImage(
#     file="update_doctor_confirm_image/button_1.png")
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
#     text="Doctor’s data that can be\n updated",
#     fill="#FFFFFF",
#     font=("Perpetua", 30, 'bold')
# )
#
# entry_image_1 = PhotoImage(
#     file="update_doctor_confirm_image/entry_1.png")
# entry_bg_1 = canvas.create_image(
#     332.5,
#     152.5,
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
#     x=203.0,
#     y=135.0,
#     width=259.0,
#     height=37.0
# )
#
# entry_image_2 = PhotoImage(
#     file="update_doctor_confirm_image/entry_2.png")
# entry_bg_2 = canvas.create_image(
#     332.5,
#     223.5,
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
#     x=203.0,
#     y=206.0,
#     width=259.0,
#     height=37.0
# )
# window.resizable(False, False)
# window.mainloop()
