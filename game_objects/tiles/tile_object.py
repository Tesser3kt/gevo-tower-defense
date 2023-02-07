from inactive_object import InactiveObject
from immobile_object import ImmobileObject

from pygame.surface import Surface

class TileObject(InactiveObject,ImmobileObject):
    """ Most general class for tile objects """

    def __init__(
        self, x: int, y: int, width: int, height: int, image: Surface,
        #possible types:
        #occupied, buildable, wall, default
        type:str="default",

    ) -> None:
        InactiveObject.__init__(x, y, width, height, image)
        ImmobileObject.__init__(x, y, width, height, image)

        self.type=type
        #change the image based on the tile type from the config.
    
    def update(self)->None:
        InactiveObject.update(self)
        ImmobileObject.update(self)

    