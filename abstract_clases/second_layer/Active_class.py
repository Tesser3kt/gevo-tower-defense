from game_object import GameObject
from pygame.sprite import Sprite

class ActiveObjects(GameObject):
    """ Class for objects that do something on their own """

    def __init__(
        self, x:int, y:int, width:int, height:int, image:Sprite, animation:list[Sprite], animation_index:int = 0
        ) -> None:

        super().__init__(x,y,width,height,image)
        self.animation=animation
        self.animation_index=animation_index
    
    def continue_animation(self):
        """ Moves the animation one frame ahead """

        self.animation_index+=1
        self.animation_index=self.animation%len(self.animation)
        #draw the sprite
 
          