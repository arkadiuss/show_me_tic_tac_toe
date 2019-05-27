from state.state import State
import vision.state_reader as sr


class VisionState(State):

    def __init__(self, board, moves):
        super().__init__(board, moves)
        sr.init()

    def board(self):
        return sr.get_state()

    def move(self, r, c, move):
        pass

    def __del__(self):
        sr.destroy()
