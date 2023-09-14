from PIL import Image
from config.settings.general_config import Colors
from config.settings.general_config import Tile
from config.settings.wall_generator_config import *
from random import randint

def load_image(lvl):
    img = Image.open(f"assets/level_maps/level_{lvl}.png")
    return img
    
def draw_point_vertical(x:int, y:int, img:Image)->None:
    """Create 1 point on a specific pixel on the image"""
    img.putpixel((x, y), Colors.WALLS_VERTICAL)

def draw_point_horizontal(x:int, y:int, img:Image)->None:
    """Create 1 point on a specific pixel on the image"""
    img.putpixel((x, y), Colors.WALLS_HORIZONTAL)

def save_image(img: Image, lvl: int):
    img.save(f"assets/level_maps/level_{lvl}.png")

def convert_to_array(img: Image) -> list:

    converted_image = [
        [None for _ in range(50)]
        for _ in range(60)
    ]
    img_data = list(img.getdata())
    for index, color in enumerate(img_data):
        converted_image[index % 60][index // 60] = color

    return converted_image

def generate_walls(img: Image, lvl: int):
    converted_image = convert_to_array(img)
    points_to_draw_vertical = []
    points_to_draw_horizontal = []
    walls_vertical = []
    walls_horizontal = []

    while len(walls_horizontal) < NUMBER_OF_WALLS_DICTIONARY[lvl]:
        x_one = randint(0, Tile.WIDTH - 1)
        y_one = randint(0, Tile.HEIGHT - 1)

        x_two = randint(0, Tile.WIDTH - 1)
        y_two = randint(0, Tile.HEIGHT - 1)
        
        y = y_one
        x = x_one
        trash_wall = False

        wall_length = 0

        while y < y_two:
            y += 1
            wall_length += 1
            if converted_image[x_one][y] == Colors.PATH or converted_image[x_one][y] == Colors.START or converted_image[x_one][y] == Colors.END:
                trash_wall = True
                y = y_one
                wall_length = 0
                break
            points_to_draw_vertical.append((x_one, y))


        while y > y_two:
            y -= 1
            wall_length += 1
            if converted_image[x_one][y] == Colors.PATH or converted_image[x_one][y] == Colors.START or converted_image[x_one][y] == Colors.END:
                trash_wall = True
                y = y_one
                wall_length = 0
                break
            points_to_draw_vertical.append((x_one, y))


        while x < x_two:
            x += 1
            wall_length += 1
            if converted_image[x][y_one] == Colors.PATH or converted_image[x][y_one] == Colors.START or converted_image[x][y_one] == Colors.END:
                trash_wall = True
                x = x_one
                wall_length = 0
                break
            points_to_draw_horizontal.append((x, y_one))


        while x > x_two:
            x -= 1
            wall_length += 1
            if converted_image[x][y_one] == Colors.PATH or converted_image[x][y_one] == Colors.START or converted_image[x][y_one] == Colors.END:
                trash_wall = True
                x = x_one
                wall_length = 0
                break
            points_to_draw_horizontal.append((x, y_one))

        if converted_image[x_one][y_one] == Colors.PATH or converted_image[x_one][y_one] == Colors.START or converted_image[x_one][y_one] == Colors.END:
            trash_wall = True

        points_to_draw_vertical.append((x_one, y_one))

        if wall_length < MINIMUM_LENGTH_OF_WALLS:
            trash_wall = True

        if converted_image[x_one][y_one] == Colors.WALLS_VERTICAL and converted_image[x_two][y_two] == Colors.WALLS_VERTICAL or Colors.WALLS_HORIZONTAL and converted_image[x_two][y_two] == Colors.WALLS_HORIZONTAL:
            trash_wall = True

        if not trash_wall:
            walls_vertical.append(points_to_draw_vertical.copy())
            walls_horizontal.append(points_to_draw_horizontal.copy())
        points_to_draw_horizontal = []
        points_to_draw_vertical = []

    for wall in walls_vertical:
        for point in wall:
            draw_point_vertical(point[0], point[1], img)

    for wall in walls_horizontal:
        for point in wall:
            draw_point_horizontal(point[0], point[1], img)
    


    
def create_walls(lvl: int):
    image = load_image(lvl)
    generate_walls(image, lvl)
    save_image(image, lvl)