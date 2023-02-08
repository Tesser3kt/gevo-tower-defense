from active_object import ActiveObject
from immobile_object import ImmobileObject

from pygame.surface import Surface


class TowerObject(ActiveObject,ImmobileObject):
    """ Most general class for tower objects """

    def __init__(self, x: int, y: int, width: int, height: int, image: Surface,
     animation: list[Surface],damage:int,reload_speed:int,
     tower_type:str, animation_index: int = 0, lvl:int=1,
     
     ) -> None:
        ActiveObject.__init__(x,y,width,height,image,animation,animation_index,lvl)
        ImmobileObject.__init__(x,y,width,height,height,image)

        self.damage=damage
        self.reload_speed=reload_speed
        self.tower_type=tower_type

    def update(self):
        ActiveObject.update(self)
        ImmobileObject.update(self)

    def upgrage(self):
        """ Update the coresponding stats based on the lvl"""


    def fire(self)->None:
        """ Fires the coresponding projectile type to the neares enemy """

        pass