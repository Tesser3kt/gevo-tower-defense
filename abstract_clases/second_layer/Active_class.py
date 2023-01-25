from game_object import GameObject
from pygame.sprite import Sprite

class ActiveObjects(GameObject):
    """ Class for objects that do something on their own """

    def __init__(
        self, x:int, y:int, width:int, height:int, sprite:Sprite, animation:list[Sprite], animation_index:int = 0
        ) -> None:

        super().__init__(x,y,width,height,sprite)
        self.animation=animation
        self.animation_index=animation_index
    
    def continue_animation(self):
        """ Moves the animation one frame ahead """

        self.animation_index+=1
        if self.animation_index>=len(self.animation):
            self.animation_index=0
        self.sprite=self.animation[self.animation_index]
        #draw the sprite
 
         