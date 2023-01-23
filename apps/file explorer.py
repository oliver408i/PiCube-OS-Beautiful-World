import tkinter as tk
import sys, os, functools
from os import listdir
from os.path import isfile, join
sys.path.insert(0, 'apps')
def run():
    global window
    window=tk.Tk()
    window.title("File Explorer")
    window.geometry("400x250")
    appFrame = tk.Frame(window,highlightbackground="blue", highlightthickness=1,width=500, height=500)
    for i in listdir("apps"):
        hide_list = ["__pycache__"]
        if i not in hide_list:
            def open_file(i):
                def open_file_with_i():
                    print(open(i, "r").read())
                return open_file_with_i
            button = tk.Button(appFrame,text=i,command=open_file(f'apps/{i}'))
            button.pack()

    
    
    appFrame.pack(padx=20, pady=20)
def __init__(workingspace):
    global window
    #window = workingspace
def close():
    global window
    window.destroy()
    quit()

'''
Extras:
•
┌ ┐ ┘ └ ├ ┤ ┬ ┴ ┼ ─ |
█ ░ ▒ ▓
□ ▣
▖ ▗ ▘ ▝ ▙ ▚ ▛ ▜
▲►▼◄

Examples:

▼ Folder
├─▼ Expanded Folder
| ├─□ Unselected File
| └─▣ Selected File
└─► Unexpanded folder
'''