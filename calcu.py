from tkinter import *
from tkinter import ttk
from tkinter import messagebox
form = Tk()
form.title('Simple Calculator')
form.geometry('680x370')
form.maxsize(900, 350)
form.minsize(680, 370)
form.config(bg = 'yellow')
fnt = 'none 30 bold'

form.iconbitmap('D:\py\projects\Calculator\C.ico')

Lnum1 = Label(form, text = 'Number 1:', font = fnt, bg = 'lightgreen')
Lnum2 = Label(form, text = 'Number 2:', font = fnt, bg = 'lightgreen')

sv1 = StringVar()
sv2 = StringVar()

Tnum1 = Entry(form, font = fnt, bg = '#0aafff' , textvariable = sv1)
Tnum2 = Entry(form, font = fnt, bg = '#0aafff' , textvariable = sv2)

Lnum1.grid(row = 0, column = 0, padx = 10, pady = 10)
Tnum1.grid(row = 0, column = 1)
sv1.set('1')

Lnum2.grid(row = 1, column = 0, padx = 10, pady = 10)
Tnum2.grid(row = 1, column = 1)
sv2.set('1')

frame = Frame(form)

from tkinter import messagebox

def calc(ope):
    strt1 = str(Tnum1.get())
    strt2 = str(Tnum2.get())
    n1 = int(strt1)
    n2 = int(strt2)
    r = 0
    if ope == '+':
        r = n1 + n2
    elif ope == '-':
        r = n1 - n2
    elif ope == '*':
        r = n1 * n2
    else:
        if n2 == 0 :
            n2 = 1
            messagebox.showerror('Error', "Error By Zero ^ Number 2 = 1")
        r = n1 / n2
    Lr['text'] = ('Result: %s %s %s = %s' % (n1, ope, n2,round(r,4) ))
    
        
    
btn_width = 5

btns = ttk.Style()
btns.configure('TButton',font= 'none 20 bold', bg = 'red', padding = 15)

B1 = ttk.Button(frame, text = '+', width = btn_width, command = lambda:calc('+'))
B2 = ttk.Button(frame, text = '-', width = btn_width, command = lambda:calc('-'))
B3 = ttk.Button(frame, text = '*', width = btn_width, command = lambda:calc('*'))
B4 = ttk.Button(frame, text = '/', width = btn_width, command = lambda:calc('/'))

frame.grid(row = 2, column = 0, columnspan = 2, pady = 10)

B1.grid(row = 0, column = 0)
B2.grid(row = 0, column = 1)
B3.grid(row = 0, column = 2)
B4.grid(row = 0, column = 3)

Lr = Label(frame, text = 'Result:', font = 'tahoma 20')
Lr.grid(row = 1, column = 0,columnspan = 4, pady = 10)

f = Frame(form)
f.grid(row = 3, column = 0, columnspan = 4)

def C():
    sv1.set('')
    sv2.set('')
    Tnum1.focus()

clear = Button(f, text = 'Clear', font = 'consolas 20 bold' , bg = '#0aafff', command = C)
clear.grid(row = 0, column = 1)

def info():
    messagebox.showinfo('Info','             ( Simple Calculator )\n\nThis Proggrame Made By DZ hacker\n\n             Thanks For Use It :)')

info = Button(f, text = 'Info', font = 'consolas 20 bold' , bg = 'green' ,  command = info)
info.grid(row = 0, column = 0)

def des():
    form.destroy()



Button(f, text = 'Exit', bg = 'red' , font = 'consolas 20 bold' ,command = des).grid(row = 0, column = 2)









form.mainloop()
