# Imports
from settings import SettingsClass

# Used varibles
settings = SettingsClass()

# Some usefull function

# Function used in piece
def absolute_moves(piece: object, list_moves: list) -> list[tuple]:
    """Takes the list of the relatives moves of the given piece 
    and return the a list of absolute moves in the chess board 

    Args:
        piece (object): Any Chess Piece
        list_moves (list): List of tuple with the possble position of the piece

    Returns:
        List of tuple(row, collumn) with the absolute moves in the chess board
    """
    absolute_moves = []
    for element in list_moves:
        new_position_row = element[0] + piece.get_row()
        new_position_col = element[1] + piece.get_col()
        
        if 0 <= new_position_row < settings.number_squares and 0 <= new_position_col < settings.number_squares:
            new_position = (new_position_row, new_position_col)
            absolute_moves.append(new_position)
                    
    return absolute_moves

#################                                       #################
#################         EXTREMELY BAD WRITTEN SHIT    #################
#################                                       #################

def rook_remove_moves(board: object, piece: object):
    moves_col_positive = []
    moves_col_negative = []
    moves_row_positive = []
    moves_row_negative = []

    for move in piece.list_moves:
        if move[0] == piece.get_row():
            if move[1] > piece.get_col():
                moves_row_positive.append(move)
            elif move[1] < piece.get_col():
                moves_row_negative.append(move)
        elif move[1] == piece.get_col():
            if move[0] > piece.get_row():
                moves_col_positive.append(move)
            elif move[0] < piece.get_row():
                moves_col_negative.append(move)

    moves_row_plus = []
    for index in range(len(moves_row_positive)):
        move = moves_row_positive[index]
        if board[move[0]][move[1]]._name == "*":
            moves_row_plus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_row_plus.append(move)
            break
        else:
            break

    moves_row_minus = []
    moves_row_negative.reverse()
    for index in range(len(moves_row_negative)):
        move = moves_row_negative[index]
        if board[move[0]][move[1]]._name == "*":
            moves_row_minus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_row_minus.append(move)
            break
        else:
            break

    moves_col_plus = []
    for index in range(len(moves_col_positive)):
        move = moves_col_positive[index]
        if board[move[0]][move[1]]._name == "*":
            moves_col_plus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_col_plus.append(move)
            break
        else:
            break

    moves_col_minus = []
    moves_col_negative.reverse()
    for index in range(len(moves_col_negative)):
        move = moves_col_negative[index]
        if board[move[0]][move[1]]._name == "*":
            moves_col_minus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_col_minus.append(move)
            break
        else:
            break

    piece.list_moves = (
        moves_col_minus + moves_col_plus + moves_row_minus + moves_row_plus
    )   
    
def bishop_remove_moves(board: object, piece: object):
            moves_diag_1 = []
            moves_diag_2 = []
            moves_diag_3 = []
            moves_diag_4 = []

            for move in piece.list_moves:
                if move[1] > piece.get_col():
                    if move[0] < piece.get_row():
                        moves_diag_1.append(move)
                    elif move[0] > piece.get_row():
                        moves_diag_4.append(move)

                elif move[1] < piece.get_col():
                    if move[0] < piece.get_row():
                        moves_diag_2.append(move)
                    elif move[0] > piece.get_row():
                        moves_diag_3.append(move)

            moves_diag_1.reverse()
            poss_moves_diag_1 = []
            for index in range(len(moves_diag_1)):
                move = moves_diag_1[index]
                if board[move[0]][move[1]]._name == "*" or board[move[0]][move[1]]._name == "K":
                    poss_moves_diag_1.append(move)
                else:
                    poss_moves_diag_1.append(move)
                    break

            moves_diag_2.reverse()
            poss_moves_diag_2 = []
            for index in range(len(moves_diag_2)):
                move = moves_diag_2[index]
                if board[move[0]][move[1]]._name == "*" or board[move[0]][move[1]]._name == "K":
                    poss_moves_diag_2.append(move)
                else:
                    poss_moves_diag_2.append(move)
                    break

            poss_moves_diag_3 = []
            for index in range(len(moves_diag_3)):
                move = moves_diag_3[index]
                if board[move[0]][move[1]]._name == "*" or board[move[0]][move[1]]._name == "K":
                    poss_moves_diag_3.append(move)
                else:
                    poss_moves_diag_3.append(move)
                    break

            poss_moves_diag_4 = []
            for index in range(len(moves_diag_4)):
                move = moves_diag_4[index]
                if board[move[0]][move[1]]._name == "*" or board[move[0]][move[1]]._name == "K":
                    poss_moves_diag_4.append(move)
                else:
                    poss_moves_diag_4.append(move)
                    break

            piece.list_moves = (
                poss_moves_diag_1
                + poss_moves_diag_2
                + poss_moves_diag_3
                + poss_moves_diag_4
            )

