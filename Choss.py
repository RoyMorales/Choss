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

        # Set Board
        self.game_board = Board()
        self.selected_piece_moving = False
        self.selected_piece = None
        # Empty Space
        self.No_Piece_Ref = No_Piece((-1, -1), Player.NONE)

    # ________________________________ Runner____________________________________
    def run_app(self):
        while True:
            self.check_event()
            self.draw_board()
            self.draw_pieces()
            
            pygame.display.update()

    # ________________________________ Events ___________________________________
    def check_event(self):
        event = pygame.event.wait(100)

        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.selected_piece_moving = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = pygame.mouse.get_pressed()
            # Mouse [0] -> Left Click
            # Mouse [1] -> Right Click
            if mouse_press[0]:
                print("Mouse Position:", mouse_pos)
                self.click_collisions(mouse_pos)
            elif mouse_press[1]:
                print("Right Mouse Click: ", mouse_pos)
        #elif event.type == pygame.MOUSEMOTION and self.selected_piece_moving == True:
        #    self.moving_animation(mouse_pos)

    # ________________________________ Draw Board _______________________________
    def draw_board(self):
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
        if self.selected_piece != None:
            self.highlight_moves()

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
            
    # _________________________________Hightlight Moves _____________________________
    def highlight_moves(self) -> None:
            # NOT ALL PIECE MOVES
            if self.selected_piece.moves == None:
                return 
            
            list_moves = self.selected_piece.moves()
            
            for element in list_moves:
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
    def click_collisions(self, mouse_pos):
        board_pos_x = int(mouse_pos[0] / self.settings.grid_width)
        board_pos_y = int(mouse_pos[1] / self.settings.grid_height)

        self.selected_piece = self.game_board.board[board_pos_y][board_pos_x]

        if self.selected_piece._name == self.No_Piece_Ref._name:
            print("Empty Space")
        else:
            print("Piece Selected: ", self.selected_piece._name)
            print("Piece Colour: ", self.selected_piece._player.name)
            print("Position X: ", self.selected_piece.get_col())
            print("Position Y: ", self.selected_piece.get_row())
            self.selected_piece_moving = True
        print()
    # _______________________________ Moving Animation ___________________________
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