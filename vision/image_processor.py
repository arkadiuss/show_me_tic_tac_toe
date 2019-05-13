import cv2
import numpy as np


def to_binary_color(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return binary


def split_to_squares(frame):
    #v =  cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=1)
    #h =  cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=1)
    # return v

    #kernel = np.ones((1, 100))
    #return cv2.dilate(frame, kernel, iterations=1)

    kernel = np.ones((1, 100))
    hlines = cv2.dilate(frame, kernel, iterations=1)
    lines = cv2.HoughLines(hlines, 1, np.pi/180, 200)
    print(lines)
    return hlines
