from copy import deepcopy
import cv2
import vision.image_processor as ip
import numpy as np


def init():
    global cap
    cap = cv2.VideoCapture(0)


def _paste_non_zero(src, dest):
    s = deepcopy(src)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if np.all(dest[i][j] == 0):
                s[i][j] = dest[i][j]
    return s


def _create_lines_image(frame, lines):
    res = np.zeros(frame.shape)
    for i in lines[0]:
        res[i, :] = 127

    for i in lines[1]:
        res[:, i] = 127
    return res


def get_state():
    # ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    # cv2.imwrite('out2.png', frame)
    # cv2.waitKey(1) & 0xFF == ord('q')
    # return frame
    # for testing
    frame = cv2.imread('out2.png')
    binary = ip.to_binary_color(frame)
    sq, lines = ip.split_to_squares(binary)
    state = []
    for row in sq:
        state.append([])
        for column in row:
            state[-1].append(ip.recognize_shape(column))
    cv2.imshow('frame', _paste_non_zero(frame, _create_lines_image(frame, lines)))
    cv2.waitKey(1) & 0xFF == ord('q')  # required to show
    return state


def destroy():
    cap.release()
    cv2.destroyAllWindows()
