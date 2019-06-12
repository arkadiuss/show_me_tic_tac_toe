import math

import cv2
import numpy as np

from properties import GlobalProperties


def to_binary_color(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, GlobalProperties.black_threshold, 255, cv2.THRESH_BINARY)
    return binary


def _get_lines(frame, kernel):
    dltd = cv2.dilate(frame, kernel, iterations=1)
    lines = cv2.HoughLines(255 - dltd, 1, np.pi / 180, GlobalProperties.line_votes)
    return [] if lines is None else np.array([abs(l[0][0]) for l in lines])


def _filter_lines(lines):
    threshold = GlobalProperties.line_space_threshold
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
    hlines = [0] + _filter_lines(_get_lines(frame, hkernel)) + [frame.shape[0] - 1]
    vlines = [0] + _filter_lines(_get_lines(frame, vkernel)) + [frame.shape[1] - 1]
    hlines.sort()
    vlines.sort()
    res = []
    for i in range(1, len(hlines)):
        res.append([])
        for j in range(1, len(vlines)):
            res[-1].append(frame[hlines[i - 1]:hlines[i], vlines[j - 1]:vlines[j]])
    return res, (hlines, vlines)


def _is_circle(frame):
    if np.all(frame == 0):
        return False
    circ = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=25, minRadius=0, maxRadius=0)
    return circ is not None and len(circ) == 1


def _pad_image(frame, padding=40):
    sh = frame.shape
    return frame[padding:sh[0] - padding, padding:sh[1] - padding]


def _is_empty(frame):
    threshold = 50
    padded = _pad_image(frame)
    return np.count_nonzero(255 - padded) < threshold


def _filter_cross_lines(lines):
    if lines is None:
        return []
    threshold = 0.35
    min = GlobalProperties.min_cross_angle  # minimal angle
    max = GlobalProperties.max_cross_angle  # maximal angle
    res = []
    for l in lines:
        ang = l[0][1] if l[0][1] < math.pi/2 else math.pi - l[0][1]
        if ang < min or ang > max:
            continue
        toadd = True
        for r in res:
            if abs(r - l[0][1]) < threshold:
                toadd = False
        if toadd:
            res.append(l[0][1])
    return res


def _is_cross(frame):
    if np.all(frame == 0):
        return False
    pframe = _pad_image(frame, 20)
    lines = cv2.HoughLines(255 - pframe, 1, np.pi / 180, 120)
    # cv2.imshow('frame2', pframe)
    # print(lines)
    # print(_filter_cross_lines(lines))
    return len(_filter_cross_lines(lines)) == 2


def recognize_shape(frame):
    if _is_cross(frame):
        return 'x'
    if _is_circle(frame):
        return 'o'
    return 0
