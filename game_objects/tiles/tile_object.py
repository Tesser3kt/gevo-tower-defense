from game_objects.inactive_object import InactiveObject
from game_objects.immobile_object import ImmobileObject

from game_objects.tiles.tile_type import TileType
from pygame.surface import Surface

class TileObject(InactiveObject,ImmobileObject):
    """ Most general class for tile objects """

    def __init__(
        self, x: int, y: int, width: int, height: int, image: Surface,
        #possible types:
        #occupied, buildable, wall, default
        type:TileType=TileType.DEFAULT

    ) -> None:
        InactiveObject.__init__(self, x, y, width, height, image)
        ImmobileObject.__init__(self, x, y, width, height, image)

        self.type=type
        #change the image based on the tile type from the config.
    
    def update(self)->None:
        InactiveObject.update(self)
        ImmobileObject.update(self)

    def built_on(self)->None:
        self.type=TileType.OCCUPIED
        #change the surface to the occupied surface (just the outside of the tower)
