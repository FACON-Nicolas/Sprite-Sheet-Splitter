from PIL import Image
import os
import logging
import traceback

logging.basicConfig(filename="window.log",
                    format='[%(levelname)s] %(message)s',
                    filemode='w')

logger = logging.getLogger('saver')
logger.setLevel(logging.DEBUG)


class ImageSaveComposite:
    """

    ImageSaveComposite class, used to save images correctly at the good point.

    To do its job, the class needs an image, a path and a name. To get the
    filename the constructor make a concatenation between path and name.

    """
    def __init__(self, path: str, name: str, type_img: str) -> None:
        """

        ImageSaveComposite constructor, needs an img, a path, a name.

        In this constructor, the filename is got by a
        concatenation between the path and the name values.

        :return: nothing
        :rtype: None

        """
        logger.info("init image saver")
        self.images = []
        self.path = path + '/'
        self.name = name
        self.type = type_img

    def save(self) -> None:
        """

        Save img in the computer.

        if the path directory doesn't exist, the method
        create it, and save the image in filename location.

        :return: nothing
        :rtype: None

        """
        logger.info("start save recursively")
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            logger.debug("path " + self.path + " created successfully.")
        for i in range(len(self.images)):
            name = self.path + self.name + str(i) + '.' + self.type
            self.images[i].save(name)
            logger.debug("image " + name + " saved successfully.")
        logger.info("end save recursively")

    def append(self, image) -> None:
        """

        add image in composite.

        To add this image in the composite, the class possesses a list
        to store all images, composite.append(image) calls append in list.

        :return: nothing
        :rtype: None

        """
        logger.info("add an image")
        self.images.append(image)

    def remove(self, image) -> None:
        """

        add image in composite.

        To add this image in the composite, the class possesses a list
        to store all images, composite.remove(image) calls remove in list,
        but List.remove(image) throws ValueError if the value is not in list,
        so a try / catch is implemented in this method to handle Exceptions.

        :return: nothing
        :rtype: None

        """
        logger.info("remove an image")
        try:
            self.images.remove(image)
            logger.info("remove an image successfully")
        except ValueError:
            logger.error("remove an image with errors")
            print(traceback.format_exc())

    @staticmethod
    def from_images_to_composite(images, path: str, name: str, type_img: str):
        """

        construct a composite from a list[Image], a path, a name and an image type.

        This static method instances a new composite, get the images empty list and
        replace it by the list[Image] in parameters and return the new composite.

        :return: nothing
        :rtype: None

        """
        logger.info("init saver with images")
        composite = ImageSaveComposite(path, name, type_img)
        composite.images = images
        logger.info("end init saver with images")
        return composite
