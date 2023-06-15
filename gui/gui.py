from pygame.font import Font
from config.settings.general_config import Gui_font, Colors, Window, Tile
from config.settings.towers import *
from game_objects.game_object import GameObject



from pygame.transform import scale
class Gui():
    def __init__(self) -> None:
        self.position  = Window.GUI_POS
        self.size = Gui_font.size
        self.path = Gui_font.path
        self.color = Colors.MENU_TEXT
        self.background_color = Colors.MENU_BG


        self.font = Font(self.path, self.size)


        self.lives_pos = Window.LIVES_POS
        self.coins_pos = Window.COINS_POS
        self.wave_pos = Window.WAVE_POS
        self.towers_pos = ((0, 5), (32, 5),(64, 5),(96, 5),(128, 5),(160, 5),(192, 5),(218, 5),)#Window.TOWERS_POS
        self.changed_rects = []

    def show_lives(self, screen, lives:int):
        screen.blit(self.font.render(f'Lives: {str(lives)}', True, self.color, self.background_color), self.lives_pos)

    def show_towers(self, screen, textures:dict):
        for index, tower_type in enumerate(tower_types):
            image_name = tower_type.IMAGE
            image = textures["game_objects"]["towers"][image_name][0]
            image = scale(image, (Tile.PIXEL_SIZE, Tile.PIXEL_SIZE))
            tower_card = GameObject(self.towers_pos[index][0],self.towers_pos[index][1] , width=Tile.PIXEL_SIZE, height=Tile.PIXEL_SIZE, image=image)
            screen.blit(tower_card.image, tower_card.rect)
            self.changed_rects.append(tower_card.rect)

    def show_coins(self, screen, coins:int):
        screen.blit(self.font.render(f'Coins: {str(coins)}', True, self.color, self.background_color), self.coins_pos)

    def show_wave(self, screen, wave:int):
        screen.blit(self.font.render(f'Wave: {str(wave)}', True, self.color, self.background_color), self.wave_pos)

    def change_size(self, size:int):
        self.size = size
        self.font = Font(self.path, self.size)

    def change_color(self, color:tuple):
        self.color = color

    def write(self, screen, text:str):
        screen.blit(self.font.render(text, True, self.color, self.background_color), self.position)


