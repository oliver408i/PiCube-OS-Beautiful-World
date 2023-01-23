import tkinter as tk
def run():
    global window
    window=tk.Tk()
    window.title("PiCube Test Window")
    window.geometry("200x200")
    class executedCode:
        placeholder = tk.Label(window, text='Placeholder Label').pack()
def __init__(workingspace):
    global window
    #window = workingspace
def close():
    global window
    window.destroy()
    quit()