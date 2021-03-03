from tkinter import *
import time
import datetime
from time import strftime
from random import shuffle

window=Tk()

files=[]
btn=[]
files2=[]
label=[]
temp=0
state_of_btn=[]
nr_bombs=30
nr_open_cell=0

for i in range(238):
    state_of_btn.append(False)


window.wm_title("Sapior")
window.resizable(width=0, height=0)
window.geometry("+500+300")
# window.call('wm', 'attributes', '.', '-topmost', '1')

def you_lose_window():
    global newWindow
    newWindow = Toplevel(window)
    newWindow.title("you lose")
    newWindow.geometry("+500+300")
    # newWindow.geometry("200x100")

    l1=Label(newWindow,text ="You lose")
    l1.grid(row=0,column=8,pady=10)
    b1=Button(newWindow,text="New game",width=16,command=new_game)
    b1.grid(row=1,column=0,pady=10)
    b2=Button(newWindow,text="Exit game",width=16,command=exit_game)
    b2.grid(row=1,column=10,pady=10)

def new_game():
    stop_time()
    global state_of_btn
    global nr_bombs
    global nr_open_cell
    nr_open_cell=0
    nr_bombs=30
    l2.config(text=nr_bombs)
    files2=[]
    map1=["*"]*30
    map2=['']*150
    map=map1+map2
    shuffle(map)
    show(map,15)
    map=create_borders(map)
    show(map,17)
    map=arange_numbers(map)
    show(map,17)

    for i in map:
        files2.append(str(i))
        # print('map[',i,'] =',map[i])

    give_color = {
        "*":'black',
        '1':'blue',
        '2':'green',
        '3':'red',
        '4':'brown',
        '5':'brown',
        '6':'brown',
        '-':'brown',
        '':'brown'
    }
    for i in range(len(files2)):
        label[i].config(text=files2[i],bg='linen')
        if label[int(i)].cget('text') in ['1','2','3','4']:
            label[int(i)].config(bg="grey85",fg=give_color[files2[i]])

    arrange_buttons()
    hide_borders()

    for i in range(len(files)):
        if btn[i].cget('text') == 'X':
            btn[i].config(text=i,fg='grey95')

    state_of_btn=[]
    for i in range(238):
        state_of_btn.append(False)

    try:
        newWindow.destroy()
    except NameError:
        pass

def exit_game():
    print('exit')
    window.destroy()

def you_lose():
    stop_time()

    l1.after(1000)
    for i in range(238):
        if (label[int(i)]).cget('text') == '*':
            btn[int(i)].grid_forget()
            label[int(i)].config(bg="red")

    you_lose_window()

def you_win_window():
    #stop timer
    global temp
    show_time.time_is_showing = False

    global winWindow
    winWindow = Toplevel(window)
    winWindow.title("you win")
    winWindow.geometry("+500+300")
    # newWindow.geometry("200x100")

    l1=Label(winWindow,text ="You win")
    l1.grid(row=0,column=8,pady=10)
    b1=Button(winWindow,text="New game",width=16,command=new_game)
    b1.grid(row=1,column=0,pady=10)
    b2=Button(winWindow,text="Exit game",width=16,command=exit_game)
    b2.grid(row=1,column=10,pady=10)

def show_time():
    global temp

    if show_time.time_is_showing == True:
        stopwatch_time=datetime.datetime.utcfromtimestamp(temp).strftime('%M:%S')
        temp+=1
        l1.config(text=stopwatch_time)
        l1.after(1000, show_time)

#use to know if the function was called
show_time.time_is_showing = False

def stop_time():
    global temp
    show_time.time_is_showing = False
    l1.config(text='00:00')
    temp=0

def atualaze_nr_bombs(nr):
    global nr_bombs
    nr_bombs=nr_bombs+nr
    l2.config(text=nr_bombs)

#---Interaction---------------
def expend_cell(i):
    if 0 >= int(i) >= 180:
        return False
    if label[int(i)].cget('text') == '*':
        return False
    if label[int(i)].cget('text') == '-':
        return False
    if btn[i].open == True:
        return False

    return True

def open_cell_aruound(i):
    #don't expend cell with numbers
    if int(label[int(i)].cget('text')) > 0:
        return

    i=int(i)

    if(expend_cell(i-16)):
        open_cell(i-16)
    if(expend_cell(i-17)):
        open_cell(i-17)
    if(expend_cell(i-18)):
        open_cell(i-18)
    if(expend_cell(i-1)):
        open_cell(i-1)
    if(expend_cell(i+1)):
        open_cell(i+1)
    if(expend_cell(i+16)):
        open_cell(i+16)
    if(expend_cell(i+17)):
        open_cell(i+17)
    if(expend_cell(i+18)):
        open_cell(i+18)

def open_cell(i):
    print('btn[i].open =',btn[int(i)].open)
    btn[int(i)].open=True
    global nr_open_cell
    nr_open_cell=nr_open_cell+1
    print('nr_open_cell =',nr_open_cell)
    print('btn[i].open =',btn[int(i)].open)

    if show_time.time_is_showing==False:
        show_time.time_is_showing=True
        show_time()
    if 0 > int(i) > 180:
        return

    btn[int(i)].grid_forget()
    if(label[int(i)]).cget('text') == '':
        label[int(i)].config(bg="grey95",fg="gray95",text='0')
        open_cell_aruound(i)
    if(label[int(i)]).cget('text') == '*':
        you_lose()

    if nr_open_cell == 150:
        print('trigger you_win_window')
        you_win_window()

