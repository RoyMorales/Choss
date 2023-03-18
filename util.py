# Imports
from settings import SettingsClass

# Used varibles
settings = SettingsClass()

# Some usefull function

# Function used in piece
def absolute_moves(piece: object) -> list[tuple]:
    """Takes the list of the relatives moves of the given piece 
    and return the a list of absolute moves in the chess board 

    Args:
        piece (object): Any Chess Piece

    Returns:
        List of tuple(row, collumn) with the absolute moves in the chess board
    """
    absolute_moves = []
    for element in piece.relative_moves:
        new_position_row = element[0] + piece.get_row()
        new_position_col = element[1] + piece.get_col()
        
        if 0 <= new_position_row < settings.number_squares and 0 <= new_position_col < settings.number_squares:
            new_position = (new_position_row, new_position_col)
            absolute_moves.append(new_position)
                    
    return absolute_moves