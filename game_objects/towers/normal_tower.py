from pygame.surface import Surface

from tower_object import TowerObject

class NormalTower(TowerObject):
    """ Class for normal tower objects """

    def __init__(
     self, x: int, y: int, width: int, height: int, image: Surface,
     animation: list[Surface],damage:int,reload_time:int,
     tower_type:TowerType, animation_index: int = 0, lvl:int=1,
     projectile_animation:list[Surface]
    )->None:

    self.projectile_animation=projectile_animation

    def update(self):
        TowerObject.update(self)

    def fire(self)->class:
        #return a projectile with projectile animation