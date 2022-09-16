from copy import deepcopy
import math
from tictactoe import minimax

state_1_board = [["x", "o", "x"], ["", "", "o"], ["", "", ""]]

state_2_board = deepcopy(state_1_board)
state_2_board[0][2] = "x"
score = minimax(state_2_board, False)
print(f"State 2 score is {score} and it should be 10") # Instant win

state_3_board = deepcopy(state_1_board)
state_3_board[1][2] = "x"
score = minimax(state_3_board, False)
print(f"State 3 score is {score} and it should be -10")

# It should be -10, because the next turn is O's, so we are minimizing
# and the "list of scores" SHOULD contain -10, because O can win with 
# the following situation
# x x o
# o o x
# o x  