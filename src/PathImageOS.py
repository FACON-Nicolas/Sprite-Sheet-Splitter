from __future__ import annotations
import flet as ft
import platform


class PathImageOSManager:
    """

    PathImageOSManager is a class developed for the new version of
    the project for the flet library. A path given when a file is
    loaded from the user's file explorer,you can't get it using the
    same lines of code according to your OS, especially for macOS.

    The PathImageOSManager is here to handle this issue. Its init
    constructor method calls a PathImageOS that handles the path
    of the file loaded for each OS.s

    """

    def __init__(self) -> None:
        """

        Constructor for the PathImageOSManager, used to initialize
        the class to use according to your OS. The method looks if
        the program runs on a Darwin platform or not, and assign a
        PathImageOS according to it.

        """
        self.pathImage: PathImageOS
        if platform.platform().lower() == "darwin":
            self.pathImage = PathImageMacOS()
        else:
            self.pathImage = PathImageOS()

    def get_path(self, event: ft.FilePickerResultEvent) -> str | None:
        """

        The method to get the path of the file loaded, it uses the
        get_path(event : ft.FilePickerResultEvent) method used in
        your PathImageOS to get the filename and return it as str.

        """
        return self.pathImage.get_path(event)


class PathImageOS:
    """

    PathImageOS is a class used to get path file in Windows and Linux.

    """

    def __init__(self) -> None:
        """

        PathImageOS's constructor method, init filename as empty str.

        """
        self.filename: str = ""

    def get_path(self, event: ft.FilePickerResultEvent) -> str | None:
        """

        The method to get the path of the file loaded, it checks
        if the files inside the event used are not None and exist.
        As it is impossible to load many files, the method keeps
        only the first one and return it as str.

        """
        if event.files and len(event.files):
            self.filename = event.files[0].path
            return self.filename


class PathImageMacOS(PathImageOS):
    """

    PathImageMacOS is a class used to get path file in Darwin computers(mac).

    """

    def __init__(self) -> None:
        """

        PathImageMacOS's constructor method, calls super init method.

        """
        super().__init__()

    def get_path(self, event: ft.FilePickerResultEvent) -> str | None:
        """

        The method to get the path of the file loaded, it checks
        if the files inside the event used are not None and exist.
        As it is impossible to load many files, the method keeps
        only the first one and return it as str.

        """
        if event.files and len(event.files):
            self.filename = event.files[0].path.split('HD')[1]
            return self.filename
