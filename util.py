
def absolute_moves(object, relative_moves):
    absolute_moves = []
    for element in relative_moves:
        move_row = element[0]
        move_col = element[1]
        
        position_row = object.get_row()
        position_col = object.get_col()
        
        new_position_row = position_row + move_row
        new_position_col = position_col + move_col
        
        
        if 0 <= new_position_row < 8 and 0 <= new_position_col < 8:
            new_position = (new_position_row, new_position_col)
            absolute_moves.append(new_position)
                    
    return absolute_moves
