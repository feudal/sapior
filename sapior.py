from tkinter import *
import time

window=Tk()

files=[]
btn=[]

window.wm_title("Sapior")
window.resizable(width=0, height=0)
window.call('wm', 'attributes', '.', '-topmost', '1')

def hide_button(i):
    print(i)
    print(btn[int(i)])
    btn[int(i)].grid_forget()

#top of window
l1=Label(window,text="time")
l1.grid(row=0,column=0,columnspan=8)
l2=Label(window,text="nr")
l2.grid(row=0,column=6,columnspan=7)

# for i in range(15):
#     for j in range(12):
#         b=Button(window,text="",width=2,command=open)
#         b.grid(row=j+1,column=i)

#create 180 buttons with text
for i in range(180):
    files.append(str(i))

for i in range(len(files)):
    btn.append(Button(window,text=files[i],width=2,command=lambda c=i:hide_button(btn[c].cget("text"))))#fg="linen",

# for j in range(1):
#     for i in range(int(len(btn)/3)):
#         print(j, ' ', i)
#         btn[i].grid(row=j,column=i)
#
# for j in range(1,2):
#     for i in range(int(len(btn)/3), len(btn)-15):
#         print(j, ' ', i)
#         btn[i].grid(row=j,column=i-15)
#
# for j in range(2,3):
#     for i in range(int(len(btn)/3)*2, len(btn)):
#         print(j, ' ', i)
#         btn[i].grid(row=j,column=i-30)

#arange all button in the window
for j in range(0,12):
    for i in range(15*j,15*(j+1)):
        print(j, ' ', i)
        btn[i].grid(row=j,column=i-15*j)



window.mainloop()
