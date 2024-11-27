from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
window = Tk()
window.title("Updating Course's Data")
window.geometry("754x414+340+190")
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
    file= 'add_course_image/image_1.png')
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
    y=350.0,
    width=150.0,
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
    y=350.0,
    width=150.0,
    height=35.0
)

window.resizable(False, False)
window.mainloop()



# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
#
# def on_click():
#     pass
#
#
# window = Tk()
# window.title("Updating Course's Data")
# window.geometry("530x400+480+170")
# window.configure(bg = "#FFFFFF")
# window.resizable(False, False)
#
# canvas = Canvas(
#     window,
#     bg = "#FFFFFF",
#     height = 400,
#     width = 530,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge"
# )
#
# canvas.place(x = 0, y = 0)
# background_image = PhotoImage(
#     file='course_update_data_image/image_1.png')
# image_1 = canvas.create_image(
#     265.0,
#     211.0,
#     image=background_image
# )
#
# canvas.create_text(
#     47.0,
#     268.0,
#     anchor="nw",
#     text="Click Confirm to update course’s data\n in the system",
#     fill="#FFFFFF",
#     font=("perpetua", 21)
# )
#
# canvas.create_text(
#     59.0,
#     112.0,
#     anchor="nw",
#     text="Credit Hours:",
#     fill="#FFFFFF",
#     font=("perpetua", 20)
# )
#
# canvas.create_text(
#     114.0,
#     155.0,
#     anchor="nw",
#     text="Level:",
#     fill="#FFFFFF",
#     font=("perpetua", 20)
# )
#
# canvas.create_text(
#     57.0,
#     200.0,
#     anchor="nw",
#     text="Departement:",
#     fill="#FFFFFF",
#     font=("perpetua", 20)
# )
#
# button_image_1 = PhotoImage(
#     file=("course_update_data_image/button_1.png"))
# button_1 = Button(
#     image=button_image_1,
#     borderwidth=0,
#     highlightthickness=0,
#     command=on_click,
#     relief="flat"
# )
# button_1.place(
#     x=146.0,
#     y=343.0,
#     width=276.0,
#     height=36.0
# )
#
# canvas.create_text(
#     20.0,
#     13.0,
#     anchor="nw",
#     text="Course’s Data can be\n updated",
#     fill="#FFFFFF",
#     font=("Perpetua", 30, 'bold')
# )
#
# entry_image_1 = PhotoImage(
#     file=("course_update_data_image/entry_1.png"))
# entry_bg_1 = canvas.create_image(
#     339.5,
#     127.0,
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
#     x=215.0,
#     y=111.0,
#     width=249.0,
#     height=30.0
# )
#
# entry_image_2 = PhotoImage(
#     file=("course_update_data_image/entry_2.png"))
# entry_bg_2 = canvas.create_image(
#     339.5,
#     170.0,
#     image=entry_image_2
# )
# level_entry = Entry(
#     bd=0,
#     bg="#D9D9D9",
#     fg="#000716",
#     highlightthickness=0,
#     font=("rockwell", 12)
# )
# level_entry.place(
#     x=215.0,
#     y=154.0,
#     width=249.0,
#     height=30.0
# )
#
# entry_image_3 = PhotoImage(
#     file=("course_update_data_image/entry_3.png"))
# entry_bg_3 = canvas.create_image(
#     339.5,
#     213.0,
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
#     x=215.0,
#     y=197.0,
#     width=249.0,
#     height=30.0
# )
#
# window.mainloop()
