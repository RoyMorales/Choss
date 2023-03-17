# Settings

class SettingsClass:
    def __init__(self):
         # Window Settings
        self.window_width = 800
        self.window_height = 800

        # Game Grid
        self.number_squares = int(8)
        self.grid_width = self.window_width / self.number_squares
        self.grid_height = self.window_width / self.number_squares

        # Grid Color
        self.square_colour_bright = (242, 172, 102, 95)
        self.square_colour_dark = (112, 80, 47, 44)
        self.square_colour_move = (240, 135, 29, 94)
        self.square_colour_piece = (204, 205, 210, 81)
        self.square_colour_highlight = (210, 62, 53, 82)
        # Grid Lines
        self.lines_colour = (112, 63, 13, 44)
        self.lines_width = 6