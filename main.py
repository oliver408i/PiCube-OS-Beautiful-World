print('<early_loading> load_modules')
import tkinter as tk
import threading, time, os, sys, mainmenu
from PIL import Image, ImageTk
window = tk.Tk()
window.title("PiCube")
window.geometry("300x300")
#'''TopMost
topmost = False #
if topmost:
    window.attributes("-topmost", True)
#'''
lock = True
# Load logind
logind_data = {}
with open("logind","r") as f:
    for i in f.readlines():
        i = i.split(" ")
        logind_data[i[0]] = i[1]

def fullscreen():
    window.attributes("-fullscreen", not window.attributes("-fullscreen"))
def lock():
    global lock
    while 1:
        if lock:
            if not window.attributes("-fullscreen"):
                window.attributes("-fullscreen", True)
t = threading.Thread(target=lock)
t.daemon = True
t.start()

logind = None

#--------------

transparent_image = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
transparent_photo = ImageTk.PhotoImage(transparent_image)
#--------------
window.attributes('-alpha', 0)
image1 = Image.open("assets/bg.png")
print('<PIL.image_handler>',image1.size)
image1 = image1.resize((688+500, 430+500), Image.LANCZOS)
bgp = ImageTk.PhotoImage(image1)
bg = tk.Label(image=bgp)
bg.place(x=0,y=0)

def logout():
    global logind, username, password, logind_label
    clear()
    msg = tk.Label(frame,text="Signing out...")
    msg.pack()
    print("<logind.service> logout_user")
    print("<logind.service>",logind)
    username, password, logind_label = mainmenu.showMenu(frame,login)
    logind = None
    msg.destroy()
    
    
def login():
    global logind
    try:
        if logind_data[username.get()] == password.get():
            logind = username.get()
            clear()
            
            print("<logind.service> login_as")
            print("<logind.service>",logind)
            mainmenu.showDesktop(frame,logind,logout)
        else:
            print("<logind.service> user_password_error")
            logind_label.config(text="Bad username or password")
    except KeyError as e:    
        print("<logind.service> user_exist_error")
        print("<logind.service>",e)
        logind_label.config(text="Bad username or password")
    
print('<early_loading> init_graphical')
#'''
frame = tk.Frame(window)

frame.place(x=100,y=200)


username, password, logind_label = mainmenu.showMenu(frame,login)
#'''


class objects:
    class spacer:
        def new(size=1):
            spacer = tk.Label(text='\n'*size)
            spacer.pack()


def shutdown():
    print('<Shutdown>')
    window.destroy()
    raise SystemExit
def restart():
    window.destroy()
    print('<Restart>')
    os.execl(sys.executable, sys.executable, *sys.argv)
    raise SystemExit
def clear(parent=frame):
    for i in parent.winfo_children():
        i.destroy()
    

shutdown_button = tk.Button(text='Shutdown',command=shutdown)
restart_button = tk.Button(text='Restart',command=restart)
toggled = False
def toggle_more():
    global toggled
    if toggled == False:
        shutdown_button.pack()
        restart_button.pack()
        more.config(text='Power')
        toggled = True
    elif toggled == True:
        shutdown_button.pack_forget()
        restart_button.pack_forget()
        more.config(text='Power')
        toggled = False
        
    print(f'<Toggle_Power_Options [{toggled}]>')

objects.spacer.new()
more = tk.Button(text="Power",command=toggle_more,background='red')
more.pack()




#'''
class disable_window_close:
    def disable_event():
        pass
    window.protocol("WM_DELETE_WINDOW", disable_event)
tk.mainloop()
