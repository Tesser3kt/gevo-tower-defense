from abc import ABC, abstractmethod
from pygame.sprite import RenderUpdates, spritecollideany, groupcollide, Sprite
from pygame import Surface, SCALED, Rect


class GameObject:
    """ The most general of the clases """
    
    def __init__(
        self, x:int, y:int, width:int, height:int, sprite:Surface
        ) -> None:

        self.Rect=Rect(x,y,width,height)
        self.sprite=sprite
    
    def draw_me(self):
        """ Initializes the objects and draws it on the screen """

        #draw the sprite on top of the rectangle
        pass

 

