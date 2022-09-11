import tkinter
from tkinter import Button, Label, filedialog

window = tkinter.Tk()
window.title("File Browser")
window.geometry('700x500')


def open_file():
    file = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    print(file)


bt1 = Button(window,
             text="Input Path",
             bg="green",
             fg="white",
             command=open_file)
bt1.grid(column=0, row=0)
bt2 = Button(window,
             text="Output Path",
             bg="green",
             fg="white",
             command=open_file)
bt2.grid(column=0, row=2)
window.mainloop()
