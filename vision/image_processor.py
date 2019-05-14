import math

import cv2
import numpy as np


def to_binary_color(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return binary


def _get_lines(frame, kernel):
    dltd = cv2.dilate(frame, kernel, iterations=1)
    lines = cv2.HoughLines(255 - dltd, 1, np.pi / 180, 200)
    return np.array([abs(l[0][0]) for l in lines])
    #old for printing lines
    res = np.ones(frame.shape)
    if lines is not None:
        for i in range(len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            print(pt1, pt2, frame.shape)
            cv2.line(res, pt1, pt2, (0, 255, 0), 3, cv2.LINE_AA)
    return res


def _filter_lines(lines):
    threshold = 40 # TODO: make it dynamic
    res = []
    for l in lines:
        take = True
        for lr in res:
            if abs(l - lr) < threshold:
                take = False

        if take:
            res.append(int(l))
    return res


def split_to_squares(frame):
    hkernel = np.ones((1, 100))
    vkernel = np.ones((100, 1))
    hlines = [0] + _filter_lines(_get_lines(frame, hkernel)) + [frame.shape[0]]
    vlines = [0] + _filter_lines(_get_lines(frame, vkernel)) + [frame.shape[1]]
    hlines.sort()
    vlines.sort()
    res = []
    for i in range(1, len(hlines)):
        res.append([])
        for j in range(1, len(vlines)):
            res[-1].append(frame[hlines[i-1]:hlines[i], vlines[j-1]:vlines[j]])
    return res[1][1]
