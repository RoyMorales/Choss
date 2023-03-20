from settings import SettingsClass
from piece import *
from player import Player
from util import *


class Board:
    def __init__(self):
        # Set Settings
        self.settings = SettingsClass()

        # Set first player
        self.player_turn = Player.WHITE

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


    # ______________________________ Set and Get and Remove_____________________
    def get_piece(self, position: tuple) -> object:
        return self.board[position[0]][position[1]]

    def set_piece(self, position: tuple, piece: object):
        self.board[position[0]][position[1]] = piece
        piece

    # ____________________________ Print Console Board__________________________
    def print_board(self) -> None:
        for row in range(len(self.board)):
            print("| ", end="")
            for element in self.board[row]:
                print(element._name, end=" | ")
            print()
            print("---------------------------------")

    # ________________________________ Switch Player ____________________________
    def switch_player(self):
        if self.player_turn == Player.WHITE:
            self.player_turn = Player.BLACK
        elif self.player_turn == Player.BLACK:
            self.player_turn == Player.WHITE

    # _______________________________ Remove Piece Move Same Color_______________
    # Remove from piece moves prohibited moves
    # For Knights Kings Pawns
    def remove_move_colour(self, piece: object):
        piece_colour = piece._player
        update_list_moves = []
        for move in piece.list_moves:
            piece_analise = self.get_piece(move)

            if piece_analise._player != piece_colour:
                update_list_moves.append(move)

        piece.list_moves = update_list_moves

    # _________________________________Remove Move over Pieces ___________________
    # For Rooks Bishops Queen
    def remove_move_over_piece(self, piece: object):
        if piece._name == "R":
            rook_remove_moves(self.board, piece)    
        elif piece._name == "B":
            bishop_remove_moves(self.board, piece)
        elif piece._name == "Q":
            queen_remove_moves(self.board, piece)
        elif piece._name == "P":
            list_moves_player = []
            for move in piece.list_moves:
                if self.board[move[0]][move[1]]._name == "*":
                    list_moves_player.append(move)
                else:
                    break
            piece.list_moves = list_moves_player
            self.pawn_attack(piece)

    # _______________________________ Pawn Attack __________________________
    def pawn_attack(self, piece):
        list_attacks = []
        for move in piece.list_attack:
            if self.board[move[0]][move[1]]._player != piece._player and self.board[move[0]][move[1]]._name != '*':
                list_attacks.append(move)
        piece.list_moves = piece.list_moves + list_attacks
                
    # _______________________________ Moving Piece __________________________
    def move_piece(self, piece_to_move, new_position):
        piece_to_move_row = piece_to_move.get_row()
        piece_to_move_col = piece_to_move.get_col()

        new_position_row = new_position.get_row()
        new_position_col = new_position.get_col()

        piece_to_move = self.board[piece_to_move_row][piece_to_move_col]
        piece_to_move.moves()
        self.remove_move_over_piece(piece_to_move)
        self.remove_move_colour(piece_to_move)

        if self.verify_move_piece(piece_to_move, (new_position_row, new_position_col)):
            self.board[piece_to_move_row][piece_to_move_col] = No_Piece(
                (piece_to_move_row, piece_to_move_col), Player.NONE
            )
            self.board[new_position_row][new_position_col] = piece_to_move
            piece_to_move.change_row(new_position_row)
            piece_to_move.change_col(new_position_col)

            # Pawn First Move
            if piece_to_move._name == "P":
                piece_to_move.piece_moved = True
    
            # King First Move
            elif piece_to_move._name == "K":
                piece_to_move.castle == False
            # Rook First Move
            elif piece_to_move._name == "R":
                piece_to_move.castle == False

    # _______________________________ Moving Piece __________________________
    def verify_move_piece(self, piece: object, move: (tuple)):
        piece_moves = piece.list_moves

        if move not in piece_moves:
            return False
        else:
            return True


if __name__ == "__main__":
    board = Board()
    board.print_board()

