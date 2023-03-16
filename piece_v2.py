
import pygame

from settings import SettingsClass

# Default Messages
path_blocked = "Piece can not move to blocked square"
path_incorrect = "Square outside of the range of the piece"

class Player:
    Player_1 = "White"
    Player_2 = "Black"
    


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
            
    Colour:
        White
        Black
        NONE
    """
    def __init__(self, colour):
        self.piece_name = ""
        self.colour = colour

    def get_piece(self):
        return self.piece_name

    def get_colour(self):
        return self.colour


class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour)

        self.piece_name = "P"
        
        if colour == "White":
            self.piece_image = pygame.image.load("./resources/pawn_white.png")
        elif colour == "Black":
            self.piece_image = pygame.image.load("./resources/pawn_black.png")
        else:
            print("Pawn image not found!")


class Rook(Piece):
    def __init__(self, colour, first_move = True):
        super().__init__(colour)

        self.piece_name = "R"
        self.first_move = True

        if colour == "White":
            self.piece_image = pygame.image.load("./resources/rook_white.png")
        elif colour == "Black":
            self.piece_image = pygame.image.load("./resources/rook_black.png")
        else:
            print("Rook image not found!")

class Knight(Piece):
    def __init__(self, colour):
        super().__init__(colour)

        self.piece_name = "H"

        if colour == "White":
            self.piece_image = pygame.image.load("./resources/knight_white.png")
        elif colour == "Black":
            self.piece_image = pygame.image.load("./resources/knight_black.png")
        else:
            print("Knight image not found!")
        

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour)

        self.piece_name = "B"

        if colour == "White":
            self.piece_image = pygame.image.load("./resources/bishop_white.png")
        elif colour == "Black":
            self.piece_image = pygame.image.load("./resources/bishop_black.png")
        else:
            print("Bishop image not found!")



class Queen(Piece):
    def __init__(self, colour):
        super().__init__(colour)

        self.piece_name = "Q"

        if colour == "White":
            self.piece_image = pygame.image.load("./resources/queen_white.png")
        elif colour == "Black":
            self.piece_image = pygame.image.load("./resources/queen_black.png")
        else:
            print("Queen image not found!")




class King(Piece):
    def __init__(self, colour):
        super().__init__(colour)

        self.piece_name = "K"

        if colour == "White":
            self.piece_image = pygame.image.load("./resources/king_white.png")
        elif colour == "Black":
            self.piece_image = pygame.image.load("./resources/king_black.png")
        else:
            print("King image not found!")


class No_P(Piece):
    def __init__(self, colour):
        super().__init__(colour)

        self.piece_name = "*"
        self.colour = "No_Colour"
        self.piece_image = "No_Image"



