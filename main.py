from errors.move_error import MoveError
from speech import Speech
from strategies.console_game import ConsoleGame
from strategies.vision_game import VisionHumanPlayersGame


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

narrator.say(strategy.introduce())

error = False
while not state.end():
    print(state)
    narrator.say("Now it's {0} move".format(players[turn].name))
    try:
        players[turn].move(state, players[(turn+1) % 2])
    except (MoveError, TypeError) as me:
        narrator.say("There was an error. You probably did forbidden thing")
        error = True
        break
    turn = (turn + 1) % 2

if not error:
    narrator.say(result_text(state.result(), players))
else:
    narrator.say("Game ended without result")