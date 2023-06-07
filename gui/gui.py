from pygame.font import Font
from config.settings.general_config import Gui_font, Colors

class Gui():
    def __init__(self, position:tuple) -> None:
        self.position  = position
        self.size = Gui_font.size
        self.path = Gui_font.path
        self.color = Colors.MENU_TEXT
        self.background_color = Colors.MENU_BG


        self.font = Font(self.path, self.size)

    def change_size(self, size:int):
        self.size = size
        self.font = Font(self.path, self.size)

    def change_color(self, color:tuple):
        self.color = color

    def write(self, text, screen):
        screen.blit(self.font.render(text, True, self.color, self.background_color), self.position)
