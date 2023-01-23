class Launcher:
    @staticmethod
    def launchImport(file):
        try:
            __import__(file)
        except:
            return 0
        return 1
launcher = Launcher()
def clear(frame):
    for i in frame.winfo_children():
        i.destroy()