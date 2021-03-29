from tkinter import *
from tkinter.filedialog import *
from tkinter import filedialog
from tkinter.messagebox import showerror

filename = None
root = Tk()

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
    
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.clsoe()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")
        
def openFile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def black():
    root['bg'] = 'black'

def green():
    root['bg'] = 'green'

def white():
    root['bg'] = 'white'

def red():
    root['bg'] = 'red'

def blue():
    root['bg'] = 'blue'


root.title("Text Editor")
root.iconbitmap(r"notebook.ico")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400, )
text.pack()

menubar = Menu(root)
filemenu2= Menu(menubar)
filemenu2.add_command(label="Black", command=black)
filemenu2.add_command(label="White", command=white)
filemenu2.add_command(label="Blue", command=blue)
filemenu2.add_command(label="Red", command=red)
filemenu2.add_command(label="Green", command=green)
filemenu2.add_separator()
menubar.add_cascade(label="Background Colour", menu=filemenu2)

filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()