import tkinter
import tkinter.ttk as ttk
import os

from tkinter import filedialog


class Singleton():

    __instance = None

    def __new__(self, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = super(Singleton, self).__new__(self, *args, **kwargs)
        return Singleton.__instance

class Window(Singleton):

    WIDTH = 1600
    HEIGHT = 900
    WINDOW = tkinter.Tk()

    def __new__(self, *args, **kwargs):
        instance = super().__new__(self, *args, **kwargs)
        instance.WINDOW.geometry(str(Window.WIDTH)+"x"+str(Window.HEIGHT))
        instance.WINDOW.title('Sprite Sheet Splitter')
        return instance

    def browse_file():
        filename = filedialog.askopenfilename(
            initialdir=os.path.expanduser("~"),
            title="Select an image",
            filetypes=(
                ("PNG", "*.png*"),
                ("JPEG", "*.jpeg*"),
                ("JPG", "*.jpg*")
            )
        )

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = os.path.expanduser('~'),
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    l.configure(text="File Opened: "+filename)
    l.pack()

if '__main__' == __name__:
    w = Window()
    b = tkinter.Button(w.WINDOW, text="Text", command=browseFiles)
    l = tkinter.Label(w.WINDOW, text="", width=100, height=100, fg='blue')
    b.pack()
    w.WINDOW.mainloop()