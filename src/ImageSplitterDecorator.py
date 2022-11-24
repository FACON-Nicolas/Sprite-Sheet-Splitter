from PIL import Image
import numpy as np


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
                 top: int = 0):
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

        if rows == 0 or columns == 0:
            raise ValueError(f"row or column cannot be equals to 0, (row, col)=({rows}, {columns})")
        self.decore = decore
        self.rows = rows
        self.columns = columns
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def split(self) -> list[Image]:
        """

        get the current image as array, resized by margin and split it.

        To split the image, the row size and column size is calculated.
        from these results, it's possible to split image, row by row and
        column by column, split is stored as image in a List returned.

        :return: all images stored in a list
        :rtype: list[PIL.Image]

        """
        array = self.resize()
        row_size = int(len(array) / self.rows)
        col_size = (len(array[0]) / self.columns)
        print(self.rows, self.columns)
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
                pictures[-1].show()
        return pictures

    def resize(self) -> np.array:
        array = np.array(self.decore)
        if self.left != 0:
            array = [L[self.left:] for L in array]
        if self.right != 0:
            array = [L[:len(L)-self.right] for L in array]
        if self.top != 0:
            array = array[self.top:]
        if self.bottom != 0:
            array = array[:len(array)-self.bottom]
        return array
