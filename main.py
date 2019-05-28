from speech import Speech
from strategies.console_game import ConsoleGame
from strategies.vision_game import VisionHumanPlayersGame

# VISION TEST
# import time
# import vision.state_reader as reader
# reader.init()
#
# while 1:
#     frame = reader.get_state()
#     print(frame)
#     # time.sleep(3)
# reader.destroy()


def result_text(sym, plrs):
    if sym == 0:
        return "Tie"
    for p in plrs:
        if p.symbol == sym:
            return "And the winner is... {0}!".format(p.name)
    return "Unknown result"


# strategy = ConsoleGame()
strategy = VisionHumanPlayersGame()
state = strategy.state
players = strategy.players
turn = 0
narrator = Speech(women=True)

narrator.say("Please show me the board")
while not state.end():
    print(state)
    narrator.say("Now it's {0} move".format(players[turn].name))
    try:
        players[turn].move(state, players[(turn+1) % 2])
    except TypeError as te:
        print(te)
        break
    turn = (turn + 1) % 2

narrator.say(result_text(state.result(), players))