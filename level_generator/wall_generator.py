from PIL import Image
from config.settings.general_config import Colors
from config.settings.general_config import Tile
NUMBER_OF_WALLS_DICTIONARY  = {
    0: 5,
    1: 10,
    2: 15,
    3: 20,
    4: 25,
    5: 30,
}
from random import randint

def load_image(lvl):
    img = Image.open(f"assets/level_maps/level_{lvl}.png")
    return img
    
def draw_point(x:int, y:int, img:Image)->None:
    """Create 1 point on a specific pixel on the image"""
    img.putpixel((x, y), Colors.WALLS)

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

    for wall in range(NUMBER_OF_WALLS_DICTIONARY[lvl]):
        x_one = randint(0, Tile.WIDTH - 1)
        y_one = randint(0, Tile.HEIGHT - 1)

        x_two = randint(0, Tile.WIDTH - 1)
        y_two = randint(0, Tile.HEIGHT - 1)
        
        y = y_one
        x = x_one

        while y < y_two:
            y += 1
            if converted_image[x_one][y] == Colors.PATH or converted_image[x_one][y] == Colors.START or converted_image[x_one][y] == Colors.END:
                continue
            draw_point(x_one, y, img)


        while y > y_two:
            y -= 1
            if converted_image[x_one][y] == Colors.PATH or converted_image[x_one][y] == Colors.START or converted_image[x_one][y] == Colors.END:
                continue
            draw_point(x_one, y, img)


        while x < x_two:
            x += 1
            if converted_image[x][y_one] == Colors.PATH or converted_image[x][y_one] == Colors.START or converted_image[x][y_one] == Colors.END:
                continue
            draw_point(x, y_one, img)


        while x > x_two:
            x -= 1
            if converted_image[x][y_one] == Colors.PATH or converted_image[x][y_one] == Colors.START or converted_image[x][y_one] == Colors.END:
                continue
            draw_point(x, y_one, img)


        if converted_image[x_one][y_one] == Colors.PATH or converted_image[x_one][y_one] == Colors.START or converted_image[x_one][y_one] == Colors.END:
            continue
        draw_point(x_one, y_one, img)

    
def create_walls(lvl: int):
    image = load_image(lvl)
    generate_walls(image, lvl)
    save_image(image, lvl)