import pygame
from lib.collider import Collider

class Clutter:
    def __init__(self, core, pos, image, size=None, obstacle=False, trigger=False):
        self.core = core
        self.image = pygame.image.load(image)
        if size is not None:
            self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        self.x = pos[0]
        self.y = pos[1]
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.obstacle = obstacle
        self.trigger = trigger
        self.collider = Collider(self)

    def loop(self):
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        if self.obstacle:
            self.checkcolliding()
        if self.trigger:
            self.checktriggering()
        self.core.screen.blit(self.image, (self.x, self.y))

    def checkcolliding(self):
        pass

    def checktriggering(self):
        pass
