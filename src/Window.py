from __future__ import annotations
import tkinter
import os
from tkinter import filedialog
import PIL.Image
from ImageResizeDecorator import ImageResizeDecorator
from ImageSplitterDecorator import ImageSplitterDecorator


class Singleton:
    """

    Singleton class is used for the window class.

    The Singleton is a Design Pattern with which it's possible to create only
    one instance for a specific object. The functioning is easy, the class
    contains an instance attribute, if this instance is None then an instance
    is created, else nothing is done. After that, the unique instance is returned.

    """
    
    __instance = None

    def __new__(cls, *args, **kwargs) -> object:
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

    label = None
    import_button = None
    filename = None
    picture_label = None

    row_field = None
    column_field = None

    row_label = None
    column_label = None

    left_margin_field = None
    right_margin_field = None
    top_margin_field = None
    bottom_margin_field = None

    left_margin_label = None
    right_margin_label = None
    top_margin_label = None
    bottom_margin_label = None

    cut_button = None
    save_button = None

    def __new__(cls, *args, **kwargs) -> object:
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
        cls.init_window()
        return instance

    @staticmethod
    def browse_file() -> None:
        """
        
        browse a file in your file explorer.

        This method calls filedialog from Tkinter to get access to
        your explorer file, by this access it's possible to choose an
        image file (PNG, JPG, JPEG) and the file's absolute path is
        returned at the end of the function. 

        :rtype: str | None
        
        """
        filename = filedialog.askopenfile(
            initialdir=os.path.expanduser("~"),
            title="Select an image",
            filetypes=(
                ("PNG", "*.png*"),
                ("JPEG", "*.jpeg*"),
                ("JPG", "*.jpg*")
            )
        )

        try:
            Window.label.configure(text="File Opened: " + filename.name)
            Window.label.pack()
            Window.filename = filename.name
            Window.open_image()
        except FileNotFoundError:
            pass
        except AttributeError:
            pass
        except ValueError:
            pass

    @staticmethod
    def open_image() -> None:
        """

        Open an image from a file name.

        the file name is given by the Window.filename attribute, from this attribute, we have
        access to an image by the absolute path. Thanks to this absolute path and PIL library,
        it's possible to get an Image compatible with Tkinter and show it in the application.

        :rtype: None

        """
        decorator = ImageResizeDecorator(1000, 600, Window.filename)

        splitter = ImageSplitterDecorator(
            PIL.Image.open(Window.filename),
            int(Window.row_field.get()),
            int(Window.column_field.get()),
            int(Window.left_margin_field.get()),
            int(Window.right_margin_field.get()),
            int(Window.top_margin_field.get()),
            int(Window.bottom_margin_field.get())
        )

        Window.picture_label = tkinter.Label(
            Window.WINDOW,
            width=1000,
            height=600,
            image=decorator.new_img
        )

        Window.picture_label.image = decorator.new_img
        Window.picture_label.place(x=100, y=100)
        splitter.split()

    @staticmethod
    def init_window() -> None:
        """

        Init the window and its settings.

        This method set the title and the size (x, y), the width
        and the height values are static constants in the Window
        class. The buttons and Labels are initialized and ready
        to be used in the application, the mainloop is called here.

        """
        Window.WINDOW.title('Sprite Sheet Splitter')
        Window.WINDOW.geometry(str(Window.WIDTH)+"x"+str(Window.HEIGHT))

        Window.label = tkinter.Label(
            Window.WINDOW,
            width=100,
            height=4,
            fg='blue'
        )

        Window.import_button = tkinter.Button(
            Window.WINDOW,
            width=30,
            height=4,
            text="Select a file",
            command=Window.browse_file,
            background="red"
        )

        Window.row_field = tkinter.Entry(
            Window.WINDOW,
            width=23
        )

        Window.column_field = tkinter.Entry(
            Window.WINDOW,
            width=23
        )

        Window.left_margin_field = tkinter.Entry(
            Window.WINDOW,
            width=23
        )

        Window.right_margin_field = tkinter.Entry(
            Window.WINDOW,
            width=23
        )

        Window.top_margin_field = tkinter.Entry(
            Window.WINDOW,
            width=23
        )

        Window.bottom_margin_field = tkinter.Entry(
            Window.WINDOW,
            width=23
        )

        Window.row_label = tkinter.Label(
            Window.WINDOW,
            width=10,
            text='row'
        )

        Window.column_label = tkinter.Label(
            Window.WINDOW,
            width=10,
            text='column'
        )

        Window.left_margin_label = tkinter.Label(
            Window.WINDOW,
            width=10,
            text="left"
        )

        Window.right_margin_label = tkinter.Label(
            Window.WINDOW,
            width=10,
            text="right"
        )

        Window.top_margin_label = tkinter.Label(
            Window.WINDOW,
            width=10,
            text="top"
        )

        Window.bottom_margin_label = tkinter.Label(
            Window.WINDOW,
            width=10,
            text="bottom"
        )

        Window.import_button.place(x=1300, y=100)
        Window.row_label.place(x=1300, y=200)
        Window.row_field.place(x=1370, y=200)
        Window.column_label.place(x=1300, y=260)
        Window.column_field.place(x=1370, y=260)
        Window.left_margin_label.place(x=1300, y=320)
        Window.left_margin_field.place(x=1370, y=320)
        Window.right_margin_label.place(x=1300, y=380)
        Window.right_margin_field.place(x=1370, y=380)
        Window.top_margin_label.place(x=1300, y=440)
        Window.top_margin_field.place(x=1370, y=440)
        Window.bottom_margin_label.place(x=1300, y=500)
        Window.bottom_margin_field.place(x=1370, y=500)
        Window.WINDOW.mainloop()
