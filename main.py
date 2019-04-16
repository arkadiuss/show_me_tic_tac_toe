import vision.state_reader as reader
from models.computer_player import ComputerPlayer
from models.human_player import HumanPlayer
from models.state import State

reader.init()

players = [HumanPlayer("Humek"), ComputerPlayer("Compek")]
turn = 0
state = State([[0,0,0], [0,0,0], [0,0,0]])

while True:
    frame = reader.get_state()
    print(frame)
    players[turn].move(state)
    turn = (turn + 1) % 2

reader.destroy()