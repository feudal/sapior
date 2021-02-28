from tkinter import *
import time
from random import shuffle

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

def count_combs(m,elem):
    try:
        bombs=0
        if m[elem-14] =="*":
            bombs+=1
        if m[elem-15] =="*":
            bombs+=1
        if m[elem-16] =="*":
            bombs+=1

        if m[elem-1] =="*":
            bombs+=1
        if m[elem+1] =="*":
            bombs+=1

        if m[elem+14] =="*":
            bombs+=1
        if m[elem+15] =="*":
            bombs+=1
        if m[elem+16] =="*":
            bombs+=1
    except:
        pass

    if int(bombs) != 0:
        return bombs
    else:
        return ''

def arange_numbers(m):
    for i in range(180):
        if m[i]!="*":
            m[i]=count_combs(m,i)
    return m

def create_field():
    #plant 35 bombs in fiels map
    map1=["*"]*25
    map2=['']*155
    map=map1+map2
    #shake the list map
    shuffle(map)

    #put the numbers around the bombs
    map=arange_numbers(map)

    for i in map:
        files2.append(str(i))

def arrange_labels():#labels is field with bombs
    #create 180 labels with text
    create_field()

    give_color = {
        "*":'black',
        '1':'blue',
        '2':'green',
        '3':'red',
        '4':'brown',
        '5':'brown',
        '':'yellow'
    }
    for i in range(len(files2)):
        print(files2[i])
        label.append(Label(window,text=files2[i],fg=give_color[files2[i]],width=2))

    #arange all label in the window
    for j in range(0,12):
        for i in range(15*j,15*(j+1)):
            # print(j, ' ', i)
            label[i].grid(row=j+1,column=i-15*j)

def arrange_buttons():
    #create 180 buttons with text
    for i in range(180):
        files.append(str(i))

    for i in range(len(files)):
        btn.append(Button(window,text=files[i],width=2,command=lambda c=i:hide_button(btn[c].cget("text"))))#fg="linen",

    #arange all button in the window
    for j in range(0,12):
        for i in range(15*j,15*(j+1)):
            # print(j, ' ', i)
            btn[i].grid(row=j+1,column=i-15*j)

def init_window():
    create_top()
    arrange_labels()
    #arrange_buttons()

init_window()

window.mainloop()
