# Imports
import pygame

from player import Player
from util import absolute_moves


class Piece:
    """
    Super Class for Pieces
    
    Pieces:
        Pawn -> P
        Rook -> R
        Knight -> H
        Bishop -> B
        Queen -> Q
        King -> K
        NONE -> E | *
    """

    def __init__(self, position: tuple[int, int], player: Player):
        self.row_number = position[0]
        self.col_number = position[1]
        self._player = player

    def get_row(self) -> int:
        return self.row_number

    def get_col(self) -> int:
        return self.col_number
    
    def get_pos(self) -> tuple:
        return (self.row_number, self.col_number)
    
    def get_player(self) -> Player:
        return self._player

    def change_pos(self, position: tuple[int, int]):
        self.row_number = position[0]
        self.col_number = position[1]

    def change_row(self, new_row: int):
        self.row_number = new_row

    def change_col(self, new_col: int):
        self.col_number = new_col


class Rook(Piece):
    def __init__(self, position: tuple[int, int], player: Player):
        super().__init__(position, player)
        self._name = "R"
        self.list_moves = []
        self.relative_moves = []

        # Castlings Stuff
        self.piece_moved = False
        
        # Set Piece Movement
        self.relative_move()

        # Image for the Piece White or Black
        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/rook_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/rook_black.png")
        else:
            print("Rook image not found!")

    def get_name(self) -> str:
        return self._name
    
    # Rook Piece can move horizontally or vertically in all directions 
    def relative_move(self):
        moves = []
        for i in range(-7, 8):
            if i != 0:
                moves.append((0, i))
                moves.append((i, 0))
        self.relative_moves = moves
        
    # Updates list of moves possible for the piece in the given position
    def moves(self):    
        self.list_moves = absolute_moves(self, self.relative_moves)



class Knight(Piece):
    def __init__(self, position: tuple[int, int], player: Player):
        super().__init__(position, player)
        self._name = "H"
        self.list_moves = []
        self.relative_moves = []
        self.piece_moved = False

        
        # Set Piece Movement
        self.relative_move()

        # Image for the Piece White or Black
        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/knight_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/knight_black.png")
        else:
            print("Knight image not found!")

    def get_name(self) -> str:
        return self._name
    
    # Knight Piece can move in L shape in all directions
    def relative_move(self):
        self.relative_moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    
    # Updates list of moves possible for the piece in the given position
    def moves(self):
        self.list_moves = absolute_moves(self, self.relative_moves)


class Bishop(Piece):
    def __init__(self, position: tuple[int, int], player: Player):
        super().__init__(position, player)
        self._name = "B"
        self.list_moves = []
        self.relative_moves = []
        self.piece_moved = False

        
        # Set Piece Movement
        self.relative_move()

        # Image for the Piece White or Black
        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/bishop_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/bishop_black.png")
        else:
            print("Bishop image not found!")

    def get_name(self) -> str:
        return self._name
    
    # Bishop Piece can move in the diagonal in all directions
    def relative_move(self):
        moves = []
        for i in range(-7, 8):
            if i != 0:
                moves.append((i, i))
                moves.append((i, -i))
        self.relative_moves = moves        
    
    # Updates list of moves possible for the piece in the given position
    def moves(self):
        self.list_moves = absolute_moves(self, self.relative_moves)


class Pawn(Piece):
    def __init__(self, position: tuple[int, int], player: Player):
        super().__init__(position, player)
        self._name = "P"
        self.list_moves = []
        self.list_attack = []
        self.relative_moves = []

        # First Move 2 Squares
        self.piece_moved = False
        
        # Set Piece Movement
        self.relative_move()
        self.attack_move()

        # Image for the Piece White or Black
        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/pawn_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/pawn_black.png")
        else:
            print("Pawn image not found!")

    def get_name(self) -> str:
        return self._name

    # Pawn Piece can only move in horizontal 
    # Pawn Piece can move one or two squares in the first move
    # Pawn Piece can only move one square after the first move
    def relative_move(self):
        if self._player == Player.WHITE:
            if self.piece_moved == False:
                moves = [(-1, 0), (-2, 0)]
            elif self.piece_moved == True:
                moves = [(-1, 0)]

        elif self._player == Player.BLACK:
            if self.piece_moved == False:
                moves = [(1, 0), (2, 0)]
            elif self.piece_moved == True:
                moves = [(1, 0)]
        self.relative_moves = moves
    
    # Pawn Piece can only attack the the first square on the diagonal in front of it
    def attack_move(self):
        if self._player == Player.WHITE:
            relative_moves = [(-1, -1), (-1, 1)]
        elif self._player == Player.BLACK:
            relative_moves = [(1, 1), (1, -1)]
        
        self.list_attack = absolute_moves(self, relative_moves)
        
    # Updates list of moves possible for the piece in the given position
    def moves(self):
        self.relative_move()
        self.attack_move()
        self.list_moves = absolute_moves(self, self.relative_moves)
  

class Queen(Piece):
    def __init__(self, position: tuple[int, int], player: Player):
        super().__init__(position, player)
        self._name = "Q"
        self.list_moves = []
        self.relative_moves = []
        self.piece_moved = False

        
        # Set Piece Movement
        self.relative_move()

        # Image for the Piece White or Black
        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/queen_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/queen_black.png")
        else:
            print("Queen image not found!")

    def get_name(self) -> str:
        return self._name
    
    # Queen Piece can move as the combination of the Rook Piece and Bishop Piece
    def relative_move(self):
        moves = []
        for i in range(-7, 8):
            if i != 0:
                moves.append((0, i))
                moves.append((i, 0))
                moves.append((i, i))
                moves.append((i, -i))
        self.relative_moves = moves
    
    # Updates list of moves possible for the piece in the given position
    def moves(self):
        self.list_moves = absolute_moves(self, self.relative_moves)


class King(Piece):
    def __init__(self, position: tuple[int, int], player: Player):
        super().__init__(position, player)
        self._name = "K"
        self.list_moves = []
        self.relative_moves = []
        self.castle_moves = []
        
        # Speical rules stuff
        self.piece_moved = False
        self.castle_left = False
        self.castle_right = False
        
        # Set Piece Movement
        self.relative_move()

        # Image for the Piece White or Black
        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/king_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/king_black.png")
        else:
            print("King image not found!")

    def get_name(self) -> str:
        return self._name

    # King Piece can only move one square in all directions
    def relative_move(self):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    moves.append((i, j))
        self.relative_moves = moves
    
    # Caslting left
    def left_castle_move(self):
        move = absolute_moves(self, [(0, -1)])
        if self.castle_left == True:
            self.list_moves = self.list_moves + move

    # Caslting Right
    def left_castle_move(self):
        move = absolute_moves(self, [(0, 1)])
        if self.castle_right == True:
            self.list_moves = self.list_moves + move

    # Updates list of moves possible for the piece in the given position       
    def moves(self):
        self.list_moves = absolute_moves(self, self.relative_moves)
        

# No_Piece acts as a empty space
# Needed for simplicity of the code and as a reference
class No_Piece(Piece):
    def __init__(self, position: tuple[int, int], player: Player):
        super().__init__(position, player)
        self._name = "*"
        self.list_moves = []
        self.piece_moved = True

    def get_name(self) -> str:
        return self._name

    # No_Piece has no moves
    def moves(self) :
        self.list_moves = []