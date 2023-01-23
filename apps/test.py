import tkinter as tk
window = None
def __init__(workingspace):
    global window
    window = workingspace
def run():
    tk.Label(window,text='Test app').pack()
def close():
    pass