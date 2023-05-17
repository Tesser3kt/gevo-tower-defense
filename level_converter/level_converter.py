from PIL import Image
from config.settings.general_config import Tile, Colors, Window, Directory
import pygame as pg
import os
import logging

#screen = pg.display.set_mode((Window.WIDTH, Window.HEIGHT), pg.SCALED)
#screen.fill((Colors.BACKGROUND))

#Load image
def load_image(level_difficulty: int):
    """Load level image"""
    try:
        logging.debug(f"Loading level {level_difficulty}")
        level = Image.open(os.path.join(Directory.ASSETS_DIR, "level_maps", f'level_{level_difficulty}.png'))
    except FileNotFoundError:
        logging.error(f"Level {level_difficulty} not found")
        raise FileNotFoundError
    return level


#Create rect
def create_rect(position: tuple)-> pg.Rect:
    """Create a rect from a color and a position"""
    try:
        return pg.Rect(position[0], position[1], Tile.PIXEL_SIZE, Tile.PIXEL_SIZE)
    except pg.error as e:
        logging.error(f"Level converter -> create_rect(): Cannot create rect from {position}. Error: {e}")


def convert_level(level_difficulty: int)-> dict:
    """Convert level image into pygame"""

    #Get data from level generator's image
    try:
        pixels = list(load_image(level_difficulty).getdata())
    except Exception as e:
        logging.error(f"Level converter -> convert_level(): Cannot load image. Error: {e}")
        raise e

    path_rect = []
    walls_rect = []
    start_rect = []
    end_rect = []
    free_tile_rect = []

    tiles = {
        "path": path_rect,
        "walls": walls_rect,
        "start": start_rect,
        "end": end_rect,
        "free_tile": free_tile_rect
    }

    #Process data from image
    for i, pixel in enumerate(pixels):
        x = i%Tile.WIDTH*Tile.PIXEL_SIZE
        y = i//Tile.WIDTH*Tile.PIXEL_SIZE

        
        #Detect colors
        if pixel == Colors.WALLS:
            square = create_rect((x, y))
            walls_rect.append(square)
        elif pixel == Colors.PATH:
            square = create_rect((x, y))
            path_rect.append(square)
        elif pixel == Colors.START:
            square = create_rect((x, y))
            start_rect.append(square)
        elif pixel == Colors.END:
            square = create_rect((x, y))
            end_rect.append(square)
        elif pixel == Colors.BACKGROUND:
            square = create_rect((x, y))
            free_tile_rect.append(square)
        else:
            logging.error(f"Level converter: Unknown color: {pixel}")



   #    -----------------------------------------------------------------------------
   #    -----------------------------------------------------------------------------
   #    -----------------------------------TESTING-----------------------------------
   #    -----------------------------------------------------------------------------
   #    -----------------------------------------------------------------------------
   #
   #screen = pg.display.set_mode((Window.WIDTH, Window.HEIGHT), pg.SCALED)
   #screen.fill((Colors.BACKGROUND))
   #print((len(tiles["free_tile"])+ len(tiles["path"])+ len(tiles["start_end"])+ len(tiles["walls"])))
   #while True:
   #    for event in pg.event.get():
   #        if event.type == pg.QUIT:
   #            pg.quit()
   #            quit()

   #     
   #    for j, tile in enumerate(tiles.values()):
   #        for i, rect in enumerate(tile):
   #            pg.draw.rect(screen, ((j+1)*10, (j+1)*50, (j+1)*50) , rect)
   #            #print("yes") if rect.x == 0 and rect.y == 0 else None

   #    pg.display.update()

    return tiles
