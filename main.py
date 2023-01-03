from tkinter import *


def calculate():
    input_number = entry.get()
    state = radio_state.get()
    if state == 0:
        answer = round(float(input_number) * 1.609, 2)
    else:
        answer = round(float(input_number) / 1.609, 2)
    label3.config(text=f"{answer}")

def km_to_miles():
    label1.config(text="Km")
    label2.config(text="Mile(s)")
    window.title("Km to Mile converter")

def mile_to_km():
    label1.config(text="Mile(s)")
    label2.config(text="Km")
    window.title("Mile to Km converter")


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=100)

label = Label(text="is equal to")
label.grid(column=1, row=2)

label1 = Label(text="Mile(s)")
label1.grid(column=3, row=1)

label2 = Label(text="Km")
label2.grid(column=3, row=2)

entry = Entry(width=10)
entry.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

label3 = Label(text="0")
label3.grid(column=2, row=2)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles to Km", value=0, variable=radio_state, command=mile_to_km)
radiobutton2 = Radiobutton(text="Km to Miles", value=1, variable=radio_state, command=km_to_miles)
radiobutton1.grid(column=4, row=3)
radiobutton2.grid(column=4, row=4)
state = 0
window.mainloop()
