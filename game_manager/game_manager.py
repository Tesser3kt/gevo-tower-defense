from pygame.sprite import RenderUpdates
from pygame.time import Clock
from pygame import event, QUIT, quit
from pygame import locals

from config.settings.general_config import Economy, Game


class GameManager:
    def __init__(self) -> None:
        self.objects = RenderUpdates()

        self.projectiles = RenderUpdates()
        self.towers = RenderUpdates()
        self.enemies = RenderUpdates()
        self.effects = RenderUpdates()

        self.moving_objects = RenderUpdates()
        self.static_objects = RenderUpdates()

        self.ui = RenderUpdates()

        self.coins:int = Economy.STARTING_MONEY
        self.lives:int = Economy.STARTING_LIVES
        self.level:int = Game.START_LEVEL
        self.wave:int = Game.START_WAVE


        self.clock = Clock()

        self.running = True
        self.pause = False


    def handle_input(self):
        for event in event.get():
            if event.type == QUIT:
                quit()
            elif event.type == locals.K_ESCAPE:
                self.pause = not self.pause

    def update(self):
        pass

    def run(self):
        while self.running:
            self.clock.tick(Game.FPS)

            self.handle_input()

            if self.pause:
                continue

    
        