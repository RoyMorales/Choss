import pygame
import sys

from settings import *
from board import *
from piece import *
from player import *


class Choss:
    def __init__(self):
        # App Title
        pygame.display.set_caption("Choss")

        # Set Settings
        self.settings = SettingsClass()
        self.screen_game = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height)
        )
        self.font_path = "./resources/font/"
        self.font_board_path = self.font_path + "theboldfont.ttf"
        self.font_board = pygame.font.SysFont("theboldfont", int(self.settings.grid_height / 4))
        print("Font Size: ", int(self.settings.grid_height / 4))
        
        # Set Board
        self.game_board = Board()
        self.selected_piece_moving = False
        self.selected_piece = None
        self.player_turn = self.game_board.player_turn
        self.player_change = None
        # Empty Space
        self.No_Piece_Ref = No_Piece((-1, -1), Player.NONE)
        
        # Click History
        self.left_click_history = []
        self.right_click_history = []
        self.LEFT = 1
        self.RIGHT = 3

    # ________________________________ Runner____________________________________
    def run_app(self):
        while True:
            self.check_event()
            self.draw_board()
            self.draw_pieces()
            self.player_change = self.game_board.player_change
            
            # Single Calculation of pieces moves
            if self.player_change == None:
                self.game_board.set_pieces_moves()
                print("-----------------------------------------")
                print("Player to play: ", self.game_board.player_change)
            
            pygame.display.update()

    # ________________________________ Events ___________________________________
    def check_event(self):
        event = pygame.event.poll()
        mouse_pos = pygame.mouse.get_pos()
        
        if event.type == pygame.QUIT:
            sys.exit()
        
        # Event Mouse Left Button 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self.LEFT:
            print("Left Mouse Click:", mouse_pos)
            piece_selected = self.click_collisions(mouse_pos)
            
            # Clear User Highlighed Squares
            if len(self.right_click_history) > 0:
                self.right_click_history = []
            else:
                # Left button history only has length 2 
                # First element on the list -> Piece to move
                # Second elemnt on the list -> Position to move the piece
                if  len(self.left_click_history) == 0:
                    if piece_selected._name != self.No_Piece_Ref._name and piece_selected._player == self.player_turn:
                        self.left_click_history.append(piece_selected) 

                # Only one click to hightlight frindly pieces
                elif len(self.left_click_history) == 1:
                    if piece_selected._player == self.player_turn:
                        self.left_click_history = [piece_selected]
                    else:
                        self.left_click_history.append(piece_selected)
                        self.game_board.move_piece(self.left_click_history[0], self.left_click_history[1])
                        self.player_turn = self.game_board.player_turn
                        self.left_click_history = []
        
        # Event Mouse Right Button 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self.RIGHT:
            print("Right Mouse Click: ", mouse_pos)
            piece_selected = self.click_collisions(mouse_pos)
            
            # Clear left click history with one right mouse click
            if len(self.left_click_history) > 0:
                    self.left_click_history = []
            else:
                self.right_click_history.append(piece_selected)
                self.highlight_squares()
                
    # ________________________________ Draw Board _______________________________
    def draw_board(self) -> None:
        # Draw Initial Black
        self.screen_game.fill((0, 0, 0))

        # Draw Bight and Dark Squares
        counter = 0
        for white_square_row in range(0, self.settings.number_squares):
            for white_square_collumn in range(0, self.settings.number_squares):
                if counter % 2 == 0:
                    pygame.draw.rect(
                        self.screen_game,
                        self.settings.square_colour_bright,
                        [
                            self.settings.grid_width * white_square_row,
                            self.settings.grid_height * white_square_collumn,
                            self.settings.grid_width,
                            self.settings.grid_height,
                        ],
                    )
                else:
                    pygame.draw.rect(
                        self.screen_game,
                        self.settings.square_colour_dark,
                        [
                            self.settings.grid_width * white_square_row,
                            self.settings.grid_height * white_square_collumn,
                            self.settings.grid_width,
                            self.settings.grid_height,
                        ],
                    )

                counter += 1
            counter -= 1
            
        # Highlight Moves
        if len(self.left_click_history) == 1:
            self.highrlight_piece()
            self.highlight_moves()
        # Highrlight Squares
        if len(self.right_click_history) != 0:
            self.highlight_squares() 
            
        if self.game_board.king_check == True:
            self.hightlight_check()
            
        # Draw lines
        # Horizontal
        for line in range(1, self.settings.number_squares):
            pygame.draw.line(
                self.screen_game,
                self.settings.lines_colour,
                (0, self.settings.grid_height * line),
                (
                    self.settings.grid_height * self.settings.number_squares,
                    self.settings.grid_height * line,
                ),
                width=self.settings.lines_width,
            )
        # Vertical
        for line in range(1, self.settings.number_squares):
            pygame.draw.line(
                self.screen_game,
                self.settings.lines_colour,
                (self.settings.grid_width * line, 0),
                (
                    self.settings.grid_width * line,
                    self.settings.grid_width * self.settings.number_squares,
                ),
                width=self.settings.lines_width,
            )
            
        # Letters
        letter_suface_A = self.font_board.render("A", True, self.settings.square_colour_bright)
        letter_suface_B = self.font_board.render("B", True, self.settings.square_colour_dark)
        letter_suface_C = self.font_board.render("C", True, self.settings.square_colour_bright)
        letter_suface_D = self.font_board.render("D", True, self.settings.square_colour_dark)
        letter_suface_E = self.font_board.render("E", True, self.settings.square_colour_bright)
        letter_suface_F = self.font_board.render("F", True, self.settings.square_colour_dark)
        letter_suface_G = self.font_board.render("G", True, self.settings.square_colour_bright)
        letter_suface_H = self.font_board.render("H", True, self.settings.square_colour_dark)

        self.screen_game.blit(letter_suface_A, (1 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        self.screen_game.blit(letter_suface_B, (2 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        self.screen_game.blit(letter_suface_C, (3 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        self.screen_game.blit(letter_suface_D, (4 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        self.screen_game.blit(letter_suface_E, (5 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        self.screen_game.blit(letter_suface_F, (6 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        self.screen_game.blit(letter_suface_G, (7 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        self.screen_game.blit(letter_suface_H, (8 * self.settings.grid_height - self.settings.grid_height / 6, 8 * self.settings.grid_width - self.settings.grid_width / 6))
        
        # Numbers
        number_surface_1 = self.font_board.render("1", False, self.settings.square_colour_dark)
        number_surface_2 = self.font_board.render("2", False, self.settings.square_colour_bright)
        number_surface_3 = self.font_board.render("3", False, self.settings.square_colour_dark)
        number_surface_4 = self.font_board.render("4", False, self.settings.square_colour_bright)
        number_surface_5 = self.font_board.render("5", False, self.settings.square_colour_dark)
        number_surface_6 = self.font_board.render("6", False, self.settings.square_colour_bright)
        number_surface_7 = self.font_board.render("7", False, self.settings.square_colour_dark)
        number_surface_8 = self.font_board.render("8", False, self.settings.square_colour_bright)
        
        self.screen_game.blit(number_surface_1, (self.settings.grid_width / 10, 0 * self.settings.grid_height + self.settings.grid_height / 8))
        self.screen_game.blit(number_surface_2, (self.settings.grid_width / 10, 1 * self.settings.grid_height + self.settings.grid_height / 8))
        self.screen_game.blit(number_surface_3, (self.settings.grid_width / 10, 2 * self.settings.grid_height + self.settings.grid_height / 8))
        self.screen_game.blit(number_surface_4, (self.settings.grid_width / 10, 3 * self.settings.grid_height + self.settings.grid_height / 8))
        self.screen_game.blit(number_surface_5, (self.settings.grid_width / 10, 4 * self.settings.grid_height + self.settings.grid_height / 8))
        self.screen_game.blit(number_surface_6, (self.settings.grid_width / 10, 5 * self.settings.grid_height + self.settings.grid_height / 8))
        self.screen_game.blit(number_surface_7, (self.settings.grid_width / 10, 6 * self.settings.grid_height + self.settings.grid_height / 8))
        self.screen_game.blit(number_surface_8, (self.settings.grid_width / 10, 7 * self.settings.grid_height + self.settings.grid_height / 8))
            
    # _________________________________Hightlight Moves _____________________________
    def highlight_moves(self) -> None:
            # NOT ALL PIECE MOVES
            if len(self.left_click_history) > 1:
                return
            
            self.selected_piece = self.left_click_history[0]

            for element in self.selected_piece.list_moves:
                board_pos_row = element[0]
                board_pos_col = element[1]
        
                pygame.draw.rect(
                    self.screen_game,
                    self.settings.square_colour_move,
                    [
                        self.settings.grid_width * board_pos_col,
                        self.settings.grid_height * board_pos_row,
                        self.settings.grid_width,
                        self.settings.grid_height,
                    ],
                )   
    # ________________________________Hightlight Squares _________________________
    # Gives user selected squares a diferent colour
    def highlight_squares(self) -> None:
        for element in self.right_click_history:
            board_pos_row = element.get_row()
            board_pos_col = element.get_col()
            pygame.draw.rect(
                self.screen_game,
                self.settings.square_colour_highlight,
                [
                    self.settings.grid_width * board_pos_col,
                    self.settings.grid_height * board_pos_row,
                    self.settings.grid_width,
                    self.settings.grid_height,
                ],
            ) 
    
    # Gives selected piece a diferent colour square
    def highrlight_piece(self) -> None:
        self.selected_piece = self.left_click_history[0]
        pygame.draw.rect(
            self.screen_game,
            self.settings.square_colour_piece,
            [
                self.settings.grid_width * self.selected_piece.get_col(),
                self.settings.grid_height * self.selected_piece.get_row(),
                self.settings.grid_width,
                self.settings.grid_height,
            ],
        )  
        
    # ________________________________Hightlight Check _________________________
    def hightlight_check(self) -> None:
        king = self.game_board.get_king(self.player_turn)
        if self.game_board.verify_king_check:
            pygame.draw.rect(
                self.screen_game,
                self.settings.square_colour_highlight,
                [
                    self.settings.grid_width * king.get_col(),
                    self.settings.grid_height * king.get_row(),
                    self.settings.grid_width,
                    self.settings.grid_height,
                ]
            )
            
    # ________________________________ Draw Pieces _______________________________
    def draw_pieces(self) -> None:
        counter_y = self.settings.grid_height / 8
        for piece_row in range(len(self.game_board.board)):
            counter_x = self.settings.grid_width / 8
            for element in self.game_board.board[piece_row]:
                if element._name != self.No_Piece_Ref._name:
                    image = pygame.transform.scale(
                        element.piece_image,
                        (
                            self.settings.grid_width - self.settings.grid_width / 4,
                            self.settings.grid_height - self.settings.grid_height / 4,
                        ),
                    )
                    self.screen_game.blit(image, (counter_x, counter_y))
                counter_x += self.settings.grid_width
            counter_y += self.settings.grid_width

    # _______________________________ Detect Collisions ___________________________
    def click_collisions(self, mouse_pos) -> object:
        board_pos_x = int(mouse_pos[0] / self.settings.grid_width)
        board_pos_y = int(mouse_pos[1] / self.settings.grid_height)
        
        selected_piece = self.game_board.board[board_pos_y][board_pos_x]
        
        if selected_piece._name != self.No_Piece_Ref._name:
            print("-----------------------------------------")
            print("Piece Selected: ", selected_piece._name)
            print("Piece Colour: ", selected_piece._player.name)
            print("Position Row: ", selected_piece.get_row())
            print("Position Col: ", selected_piece.get_col())
            print("-----------------------------------------")            
        return selected_piece
    
    # _______________________________ Moving Animation ___________________________
    # Not implemented
    def moving_animation(self, mouse_pos):
        if self.selected_piece == None:
            print("Can not move None Piece")
        else:
            image = pygame.transform.scale(
                self.selected_piece.piece_image,
                (
                    self.settings.grid_width,
                    self.settings.grid_height
                )
            )
            self.screen_game.blit(image, mouse_pos)


if __name__ == "__main__":
    pygame.init()
    Choss().run_app()
