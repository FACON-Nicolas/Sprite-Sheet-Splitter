import PIL
from PIL import Image, ImageTk


class ImageResizeDecorator:
    """

    ImageResizeDecorator class is used to resize image and keep the ratio.

    This Decorator is here to resize image and keep the ratio, it's very
    important to avoid many bugs when the application will want to show
    the image imported to the user. This class is here to do these actions
    and keep a clean code if I would work on the project again.

    """
    def __init__(self, width: int, height: int,  decore: PIL.Image) -> None:
        """

        ImageResizeDecorator class constructor, this method take as argument
        the width, used to know the max width for the image, the height, to
        know the max height for the image, and decore, here decore's type is
        PIL Image, this is use as it to resize as good as possible the image.

        :param width: max width
        :param height: max height
        :param decore: image to resize

        :type width: int
        :type height: int
        :type width: PIL.Image

        :rtype: None

        """
        self.width = width
        self.height = height
        self.decore = decore

    def get_ratio(self) -> float:
        """

        Get ratio method, use to know the width / height ratio.

        :return: width / height ratio.
        :rtype: float

        """
        return self.width / self.height

    def resize_as_img_tk(self) -> ImageTk:
        image = ImageTk.getimage(self.decore)
        width = self.width
        height = width * self.get_ratio()
        image.resize((width, height))
        return image
