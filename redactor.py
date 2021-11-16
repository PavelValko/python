import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox


FILE_NAME = tkinter.NONE


def new_file():
    pass


def delete():
    global FILE_NAME
    FILE_NAME = 'Untitled'
    text.delete(1.0, tkinter.END)


def save_file():
    data = text.get(1.0, tkinter.END)
    with open(FILE_NAME, 'w') as f:
        f.write(data)


def save_as_file():
    file = asksaveasfile(mode='w', defaultextension='txt')
    data = text.get(1.0, tkinter.END)
    try:
        file.write(data.rstrip())
    except Exception:
        showerror(title='Error', message='Saving error')


def open_file():
    global FILE_NAME
    file = askopenfile(mode='r')
    if file is None:
        return
    FILE_NAME = file.name
    data = file.read()
    text.delete(1.0, tkinter.END)
    text.insert(1.0, data)


def info():
    messagebox.showinfo('Information', 'Text Editor\nBy Pavel Valko')


run = tkinter.Tk()
run.title('Text Editor')

run.minsize(width=500, height=500)
run.maxsize(width=1920, height=1080)

text = tkinter.Text(run, width=400, height=400, wrap='word')
scroll_bar = Scrollbar(run, orient=VERTICAL, command=text.yview)
scroll_bar.pack(side='right', fill='y')
text.configure(yscrollcommand=scroll_bar.set)


text.pack()

menuBar = tkinter.Menu(run)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label='New', command=new_file)
fileMenu.add_command(label='Open', command=open_file)
fileMenu.add_command(label='Save', command=save_file)
fileMenu.add_command(label='Save as...', command=save_as_file)
fileMenu.add_command(label='Delete', command=delete)

menuBar.add_cascade(label='File', menu=fileMenu)
menuBar.add_cascade(label='Info', command=info)
menuBar.add_cascade(label='Exit', command=run.quit)
run.config(menu=menuBar)

run.mainloop()


