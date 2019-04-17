#import vision.state_reader as reader
from models.computer_player import ComputerPlayer
from models.human_player import HumanPlayer
from models.state import State

#reader.init()

players = [HumanPlayer("O", "Humek"), ComputerPlayer("X", "Compek")]
turn = 0
state = State([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

while True:
    #frame = reader.get_state()
    #print(frame)
    print(state)

    try:
        players[turn].move(players[(turn+1) % 2], state)
    except TypeError as te:
        print(te)
        break

    if state.winning(players[turn].symbol):
        print(players[turn].name+" WINS")
        print(state)
        break
    if state.tie():
        print("TIE")
        print(state)
        break

    turn = (turn + 1) % 2
#reader.destroy()