def queen_remove_moves(board: object, piece: object):
    moves_col_positive = []
    moves_col_negative = []
    moves_row_positive = []
    moves_row_negative = []

    for move in piece.list_moves:
        if move[0] == piece.get_row():
            if move[1] > piece.get_col():
                moves_row_positive.append(move)
            elif move[1] < piece.get_col():
                moves_row_negative.append(move)
        elif move[1] == piece.get_col():
            if move[0] > piece.get_row():
                moves_col_positive.append(move)
            elif move[0] < piece.get_row():
                moves_col_negative.append(move)

    moves_row_plus = []
    for index in range(len(moves_row_positive)):
        move = moves_row_positive[index]
        if board[move[0]][move[1]]._name == "*":
            moves_row_plus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_row_plus.append(move)
            break
        else:
            break

    moves_row_minus = []
    moves_row_negative.reverse()
    for index in range(len(moves_row_negative)):
        move = moves_row_negative[index]
        if board[move[0]][move[1]]._name == "*":
            moves_row_minus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_row_minus.append(move)
            break
        else:
            break

    moves_col_plus = []
    for index in range(len(moves_col_positive)):
        move = moves_col_positive[index]
        if board[move[0]][move[1]]._name == "*":
            moves_col_plus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_col_plus.append(move)
            break
        else:
            break

    moves_col_minus = []
    moves_col_negative.reverse()
    for index in range(len(moves_col_negative)):
        move = moves_col_negative[index]
        if board[move[0]][move[1]]._name == "*":
            moves_col_minus.append(move)
        elif board[move[0]][move[1]]._player != piece._player:
            moves_col_minus.append(move)
            break
        else:
            break

    moves_diag_1 = []
    moves_diag_2 = []
    moves_diag_3 = []
    moves_diag_4 = []

    for move in piece.list_moves:
        if move[1] > piece.get_col():
            if move[0] < piece.get_row():
                moves_diag_1.append(move)
            elif move[0] > piece.get_row():
                moves_diag_4.append(move)

        elif move[1] < piece.get_col():
            if move[0] < piece.get_row():
                moves_diag_2.append(move)
            elif move[0] > piece.get_row():
                moves_diag_3.append(move)

    moves_diag_1.reverse()
    poss_moves_diag_1 = []
    for index in range(len(moves_diag_1)):
        move = moves_diag_1[index]
        if board[move[0]][move[1]]._name == "*":
            poss_moves_diag_1.append(move)
        else:
            poss_moves_diag_1.append(move)
            break

    moves_diag_2.reverse()
    poss_moves_diag_2 = []
    for index in range(len(moves_diag_2)):
        move = moves_diag_2[index]
        if board[move[0]][move[1]]._name == "*":
            poss_moves_diag_2.append(move)
        else:
            poss_moves_diag_2.append(move)
            break

    poss_moves_diag_3 = []
    for index in range(len(moves_diag_3)):
        move = moves_diag_3[index]
        if board[move[0]][move[1]]._name == "*":
            poss_moves_diag_3.append(move)
        else:
            poss_moves_diag_3.append(move)
            break

    poss_moves_diag_4 = []
    for index in range(len(moves_diag_4)):
        move = moves_diag_4[index]
        if board[move[0]][move[1]]._name == "*":
            poss_moves_diag_4.append(move)
        else:
            poss_moves_diag_4.append(move)
            break

    piece.list_moves = (
        poss_moves_diag_1
        + poss_moves_diag_2
        + poss_moves_diag_3
        + poss_moves_diag_4
        + moves_col_minus
        + moves_col_plus
        + moves_row_minus
        + moves_row_plus
    )