def put_x(e,i):
    if show_time.time_is_showing == False:
        show_time()

    global state_of_btn
    print('state_of_btn[',i,'] =',state_of_btn[i])

    if state_of_btn[i] != True:
        btn[i].config(text="X",fg='black')
        print('config one')
        atualaze_nr_bombs(-1)
    else:
        btn[i].config(text=i,fg='linen')
        print('config two')
        atualaze_nr_bombs(1)

    state_of_btn[i] = not state_of_btn[i]
    print('state_of_btn[',i,'] =',state_of_btn[i], "after changing\n")

#---------------------------

def create_top():
    global l1,b1,l2
    l1=Label(window,text="00:00")
    l1.grid(row=0,column=0,columnspan=7,ipadx=35,ipady=3)
    b1=Button(window,text="New game",command=new_game)
    b1.grid(row=0,column=7,columnspan=3,padx=0,pady=5)
    l2=Label(window,text=nr_bombs)
    l2.grid(row=0,column=11,columnspan=3,ipadx=0,ipady=3)

def count_bombs(m,elem):
    bombs=0
    if m[elem-16] =="*":
        bombs+=1
    if m[elem-17] =="*":
        bombs+=1
    if m[elem-18] =="*":
        bombs+=1

    if m[elem-1] =="*":
        bombs+=1
    if m[elem+1] =="*":
        bombs+=1

    if m[elem+16] =="*":
        bombs+=1
    if m[elem+17] =="*":
        bombs+=1
    if m[elem+18] =="*":
        bombs+=1

    if int(bombs) != 0:
        return bombs
    else:
        return ''

def show(m,lenght):
    print('show')
    n=m.copy()
    while len(n) >= lenght:
        for i in range(lenght):
            if n[i]=='':
                print(' ', end='|')
            else:
                print(n[i], end='|')
        del n[:lenght]
        print('')
    print('Show function end.','ramain ', len(n), '.', 'Elements in field: ', len(m))

def to_bideminsional(m,elem):
    print('to_bideminsional')
    n=m.copy()
    bi_n=[]

    for i in range(int(len(n)/elem)):
        bi_n.append(n[:elem])
        del n[:elem]
    print('to_bideminsional_end')

    return bi_n

def to_list(m):
    print('to_list')
    n=m.copy()
    l=[]
    for i in range(len(n)):
        for j in range(len(n[i])):
            l.append(n[i][j])
    print('to_list_end')
    return l
#---------------------------------
def create_borders(m):
    print('create_borders')
    n=m.copy()
    n=to_bideminsional(n,15)

    for i in range(len(n)):
        n[i].append('-')#left
        n[i].insert(0,'-')#right
    n.append(['-']*17)#bottom
    n.insert(0,['-']*17)#top

    n=to_list(n)
    print('create_borders_end')

    return n

def delete_borders(m):
    print('delete_borders')
    n=m.copy()
    while '-' in n:
        n.remove('-')
    print('delete_borders_end')
    return n

def arange_numbers(m):
    n=m.copy()
    print('arange_numbers')
    for i in range(len(n)):
        if n[i]!="*" and n[i]!='-':
            n[i]=count_bombs(n,i)
    print('arange_numbers_end')
    return n

def hide_borders():
    for i in range(238):
        if label[i].cget('text') == '-':
            label[i].grid_forget()
            btn[i].grid_forget()

def create_field():
    print('create_field')
    #plant 35 bombs in fiels map
    map1=["*"]*30
    map2=['']*150
    map=map1+map2
    #shake the list map
    shuffle(map)

    show(map,15)
    #createborders
    map=create_borders(map)
    show(map,17)
    #put the numbers around the bombs
    map=arange_numbers(map)
    show(map,17)
    #delete_borders
    # map=delete_borders(map)
    # show(map,17)

    for i in map:
        files2.append(str(i))
    print('create_field_end')

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
        '6':'brown',
        '-':'brown',
        '':'brown'
    }
    for i in range(len(files2)):
        label.append(Label(window,text=files2[i],fg=give_color[files2[i]],width=2))
        if label[int(i)].cget('text') in ['1','2','3','4']:
            label[int(i)].config(bg="grey85")

    #arange all label in the window
    for j in range(0,14):
        for i in range(17*j,17*(j+1)):
            # print(j, ' ', i)
            label[i].grid(row=j+1,column=i-17*j)

def arrange_buttons():
    #create (238)180 buttons with text
    for i in range(238):
        files.append(str(i))

    for i in range(len(files)):
        btn.append(Button(window,text=files[i],width=2,fg="gray95",command=lambda c=i:open_cell(btn[c].cget("text"))))
        btn[i].bind("<Button-3>",lambda e,i=i:put_x(e,i))
        btn[i].open=False#important

    #arange all button in the window
    for j in range(0,14):
        for i in range(17*j,17*(j+1)):
            # print(j, ' ', i)
            btn[i].grid(row=j+1,column=i-17*j)

def init_window():
    create_top()
    arrange_labels()
    arrange_buttons()
    hide_borders()

init_window()

window.mainloop()
