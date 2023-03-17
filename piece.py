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

    def __init__(self, position, player):
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

    def change_row(self, new_row):
        self.row_number = new_row

    def change_col(self, new_col):
        self.col_number = new_col


class Rook(Piece):
    def __init__(self, position, player):
        super().__init__(position, player)
        self._name = "R"
        self.list_moves = []

        # Castlings Stuff
        self.castle = True

        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/rook_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/rook_black.png")
        else:
            print("Rook image not found!")

    def get_name(self):
        return self._name
    
    def moves(self):
        relative_moves = []
        for i in range(-7, 8):
            if i != 0:
                relative_moves.append((0, i))
                relative_moves.append((i, 0))
        self.list_moves = absolute_moves(self, relative_moves)



class Knight(Piece):
    def __init__(self, position, player):
        super().__init__(position, player)
        self._name = "H"
        self.list_moves = []


        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/knight_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/knight_black.png")
        else:
            print("Knight image not found!")

    def get_name(self):
        return self._name
    
    def moves(self):
        # L movement
        relative_moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        self.list_moves = absolute_moves(self, relative_moves)


class Bishop(Piece):
    def __init__(self, position, player):
        super().__init__(position, player)
        self._name = "B"
        self.list_moves = []

        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/bishop_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/bishop_black.png")
        else:
            print("Bishop image not found!")

    def get_name(self):
        return self._name
    
    def moves(self):
        # X movement
        relative_moves = []
        for i in range(-7, 8):
            if i != 0:
                relative_moves.append((i, i))
                relative_moves.append((i, -i))
        self.list_moves = absolute_moves(self, relative_moves)


class Pawn(Piece):
    def __init__(self, position, player):
        super().__init__(position, player)
        self._name = "P"
        self.list_moves = []

        # First Move 2 Squares
        self.piece_moved = False

        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/pawn_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/pawn_black.png")
        else:
            print("Pawn image not found!")

    def get_name(self):
        return self._name

    def moves(self):
        if self._player == Player.WHITE:
            if self.piece_moved == False:
                relative_moves = [(-1, 0), (-2, 0)]
            elif self.piece_moved == True:
                relative_moves = [(-1, 0)]
            else:
                print("Somethin Wrong lol - Invalid Move")
        elif self._player == Player.BLACK:
            if self.piece_moved == False:
                relative_moves = [(1, 0), (2, 0)]
            elif self.piece_moved == True:
                relative_moves = [(1, 0)]
            else:
                print("Somethin Wrong lol - Invalid Move")
    
        self.list_moves = absolute_moves(self, relative_moves)
  

class Queen(Piece):
    def __init__(self, position, player):
        super().__init__(position, player)
        self._name = "Q"
        self.list_moves = []

        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/queen_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/queen_black.png")
        else:
            print("Queen image not found!")

    def get_name(self):
        return self._name
    
    def moves(self) -> list:
        # X movement
        relative_moves = []
        for i in range(-7, 8):
            if i != 0:
                relative_moves.append((0, i))
                relative_moves.append((i, 0))
                relative_moves.append((i, i))
                relative_moves.append((i, -i))
                
        self.list_moves = absolute_moves(self, relative_moves)


class King(Piece):
    def __init__(self, position, player):
        super().__init__(position, player)
        self._name = "K"
        self.list_moves = []
        
        self.castle = True

        if self._player == Player.WHITE:
            self.piece_image = pygame.image.load("./resources/king_white.png")
        elif self._player == Player.BLACK:
            self.piece_image = pygame.image.load("./resources/king_black.png")
        else:
            print("King image not found!")

    def get_name(self):
        return self._name

    def moves(self) -> list:
        relative_moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    relative_moves.append((i, j))
        self.list_moves = absolute_moves(self, relative_moves)



class No_Piece(Piece):
    def __init__(self, position, player):
        super().__init__(position, player)
        self._name = "*"
        self.list_moves = []

    def get_name(self):
        return self._name

    def moves(self) :
        self.list_moves = []