from pygame.font import Font
from config.settings.general_config import Gui_font, Colors, Window, Tile
from config.settings.towers import *
from game_objects.game_object import GameObject

from pygame import draw

from pygame.transform import scale
class Gui():
    def __init__(self) -> None:
        self.position  = Window.GUI_POS
        self.font_size = Gui_font.size
        self.path = Gui_font.path
        self.color = Colors.MENU_TEXT
        self.background_color = Colors.MENU_BG


        self.font = Font(self.path, self.font_size)
        self.gui_scale = Window.GUI_SCALE

        self.gui_height = Window.GUI_HEIGHT
        self.gui_width = Window.WIDTH
        self.center_for_text = (self.gui_height-self.font_size)//2
        # Tohle bude chtit algoritmus na automaticke zarovnani
        self.lives_pos = (self.gui_width-100, self.center_for_text)
        self.coins_pos = (self.gui_width-230, self.center_for_text)
        self.wave_pos = (self.gui_width-320, self.center_for_text)

        self.lives_rect = None
        self.coins_rect = None
        self.wave_rect = None

        self.towers_pos = []
        self.changed_rects = []

    def create_gui(self, screen, lives:int, coins:int, wave:int, textures:dict):
        """ Creates the gui"""
        self.background(screen)
        self.show_lives(screen, lives)
        self.show_coins(screen, coins)
        self.show_wave(screen, wave)
        self.show_towers(screen, textures)



    def background(self, screen):
        """ Draws the background of the gui"""
        draw.rect(screen, self.background_color, (self.position[0], self.position[1], Window.WIDTH, Window.GUI_HEIGHT))

    def create_towers_grid(self):
        """ Creates the grid of tower cards"""
        for tower in range(len(tower_types)):
            self.towers_pos.append((5+tower*Tile.PIXEL_SIZE*self.gui_scale+5*tower, (self.gui_height-Tile.PIXEL_SIZE*self.gui_scale)//2))

    def show_lives(self, screen, lives:int):
        """ Shows the lives on the screen"""

        # Draw a rectangle to cover the previous text
        if self.lives_rect:
            draw.rect(screen, self.background_color, self.lives_rect)
        # Create the new text
        lives_text = self.font.render(f'Lives: {str(lives)}', True, self.color, self.background_color)
        self.lives_rect = lives_text.get_rect(topleft=self.lives_pos)
        self.changed_rects.append(self.lives_rect)
        screen.blit(lives_text, self.lives_pos)

    def show_coins(self, screen, coins:int):
        """ Shows the coins on the screen"""
        if self.coins_rect:
            draw.rect(screen, self.background_color, self.coins_rect)
        coins_text = self.font.render(f'Coins: {str(coins)}', True, self.color, self.background_color)
        self.coins_rect = coins_text.get_rect(topleft=self.coins_pos)
        self.changed_rects.append(self.coins_rect)
        screen.blit(coins_text, self.coins_pos)

    def show_wave(self, screen, wave:int):
        """ Shows the wave on the screen"""
        if self.wave_rect:
            draw.rect(screen, self.background_color, self.wave_rect)
        wave_text = self.font.render(f'Wave: {str(wave)}', True, self.color, self.background_color)
        self.wave_rect = wave_text.get_rect(topleft=self.wave_pos)
        self.changed_rects.append(self.wave_rect)
        screen.blit(wave_text, self.wave_pos)


    def show_towers(self, screen, textures:dict):
            """ Shows the towers on the screen"""
            self.create_towers_grid()
            for index, tower_type in enumerate(tower_types):
                image_name = tower_type.IMAGE
                image = textures["game_objects"]["towers"][image_name][0]
                image = scale(image, (self.gui_scale*Tile.PIXEL_SIZE, self.gui_scale*Tile.PIXEL_SIZE))
                tower_card = GameObject(self.towers_pos[index][0],self.towers_pos[index][1] , width=self.gui_scale*Tile.PIXEL_SIZE, height=self.gui_scale*Tile.PIXEL_SIZE, image=image)
                screen.blit(tower_card.image, tower_card.rect)
                self.changed_rects.append(tower_card.rect)


    def change_size(self, size:int):
        """ Changes the size of the gui. Size is a multiplier of the original size"""
        self.font_size *= size
        self.font = Font(self.path, self.font_size)
        self.gui_scale = size

    def change_color(self, color:tuple):
        self.color = color


