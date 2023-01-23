import tkinter as tk
def run():
    global window
    window=tk.Tk()
    window.title("Confirm")
    window.geometry("100x50")
    def clear():
        import os
        os.sys("clear")
    tk.Label(window, text='Are you sure you want to clear the terminal?').pack()
    tk.Button(window, text='Yes', command=clear).pack()
    tk.Button(window, text='No',command=close).pack
def __init__(workingspace):
    global window
    #window = workingspace
def close():
    global window
    window.destroy()
    quit()