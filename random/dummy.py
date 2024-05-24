from functools import reduce
import cv2
from PIL import ImageChops
import math, operator


def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(
        reduce(operator.add, map(lambda h, i: h * (i**2), h, range(256)))
        / (float(im1.size[0]) * im1.size[1])
    )


im1 = cv2.imread("dheer\Pictures\wallpapers\electrified_thefatrat.jpg")
im2 = cv2.imread("dheer\Pictures\wallpapers\ingens.jpg")
rmsdiff(im1, im2)
