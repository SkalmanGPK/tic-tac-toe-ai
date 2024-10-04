import numpy as np
import random
import q_learning_agent as q
class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3,3), dtype=int)
    
    def reset(self):
        self.board = np.zeros((3,3), dtype=int)
        return self.board

    def is_valid_move(self, row, col):
        return self.board[row, col] == 0
    
    def play_move(self, row, col, player):
        if self.is_valid_move(row,col):
            self.board[row, col] = player
            return True
        return False
    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if np.all(self.board[i, :] == 1) or np.all(self.board[:, i] == 1):
                return 1
            if np.all(self.board[i, :] == -1) or np.all(self.board[:, i] == -1):
                return -1
        if np.all(np.diag(self.board) == 1) or np.all(np.diag(np.fliplr(self.board)) == 1):
            return 1
        if np.all(np.diag(self.board) == -1) or np.all(np.diag(np.fliplr(self.board)) == -1):
            return -1
        
        if np.all(self.board != 0):
            return 0 # Draw
        return None # Game ongoing

