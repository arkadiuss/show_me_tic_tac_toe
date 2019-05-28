from copy import deepcopy
import cv2
import vision.image_processor as ip
import numpy as np


def init():
    global cap
    cap = cv2.VideoCapture(0)
    print("Video initialized {0}x{1}, {2} fps".format(int(cap.get(3)), int(cap.get(4)), int(cap.get(5))))


def _paste_non_zero(dest, src):
    s = deepcopy(dest)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if np.any(src[i][j] != 0):
                s[i][j] = src[i][j]
    return s


def _add_lines(frame, lines):
    sh = frame.shape
    for i in lines[0]:
        cv2.line(frame, (0, i), (sh[1], i), (0, 255, 0))

    for i in lines[1]:
        cv2.line(frame, (i, 0), (i, sh[0]), (0, 255, 0))


def get_state():
    threshold = 5
    # for testing
    # frame = cv2.imread('out3.png')
    ret, frame = cap.read()
    binary = ip.to_binary_color(frame)
    sq, lines = ip.split_to_squares(binary)
    if len(sq) < 2 or len(sq) > threshold or len(sq[0]) > threshold:
        cv2.imshow('frame', binary)
        cv2.waitKey(1) & 0xFF == ord('q')
        return []
    state = []
    # ip.recognize_shape(sq[1][1])
    for row in sq:
        state.append([])
        for column in row:
            state[-1].append(ip.recognize_shape(column))
    # cv2.imwrite('out4.png', binary)
    _add_lines(binary, lines)
    cv2.imshow('frame', binary)
    cv2.waitKey(1) & 0xFF == ord('q')  # required to show
    return state


def destroy():
    cap.release()
    cv2.destroyAllWindows()
