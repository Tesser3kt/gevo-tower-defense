""" texture loader module. """
import logging
from pygame.image import load
import pygame as pg
import os
from config.setting.general_config import *
logging.debug("Everything imported succesfully. ")
class TextureLoader:
    """ Texture loader class. """
    def __init__(self):
        #delete
        pg.init()
        pg.display.set_mode((800, 800),pg.SCALED)
        #delete end
        logging.debug("TextureLoader class object initializated succesfully. ")

    def load_all_textures(self) -> dict:
        """ Load all textures. Returns dictionary of textures sorted by folders."""
        assets_path = os.path.join(BASE_DIR, ASSETS_DIR)
        logging.debug("Assets path created succesfully. ")
        logging.info(r"Function 'load_all_textures' of TextureLoader class object called succesfully.")
        

        texture_dict = {}
        logging.debug("Empty dictionary created succesfully.")
        if not os.path.exists(os.path.join(assets_path)):
            logging.error(f"Path {assets_path} does not exist. Crashing game.")
            print(f"Path {assets_path} does not exist.")
            pg.quit()
        for folder in os.listdir(assets_path):
            logging.debug(f"Listing in folder{assets_path} ...")
            if folder not in texture_dict:
                texture_dict[folder] = {}
                logging.debug(f"Created empty dictionary for {folder}.")
            
            if not os.path.exists(os.path.join(assets_path, folder)):
                logging.error(f"Path {assets_path}\{folder} doesn't eist. ")
                pg.quit()
            for sub_folder in os.listdir(os.path.join(assets_path, folder)):
                logging.debug(f"Listing in {os.path.join(assets_path, folder)}...")
                if sub_folder not in texture_dict[folder]:
                    texture_dict[folder][sub_folder] = {}
                    logging.debug(f"Created empty dictionary for {sub_folder}.")
                
                if not os.path.exists(os.path.join(assets_path, folder, sub_folder)):
                    logging.error(f"Path {assets_path}\{folder}\{sub_folder} doesn't exist. ")
                    pg.quit()
                for textures in os.listdir(os.path.join(assets_path, folder, sub_folder)):
                    logging.debug(f"Listing in {os.path.join(assets_path, folder, sub_folder)}...")
                    if textures not in texture_dict[folder][sub_folder]:
                        texture_dict[folder][sub_folder][textures] = []
                        logging.debug(f"Created empty list for {textures}.")

                    if not os.path.exists(os.path.join(assets_path, folder, sub_folder, textures)):
                        logging.error(f"Path {os.path.join(assets_path, folder, sub_folder, textures)} doesn't exist.")
                        pg.quit()
                    for texture in os.listdir(os.path.join(assets_path, folder, sub_folder, textures)):
                        try:
                            image = load(os.path.join(assets_path, folder, sub_folder, textures, texture))
                            logging.debug(f"Loaded image {os.path.join(assets_path, folder, sub_folder, textures, texture)}")
                            image = image.convert()
                        except Exception as e:
                            logging.error(f"Failed to load or convert {texture}: {e.message}")
                            pg.quit()
                        logging.debug(f"Converted image {os.path.join(assets_path, folder, sub_folder, textures, texture)}")
                        texture_dict[folder][sub_folder][textures].append(image)
                        logging.debug(f"Appended image {os.path.join(assets_path, folder, sub_folder, textures, texture)} to the list.")

        logging.info("Function 'load_all_textures' finished. ")
        return texture_dict
        
