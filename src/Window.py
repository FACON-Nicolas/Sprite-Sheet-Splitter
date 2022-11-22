import tkinter
import os

from tkinter import filedialog


class Singleton():

    __instance = None

    def __new__(self, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = super(Singleton, self).__new__(self, *args, **kwargs)
        return Singleton.__instance

class Window(Singleton):
    """
    
    Window class used to create a window in Python for a Sprite Sheet Splitter.

    This class is a sub-class from Singleton class, the Singleton
    is a design pattern used to create an unique instance for an 
    object, there, the Singleton is a metaclass created just to
    avoid many instance of Window class (1 Window per App).

    """

    WIDTH = 1600
    HEIGHT = 900
    WINDOW = tkinter.Tk()

    def __new__(self, *args, **kwargs):
        """
        
        __new__() method for Window class.

        This method is called at each new call for an instance creation,
        in this case, it use the Singleton.__new__() method which avoid
        the creation of many Window by returning the current instance if
        it exists in the program, if the instance doesn't exist, Singleton
        __new__() method creates an instance, initializes the window's size
        and the window's title and keeps the window on __instance attribute.

        """
        instance = super().__new__(self, *args, **kwargs)
        instance.WINDOW.geometry(str(Window.WIDTH)+"x"+str(Window.HEIGHT))
        instance.WINDOW.title('Sprite Sheet Splitter')
        return instance

    def browse_file(self):
        """
        
        browse a file in your file explorer.

        This method calls filedialog from Tkinter to get an access to
        your explorer file, by this access it's possible to choose an
        image file (PNG, JPG, JPEG) and the file's ubsolute path is 
        returned at the end of the function. 
        
        """
        filename = filedialog.askopenfilename(
            initialdir=os.path.expanduser("~"),
            title="Select an image",
            filetypes=(
                ("PNG", "*.png*"),
                ("JPEG", "*.jpeg*"),
                ("JPG", "*.jpg*")
            )
        ) 

        l.configure(text="File Opened: "+filename)
        l.pack()
        return filename


if '__main__' == __name__:
    w = Window()
    b = tkinter.Button(w.WINDOW, text="Text", command=w.browse_file)
    l = tkinter.Label(w.WINDOW, text="", width=100, height=100, fg='blue')
    b.pack()
    w.WINDOW.mainloop()