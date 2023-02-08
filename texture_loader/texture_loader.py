""" texture loader module. """
from config.general_config import *
from pygame.image import load
import os


class TextureLoader:
    """ Texture loader class. """
    def __init__(self, BASE_DIR, ASSETS_DIR):
        self.BASE_DIR = BASE_DIR
        self.ASSETS_DIR = ASSETS_DIR

    def load_all_textures(self) -> dict:
        """ Load all textures. """
        assets_path = os.path.join(self.BASE_DIR, self.ASSETS_DIR)

        texture_dict = {}
        for folder in os.listdir(assets_path):
            if folder not in texture_dict:
                texture_dict[folder] = {}

            for sub_folder in os.listdir(os.path.join(assets_path, folder)):
                if sub_folder not in texture_dict[folder]:
                    texture_dict[folder][sub_folder] = {}

                for final_folder in sub_folder:

