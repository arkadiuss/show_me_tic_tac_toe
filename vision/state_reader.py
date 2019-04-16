import cv2


def init():
    global cap
    cap = cv2.VideoCapture(0)


def get_state():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    cv2.waitKey(1) & 0xFF == ord('q') # required to show
    return frame


def destroy():
    cap.release()
    cv2.destroyAllWindows()
