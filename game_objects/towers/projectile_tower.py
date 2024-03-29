from pygame.surface import Surface

from game_objects.towers.tower_object import TowerObject
from game_objects.towers.tower_type import TowerType

class ProjectileTower(TowerObject):
    """ Class for projectile tower objects """

    def __init__(
     self, x: int, y: int, width: int, height: int, image: Surface,
     animation: list[Surface],damage:int,reload_time:int,
     tower_type:TowerType,
     projectile_animation:list[Surface], 
     animation_index: int = 0, lvl:int=1
    )->None:

        TowerObject.__init__(self,x,y,width,height,image,animation,damage,reload_time,tower_type,animation_index,lvl)

        self.projectile_animation=projectile_animation

    def update(self):
        TowerObject.update(self)

    def fire(self)->None:
        pass
        #return a projectile with projectile animation
