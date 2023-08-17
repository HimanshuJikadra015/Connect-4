# Heuristic-1 is weakesh opponent.

# Working of Heuristic-1:
# Act when you are about to win or lose. Otherwise, play random move or any move.

# We check if this move is win or lose. That way red go for win, black go for reds lose.

from utils import Helper
INF = 1000
MININF = -1000

class Heuristic1:
    @staticmethod
    def evaluate(table):
        if Helper.is_winner(table,True):
            return INF
        if Helper.is_winner(table,False):
            return MININF
        return 0
