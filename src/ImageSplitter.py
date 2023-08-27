from PIL import Image
import numpy as np
from deprecated import deprecated
import logging


logging.basicConfig(filename="window.log",
                    format='[%(levelname)s] %(message)s',
                    filemode='w')

logger = logging.getLogger('splitter')
logger.setLevel(logging.DEBUG)


class ImageSplitterDecorator:
    """

    ImageSplitterDecorator class, use to split a sprite sheet to get the sprites.

    The class possesses a decore attribute as PIL Image, a row count, a column count,
    and 4 margin for left, right, top and bottom as 0 by default. It's impossible to
    instance a Splitter if the row count or the column count is less than 1 because
    it's impossible to split an image if there's no row or if there's no column.

    """
    def __init__(self,
                 decore: Image,
                 rows: int,
                 columns: int,
                 left: int = 0,
                 right: int = 0,
                 bottom: int = 0,
                 top: int = 0) -> None:
        """

        ImageSplitterDecorator's constructor, init rows, columns but also the margins
        and the decore element (PIL Image), raise exception if 0 in (rows, columns).

        :param decore: Image to split
        :param rows: row count, cannot be 0
        :param columns: column count, cannot be 0
        :param left: left margin, 0 by default
        :param right: right margin, 0 by default
        :param bottom: bottom margin, 0 by default
        :param top: top margin, 0 by default

        :type decore: Image
        :type rows: int
        :type columns: int
        :type left: int = 0
        :type right: int = 0
        :type bottom: int = 0
        :type top: int = 0

        :rtype: None

        """

        logger.info("init a splitter")
        if rows == 0 or columns == 0:
            raise ValueError(f"row or column cannot be equals to 0, (row, col)=({rows}, {columns})")
        self.decore = decore
        self.rows = rows
        self.columns = columns
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.strategy = SplitterAutoStrategy(self.rows, self.columns)
        logger.info("init a splitter ends correctly")

    def choose_strategy(self) -> object:
        """

        Choose a strategy thanks to margin parameters.

        If all margins are equal to 0, then we choose SplitterAutoStrategy,
        otherwise the SplitterStrategy is chosen to do the same task.

        """
        logger.info("choose a strategy")
        if not (self.left == self.right == self.top == self.bottom == 0):
            logger.info("auto cut strategy")
            return SplitterStrategy(self.rows, self.columns, self.left, self.right, self.top, self.bottom)
        logger.info("manual cut strategy")
        return SplitterAutoStrategy(self.rows, self.columns)

    def split(self):
        """

        get the current image as array, resizes by and splits it.

        To split the image, the row size and column size is calculated.
        from these results, it's possible to split image, row by row and
        column by column, split is stored as image in a List returned.

        :return: all images stored in a list
        :rtype: list[PIL.Image]

        """
        logger.info("split the image")
        split = self.strategy.split(self.decore)
        logger.info("end of split")
        return split

    @deprecated(
        version="2.0.0",
        reason="not useless anymore since we use flet instead of tkinter"
    )
    def resize(self):
        """

        resize the image and returns it as array.

        :return: image resized
        :rtype: numpy.array

        """
        return self.strategy.resize(self.decore)


class SplitterStrategy:
    """

    SplitterStrategy class is a class that splits the sprite-sheet
    with default algorithm, used to implement better algorithm in subclasses

    """

    def __init__(self,
                 rows: int,
                 columns: int = 0,
                 left: int = 0,
                 right: int = 0,
                 top: int = 0,
                 bottom: int = 0) -> None:
        """

        SplitterStrategy class' constructor, initializes, row and column counts and all margins.

        :param rows: row count
        :param columns: column count
        :param left: left margin
        :param right: right margin
        :param top: top count
        :param bottom: bottom count

        :type rows: int
        :type columns: int
        :type left: int
        :type right: int
        :type top: int
        :type bottom: int

        """
        self.rows = rows
        self.columns = columns
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def resize(self, image):
        """

        resize the image thanks to the margin given as argument in
        the splitter decorator constructor, and returns it as array.

        example:

        margin: top=1, right=1, bottom=1, left=1

        [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]] -> [[1]]

        :return: image resized thanks to margin
        :rtype: numpy.array

        """
        array = np.array(image)
        if self.left != 0:
            array = [L[self.left:] for L in array]
        if self.right != 0:
            array = [L[:len(L) - self.right] for L in array]
        if self.top != 0:
            array = array[self.top:]
        if self.bottom != 0:
            array = array[:len(array) - self.bottom]
        return array

    def split(self, image: ImageSplitterDecorator):
        """

        get the current image as array, resized by margin and split it.

        To split the image, the row size and column size is calculated.
        from these results, it's possible to split image, row by row and
        column by column, split is stored as image in a List returned.

        :return: all images stored in a list
        :rtype: list[PIL.Image]

        """
        array = self.resize(image)
        row_size = int(len(array) / self.rows)
        col_size = (len(array[0]) / self.columns)
        pictures = []
        for i in range(self.rows):
            row_start = int(i * row_size)
            row_end = int((i + 1) * row_size)
            picture = array[row_start:row_end]
            for j in range(self.columns):
                col_start = int(col_size * j)
                col_end = int(col_size * (j + 1))
                pic = np.array([L[col_start:col_end] for L in picture])
                pictures.append(Image.fromarray(pic))
        return pictures


