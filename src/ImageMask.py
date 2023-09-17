import numpy as np
import logging


logging.basicConfig(filename="window.log",
                    format='[%(levelname)s] %(message)s',
                    filemode='w')

logger = logging.getLogger('mask')
logger.setLevel(logging.DEBUG)


class Mask:

    def __init__(self, image):
        """
        Initializes a Mask object with the given image.

        Parameters:
            image (np.ndarray): The input image as a NumPy array.

        Returns:
            None
        """
        self.image = image
        self.mask, self.bg = self.get_mask()
        self.mask_array = np.array(self.mask)

    def get_mask(self):
        """
        Extracts the mask and background color from the input image.

        Returns:
            tuple[list[list[int]], int]: A tuple containing
            the mask as a 2D list of integers (0 or 1)
            and the background color as an integer.

        """

        im = np.array(self.image)
        image = im.tolist()
        bg = image[0][0]

        return (
            [[int(i != bg) for i in line] for line in image],
            bg
        )

    def find_sprite_contours(self):
        """
        Finds the contours of the sprite in the mask.

        Returns:
            list[tuple[int, int, int, int]]: A list of
            tuples representing the top, bottom, left, and right
            coordinates of each sprite contour found.

        """
        height, width = self.mask_array.shape
        contours = []
        visited = np.zeros((height, width), dtype=bool)

        for row in range(height):
            for col in range(width):
                if self.is_sprite_pixel(row, col, height, width) and not visited[row, col]:
                    contour = self.find_contour(row, col, visited, height, width)
                    contours.append(contour)

        return contours

    @staticmethod
    def is_valid_pixel(row, col, height, width):
        """
        Checks if the given row and column
        coordinates are valid for the image dimensions.

        Parameters:
            row (int): The row coordinate.
            col (int): The column coordinate.
            height (int): The height of the image.
            width (int): The width of the image.

        Returns:
            bool: True if the coordinates are valid, False otherwise.

        """
        return 0 <= row < height and 0 <= col < width

    def is_sprite_pixel(self, row, col, height, width):
        """
        Checks if the pixel at the given row
        and column coordinates is part of the sprite.

        Parameters:
            row (int): The row coordinate.
            col (int): The column coordinate.
            height (int): The height of the image.
            width (int): The width of the image.

        Returns:
            bool: True if the pixel is part
            of the sprite, False otherwise.

        """
        return Mask.is_valid_pixel(row, col, height, width) and self.mask_array[row, col] == 1

    def find_contour(self, start_row, start_col, visited, width, height):
        """
        Finds the contour of the sprite
        starting from the given coordinates.

        Parameters:
            start_row (int): The starting row coordinate.
            start_col (int): The starting column coordinate.
            visited (np.ndarray): A boolean array indicating visited pixels.
            height (int): The height of the image.
            width (int): The width of the image.

        Returns:
            tuple[int, int, int, int]: A tuple containing
            the top, bottom, left, and right coordinates
            of the sprite contour.

        """
        top, bottom, left, right = start_row, start_row, start_col, start_col
        stack = [(start_row, start_col)]

        while stack:
            r, c = stack.pop()
            visited[r, c] = True

            top = min(top, r)
            bottom = max(bottom, r)
            left = min(left, c)
            right = max(right, c)
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neighbors:
                if self.is_sprite_pixel(nr, nc, height, width) and not visited[nr, nc]:
                    stack.append((nr, nc))

        return top, bottom, left, right