
from settings import SettingsClass
import pieces as piece

class Board:
    def __init__(self):
        # Set Settings
        self.settings = SettingsClass()
        
        # Set Players
        self.player_turn = 1
        self.player_colour = "White"
            
        # Inicialize Board to zeros
        self.board = []
        self.No_P = piece.No_P("No_Colour")
        for i in range(self.settings.number_squares):
            self.board.append([None] * self.settings.number_squares)

        # Inicialize Spices
        # White
        self.board[7][0] = piece.Rook("White")
        self.board[7][7] = piece.Rook("White")
        self.board[7][1] = piece.Knight("White")
        self.board[7][6] = piece.Knight("White")
        self.board[7][2] = piece.Bishop("White")
        self.board[7][5] = piece.Bishop("White")
        self.board[7][3] = piece.Queen("White")
        self.board[7][4] = piece.King("White")
        # Black
        self.board[0][0] = piece.Rook("Black")
        self.board[0][7] = piece.Rook("Black")
        self.board[0][1] = piece.Knight("Black")
        self.board[0][6] = piece.Knight("Black")
        self.board[0][2] = piece.Bishop("Black")
        self.board[0][5] = piece.Bishop("Black")
        self.board[0][3] = piece.Queen("Black")
        self.board[0][4] = piece.King("Black")

        # Pawns
        # White
        for pawn in range(self.settings.number_squares):
            self.board[6][pawn] = piece.Pawn("White")

        # Black
        for pawn in range(self.settings.number_squares):
            self.board[1][pawn] = piece.Pawn("Black")

        # NONE Spaces
        for j in range(2, 6):
            for i in range(self.settings.number_squares):
                self.board[j][i] = piece.No_P("No_Colour")

    # ____________________________ Print Console Board__________________________
    def print_board(self) -> None:
        for row in range(len(self.board)):
            print("| ", end="")
            for collumn in self.board[row]:
                print(collumn.piece_name, end=' | ')
            print()
            print("---------------------------------")

        #print("Columns on the Board: ", len(self.board[0]))
        #print("Rows on the Board: ", len(self.board))

    # ________________________________ Switch Player ____________________________
    # Set Player turn
    # Player White -> 1
    # Player Black -> -1
    def switch_player(self):
        if self.player_turn == 1:
            self.player_turn = -1
        else:
            self.player_turn = 1
    # ________________________________ Get Player Colour _________________________            
    def get_player_colour(self):
        if self.player_turn == 1:
            self.player_color = "White"
        elif self.player_turn == -1:
            self.player_color = "Black"

    # _______________________________ Moving Animation ___________________________
    def move_piece(self, start_pos, end_pos):
        self.moving_piece = self.board[start_pos[0]][start_pos[1]]
        self.target_place = self.board[end_pos[0]][end_pos[1]]
                
        if self.moving_piece.piece_name == self.No_P.piece_name: 
            print("Can not move None Piece")
            return
        
        if 
        
        if self.target_place.colour == self.moving_piece.colour:
            print("Can not move to a frindly Piece")
            return
        
        
        
        
        



if __name__ == "__main__":
    board = Board()
    board.print_board()
    board.move_piece((1,1),(0,0))
