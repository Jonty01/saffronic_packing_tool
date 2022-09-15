"""Create the window and widgets"""

import shutil
import os
from tkinter import END, Tk, filedialog, messagebox, StringVar, IntVar, Button, Entry, Checkbutton, W
import openpyxl

# List Of Checkbox Items
copy_cases = ["Copy Source Images", "Copy Renders"]
check = []

# Creating object of tk class
window = Tk()

# Setting the title and background color
# disabling the resizing property
window.geometry("830x320")
window.title("Saffronic Packing Tool")
window.config(background="white")

# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()


def SourceBrowse():
    """Opening the file-dialog directory prompting the
    user to select files to copy using
    filedialog.askopenfilenames() method. Setting
    initialdir argument is optional Since multiple
    files may be selected, converting the selection
    to list using list(), also deleting the previous
    entry already there in the textbox"""

    window.sourceText.delete(0, END)
    window.file_list = list(filedialog.askopenfilenames(initialdir="C:/"))

    # Displaying the selected files in the window.sourceText
    # Entry using window.sourceText.insert()
    window.sourceText.insert("0", window.file_list)

def xlBrowse():
    window.sourceText.delete(0, END)
    window.file_list=list(filedialog.askopenfilenames(filetypes=[("Excel Files", "*.xlsx")]))
    # window.file_list=filedialog.askopenfilenames(filetypes=[("Excel Files", "*.xlsx")])
    # strvar=StringVar()
    # strvar.set(window.file_list)
    # sourceLocation.set(filedialog.askopenfilename(filetypes=["Excel Files", "*.xlsx"]))
    window.sourceText.insert('0', window.file_list)
    # window.sourceText.insert('0', window.file_list)
    # if len(window.file_list)==1:
    #     print("equal to 1")
    #     window.sourceText.insert('1', window.file_list)
    # else:
    #     window.sourceText.insert(0, window.file_list)

def DestinationBrowse():
    """Opening the file-dialog directory prompting
    the user to select destination folder to
    which files are to be copied using the
    filedialog.askopendirectory() method.
    Setting initialdir argument is optional"""
    window.destinationText.delete(0, END)
    destinationdirectory = filedialog.askdirectory(initialdir="C:/")

    # Displaying the selected directory in the
    # window.destinationText Entry using
    # window.destinationText.insert()
    # window.destinationText.insert("1", destinationdirectory)
    window.destinationText.insert("0", destinationdirectory)


def CopyFile():
    """Retrieving the source file selected by the
    user in the SourceBrowse() and storing it in a
    variable named file_list Retrieving the destination location from the
    textvariable using destinationLocation.get() and
    storing in destination_location
    """
    file_list = window.file_list
    dataframe=openpyxl.load_workbook(file_list[0])  #reads only first excel file
    dataframe1=dataframe.active

    destination_location = destinationLocation.get()

    # Looping through the files present in the list
    #for f in file_list:

        # Copying the file to the destination using
        # the copy() of shutil module copy take the
        # source file and the destination folder as
        # the arguments
        #shutil.copy(f, destination_location)
    
    for i in range(2, dataframe1.max_row+1):
        f=dataframe1.cell(row=i, column=1).value
        # shutil.copy(f, destination_location)
        if(f==None):
            continue
        shutil.copy(f, destination_location)

    for i in range(2, dataframe1.max_row+1):
        for j in range(2, dataframe1.max_column+1):
            if(check[j-2].get()==1):
                f=dataframe1.cell(row=i, column=j).value
                if(f==None):
                    continue
                shutil.copy(f, destination_location)

    # check in one loop
    messagebox.showinfo("Copied", "Files copied successfully")


def MoveFile():
    """Retrieving the source file selected by the
    user in the SourceBrowse() and storing it in a
    variable named file_list
    Retrieving the destination location from the
    textvariable using destinationLocation.get() and
    storing in destination_location"""

    file_list = window.file_list
    destination_location = destinationLocation.get()

    # Looping through the files present in the list
    for f in file_list:

        # Moving the file to the destination using
        # the move() of shutil module copy take the
        # source file and the destination folder as
        # the arguments
        shutil.move(f, destination_location)

    #  messagebox.showinfo("SUCCESSFUL")


# Create widgets
source_browseButton = Button(
    window, text="Input Path", command=xlBrowse, width=15, bg="#90ee90", fg="black"
)
source_browseButton.grid(row=2, column=0, pady=15, padx=15)

window.sourceText = Entry(window, width=50, textvariable=sourceLocation)
window.sourceText.grid(row=2, column=1, pady=15, padx=15, columnspan=2)

dest_browseButton = Button(
    window,
    text="Destination Path",
    command=DestinationBrowse,
    width=15,
    bg="#90ee90",
    fg="black",
)
dest_browseButton.grid(row=3, column=0, pady=15, padx=15)

window.destinationText = Entry(window, width=50, textvariable=destinationLocation)
window.destinationText.grid(row=3, column=1, pady=15, padx=15, columnspan=2)

window.copyButton = Button(
    window, text="Submit", command=CopyFile, width=15, bg="#8FBC8F", fg="black"
)
window.copyButton.grid(row=7, column=1, pady=5, padx=5)

window.moveButton = Button(
    window, text="Quit", command=exit, width=15, bg="#FFCCCB", fg="black"
)
window.moveButton.grid(row=7, column=2, pady=5, padx=5)

for x, n in enumerate(copy_cases):
    check.append(IntVar(window, value=0))
    cb = Checkbutton(window, text=n, variable=check[x])
    cb.grid(row=x + 4, column=0, sticky=W, padx=10, pady=10)
    # check.append(tk.Checkbutton(window, text=n))
    # check[x].grid(row=x+4, column=0, sticky=W, padx=10, pady=10)


# Defining infinite loop
window.mainloop()
