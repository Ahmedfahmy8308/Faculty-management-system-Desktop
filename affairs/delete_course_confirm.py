from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


window = Tk()
window.title('Confirm to Delete Course')
window.geometry("530x422+480+170")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 422,
    width = 530,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file='delete_course_confirm_image/image_1.png')
image_1 = canvas.create_image(
    265.0,
    198.0,
    image=image_image_1
)

canvas.create_text(
    102.0,
    73.0,
    anchor="nw",
    text="Name:",
    fill="#FFFFFF",
    font=("perpetua", 20)
)

canvas.create_text(
    46.0,
    306.0,
    anchor="nw",
    text="Are you sure you want to delete this\n course?!",
    fill="#FFFFFF",
    font=("perpetua", 22)
)

canvas.create_text(
    110.0,
    193.5,
    anchor="nw",
    text="Level:",
    fill="#FFFFFF",
    font=("perpetua", 20)
)
canvas.create_text(
    56.0,
    258.0,
    anchor="nw",
    text="Departement:",
    fill="#FFFFFF",
    font=("perpetua", 20)
)

canvas.create_text(
    64.0,
    131.0,
    anchor="nw",
    text="Credit Hours:",
    fill="#FFFFFF",
    font=("perpetua", 20)
)

button_image_1 = PhotoImage(
    file=("delete_course_confirm_image/button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=66.0,
    y=372.0,
    width=199.0,
    height=37.0
)

button_image_2 = PhotoImage(
    file=("delete_course_confirm_image/button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
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
    text="Course’s Data",
    fill="#FFFFFF",
    font=("Perpetua", 30, 'bold')
)

entry_image_1 = PhotoImage(
    file=("delete_course_confirm_image/entry_1.png"))
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
entry_1.place(
    x=215.0,
    y=65.0,
    width=259.0,
    height=37.0
)

entry_image_2 = PhotoImage(
    file=("delete_course_confirm_image/entry_2.png"))
entry_bg_2 = canvas.create_image(
    344.5,
    146.5,
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
    y=130.0,
    width=259.0,
    height=37.0
)

entry_image_3 = PhotoImage(
    file=("delete_course_confirm_image/entry_3.png"))
entry_bg_3 = canvas.create_image(
    344.5,
    210,
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
    y=192.0,
    width=259.0,
    height=37.0
)

entry_image_5 = PhotoImage(
    file=("delete_course_confirm_image/entry_5.png"))
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
window.resizable(False, False)
window.mainloop()
