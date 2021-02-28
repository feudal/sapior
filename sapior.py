from tkinter import *
import time

window=Tk()

files=[]
btn=[]
files2=[]
label=[]

window.wm_title("Sapior")
window.resizable(width=0, height=0)
window.call('wm', 'attributes', '.', '-topmost', '1')

def hide_button(i):
    print(i)
    print(btn[int(i)])
    btn[int(i)].grid_forget()
    #label[int(i)].config(fg="green")#change state of label under buttons

def create_top():
    #top of window
    l1=Label(window,text="time")
    l1.grid(row=0,column=0,columnspan=8)
    l2=Label(window,text="nr")
    l2.grid(row=0,column=6,columnspan=7)

def arrange_buttons():
    #create 180 buttons with text
    for i in range(180):
        files.append(str(i))

    for i in range(len(files)):
        btn.append(Button(window,text=files[i],width=2,command=lambda c=i:hide_button(btn[c].cget("text"))))#fg="linen",

    #arange all button in the window
    for j in range(0,12):
        for i in range(15*j,15*(j+1)):
            print(j, ' ', i)
            btn[i].grid(row=j,column=i-15*j)

def arrange_labels():
    #create 180 labels with text
    for i in range(180):
        files2.append(str(i))

    for i in range(len(files2)):
        label.append(Label(window,text=files2[i],fg="red",width=2))

    #arange all button in the window
    for j in range(0,12):
        for i in range(15*j,15*(j+1)):
            print(j, ' ', i)
            label[i].grid(row=j,column=i-15*j)

def init_window():
    create_top()
    arrange_labels()
    arrange_buttons()

init_window()

window.mainloop()
