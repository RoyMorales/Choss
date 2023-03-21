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

    # ____________________________ Print Console Board__________________________
    def print_board(self) -> None:
        print("")
        print("---------------------------------")
        for row in range(len(self.board)):
            print("| ", end="")
            for element in self.board[row]:
                if element._name == "*":
                    print(" ", end=" | ")
                else:
                    print(element._name, end=" | ")
            print()
            print("---------------------------------")
        print("")

    # ________________________________ Switch Player ____________________________
    def switch_player(self):
        if self.player_turn == Player.WHITE:
            self.player_turn = Player.BLACK
        elif self.player_turn == Player.BLACK:
            self.player_turn = Player.WHITE

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
    # For Rooks Bishops Queen Pawn
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
    def verify_move_piece(self, piece: object, move: (tuple)):
        piece_moves = piece.list_moves

        if move not in piece_moves:
            return False
        else:
            return True
        
    # _______________________________ Moving Piece __________________________
    def move_piece(self, piece_to_move, new_position):
        # PLayer con only move thier own piece
        if piece_to_move._player == self.player_turn:
            piece_to_move.moves()
            # Remove from piece moves all none possible moves
            self.remove_move_over_piece(piece_to_move)
            self.remove_move_colour(piece_to_move)
            
            if piece_to_move._name == 'K':
                if piece_to_move.piece_moved == False:
                    self.casteling(piece_to_move)

            # Verify if the move is possible
            if self.verify_move_piece(piece_to_move, (new_position.get_row(), new_position.get_col())):
                 # King First Move
                if piece_to_move._name == "K":
                    if piece_to_move.piece_moved == False:
                        print("HERE")
                        print("Castle Moves: ",piece_to_move.castle_moves)
                        print("Move: ", (new_position.get_row(), new_position.get_col()))
                        
                        if (new_position.get_row(), new_position.get_col()) in piece_to_move.castle_moves:
                            self.move_castling((new_position.get_row(), new_position.get_col()))
                            
                            # Change Player Turn
                            piece_to_move.piece_moved == True
                            new_position.piece_moved == True
                            self.switch_player()
                            return
                             
                    
                # Update old position to No_Piece
                self.board[piece_to_move.get_row()][piece_to_move.get_col()] = No_Piece(
                    (piece_to_move.get_row(), piece_to_move.get_col()), Player.NONE
                )
                # Update piece to new position
                self.set_piece((new_position.get_row(), new_position.get_col()), piece_to_move)
                piece_to_move.change_pos(new_position.get_pos())
                    
                # Pawn First Move
                if piece_to_move._name == "P":
                    piece_to_move.piece_moved = True
                    self.promotion(piece_to_move)   
                
                elif piece_to_move._name == "K":
                    piece_to_move.piece_moved == True

                # Rook First Move
                elif piece_to_move._name == "R":
                    piece_to_move.piece_moved == True        
            
                # Change Player Turn
                self.switch_player()
    
    # _______________________________ Promotion Pawn __________________________
    def promotion(self, piece: Pawn):
        pawn_row = piece.get_row()
        
        # Promote pawn to a queen in row 0 or 7
        if pawn_row == 0:
            new_piece = Queen((piece.get_pos()), Player.WHITE)
            self.board[new_piece.get_row()][new_piece.get_col()] = new_piece
            
        elif pawn_row == 7:
            new_piece = Queen((piece.get_pos), Player.BLACK)
            self.board[new_piece.get_row()][new_piece.get_col()] = new_piece
            
    # _______________________________ Casteling Calculation Move __________________________
    def casteling(self, king: King):
        white_left_rook = self.board[7][0]
        white_right_rook = self.board[7][7]
        
        black_left_rook = self.board[0][0]
        black_right_rook = self.board[0][7]
        
        # left Castle
        if white_left_rook._name == "R":
            if white_left_rook.piece_moved == False and king.piece_moved == False and king._player == Player.WHITE:
                for col in range(1, 4):
                    if self.board[7][col]._name == "*":
                        king.castle_left = True
                    else:
                        king.castle_left = False
                        break
        
        # Right Castle
        if white_right_rook._name == "R":
            if white_right_rook.piece_moved == False and king.piece_moved == False and king._player == Player.WHITE:
                for col in range(5, 7):
                    if self.board[7][col]._name == "*":
                        king.castle_right = True
                    else:
                        king.castle_right = False
                        break
                    
        # left Castle
        if black_left_rook._name == "R":
            if black_left_rook.piece_moved == False and king.piece_moved == False and king._player == Player.BLACK:
                for col in range(1, 4):
                    if self.board[0][col]._name == "*":
                        king.castle_left = True
                    else:
                        king.castle_left = False
                        break
        
        # Right Castle
        if black_right_rook._name == "R":
            if black_right_rook.piece_moved == False and king.piece_moved == False and king._player == Player.BLACK:
                for col in range(5, 7):
                    if self.board[0][col]._name == "*":
                        king.castle_right = True
                    else:
                        king.castle_right = False
                        break
        
        if king.castle_left == True and king._player == Player.WHITE:
            move = (7, 2)
            king.list_moves.append(move)
            if move not in king.castle_moves:
                king.castle_moves.append((7,2))
        if king.castle_right == True and king._player == Player.WHITE:
            move = (7, 6)
            king.list_moves.append(move)
            if move not in king.castle_moves:
                king.castle_moves.append((7,6))
            
        if king.castle_left == True and king._player == Player.BLACK:
            move = (0, 2)
            king.list_moves.append((0,2))
            if (0,2) not in king.castle_moves:
                king.castle_moves.append((0,2))
        if king.castle_right == True and king._player == Player.BLACK:
            move = (0, 6)
            king.list_moves.append((0,6))
            if (0,6) not in king.castle_moves:
                king.castle_moves.append((0,6))

    # _______________________________ Casteling Move __________________________
    def move_castling(self, move):
        # White Left
        if self.board[7][0].piece_moved == False and self.board[7][4].piece_moved == False:
            if move == (7,2):
                self.board[7][0] = No_Piece((7,0), Player.NONE)    
                self.board[7][4] = No_Piece((7,4), Player.NONE)    
                self.board[7][3] = Rook((7, 3), Player.WHITE)
                self.board[7][2] = King((7,2), Player.WHITE)
                
                self.board[7][3].piece_moved = True
                self.board[7][2].piece_moved = True

        # White Right
        if self.board[7][7].piece_moved == False and self.board[7][4].piece_moved == False:
            if move == (7,6):
                self.board[7][7] = No_Piece((7,7), Player.NONE)    
                self.board[7][4] = No_Piece((7,4), Player.NONE)    
                self.board[7][5] = Rook((7, 5), Player.WHITE)
                self.board[7][6] = King((7,6), Player.WHITE)
                
                self.board[7][5].piece_moved = True
                self.board[7][6].piece_moved = True
        # Black Left
        if self.board[0][0].piece_moved == False and self.board[0][4].piece_moved == False:
            if move == (0,2):
                self.board[0][0] = No_Piece((0,0), Player.NONE)    
                self.board[0][4] = No_Piece((0,4), Player.NONE)    
                self.board[0][3] = Rook((0, 3), Player.BLACK)
                self.board[0][2] = King((0,2), Player.BLACK)
                
                self.board[0][3].piece_moved = True
                self.board[0][2].piece_moved = True
        #Black Right
        if self.board[0][7].piece_moved == False and self.board[0][4].piece_moved == False:
            if move == (0,6):
                self.board[0][7] = No_Piece((0,7), Player.NONE)    
                self.board[0][4] = No_Piece((0,4), Player.NONE)    
                self.board[0][5] = Rook((0, 5), Player.BLACK)
                self.board[0][6] = King((0,6), Player.BLACK)
                
                self.board[0][5].piece_moved = True
                self.board[0][6].piece_moved = True
        


if __name__ == "__main__":
    board = Board()
    board.print_board()

