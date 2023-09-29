import chess
import copy
board = chess.Board()
temp_board = copy.deepcopy(board)
temp_board.push_uci("e2e4")
print(board)
print(temp_board)