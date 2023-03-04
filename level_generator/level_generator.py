"""Avek sa kan dan la man"""

from enum import Enum
import random
from PIL import Image

from config.general_config import Tile, Colors
from config.level_generator_config import *

class Direction(Enum):
    """Class that contains Direction vectors"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def first_direction(start_point:tuple[int]) -> Direction:
    """Return start direction on base of start point"""
    x, y = start_point
    if x == 0:
        return Direction.RIGHT
    elif x == Tile.WIDTH-1:
        return Direction.LEFT
    elif y == 0:
        return Direction.DOWN
    else:
        return Direction.UP

def init_probs(probability:dict, first_direction:Direction) -> None:
    """Change all probabilities to zero and than change the starting direction probability to 100 %"""
    for direction in Direction:
        probability[direction.value] = 0

    probability[first_direction.value] = Config_lvl_gen.MAX_PROB

def update_probs(probability:dict, last_direction:Direction, pref_directions:list) -> None:
    """Update the probability after going in the same direction"""

    
    #Sníží probabilitu o 1 prob. decrease
    probability[last_direction.value] -= Config_lvl_gen.PROB_DECREASE

    #Přidá probability do 2 zbývajících směrů (směry kolmé na předchozí)
    x, y = last_direction.value
    if (y, x) in pref_directions:
        probability[(y, x)] += (Config_lvl_gen.PROB_DECREASE // Config_lvl_gen.PROB_DIVISOR)*(Config_lvl_gen.PROB_NUMERATOR)
        probability[(-y, -x)] += (Config_lvl_gen.PROB_DECREASE // Config_lvl_gen.PROB_DIVISOR)*(Config_lvl_gen.PROB_DIVISOR - Config_lvl_gen.PROB_NUMERATOR)
    else:
        probability[(y, x)] += (Config_lvl_gen.PROB_DECREASE // Config_lvl_gen.PROB_DIVISOR)*(Config_lvl_gen.PROB_DIVISOR-Config_lvl_gen.PROB_NUMERATOR)
        probability[(-y, -x)] += (Config_lvl_gen.PROB_DECREASE // Config_lvl_gen.PROB_DIVISOR)*(Config_lvl_gen.PROB_NUMERATOR)

    #Preferovat smery od startu, rozdelit na mensi casti

def pref_directions(start_point:tuple[int]) -> list[Direction]:
    """"Return preferable directions from start point"""
    x, y = start_point
    pref_directions =[]
    if x > Tile.WIDTH//2:
        pref_directions.append(Direction.LEFT.value)
    else:
        pref_directions += [Direction.RIGHT.value]
    if y > Tile.HEIGHT//2:
        pref_directions += [Direction.UP.value]
    else:
        pref_directions += [Direction.DOWN.value]

    return pref_directions

def draw_point(x:int, y:int, img:Image)->None:
    """Create 1 point on a specific pixel on the image"""
    img.putpixel((x, y), Colors.PATH)

def my_random_direction(probability:dict) -> Direction:
    """Return a random direction based on probabilities"""
    vectors_probability = []
    for i in range(probability[Direction.UP.value]):
        vectors_probability.append(Direction.UP)
    for i in range(probability[Direction.DOWN.value]):
        vectors_probability.append(Direction.DOWN)
    for i in range(probability[Direction.RIGHT.value]):
        vectors_probability.append(Direction.RIGHT)
    for i in range(probability[Direction.LEFT.value]):
        vectors_probability.append(Direction.LEFT)
    
    return random.choice(vectors_probability)

def move_to(rnd_direction:Direction, x:int, y:int) -> tuple:
    """Change x, y to a new value based on the Direction"""
    x += rnd_direction.value[0]
    y += rnd_direction.value[1]
    return x, y

def end_points(start_point:tuple)->list[tuple]:
    """Creates a list of coords of legal end points"""
    if start_point[0] == 0:
        return [(Tile.WIDTH-1, y) for y in range(Tile.HEIGHT)]
    elif start_point[1] == 0:
        return [(x, Tile.HEIGHT-1) for x in range(Tile.WIDTH)]
    elif start_point[0] == Tile.WIDTH-1:
        return [(0, y) for y in range(Tile.HEIGHT)]
    else:
        return [(x, 0) for x in range(Tile.WIDTH)]

def legal_move(x:int, y:int):
    return 0<=x<Tile.WIDTH and 0<=y<Tile.HEIGHT

def generate_level(lvl:int, difficulty:int):
    """Generate a level"""

    probability = {
        Direction.UP.value: 250,
        Direction.DOWN.value: 250,
        Direction.LEFT.value: 250,
        Direction.RIGHT.value: 250
    }

    img = Image.new('RGB', (Tile.WIDTH, Tile.HEIGHT), color = (0, 0, 0))

    #Vytvoří random start na random ose a pak vybere 1 start 
    start_osa_1 = 0, random.randint(5, Tile.HEIGHT-5)
    start_osa_2 = random.randint(5, Tile.WIDTH-5), 0
    start_osa_3 = Tile.WIDTH-1, random.randint(5, Tile.HEIGHT-5)
    start_osa_4 = random.randint(5, Tile.WIDTH-5), Tile.HEIGHT-1
    #Vybraný start
    chosen_start = random.choice([start_osa_1, start_osa_2, start_osa_3, start_osa_4])

    # Define the border pixels
    border_pixels = set(
        [(x, 0) for x in range(Tile.WIDTH)] + 
        [(x, Tile.HEIGHT-1) for x in range(Tile.WIDTH)] + 
        [(0, y) for y in range(1, Tile.HEIGHT-1)] + 
        [(Tile.WIDTH-1, y) for y in range(1, Tile.HEIGHT-1)]
    )

    #Start direction
    first_direction_1 = first_direction(chosen_start)

    #Initialize probabilities
    init_probs(probability, first_direction_1)

    x, y = chosen_start
    #Nakreslí start
    draw_point(*chosen_start, img)

    #Posunese o pixel dál
    x, y = x+first_direction_1.value[0], y+first_direction_1.value[1]
    draw_point(x, y, img)
    last_direction = first_direction_1

    pref_directions_1 = pref_directions(chosen_start)

    end_points_1 = end_points(chosen_start)
    counter = 0 #Počet kroků rovně

    while (x, y) not in end_points_1:

        direction = my_random_direction(probability)
        while not legal_move(*move_to(direction, x, y)):
            direction = my_random_direction(probability)
            if probability[direction.value] == Config_lvl_gen.MAX_PROB:
                update_probs(probability, direction, pref_directions_1)
            
        x, y = move_to(direction, x, y)
        draw_point(x, y, img)

        if direction == last_direction:
            if counter > Config_lvl_gen.MIN_STRAIGHT_LINE:
                update_probs(probability, last_direction, pref_directions_1)
            else:
                counter += 1
        else:
            init_probs(probability, direction)
            last_direction = direction
            counter = 0

    # Save the image
    i = lvl
    img.save(f"assets/level_maps/level_{i}.png")