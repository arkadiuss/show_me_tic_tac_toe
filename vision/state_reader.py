from copy import deepcopy
import cv2
import vision.image_processor as ip
import numpy as np


def init():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 1)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = int(cap.get(5))
    print(width, height, fps)


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
    # ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    # cv2.imwrite('out2.png', frame)
    # cv2.waitKey(1) & 0xFF == ord('q')
    # return frame
    # for testing
    # frame = cv2.imread('out2.png')
    ret, frame = cap.read()
    binary = ip.to_binary_color(frame)
    sq, lines = ip.split_to_squares(binary)
    state = []
    for row in sq:
        state.append([])
        for column in row:
            state[-1].append(ip.recognize_shape(column))
    _add_lines(binary, lines)
    cv2.imshow('frame', binary)
    cv2.waitKey(1) & 0xFF == ord('q')  # required to show
    print(state)
    return state


def destroy():
    cap.release()
    cv2.destroyAllWindows()
