from state.state import State
import vision.state_reader as sr
import threading


class VisionState(State):

    def __init__(self):
        sr.init()
        self.board = sr.get_state()
        threading.Thread(target=self.observe).start()

    def observe(self):
        while 1:
            state = sr.get_state()

    def board(self):
        return self.board

    def end(self):
        pass

    def result(self):
        pass

    def move(self, r, c, move):
        pass

    def __del__(self):
        sr.destroy()
