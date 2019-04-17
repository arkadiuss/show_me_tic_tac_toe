import vision.state_reader as reader
from models.computer_player import ComputerPlayer
from models.human_player import HumanPlayer
from models.memory_state import MemoryState

reader.init()

players = [HumanPlayer("O", "Humek"), ComputerPlayer("X", "Compek")]
turn = 0
state = MemoryState([[0, 0, 0], [0, 0, 0], [0, 0, 0]], moves=["O", "X"])

while not state.end():
    #frame = reader.get_state()
    #print(frame)
    print(state)

    try:
        players[turn].move(players[(turn+1) % 2], state)
    except TypeError as te:
        print(te)
        break

    turn = (turn + 1) % 2

print(state.result())
reader.destroy()
