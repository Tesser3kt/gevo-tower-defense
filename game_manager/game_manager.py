from pygame.sprite import RenderUpdates
from pygame.time import Clock
from config.settings.general_config import Economy, Game


class GameManager:
    def __init__(self) -> None:
        self.objects = RenderUpdates()

        self.projectiles = RenderUpdates()
        self.towers = RenderUpdates()
        self.enemies = RenderUpdates()

        self.moving_objects = RenderUpdates()
        self.static_objects = RenderUpdates()



        self.ui = RenderUpdates()

        self.coins:int = Economy.STARTING_MONEY
        self.lives:int = Economy.STARTING_LIVES
        self.level:int = Game.START_LEVEL
        self.wawe:int = Game.START_WAVE
        self.effects = RenderUpdates()

        self.clock = Clock()
        self.running = True
        self.paused = False
        self.game_over = False

    #   
    def run(self):
        while self.running:
            self.clock.tick(Game.FPS)
            #TODO: finish the game loop, add pause, křížek