from PIL import Image
import os
from ImageSplitterDecorator import ImageSplitterDecorator


class ImageSaveComposite:
    """

    ImageSaveComposite class, used to save images correctly at the good point.

    To do its job, the class needs an image, a path and a name. To get the
    filename the constructor make a concatenation between path and name.

    """
    def __init__(self, path: str, name: str, type: str) -> None:
        """

        ImageSaveComposite constructor, needs an img, a path, a name.

        In this constructor, the filename is got by a
        concatenation between the path and the name values.

        :return: nothing
        :rtype: None

        """
        self.images = []
        self.path = path + '/'
        self.name = name
        self.type = type

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
        for i in range(len(self.images)):
            name = self.path + self.name + str(i) + '.' + self.type
            self.images[i].save(name)

    def append(self, image: Image) -> None:
        self.images.append(image)

    def remove(self, image: Image) -> None:
        try:
            self.images.remove(image)
        except ValueError:
            pass

    @staticmethod
    def from_images_to_composite(images: list[Image], path: str, name: str, type: str) -> object:
        composite = ImageSaveComposite(path, name, type)
        composite.images = images
        return composite
