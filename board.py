
from settings import SettingsClass
from piece import *
from player import Player

class Board:
    def __init__(self):
        # Set Settings
        self.settings = SettingsClass()
            
        # Inicialize Board
        self.board = []
        for i in range(self.settings.number_squares):
            self.board.append([None] * self.settings.number_squares)

        # Inicialize Spices
        # White
        self.board[7][0] = Rook((7, 0), Player.WHITE)
        self.board[7][7] = Rook((7, 7), Player.WHITE)
        self.board[7][1] = Knight((7, 1), Player.WHITE)
        self.board[7][6] = Knight((7, 6), Player.WHITE)
        self.board[7][2] = Bishop((7, 2), Player.WHITE)
        self.board[7][5] = Bishop((7, 5), Player.WHITE)
        self.board[7][3] = Queen((7, 3), Player.WHITE)
        self.board[7][4] = King((7, 4), Player.WHITE)
        # Black
        self.board[0][0] = Rook((0, 0), Player.BLACK)
        self.board[0][7] = Rook((0, 7), Player.BLACK)
        self.board[0][1] = Knight((0, 1), Player.BLACK)
        self.board[0][6] = Knight((0, 6), Player.BLACK)
        self.board[0][2] = Bishop((0, 2), Player.BLACK)
        self.board[0][5] = Bishop((0, 5), Player.BLACK)
        self.board[0][3] = Queen((0, 3), Player.BLACK)
        self.board[0][4] = King((0, 4), Player.BLACK)
        # Pawns
        # White
        for col in range(self.settings.number_squares):
            self.board[6][col] = Pawn((6, col), Player.WHITE)

        # Black
        for col in range(self.settings.number_squares):
            self.board[1][col] = Pawn((1, col), Player.BLACK)

        # NONE Spaces
        for row in range(2, 6):
            for col in range(self.settings.number_squares):
                self.board[row][col] = No_Piece((row, col), Player.NONE)     

    # ____________________________ Print Console Board__________________________
    def print_board(self) -> None:
        for row in range(len(self.board)):
            print("| ", end="")
            for element in self.board[row]:
                print(element._name, end=' | ')
            print()
            print("---------------------------------")

        #print("Columns on the Board: ", len(self.board[0]))
        #print("Rows on the Board: ", len(self.board))

    # ________________________________ Switch Player ____________________________

    # ________________________________ Get Player Colour ________________________            

    # _______________________________ Moving Animation __________________________
        
        



if __name__ == "__main__":
    board = Board()
    board.print_board()
