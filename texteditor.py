import os
from tkinter.filedialog import *
import win32api
from tkinter import filedialog, messagebox, Scrollbar
from time import sleep
from ttkthemes import ThemedTk
import tkinter as tk
import pyperclip

filename = None
root = ThemedTk(theme="arc")
w = Scrollbar(root)
w.pack(side=RIGHT, fill=Y)





def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def saveFile():
    try:
        global filename
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
        alert("Info", "Saved File")
    except Exception as e:
        print(e)
        alert("Error!", "Error Occurred While Saving..", kind="warning")


def saveAs():
    try:
        f = asksaveasfile(mode='w', defaultextension='.txt', filetypes = (("Text Files","*.txt"), ("Python", "*.py"), ("All Files","*.*")))
        t = text.get(0.0, END)
        f.write(t.rstrip())
    except Exception as e:
        print(e)
        alert("Error!", "Error Occurred While Saving..", kind="warning")





def openFile():
    try:
        global filename
        f = filedialog.askopenfile(mode='r', filetypes = (("Text Files","*.txt"), ("Python", "*.py"), ("All Files","*.*")))
        t = f.read()
        filename = f.name
        text.delete(0.0, END)
        text.insert(0.0, t)
        sleep(0.5)
        alert("Info", "File Opened Successfully!")
    except Exception as e:
        print(e)
        alert("Error!", "Error Occurred While Opening File..", kind="warning")


def darkOn():
    root.theme = 'scidgrey'
    alert("Changed!", "Dark Mode Is Now On!")


def darkOff():
    root.theme = "arc"
    text.bg = 'black'
    alert("Changed!", "Dark Mode Is Now Off!")

def tab():
    text.insert(tk.INSERT, " " * 4)
    return 'break'

def copy():
    input = text.get(1.0, END)
    pyperclip.copy(input)

def cut():
    input = text.get(0.0, END)
    pyperclip.copy(input)
    text.delete(1.0, END)


def undo():
    text.edit_undo()
    return

def redo():
    text.edit_redo()
    return

def delete():
    text.delete(0.0, END)

def select():
    text.tag_add("sel", "1.0", "end")

def quit():
    global filename
    if filename is None:
        pass
    else:
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
        root.quit()



def print_file():
    global filename
    try:
        if filename is None:
            file_to_print = filedialog.askopenfilename(
                initialdir="/", title="Select file",
                filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

            if file_to_print:
                win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
        else:
            win32api.ShellExecute(0, "print", filename, None, ".", 0)
    except Exception as e:
        alert("Error!", e, kind="error")


root.geometry("200x400")
root.title("Text Editor")
root.iconbitmap(r"notebook.ico")
root.minsize(width=400, height=400)
root.maxsize(width=root.winfo_screenwidth(), height=root.winfo_screenheight())

text = Text(root, width=400, height=400, yscrollcommand = w.set, undo=True)
text.pack()
text.bind("<Tab>", tab)
text.bind("<Control-c>", copy)
text.bind("<Control-z>", undo)

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_command(label="Print", command=print_file)
menubar.add_cascade(label="File", menu=filemenu)

filemenu2 = Menu(menubar)
filemenu2.add_command(label="On", command=darkOn)
filemenu2.add_command(label="Off", command=darkOff)
menubar.add_cascade(label="Dark/Light Mode", menu=filemenu2)

textediting = Menu(menubar)
textediting.add_command(label="Copy", command=copy)
textediting.add_command(label="Cut", command=cut)
textediting.add_command(label="Undo", command=undo)
textediting.add_command(label="Redo", command=redo)
textediting.add_command(label="Select All Text", command=select)
textediting.add_command(label="Delete All Text", command=delete)
menubar.add_cascade(label="Text Options", menu=textediting)

menubar.add_command(label="Quit", command=root.quit)

root.config(menu=menubar)
root.mainloop()
