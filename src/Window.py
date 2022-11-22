import future.moves.tkinter as tkinter
import os

from future.moves.tkinter import filedialog


class Singleton:
    """

    Singleton class is used for the window class.

    The Singleton is a Design Pattern with which it's possible to create only
    one instance for a specific object. The functioning is easy, the class
    contains an instance attribute, if this instance is None then an instance
    is created, else nothing is done. After that, the unique instance is returned.

    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        """

        __new__() method for Window class.

        This method is called at each new call for an instance creation,
        in this case, to avoid the creation of many Singleton objects, if
        the instance doesn't exist, Singleton __new__() method creates an
        instance, and after that, the instance is returned at each call.

        :rtype: Singleton

        """
        if Singleton.__instance is None:
            Singleton.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return Singleton.__instance


class Window(Singleton):
    """
    
    Window class used to create a window in Python for a Sprite Sheet Splitter.

    This class is a subclass from Singleton class, the Singleton
    is a design pattern used to create a unique instance for an
    object, there, the Singleton is a metaclass created just to
    avoid many instance of Window class (1 Window per App).

    """

    WIDTH = 1600
    HEIGHT = 900
    WINDOW = tkinter.Tk()

    def __new__(cls, *args, **kwargs) -> Singleton:
        """
        
        __new__() method for Window class.

        This method is called at each new call for an instance creation,
        in this case, it uses the Singleton.__new__() method which avoid
        the creation of many Window by returning the current instance if
        it exists in the program, if the instance doesn't exist, Singleton
        __new__() method creates an instance, initializes the window's size
        and the window's title and keeps the window on __instance attribute.

        :rtype: Singleton

        """
        instance = super().__new__(cls, *args, **kwargs)
        Window.WINDOW.geometry(str(Window.WIDTH)+"x"+str(Window.HEIGHT))
        Window.WINDOW.title('Sprite Sheet Splitter')
        return instance

    @staticmethod
    def browse_file() -> str | None:
        """
        
        browse a file in your file explorer.

        This method calls filedialog from Tkinter to get access to
        your explorer file, by this access it's possible to choose an
        image file (PNG, JPG, JPEG) and the file's absolute path is
        returned at the end of the function. 

        :rtype: str | None
        
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

        if filename != ():
            label.configure(text="File Opened: "+filename)
            label.pack()
            return filename


if '__main__' == __name__:
    w = Window()
    button = tkinter.Button(Window.WINDOW, text="Text", command=w.browse_file)
    label = tkinter.Label(Window.WINDOW, text="", width=100, height=100, fg='blue')
    button.pack()
    Window.WINDOW.mainloop()
