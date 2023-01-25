from game_object import GameObject
from pygame.sprite import Sprite

class ImobileObjects(GameObject):
    """ Class for objects that are solid"""

    def __init__(self, x: int, y: int,  width:int, height:int, sprite: Sprite) -> None:
        super().__init__(x, y, width, height, sprite)