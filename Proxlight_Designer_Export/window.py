from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("488x420")
window.configure(bg = "#612d81")
canvas = Canvas(
    window,
    bg = "#612d81",
    height = 420,
    width = 488,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"\Proxlight_Designer_Export\_background.png")
background = canvas.create_image(
    205.0, 85.0,
    image=background_img)

entry0_img = PhotoImage(file = f"\Proxlight_Designer_Export\img_textBox0.png")
entry0_bg = canvas.create_image(
    351.5, 263.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 267, y = 173,
    width = 169,
    height = 179)

entry1_img = PhotoImage(file = f"\Proxlight_Designer_Export\img_textBox1.png")
entry1_bg = canvas.create_image(
    96.0, 262.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 16, y = 170,
    width = 160,
    height = 182)

img0 = PhotoImage(file = f"Proxlight_Designer_Export\ img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 146, y = 369,
    width = 165,
    height = 31)

window.resizable(False, False)
window.mainloop()
