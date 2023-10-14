from pygame.font import Font
from config.settings.general_config import Gui_font, Colors, Window
from config.settings.towers import *
from game_objects.game_object import GameObject
from graphics_manager.graphics_manager import GraphicsManager

from pygame import draw, display, Surface
from pygame.sprite import RenderUpdates, Sprite
from pygame.transform import scale


class Gui():
    def __init__(self, gfx_manager:GraphicsManager) -> None:
        self.graphics_manager = gfx_manager
        self.position  = Window.GUI_POS
        self.font_size = Gui_font.size
        self.path = Gui_font.path
        self.color = Colors.MENU_TEXT
        self.background_color = Colors.MENU_BG

        self.background = None

        self.font = Font(self.path, self.font_size)
        self.small_font = Font(self.path, self.font_size//2)
        self.gui_scale = Window.GUI_SCALE

        self.gui_height = Window.GUI_HEIGHT
        self.gui_width = Window.GAME_WIDTH
        self.center_for_text = (self.gui_height-self.font_size)//2
        # Tohle bude chtit algoritmus na automaticke zarovnani
        self.stats_position = ((Window.GUI_WIDTH//2)*1.25, self.center_for_text)
        self.pause_pos = (Window.GUI_WIDTH//2, Window.GUI_HEIGHT-10-self.font_size)

        self.towers_pos = []
        self.tower_pos_types = []

        self.tower_cards = RenderUpdates()


    def create_gui(self, lives:int, coins:int, wave:int, textures:dict):
        """ Creates the gui"""
        self.draw_background()
        self.show_stats(lives, coins, wave)
        self.show_towers(textures)


    def draw_background(self):
        """ Draws the background of the gui"""
        #draw.rect(screen, self.background_color, (self.position[0], self.position[1], Window.WIDTH, Window.GUI_HEIGHT))
        self.background = Surface((Window.GUI_WIDTH, Window.GUI_HEIGHT))
        self.background.fill(self.background_color)
        self.background = self.background.convert()

        background_object = GameObject(0, 0, Window.GUI_WIDTH, Window.GUI_HEIGHT, self.background)
        self.graphics_manager.draw_object(background_object, False)


    def create_towers_grid(self):
        """ Creates the grid of tower cards"""
        for tower, tower_type in enumerate(tower_types):
            position = (Window.CARD_RECT_WIDTH+tower*Window.PIXEL_SIZE*self.gui_scale+tower*Window.CARD_RECT_WIDTH, (self.gui_height-Window.PIXEL_SIZE*self.gui_scale)//2)
            self.towers_pos.append(position)
            self.tower_pos_types.append((position, tower_type))

    def show_stats(self, lives:int, coins:int, wave:int):
        stats_text = self.font.render(f'Wave: {wave}    Coins: {coins}    Lives: {lives}', True, self.color, self.background_color)
        stats_rect = stats_text.get_rect(topleft=self.stats_position)
        stats = GameObject(stats_rect.x, stats_rect.y, stats_rect.width, stats_rect.height, stats_text)

        self.graphics_manager.draw_object(stats, False, self.background)
    
    def show_tower_info(self, tower_type):
        info_text = self.small_font.render(f'{tower_type.__name__}:    Cost: {tower_type.COST}    Range: {tower_type.RANGE}    Damage: {tower_type.DAMAGE}    Reload time: {tower_type.RELOAD_TIME}                                  ', True, self.color, self.background_color)
        info_rect = info_text.get_rect(topleft=(10, Window.GUI_HEIGHT-self.font_size//2-5))
        info = GameObject(info_rect.x, info_rect.y, info_rect.width, info_rect.height, info_text)

        self.graphics_manager.draw_object(info, False, self.background)

    def show_towers(self, textures:dict):
            """ Shows the towers on the screen"""
            self.tower_cards.empty()
            self.create_towers_grid()
            for index, tower_type in enumerate(tower_types):
                image_name = tower_type.IMAGE
                image = textures["game_objects"]["towers"][image_name][0]
                image = scale(image, (self.gui_scale*Window.PIXEL_SIZE, self.gui_scale*Window.PIXEL_SIZE))
                tower_card = GameObject(self.towers_pos[index][0],self.towers_pos[index][1], width=self.gui_scale*Window.PIXEL_SIZE, height=self.gui_scale*Window.PIXEL_SIZE, image=image)
                self.tower_cards.add(tower_card)
            self.graphics_manager.draw_group(self.tower_cards, False, self.background)

    # def pause_text(self, pause:bool):
    #     """ Shows the pause on the screen"""
    #     if pause:
    #         pause_text = self.font.render(f'Pause', True, Colors.BUTTONS, self.background_color)
    #         pause_rect = pause_text.get_rect(topleft=self.pause_pos)

    #         pause_G = GameObject(pause_rect.x, pause_rect.y, pause_rect.width, pause_rect.height, pause_text)
    #         self.pause_object = pause_G
    #         self.graphics_manager.draw_object(pause_G, False, self.background)

    def change_size(self, size:int):
        """ Changes the size of the gui. Size is a multiplier of the original size"""
        self.font_size *= size
        self.font = Font(self.path, self.font_size)
        self.gui_scale = size

    def change_color(self, color:tuple):
        """ Changes the color of the font in gui"""
        self.color = color
