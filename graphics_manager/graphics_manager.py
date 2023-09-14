""" Graphics manager."""
import pygame as pg #importing pygame
import logging #importing logging
from config.settings.general_config import Window #importing Window class from config
from config.settings.general_config import Colors #importing colors class from config
from texture_loader.texture_loader import TextureLoader #importing texture_loader
from game_objects.game_object import GameObject #importing GameObject
#from config.enums.object_animation import ObjectAnimation
logging.debug("everything imported succesfully. ")

class GraphicsManager:
    def __init__(self) -> None:
        """ Graphics manager class."""
        logging.info("GraphicsManager called.")
        self.screen: pg.Surface = None
        self.textures: dict = {}
        self.background: pg.Surface = None
        self.rects_to_update = []

        self.canvas_game: pg.Surface = None
        self.canvas_gui: pg.Surface = None
        logging.debug("GraphicsManager class initializer ran succesfully.")

    def draw_object(self, object: GameObject, canvas, background=None) -> None:
        """ Draws object.image texture on object.rect place."""
        logging.debug(" draw_object method of GraphicsManager called succesfully.")
        if background is None:
            background = self.background
        self.rects_to_update.append(canvas.blit(object.image, object.rect))
        logging.debug("Object drawn succesfully.")

    def draw_group(self, group: pg.sprite.RenderUpdates, game:bool, background=None) -> None:
        """ Draws object.image texture on object.rect place."""
        logging.debug(" draw_object method of GraphicsManager called succesfully.")
        if background is None:
            background = self.background
        if game:
            surface = self.canvas_game
        else:
            surface = self.canvas_gui
        
        group.clear(surface, background)
        if game:
            self.rects_to_update += [pg.Rect(rect.x + Window.GUI_WIDTH, rect.y + Window.GUI_HEIGHT,
                                             rect.width, rect.height) for rect in group.draw(surface)]
        else:
            self.rects_to_update += group.draw(surface)


    def load_all_textures(self) -> None:
        """Initializates load_all_textures method."""
        logging.debug("Load_all_functions called.")
        self.textures = TextureLoader.load_all_textures(self)

    def init_graphics(self) -> None:
        """ Initializate graphics. """
        logging.debug("Function init_graphics called.")
        self.screen = pg.display.set_mode((Window.WINDOW_WIDTH, Window.WINDOW_HEIGHT), pg.SCALED)    #creating window
        logging.info("Window initialized succesfully.")

        self.background = pg.Surface(self.screen.get_size())       #defining background
        self.background.fill(Colors.BACKGROUND)     #filling background with colour
        self.background = self.background.convert()  #converting background
        
        self.canvas_game = pg.Surface((Window.GAME_WIDTH, Window.GAME_HEIGHT))
        self.canvas_gui = pg.Surface((Window.GUI_WIDTH, Window.GUI_HEIGHT))


        logging.debug("Background created succesfully.")
        logging.debug("Function init_graphics ran succesfully.")

    def update(self):
        """ Update screen. """
        logging.debug("screen update function called.")
        self.screen.blit(self.canvas_game, (Window.GUI_WIDTH, Window.GUI_HEIGHT))
        self.screen.blit(self.canvas_gui, (0,0))
        pg.display.update(self.rects_to_update)
        self.rects_to_update = []
        logging.debug("Rects_to_update erased.")
        logging.debug("Screen updated succesfully!")

    def get_object_animation(self, object) -> list:
        """ Returns list of animations. """
        logging.debug(" Get_object_animation function of GraphicsManager class called.")
        objects_animations = []
        for folder1 in self.textures:
            for folder2 in self.textures[folder1]:
                for folder3 in self.textures[folder1][folder2]:
                    if folder3 == object.value:
                        for texture in self.textures[folder1][folder2][folder3]:
                            objects_animations.append(texture)
        return objects_animations