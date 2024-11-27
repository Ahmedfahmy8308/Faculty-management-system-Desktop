from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
from firebase_admin import credentials, initialize_app, db
import os
import sys
import subprocess
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import pickle
import os, cv2
from PIL import Image, ImageTk
import tkinter as tk
import face_recognition
import numpy as np
#
# cred = credentials.Certificate("serviceAccountKey.json")
# initialize_app(cred, {
#     'databaseURL': "https://face-recognition-94cf6-default-rtdb.firebaseio.com/",
#     'storageBucket': "face-recognition-94cf6.appspot.com"
#
# })

path = os.getcwd()
path = path.split('affairs')[0]


ref = db.reference('lecture')

def attendance():

    path = os.getcwd()
    path = path.split('doctor')[0]

    file = open('EncodeFile.p', 'rb')
    encodeListKnown = pickle.load(file)
    file.close()
    encodelist, studentIds = encodeListKnown

    window = Tk()
    window.title("Students' Attendance System")
    window.geometry("1190x690+100+50")
    background_image = ImageTk.PhotoImage(file="../affairs/affairs_image/image_1.png")
    bg_label = tk.Label(window, image=background_image)
    bg_label.place(x=-3, y=0)
    window.resizable(False, False)

    doc_cam_frame = tk.Frame(window, bg='white', width=270, height=157)
    doc_cam_frame.place(x=185, y=425)

    id_list = []
    name_list =[]
    dec ={}
    def stop():
        dec = dict(zip(id_list, name_list))
        print(dec)
        ref = db.reference(f'lecture/{lec_name}')
        ref.child('students_id').set(dec)
        messagebox.showinfo('Success' , 'Attendance added to database \ngoodbye')
        window.destroy()
        # sys.exit()




    def get_data(id):
        data = db.reference(f'Students/{id}').get()
        if id not in id_list:
            id_list.append(id)
            name_list.append(data['name'])
        stu_image = PhotoImage(file=f'../images/{id}.png')
        stu_image_label.configure(image=stu_image)
        stu_image_label.image = stu_image
        name_value_label.configure(text=data['name'])
        id_value_label.configure(text=data['id'])
        level_value_label.configure(text=data['level'])
        dept_value_label.configure(text=data['department'])
        email_value_label.configure(text=data['email'])

        return data['name'].split(' ')[0]

    details_label = tk.Label(window,
                             text="Attended Student's Details",
                             font=('perpetua', 21, 'bold'),
                             bg='#A22B6D',
                             fg='white'
                             )
    details_label.place(x=650, y=45)
    student_details = tk.Frame(window, bg='#A22B6D', width=530, height=580)
    student_details.place(x=650, y=80)

    photo_label = tk.Label(
        student_details,
        text='Photo:',
        font=('perpetua', 19, 'bold'),
        bg='#A22B6D',
        fg='white'
    )
    global stu_image_label
    photo_label.grid(row=0, column=0, padx=10, pady=10)
    stu_image = PhotoImage(file=f'../images/1.png')
    stu_image_label = tk.Label(student_details, image=stu_image)
    stu_image_label.grid(row=1, column=1)

    name_label = tk.Label(student_details,
                          text='Name:',
                          font=('perpetua', 19, 'bold'),
                          bg='#A22B6D',
                          fg='white'
                          )
    name_label.grid(row=3, column=0, padx=20)

    name_value_label = tk.Label(student_details,
                                text='Ahmed',
                                font=('perpetua', 18, 'bold'),
                                bg='#A22B6D',
                                fg='white'
                                )
    name_value_label.grid(row=3, column=1)

    id_label = tk.Label(student_details,
                        text='ID:',
                        font=('perpetua', 19, 'bold'),
                        bg='#A22B6D',
                        fg='white'
                        )
    id_label.grid(row=4, column=0, padx=20, pady=16)

    # هتجيب id من الداتا بيز هنا
    id_value_label = tk.Label(student_details,
                              text='1',
                              font=('perpetua', 18, 'bold'),
                              bg='#A22B6D',
                              fg='white'
                              )
    id_value_label.grid(row=4, column=1, padx=20, pady=16)

    level_label = tk.Label(student_details,
                           text='Level:',
                           font=('perpetua', 19, 'bold'),
                           bg='#A22B6D',
                           fg='white'
                           )
    level_label.grid(row=5, column=0, padx=20, pady=18)

    level_value_label = tk.Label(student_details,
                                 text='4',
                                 font=('perpetua', 18, 'bold'),
                                 bg='#A22B6D',
                                 fg='white'
                                 )
    level_value_label.grid(row=5, column=1, padx=20, pady=18)

    dept_label = tk.Label(student_details,
                          text='Departemet:',
                          font=('perpetua', 19, 'bold'),
                          bg='#A22B6D',
                          fg='white'
                          )

    dept_label.grid(row=6, column=0, padx=20, pady=20)

    # هتجيب deprt من الداتا بيز هنا
    dept_value_label = tk.Label(student_details,
                                text='cs',
                                font=('perpetua', 18, 'bold'),
                                bg='#A22B6D',
                                fg='white'
                                )
    dept_value_label.grid(row=6, column=1, padx=20, pady=20)

    email_label = tk.Label(student_details,
                           text='E-mail:',
                           font=('perpetua', 19, 'bold'),
                           bg='#A22B6D',
                           fg='white'
                           )
    email_label.grid(row=7, column=0, padx=20, pady=22)
    # هتجيب e-mail من الداتا بيز هنا
    email_value_label = tk.Label(student_details,
                                 text='fahmy8308@gmail.com',
                                 font=('perpetua', 18, 'bold'),
                                 bg='#A22B6D',
                                 fg='white'
                                 )
    email_value_label.grid(row=7, column=1, padx=20, pady=22)

    class camera:

        def get_attendance(self):
            if not self.video_capture.isOpened():
                self.video_capture = cv2.VideoCapture(0)
                self.update_camera()

        def stop(self):
            if self.video_capture.isOpened():
                self.video_capture.release()

        # buttons functionality ended
        def __init__(self, window):
            self.window = window

            doc_name = "Amr"  # doctor's name selected from database
            global student_details
            welcome_label = tk.Label(window,
                                     text=f'Hi Dr. {doc_name} Welcome Back',
                                     font=('perpetua', 34, 'italic bold'),
                                     bg='#6127A2',
                                     fg='white'
                                     )
            welcome_label.place(x=60, y=18)

            welcome_label.place(x=60, y=18)

            self.video_capture = cv2.VideoCapture(0)

            self.current_image = None

            self.big_frame = tk.Canvas(window, width=540, height=330)
            self.big_frame.place(x=60, y=80)

            self.small_frame = tk.Canvas(window, width=270, height=157)
            self.small_frame.place(x=185, y=425)

            # buttons position
            self.btn_resum = tk.Button(window, bg='#A22B6D', fg='white', font=('times', 19, 'italic bold'),
                                       text='Pause', borderwidth=1.5, highlightthickness=0,
                                       command=self.stop,
                                       relief="flat")
            self.btn_resum.place(x=270.0,
                                 y=615.0,
                                 width=150.0,
                                 height=40.0)

            self.btn_get_attend = tk.Button(window, bg='#A22B6D', fg='white', font=('times', 19, 'italic bold'),
                                            text='Get Attendance', borderwidth=1.5, highlightthickness=0,
                                            command=self.get_attendance,
                                            relief="flat")
            self.btn_get_attend.place(x=20.0,
                                      y=615.0,
                                      width=200.0,
                                      height=40.0)
            btn_stop = tk.Button(window, bg='#A22B6D', fg='white', font=('times', 19, 'italic bold'), text='stop',
                                 borderwidth=1.5, highlightthickness=0, command=stop, relief="flat")
            btn_stop.place(x=470.0, y=615.0, width=150.0, height=40.0)
            self.update_camera()
            self.window.mainloop()

        def update_camera(self):
            ret, frame = self.video_capture.read()

            if ret:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb_frame = cv2.resize(rgb_frame, (0, 0), None, .85, .85)
                frame = cv2.resize(frame, (0, 0), None, .5, .5)
                pil_img = Image.fromarray(rgb_frame)
                img = ImageTk.PhotoImage(image=pil_img)
                face_locations = face_recognition.face_locations(np.array(pil_img))
                encode_cur_frame = face_recognition.face_encodings(rgb_frame, face_locations)

                for encode_face, face_loc in zip(encode_cur_frame, face_locations):
                    matches = face_recognition.compare_faces(encodelist, encode_face)
                    face_dis = face_recognition.face_distance(encodelist, encode_face)
                    match_index = np.argmin(face_dis)

                    y1, x2, y2, x1 = face_loc
                    y1, x2, y2, x1 = y1 - 40, x2 + 25, y2 + 25, x1 - 20
                    cv2.rectangle(rgb_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(rgb_frame, (x1, y2), (x2, y2 + 45), (0, 255, 0), -1)

                    if matches[match_index]:
                        student_id = studentIds[match_index]
                        name = get_data(student_id)
                        cv2.putText(rgb_frame, str(name), (x1 + 5, y2 + 30), cv2.FONT_HERSHEY_COMPLEX, .8, (0, 0, 0),
                                    2)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
                self.big_frame.create_image(0, 0, image=self.photo, anchor=tk.NW)
                self.current_image = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.small_frame.create_image(0, 0, image=self.current_image, anchor=tk.NW)
                self.window.after(20, self.update_camera)

    # calling an object from the camera class
    camera_frame = camera(window)
    window.mainloop()


def submit():
    try:
        global lec_name
        lec_name = f'{entry_1.get()} {entry_2.get()}'
        lec_data = {
            "course": entry_1 .get(),
            "lec_number": entry_2.get(),
            "level": entry_3.get(),
            "department": entry_4.get(),
            "lec_time": entry_5.get(),
        }
        ref.child(lec_name).set(lec_data)
        messagebox.showinfo('success','lecture added successfully')
        window.destroy()
        subprocess.run(['python', 'EncodeGenerator.py'])
        attendance()
    except:
        pass


window = Tk()
window.title("Doctor's Lecture Attendance")
window.geometry("566x522+480+150")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 522,
    width = 566,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file="doctor_gui_image/image_1.png")
