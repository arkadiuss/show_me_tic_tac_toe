import cv2


def init():
    global cap
    cap = cv2.VideoCapture(0)


def get_state():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    print(binary)
    cv2.imshow('frame', binary)
    cv2.imwrite('out.png', binary)
    cv2.waitKey(1) & 0xFF == ord('q')  # required to show
    return frame


def destroy():
    cap.release()
    cv2.destroyAllWindows()
