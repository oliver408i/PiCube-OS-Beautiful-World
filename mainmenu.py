import tkinter as tk, utils,sys,copy
from os import listdir
from os.path import isfile, join
sys.path.insert(0, 'apps')
topMenu = None
top = None
appWindows = []
appContainer = None
def showMenu(window,login):
    print("<mainmenu.py> show_menu")
    title = tk.Label(window,text="PiCube Signin\n")
    title.pack()
    usernameLabel = tk.Label(window,text="Username:")
    usernameLabel.pack()
    username = tk.Entry(window)
    username.bind('<FocusIn>', lambda x:username.delete('0', 'end'))
    username.bind('<FocusOut>', lambda x:username.insert(0, '') if not username.get() else None)
    username.insert(0, '')
    username.pack()
    
    passwordLabel = tk.Label(window,text="Password:")
    passwordLabel.pack()
    password = tk.Entry(window)
    password.bind('<FocusIn>', lambda x:password.delete('0', 'end'))
    password.bind('<FocusOut>', lambda x:password.insert(0, '') if not password.get() else None)
    password.insert(0, '')
    password.pack()
    logind_label = tk.Label(window,text='')
    logind_label.pack()
    button = tk.Button(window,text='Unlock',command=login)
    button.pack()
    return username, password, logind_label
def closeApp(window,appFrame,sandbox,app):
    print('<apps.service> Closing app',app)
    try:
        app.close()
    except:
        pass
    sandbox.destroy()
    appFrame.destroy()
    showApps(top,False)
def launchApp(window,appFrame,app):
    print('<apps.service> Launching app',app.split('.')[:-1])
    utils.clear(appFrame)
    sandbox = tk.Frame(appFrame)
    sandbox.pack()
    try:
        app = __import__('.'.join(app.split('.')[:-1]))
        close = tk.Button(appFrame,text='Close app',command=lambda:closeApp(window,appFrame,sandbox,app))
        close.pack()
        app.__init__(sandbox)
        app.run()
    except Exception as e:
        print('<apps.service> App failure')
        print('<apps.service>',e)
def switch(dest):
    if dest == 'apps':
        appContainer.destroy()
        showApps(top,False)
def showApps(window,firstLaunch=True):
    global appContainer
    apps = [f for f in listdir('apps') if isfile(join('apps', f))]
    print('<apps.service>',apps)
    appFrame = tk.Frame(top,highlightbackground="blue", highlightthickness=2,width=500, height=500)
    appContainer = appFrame
    for i in apps:
        tk.Button(appFrame,text=i,command=lambda i=i:launchApp(top,appFrame,i)).pack()
    appFrame.pack(padx=20, pady=20)

def showDesktop(window,user,logout):
    global topMenu,top
    
    print("<mainmenu.py> show_desktop")
    label = tk.Label(window,text=f"Welcome {user}")
    label.pack()
    tk.Label(window,text='\nApps').pack()
    desktop = tk.Frame(window)
    desktop.pack()
    top =desktop
    topMenu = tk.Frame(desktop,highlightbackground="red", highlightthickness=2)
    topMenu.columnconfigure(1, weight=1)
    tk.Button(topMenu,text='App Launcher',command=lambda:switch('apps')).pack()
    topMenu.pack()
    showApps(desktop)
    logout = tk.Button(window,text="Log out",command=logout)
    logout.pack()
