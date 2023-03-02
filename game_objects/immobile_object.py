from game_object import GameObject
from pygame.surface import Surface


class ImmobileObject(GameObject):
    """ Class for objects that are solid"""

    def __init__(self, x: int, y: int,  width:int, height:int, image: Surface) -> None:
        super().__init__(x, y, width, height, image)

    def update(self)->None:
        """update"""
        GameObject.update(self)