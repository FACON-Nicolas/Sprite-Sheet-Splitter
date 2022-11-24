from PIL import Image
import os


class ImageSaveDecorator:
    """

    ImageSaveDecorator class, used to save images correctly at the good point.

    To do its job, the class needs an image, a path and a name. To get the
    filename the constructor make a concatenation between path and name.

    """
    def __init__(self, decore: Image, path: str, name: str) -> None:
        """

        ImageSaveDecorator constructor, needs an img, a path, a name.

        In this constructor, the filename is got by a
        concatenation between the path and the name values.

        :return: nothing
        :rtype: None

        """
        self.decore = decore
        self.path = path
        self.name = name
        self.filename = path + '/' + name

    def save(self) -> None:
        """

        Save img in the computer.

        if the path directory doesn't exist, the method
        create it, and save the image in filename location.

        :return: nothing
        :rtype: None

        """
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.decore.save(self.filename)
