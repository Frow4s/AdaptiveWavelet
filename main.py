import cv2
import os
from scipy import signal
import pywt

class Images:
    """
    Класс для выгрузки изображений
    """

    # image_paths = None
    def __init__(self, filepath):
        self.__set_data(filepath)
        self.image_paths = [os.path.join(filepath, file) for file in sorted(os.listdir(filepath))]
        self.images_gen = self.__f_image_gen()

    def __set_data(self, filepath):
        self.__filepath = filepath

    """
    Генератор для того, чтобы работа происходила только с одним конкретным изображением,
    и только это изображение хранилось в памяти
    """

    def __f_image_gen(self):
        for path in self.image_paths:
            yield cv2.imread(path, cv2.IMREAD_GRAYSCALE)


class WaveletAdaptiveMethod:

    def __init__(self, image):
        self.image = image

    def img_intensity(self):
        return signal.medfilt2d(self.image[:])


def print_hi(name):
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    Data = Images('Data')
    count = 1
    for i in Data.images_gen:
        cv2.imshow(str(count), i)
        count += 1
    cv2.waitKey(0)