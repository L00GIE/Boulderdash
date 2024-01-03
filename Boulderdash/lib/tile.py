from lib.collider import Collider
import pygame

class Tile:

    def __init__(self, core, sprite, coords, isfloor=True, trigger=None):
        self.core = core
        self.sprite = sprite
        self.x = coords[0]
        self.y = coords[1]
        self.w = coords[2]
        self.h = coords[3]
        self.sprite = pygame.transform.scale(self.sprite, (self.w, self.h))
        self.isfloor = isfloor
        self.trigger = trigger
        self.collider = Collider(self, debug=False)

    def loop(self):
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.core.screen.blit(self.sprite, (self.x, self.y))
