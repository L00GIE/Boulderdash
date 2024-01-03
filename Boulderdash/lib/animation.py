import pygame

class Animation:

    def __init__(self, core, sprites, parent, delay=3, scalex=None, scaley=None, flipx=False):
        self.core = core
        self.sprites = sprites
        self.parent = parent
        self.x = self.parent.x
        self.y = self.parent.y
        self.scalex = scalex
        self.scaley = scaley
        self.flipx = flipx
        self.currentframe = 0
        self.delay = delay
        self.delaycount = 0
        self.ended = False

    def play(self):
        self.ended = False
        img = self.sprites[self.currentframe]
        if self.flipx:
            img = pygame.transform.flip(self.sprites[self.currentframe], True, False)
        if self.scalex is not None and self.scaley is not None:
            img = pygame.transform.scale(img, (self.scalex, self.scaley))
        self.core.screen.blit(img, (self.parent.x, self.parent.y))
        if self.delaycount >= self.delay:
            self.delaycount = 0
            self.currentframe += 1
            if self.currentframe >= len(self.sprites):
                self.currentframe = 0
                self.ended = True
        self.delaycount += 1
        