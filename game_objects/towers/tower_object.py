from game_objects.active_object import ActiveObject
from game_objects.immobile_object import ImmobileObject

from pygame.surface import Surface
from game_objects.towers.tower_type import TowerType

import time

class TowerObject(ActiveObject,ImmobileObject):
    """ Most general class for tower objects """

    def __init__(self, x: int, y: int, width: int, height: int, image: Surface,
     animation: list[Surface],damage:int,reload_time:int,
     tower_type:TowerType, animation_index: int = 0, lvl:int=1,
     
     ) -> None:
        ActiveObject.__init__(x,y,width,height,image,animation,animation_index,lvl)
        ImmobileObject.__init__(x,y,width,height,height,image)

        self.damage=damage
        self.reload_time=reload_time
        self.tower_type=tower_type
        self.last_fired=0

    def update(self) -> None:
        ActiveObject.update(self)
        ImmobileObject.update(self)

    def upgrage(self) -> None:
        """ Update the corresponding stats based on the lvl"""
        self.lvl+=1
        #change the surface and stats

    def reloaded(self) -> bool:
        return time.time() - self.last_fired >= self.reload_time

    def fire(self)->None:
        """ Fires the coresponding projectile type to the neares enemy """
        self.last_fired=time.time()
        
