import vision.state_reader as reader
from strategies.console_game import ConsoleGame
# VISION TEST
# reader.init()
#
# while 1:
#     frame = reader.get_state()
# reader.destroy()

# MEMORY STATE TEST
strategy = ConsoleGame()
state = strategy.state
players = strategy.players
turn = 0

while not state.end():
    print(state)
    try:
        players[turn].move(state, players[(turn+1) % 2])
    except TypeError as te:
        print(te)
        break
    turn = (turn + 1) % 2

print(state.result())
