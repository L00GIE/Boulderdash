import pygame
from lib.animation import Animation
from lib.collider import Collider

class Portal:

    def __init__(self, core, pos):
        self.core = core
        self.x = pos[0]
        self.y = pos[1]
        self.w = 50
        self.h = 100
        self.collider = Collider(self, debug=False)
        self.initsprites()

    def loop(self):
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        if self.collider.colliding(self.core.scene.player):
            self.core.currentscene += 1
            self.core.scene = None
        self.anim.play()

    def initsprites(self):
        sprites = [
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_00.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_01.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_02.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_03.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_04.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_05.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_06.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_07.png"), (self.w, self.h)),
            pygame.transform.scale(pygame.image.load("data/assets/objects/portal/portal_08.png"), (self.w, self.h))
        ]
        self.anim = Animation(self.core, sprites, self, delay=5)
