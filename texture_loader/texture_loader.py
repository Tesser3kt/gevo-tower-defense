""" texture loader module. """
#from config.general_config import *
from pygame.image import load
import os
BASE_DIR = r"C:\Users\HP\repa\gevo-tower-defense-1\texture_loader"
ASSETS_DIR = "HP"

class TextureLoader:
    """ Texture loader class. """
    def __init__(self):
        ...

    def load_all_textures(self) -> dict:
        """ Load all textures. """
        #assets_path = os.path.join(BASE_DIR, ASSETS_DIR)
        assets_path = r"C:\Users\HP\repa\gevo-tower-defense-1\texture_loader"

        texture_dict = {}
        for folder in os.listdir(assets_path):
            if folder not in texture_dict:
                texture_dict[folder] = {}
            

            for sub_folder in os.listdir(os.path.join(assets_path, folder)):
                if sub_folder not in texture_dict[folder]:
                    texture_dict[folder][sub_folder] = {}

                for textures in os.listdir(os.path.join(assets_path, folder, sub_folder)):
                    if textures not in texture_dict[folder][sub_folder]:
                        texture_dict[folder][sub_folder][textures] = []

                    for texture in os.listdir(os.path.join(assets_path, folder, sub_folder, textures)):
                        image = load(texture)
                        image = image.convert()
                        texture_dict[folder][sub_folder][textures].append(image)

        return texture_dict
        

x = TextureLoader()
print(x.load_all_textures())
