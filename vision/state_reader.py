import cv2
import vision.image_processor as ip


def init():
    global cap
    cap = cv2.VideoCapture(0)


def get_state():
    # ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    # cv2.imwrite('out2.png', frame)
    # cv2.waitKey(1) & 0xFF == ord('q')
    # return frame
    # for testing
    frame = cv2.imread('out2.png')
    binary = ip.to_binary_color(frame)
    sq = ip.split_to_squares(binary)
    cv2.imshow('frame', sq)
    # cv2.imwrite('out.png', binary)
    cv2.waitKey(1) & 0xFF == ord('q')  # required to show
    return frame


def destroy():
    cap.release()
    cv2.destroyAllWindows()
