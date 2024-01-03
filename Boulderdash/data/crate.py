import pygame, random
from lib.collider import Collider
from lib.tile import Tile
from lib.constants import g

class Crate:

    def __init__(self, core, pos):
        self.core = core
        self.x = pos[0]
        self.y = pos[1]
        self.starty = self.y
        self.maxrise = 100
        self.w = 100
        self.h = 100
        self.rising = True
        self.falling = False
        self.collider = Collider(self, debug=False)
        self.initsprite()

    def loop(self):
        if not self.rising:
            self.checkfalling()
            self.checkcolliding()
        else:
            self.y -= 1
            if self.y < self.starty - self.maxrise:
                self.rising = False
                self.falling = True
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.core.screen.blit(self.sprite, (self.x, self.y))

    def checkcolliding(self):
        if hasattr(self.core.scene, "player") and self.core.scene.player is not None:
            if self.collider.colliding(self.core.scene.player):
                self.core.scene.reset()
        
    def checkfalling(self):
        if self.onplatform():
            self.falling = False
            self.rising = True
        else:
            self.falling = True
        if self.falling:
            self.y += g

    def onplatform(self):
        if self.core.scene is None:
            return
        for obj in self.core.scene.objects:
            if isinstance(obj, Tile):
                if self.collider.colliding(obj) and obj.isfloor:
                    if self.y + self.h > obj.y + 64: # the +64 is necessary for reasons
                        return False
                    return True
        return False
    
    def initsprite(self):
        img = pygame.image.load("data/assets/objects/Crate.png")
        self.sprite = pygame.transform.scale(img, (self.w, self.h))