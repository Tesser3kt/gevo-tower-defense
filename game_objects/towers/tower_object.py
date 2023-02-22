from active_object import ActiveObject
from immobile_object import ImmobileObject

from pygame.surface import Surface
from tower_type import TowerType

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

    def update(self):
        ActiveObject.update(self)
        ImmobileObject.update(self)

    def upgrage(self):
        """ Update the coresponding stats based on the lvl"""
        lvl+=1
        #change the surface and stats

    def reloaded(self):
        if self.last_fired-self.reload_time<=0:
            return True
        return False

    def fire(self)->None:
        """ Fires the coresponding projectile type to the neares enemy """
        self.last_fired=time.clock_gettime()
        