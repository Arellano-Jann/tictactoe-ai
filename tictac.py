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
        # print(self.board, self.player)

    def init_board(self):
        return np.array([[0,0,0],[0,0,0],[0,0,0]])

    def print_board(self):
        print (self.board)

    def play_game(self):
        # TODO: some while loop
        winner = 0
        # def place_marker(board, player, x, y):
        #     # print(board, 'placemarker24')
        #     if board[x][y] == 0: board[x][y] == player
        #     return board
            
        def eval_win(board):
            lines = [row for row in board.tolist()] + [list(row) for row in zip(*board)] + [[board[i][i] for i in range(3)]] + [[board[i][2-i] for i in range(3)]]
            # print('lineadd30','other>',[row.tolist() for row in board], [list(row) for row in zip(*board)], [[board[i][i] for i in range(3)]], [[board[i][2-i] for i in range(3)]])
            # board # calc row
            # + [list(row) for row in zip(*board)] # calc column
            # + [[board[i][i] for i in range(3)]] # diag 1
            # + [[board[i][2-i] for i in range(3)]] # diag 2
            # print(lines, 'lines34', board, "board34")
            if [1, 1, 1] in lines:
                return 1 # 1 wins
            elif [-1, -1, -1] in lines:
                return -1 # -1 wins
            return 0 # draw or no win. handled by len(possible_moves()) to see if it's a real draw
            
        def is_terminal(board): # returns True if a board is in it's last stage
            nonlocal winner
            winner = eval_win(board)
            # print(winner, "winner43 should match 63")
            if winner == 0 and (len(possible_moves(board)) == 0 or np.all(board != 0)): # if no one has won and there are no more moves left, then draw
                # print('no moves draw45', board)
                return True
            elif winner == 0:
                # seems like it gets stuck here. i think it's bc len possible moves never gets evaluated to 0
                # this may be because the board does not get updated as the moves get placed.
                # print('not terminal48', board)
                return False
            # print('winner50', board, winner, '< should match 63')
            return True
        
        def possible_moves(board): # returns list of possible moves that player can make (x,y)
            move_list = []
            for x in range(3):
                for y in range(3):
                    if board[x][y] == 0:
                        move_list.append([x, y])
            return move_list
        
        def minimax(player=self.player, board=self.board): # determines the best move by value
            if is_terminal(board):
                # print(winner, "Winner:63\n", board)
                # self.board = board
                return winner
            if player == 1: # GOAL: make game value large
                value = float('-inf')
                for move in possible_moves(board):
                    board[move[0]][move[1]] = 1
                    value = max(
                        value, 
                        minimax(-1, board)
                        # minimax(-1, place_marker(board, player, move[0], move[1]))
                        )
                    board[move[0]][move[1]] = 0
                # print(value, 'value80')
                return value
            elif player == -1: # GOAL: make value smallest
                value = float('inf')
                for move in possible_moves(board):
                    board[move[0]][move[1]] = -1
                    value = min(
                        value, 
                        minimax(1, board)
                        # minimax(1, place_marker(board, player, move[0], move[1]))
                        )
                    board[move[0]][move[1]] = 0
                return value
            
        def find_move(player=self.player, board=self.board):
            best_value = float('-inf') if player == 1 else float('inf')
            best_move = [0, 0]
            
            for move in possible_moves(board):
                board[move[0]][move[1]] = player
                value = minimax()
                board[move[0]][move[1]] = 0
                if (player == 1 and value > best_value) or (player == -1 and value < best_value):
                    best_value = value
                    best_move = move
            return best_move
                
        def switch_player(): self.player = -1 if self.player == 1 else 1

        while True:
            if eval_win(self.board): # if non zero returns, then...
                return self.board, winner
            move = find_move()
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