import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import shutil

class AnotherWindow:
    def __init__(self, master) -> None:
        self.master = master
        self.frame = tk.Frame(self.master)
        # self.label = tk.Label(self.frame, text="This is another window")
        # self.label.pack()
        # self.button = tk.Button(self.frame, text="Close", command=self.close_window)
        # self.button.pack()
        # self.frame.pack()
    
    def close_window(self):
        self.master.destroy()
    
    def createNecessaryWidgets(self):
        # Create the necessary widgets
        global inputPath, outputPath, inputPathButton, outputPathButton, startButton, quitButton
        inputPath = Entry(self.master, width=50, borderwidth=5, textvariable=sourceLocation)
        outputPath = Entry(self.master, width=50, borderwidth=5, textvariable=destinationLocation)
        inputPathButton = Button(self.master, text="Input Path", width=15, bg="#90ee90", fg="black", command=self.getInputPath)
        outputPathButton = Button(self.master, text="Output Path", width=15, bg="#90ee90", fg="black", command=self.getOutputPath)
        startButton = Button(self.master, text="Submit", width=15, bg="#8FBC8F", fg="black", command=self.start)
        quitButton= Button(self.master, text="Quit", width=15, bg="#FFCCCB", fg="black", command=self.master.destroy)

    # def getInputPath(self):
    #     # Get the input path
    #     global inputPath
    #     self.master.file_list=list(filedialog.askopenfilenames(initialdir="C:/"))
    #     # inputPath.delete(0, END)

    #     inputPath.insert('1', self.master.file_list)

    def getInputPath(self):
        # Get the input path
        global inputPath
        self.master.file_list=list(filedialog.askopenfilenames(initialdir="C:/"))
        # inputPath.delete(0, END)

        inputPath.insert('1', self.master.file_list)

    def getOutputPath(self):
        # Get the output path
        global outputPath
        outputPath.delete(0, END)
        outputPath.insert(0, filedialog.askdirectory())

    def start(self):
        # Start the program
        global inputPath, outputPath
        inputPath = inputPath.get()
        outputPath = outputPath.get()
        if inputPath == "" or outputPath == "":
            messagebox.showerror("Error", "Please select a path")
        else:
            # Do stuff
            pass

if __name__ == "__main__":
    window=Tk()
    window.geometry("830x320")
    window.title("Saffronic Packing Tool")
    window.config(background = "white")
    sourceLocation = StringVar()
    destinationLocation = StringVar()

    app=AnotherWindow(window)
    app.createNecessaryWidgets()
    inputPath.grid(row=0, column=1, padx=20, pady=20)
    outputPath.grid(row=1, column=1, padx=20, pady=20)
    inputPathButton.grid(row=0, column=0, padx=15, pady=15)
    outputPathButton.grid(row=1, column=0, padx=15, pady=15)
    startButton.grid(row=2, column=0, padx=5, pady=5)
    quitButton.grid(row=2, column=1, padx=5, pady=5)
    window.mainloop()