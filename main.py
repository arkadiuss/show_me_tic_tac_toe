import vision.state_reader as reader

reader.init()

while 1:
    frame = reader.get_state()
    #print(frame)

    #time.sleep(10)

# players = [HumanPlayer("O", "Humek"), ComputerPlayer("X", "Compek")]
# turn = 0
# state = MemoryState([[0, 0, 0], [0, 0, 0], [0, 0, 0]], moves=["O", "X"])
#
# while not state.end():
#
#     #print(state)
#
#     try:
#         players[turn].move(players[(turn+1) % 2], state)
#     except TypeError as te:
#         print(te)
#         break
#
#     turn = (turn + 1) % 2
#
# print(state.result())
reader.destroy()