class SplitterAutoStrategy(SplitterStrategy):
    """

    SplitterAutoStrategy class, subclass of SplitterStrategy,
    cuts the sprite automatically to keep no border. This
    SplitterStrategy class doesn't need all margin asked before.

    """
    def __init__(self, rows: int, columns: int) -> None:
        """

        SplitterStrategy class' constructor, initializes, row and column counts and all margins.

        :param rows: row count
        :param columns: column count

        :type rows: int
        :type columns: int
        """
        logger.info("init super auto")
        super().__init__(rows, columns)
        logger.info("end of init super auto")

    def split(self, image: ImageSplitterDecorator):
        """

        get the current image as array and split it.

        To split the image, the row size and column size is calculated.
        from these results, it's possible to split image, row by row and
        column by column, split is stored as image in a List returned.

        :return: all images stored in a list
        :rtype: list[PIL.Image]

        """
        logger.info("start split in splitter auto")
        pictures = super(SplitterAutoStrategy, self).split(image)
        pics = []
        for img in pictures:
            img = np.array(img)
            img = SplitterAutoStrategy.cut(img)
            pics.append(Image.fromarray(img))
        logger.info("end split in splitter auto")
        return pics

    @staticmethod
    def cut(image):
        """

        Cut the image in parameter and keeps no border.

        :param image: image to cut
        :type image: np.array

        :return: image cut by the method
        :rtype: np.array

        """
        logger.info("start cut in splitter auto")
        image = SplitterAutoStrategy.cut_top(image)
        image = SplitterAutoStrategy.cut_bottom(image)
        image = SplitterAutoStrategy.cut_left(image)
        image = SplitterAutoStrategy.cut_right(image)
        logger.info("end cut in splitter auto")
        return np.array(image)

    @staticmethod
    def column_all(image, index: int):
        """

        Column all method checks if all values in a specific column are same.

        the array is cast as list and all lines[index] values are compared.

        :param image: image to check
        :param index: column index
        :type image: np.array
        :type index: int

        :return: True if all values in a specifics column are same, else False
        :rtype: boolean

        """
        logger.info("start check all columns")
        value = image[0].tolist()[index]
        for i in range(1, len(image)):
            if image[i].tolist()[index] != value:
                logger.info("They are not all identical")
                return False
        logger.info("They are all identical")
        return True

    @staticmethod
    def cut_top(image):
        """

        cut the top of the sprite.

        While a line has the same value at each index,
        then the line is removed from the picture.

        :param image: image to cut
        :type image: np.array

        :return: image cut
        :rtype: np.array

        """
        logger.info("Start cut top")
        limit = 0
        while limit < len(image) and np.all(image[limit]):
            limit += 1
        logger.info("end cut top, vertical length = " + str(len(image) - limit))
        return image[limit:]

    @staticmethod
    def cut_bottom(image):
        """

        cut the bottom of the sprite.

        While a line has the same value at each index,
        then the line is removed from the picture.

        :param image: image to cut
        :type image: np.array

        :return: image cut
        :rtype: np.array

        """
        logger.info("Start cut bottom")
        limit = len(image)-1
        while limit >= 0 and np.all(image[limit]):
            limit -= 1
        logger.info("end cut bottom, vertical length = " + str(len(image) - limit - 1))
        return image[:limit]

    @staticmethod
    def cut_left(image):
        """

        cut the left of the sprite.

        if a column has the same value at each index,
        then the line is removed from the picture.

        :param image: image to cut
        :type image: np.array

        :return: image cut
        :rtype: np.array

        """
        logger.info("Start cut left")
        limit = 0
        while limit < len(image[0]) and SplitterAutoStrategy.column_all(image, limit):
            limit += 1
        logger.info("end cut left, length = " + str(len(image[0]) - limit))
        return [line[limit:] for line in image]

    @staticmethod
    def cut_right(image):
        """

        cut the right of the sprite.

        if a column has the same value at each index,
        then the line is removed from the picture.

        :param image: image to cut
        :type image: np.array

        :return: image cut
        :rtype: np.array

        """
        logger.info("Start cut right")
        limit = len(image[0])-1
        while limit >= 0 and SplitterAutoStrategy.column_all(image, limit):
            limit -= 1
        logger.info("end cut right, length = " + str(len(image[0]) - limit - 1))
        return [line[:limit] for line in image]
