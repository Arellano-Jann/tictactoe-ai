#!/usr/bin/python3

import numpy as np
import argparse

class TicTacToe:
    def __init__(self, board=None, player=1) -> None:
        if board is None:
            self.board = self.init_board()
        else:
            self.board = board
        self.player = player
        
        self.winner = 0
        # print(self.board, self.player)

    def init_board(self):
        return np.array([[0,0,0],[0,0,0],[0,0,0]])

    def print_board(self):
        print (self.board)

    def play_game(self):
            
        def eval_win(board):
            lines = [row for row in board.tolist()] + [list(row) for row in zip(*board)] + [[board[i][i] for i in range(3)]] + [[board[i][2-i] for i in range(3)]]
            if [1, 1, 1] in lines:
                return 1 # 1 wins
            elif [-1, -1, -1] in lines:
                return -1 # -1 wins
            return 0 if not possible_moves(board) else None # draw else none
            
        def is_terminal(board): # returns True if a board is in it's last stage
            self.winner = eval_win(board)
            if self.winner: return True # if it returns a winner for a board
            elif self.winner == 0: # draw
                return True
            else: return False
        
        def possible_moves(board): # returns list of possible moves that player can make (x,y)
            move_list = []
            for x in range(3):
                for y in range(3):
                    if board[x][y] == 0:
                        move_list.append([x, y])
            return move_list
        
        def minimax(player=self.player, board=self.board): # determines the best move by value
            if is_terminal(board): # not acc sure if this is needed but need more testcases to determine that
                return self.winner
            
            best_value = float('inf') * -player
            best_move = None
            
            for move in possible_moves(board):
                board[move[0]][move[1]] = player # Do move
                
                if is_terminal(board): # Check for instant win
                    winner = eval_win(board)
                    board[move[0]][move[1]] = 0 # Undo move so that it doesn't propagate
                    return winner, move
                
                value, _ = minimax(-player) # recursive call to get the value of a board
                
                
                if (player == 1 and value > best_value) or (player == -1 and value < best_value): # return best move and best value
                    best_value, best_move = value, move
                    
                board[move[0]][move[1]] = 0 # Undo move
                
            return best_value, best_move
                
        def switch_player(): self.player = -self.player

        while True:
            if eval_win(self.board) is not None: # if non zero returns, then...
                return self.board, eval_win(self.board)
            _, move = minimax()
            self.board[move[0]][move[1]] = self.player
            switch_player()

def load_board( filename ):
    return np.loadtxt( filename)

# def save_board( self, filename ):
# 	np.savetxt( filename, self.board, fmt='%d')

def main():
    parser = argparse.ArgumentParser(description='Play tic tac toe')
    parser.add_argument('-f', '--file', default=None, type=str ,help='load board from file')
    parser.add_argument('-p', '--player', default=1, type=int, choices=[1,-1] ,help='player that playes first, 1 or -1')
    args = parser.parse_args()

    board = load_board(args.file) if args.file else None
    testcase = np.array([[ 0,0,0],
                             [-1,1,0],
                             [-1,0,0]])
    ttt = TicTacToe(testcase, args.player)
    # ttt.print_board()
    b,p = ttt.play_game()
    print("final board: \n{}".format(b))
    print("winner: player {}".format(p))

if __name__ == '__main__':
    main()