image_1 = canvas.create_image(
    283.0,
    275.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file="doctor_gui_image/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit,
    relief="flat"
)
button_1.place(
    x=170.0,
    y=437.0,
    width=252.0,
    height=60.82759094238281
)

canvas.create_text(
    54.0,
    360.0,
    anchor="nw",
    text="Lecture Time:",
    fill="#FFFFFF",
    font=("perpetua", 21,'bold')
)

canvas.create_text(
    66.0,
    284.0,
    anchor="nw",
    text="Department:",
    fill="#FFFFFF",
    font=("perpetua", 21,'bold')
)

canvas.create_text(
    102.0,
    208.0,
    anchor="nw",
    text="Level:",
    fill="#FFFFFF",
    font=("perpetua", 21,'bold')
)

canvas.create_text(
    25.0,
    135.0,
    anchor="nw",
    text="Lecture Number:",
    fill="#FFFFFF",
    font=("perpetua", 21,'bold')
)

canvas.create_text(
    39.0,
    60.0,
    anchor="nw",
    text="Course Name:",
    fill="#FFFEFE",
    font=("perpetua", 21,'bold')
)

entry_image_1 = PhotoImage(
    file="doctor_gui_image/entry_1.png")
entry_bg_1 = canvas.create_image(
    377.5,
    76.0,
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
    x=237.0,
    y=50.0,
    width=281.0,
    height=50.0
)

entry_image_2 = PhotoImage(
    file="doctor_gui_image/entry_2.png")
entry_bg_2 = canvas.create_image(
    377.5,
    151.0,
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
    x=237.0,
    y=125.0,
    width=281.0,
    height=50.0
)

entry_image_3 = PhotoImage(
    file="doctor_gui_image/entry_3.png")
entry_bg_3 = canvas.create_image(
    377.5,
    225.0,
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
    x=237.0,
    y=199.0,
    width=281.0,
    height=50.0
)

entry_image_4 = PhotoImage(
    file="doctor_gui_image/entry_4.png")
entry_bg_4 = canvas.create_image(
    377.5,
    299.0,
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
    x=237.0,
    y=273.0,
    width=281.0,
    height=50.0
)

entry_image_5 = PhotoImage(
    file="doctor_gui_image/entry_5.png")
entry_bg_5 = canvas.create_image(
    377.5,
    377.0,
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
    x=237.0,
    y=351.0,
    width=281.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
