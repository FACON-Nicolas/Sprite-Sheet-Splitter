from __future__ import annotations
import PIL.Image
from ImageSplitter import ImageSplitterDecorator
from ImageSaveComposite import ImageSaveComposite
import traceback

import flet as ft


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

    label: ft.Text
    import_button: ft.ElevatedButton
    filename: str

    row_field: ft.TextField
    column_field: ft.TextField

    left_margin_field: ft.TextField
    right_margin_field: ft.TextField
    top_margin_field: ft.TextField
    bottom_margin_field: ft.TextField

    name_field: ft.TextField = None

    cut_button: ft.ElevatedButton
    save_button: ft.ElevatedButton
    theme_button: ft.IconButton
    isLight: bool = False
    main_container: ft.Container
    content_container: ft.Row
    image_container: ft.Container
    form_container: ft.Row
    image: ft.Image
    file_picker: ft.FilePicker
    dir_picker: ft.FilePicker

    splitter: ImageSplitterDecorator = None
    page: ft.Page = None

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
    def browse_file(e: ft.FilePickerResultEvent) -> None:
        """

        browse a file in your file explorer.

        This method calls filedialog from Tkinter to get access to
        your explorer file, by this access it's possible to choose an
        image file (PNG, JPG, JPEG) and the file's absolute path is
        returned at the end of the function.

        :rtype: str | None

        """

        try:
            if e.files and len(e.files):
                Window.filename = e.files[0].path
                Window.open_image(Window.filename)
        except FileNotFoundError:
            print(traceback.format_exc())
        except AttributeError:
            print(traceback.format_exc())
        except ValueError:
            print(traceback.format_exc())

    @staticmethod
    def open_image(filename: str) -> None:
        """

        Open an image from a file name.

        the file name is given by the Window.filename attribute, from this attribute, we have
        access to an image by the absolute path. Thanks to this absolute path and PIL library,
        it's possible to get an Image compatible with Tkinter and show it in the application.

        :rtype: None

        """
        Window.filename = filename
        Window.image.src = filename
        Window.page.update()

    @staticmethod
    def cut_image() -> list | None:
        """

        get the current image and call the methods to split it.

        a splitter is instanced to a static Window attribute and
        from this, it's possible to split the image, the value in the
        field are required because they are used in this method.

        :return: nothing
        :rtype: None

        """
        try:
            Window.splitter = ImageSplitterDecorator(
                PIL.Image.open(Window.filename),
                int(Window.row_field.value),
                int(Window.column_field.value),
                int(Window.left_margin_field.value),
                int(Window.right_margin_field.value),
                int(Window.top_margin_field.value),
                int(Window.bottom_margin_field.value)
            )

            return Window.splitter.split()
        except ValueError:
            print(traceback.format_exc())

    @staticmethod
    def save(e: ft.FilePickerResultEvent) -> None:
        """

        cut image, and save it as asked by player.

        Get all settings (row count, column count, all margin(left, right, top, bottom),
        name, path) and uses them to save all sprites split as sprites.

        :return: nothing
        :rtype: None

        """
        if e.path:
            try:
                images = Window.cut_image()
                img_type = Window.filename.split('.')[-1]
                composite = ImageSaveComposite.from_images_to_composite(
                    images,
                    e.path,
                    Window.name_field.value,
                    img_type
                )
                composite.save()
            except FileNotFoundError:
                pass
        else:
            print('test')

    @staticmethod
    def change_theme():
        Window.isLight = not Window.isLight
        if Window.isLight:
            Window.page.theme_mode = ft.ThemeMode.LIGHT
            Window.theme_button.icon = ft.icons.DARK_MODE
        else:
            Window.page.theme_mode = ft.ThemeMode.DARK
            Window.theme_button.icon = ft.icons.LIGHT_MODE
        Window.page.update()

    @staticmethod
    def init_window() -> None:
        """

        Init the window and its settings.

        This method set the title and the size (x, y), the width
        and the height values are static constants in the Window
        class. The buttons and Labels are initialized and ready
        to be used in the application, the mainloop is called here.

        """
        Window.page.title = 'Sprite Sheet Splitter'
        Window.page.window_width = Window.WIDTH
        Window.page.window_height = Window.HEIGHT
        Window.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        Window.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        Window.file_picker = ft.FilePicker(
            on_result=Window.browse_file,
        )

        Window.dir_picker = ft.FilePicker(
            on_result=Window.save,
        )

        Window.file_picker.allowed_extensions = ["png", "jpg", "jpeg"]

        # theme button to toggle screen theme
        Window.theme_button = ft.IconButton(
            icon=ft.icons.LIGHT_MODE,
            on_click=lambda e: Window.change_theme()
        )

        Window.image = ft.Image(
            src=f"placeholder.png",
            width=1000,
            height=700,
            border_radius=10,
            fit=ft.ImageFit.CONTAIN
        )

        Window.row_field = ft.TextField(label="Rows", width=300)
        Window.column_field = ft.TextField(label="Columns", width=300)
        Window.left_margin_field = ft.TextField(label="Margin left", value="0", width=300)
        Window.right_margin_field = ft.TextField(label="Margin Right", value="0", width=300)
        Window.top_margin_field = ft.TextField(label="Margin Top", value="0", width=300)
        Window.bottom_margin_field = ft.TextField(label="Margin Bottom", value="0", width=300)
        Window.name_field = ft.TextField(label="Name", width=300)
        Window.cut_button = ft.ElevatedButton(
            text="Cut your image",
            icon="cut",
            width=300,
            height=50,
            on_click=lambda _: Window.dir_picker.save_file()
        )

        Window.import_button = ft.ElevatedButton(
            text="Import an image",
            icon="upload",
            width=300,
            height=50,
            on_click=lambda _: Window.file_picker.pick_files()
        )

        Window.image_container = ft.Container(
            content=Window.image,
        )

        Window.content_container = ft.Row([
            Window.image_container,
        ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        Window.form_container = ft.Row([
            ft.Column([
                Window.import_button,
                Window.row_field,
                Window.column_field,
                Window.left_margin_field,
                Window.right_margin_field,
                Window.top_margin_field,
                Window.bottom_margin_field,
                Window.name_field,
                Window.cut_button,
            ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # The main container is here to show all components
        Window.main_container = ft.Container(
            content=ft.Row([
                Window.theme_button,
                Window.image_container,
                Window.form_container
            ],
                spacing=75,
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        Window.page.add(Window.main_container)
        Window.page.overlay.append(Window.file_picker)
        Window.page.overlay.append(Window.dir_picker)
        Window.page.update()


def main(page: ft.Page):
    Window.page = page
    Window.init_window()
    Window.page.update()
