import colorama
window = None
def __init__(workingspace):
    global window
    window = workingspace
def run():
    print(colorama.Fore.RED+"Colorama is cool!"+colorama.Fore.RESET)