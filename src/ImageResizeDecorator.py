from PIL import Image, ImageTk


class ImageResizeDecorator:

    new_img = None

    """

    ImageResizeDecorator class is used to resize image and keep the ratio.

    This Decorator is here to resize image and keep the ratio, it's very
    important to avoid many bugs when the application will want to show
    the image imported to the user. This class is here to do these actions
    and keep a clean code if I would work on the project again.

    """
    def __init__(self, width: int, height: int,  decore: str) -> None:
        """

        ImageResizeDecorator class constructor, this method take as argument
        the width, used to know the max width for the image, the height, to
        know the max height for the image, and decore, decore's type is str.

        :param width: max width
        :param height: max height
        :param decore: image's filename to resize

        :type width: int
        :type height: int
        :type width: str

        :rtype: None

        """
        self.width = width
        self.height = height
        self.decore = decore
        self.resize_as_img_tk()

    def get_ratio(self) -> float:
        """

        Get ratio method, use to know the width / height ratio.

        :return: width / height ratio.
        :rtype: float

        """
        return self.width / self.height

    def resize_as_img_tk(self) -> None:
        """

        Resize image and store the result in a static attribute.

        Thanks to the attributes in the decorator (width, height),
        it's possible to calculate the ratio width / height and
        resize the image directly in this method. Once the image
        resized, the result is stored in the static attribute new_img.

        """
        width = int(self.width)
        height = int(width // self.get_ratio())
        img = Image.open(self.decore)
        img = img.resize((width, height))
        ImageResizeDecorator.new_img = ImageTk.PhotoImage(img)
