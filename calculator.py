from tkinter import *
window = Tk()
window.title("Simple Calculator")
icon = PhotoImage(file = 'calculator_icon.png')
window.iconphoto(True,icon)

entry = Entry(window,borderwidth = 5,width = 47)
entry.grid(row = 0,column = 0,columnspan = 4)

prev = 0
op = '+'
def click(n):
    entry.insert(len(entry.get()),n)
def add():
    global op,prev
    op = '+'
    if entry.get()=='':
        return
    prev = float(entry.get())
    entry.delete(0,END)

def mul():
    global op,prev
    op = 'x'
    if entry.get()=='':
        return
    prev = float(entry.get())
    entry.delete(0,END)

def sub():
    global op,prev
    op = '-'
    if entry.get()=='':
        return
    prev = float(entry.get())
    entry.delete(0,END)

def div():
    global op,prev
    op = '/'
    if entry.get()=='':
        return
    prev = float(entry.get())
    entry.delete(0,END)

def equal():
    global prev,op
    if entry.get()=='':
        return
    cur = float(entry.get())
    if op == '+':
        res = prev+cur
    elif op == 'x':
        res = prev*cur
    elif op == '-':
        res = prev-cur
    else:
        res = prev/cur
    entry.delete(0,END)
    if res == int(res):
        res = int(res) 
    entry.insert(0,res)
    prev = res

def dot():
    entry.insert(len(entry.get()),'.')
def clear():
    global op,prev
    prev = 0
    entry.delete(0,END)

def back():
    entry.delete(len(entry.get())-1,END)

Button(window,text = 'C',bg = 'grey',activebackground = 'grey',padx = 66,pady = 15,command = clear).grid(row = 1,column = 0,columnspan = 2)
Button(window,text = 'B',bg = 'grey',activebackground = 'grey',padx = 30,pady = 15,command = back).grid(row = 1,column = 2)
Button(window,text = '/',bg = 'grey',activebackground = 'grey',padx = 31,pady = 15,command = div).grid(row = 1,column = 3)

Button(window,text = '7',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(7)).grid(row = 2,column = 0)
Button(window,text = '8',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(8)).grid(row = 2,column = 1)
Button(window,text = '9',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(9)).grid(row = 2,column = 2)
Button(window,text = 'x',bg = 'grey',activebackground = 'grey',fg = 'black',padx = 31,pady = 17,command = mul).grid(row = 2,column = 3)

Button(window,text = '4',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(4)).grid(row = 3,column = 0)
Button(window,text = '5',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(5)).grid(row = 3,column = 1)
Button(window,text = '6',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(6)).grid(row = 3,column = 2)
Button(window,text = '-',bg = 'grey',activebackground = 'grey',fg = 'black',padx = 31,pady = 17,command = sub).grid(row = 3,column = 3)

Button(window,text = '1',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(1)).grid(row = 4,column = 0)
Button(window,text = '2',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(2)).grid(row = 4,column = 1)
Button(window,text = '3',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(3)).grid(row = 4,column = 2)
Button(window,text = '+',bg = 'grey',activebackground = 'grey',fg = 'black',padx = 30,pady = 17,command = add).grid(row = 4,column = 3)

Button(window,text = '0',bg = 'grey',activebackground = 'grey',padx = 30,pady = 17,command = lambda:click(0)).grid(row = 5,column = 0)
Button(window,text = '.',bg = 'grey',activebackground = 'grey',padx = 31,pady = 17,command = dot).grid(row = 5,column = 1)
Button(window,text = '=',bg = 'grey',activebackground = 'grey',padx = 68,pady = 17,command = equal).grid(row = 5,column = 2,columnspan = 2)
window.mainloop()