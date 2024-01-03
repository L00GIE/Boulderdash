import pygame
from data.boulder import Boulder
from data.crate import Crate
from data.player import Player
from data.portal import Portal
from lib.background import Background
from lib.clutter import Clutter
from lib.scene import Scene
from lib.tile import Tile

class LevelTwo(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.player = None
        self.boulder = None
        self.bg = None
        self.portal = None
        self.cratesinit = False
        self.clutterinit = False

    def loop(self):
        if self.bg is None:
            self.initBg()
        if self.player is None:
            self.player = Player(self.core)
            self.add(self.player)
        if self.boulder is None:
            self.boulder = Boulder(self.core)
            self.add(self.boulder)
            self.boulder.y = 300
        if self.portal is None:
            self.portal = Portal(self.core, (2700, 350))
            self.add(self.portal)
        if not self.cratesinit:
            self.initCrates()
        if not self.clutterinit:
            self.initClutter()

        if self.player.x >= 300:
            self.boulder.started = True

        super().loop()

    def reset(self):
        self.objects = []
        self.player = None
        self.boulder = None
        self.bg = None
        self.portal = None
        self.clutterinit = False
        self.cratesinit = False

    def initCrates(self):
        self.add(Crate(self.core, (200, 400)))
        self.add(Crate(self.core, (1600, 250)))
        self.add(Crate(self.core, (1800, 250)))
        self.add(Crate(self.core, (2000, 250)))
        self.add(Crate(self.core, (2200, 250)))
        self.add(Crate(self.core, (2400, 250)))
        self.cratesinit = True

    def initClutter(self):
        self.add(Clutter(self.core, (405, 495), "data/assets/objects/Bush (2).png", size=(85, 50)))
        self.clutterinit = True

    def initBg(self):
        self.bg = Background(self.core, "data/assets/background/BG.png")
        self.add(self.bg)
        floorstartimg = pygame.image.load("data/assets/tiles/1.png")
        floorimg = pygame.image.load("data/assets/tiles/2.png")
        floorendimg = pygame.image.load("data/assets/tiles/3.png")
        waterimg = pygame.image.load("data/assets/tiles/17.png")
        floatstartimg = pygame.image.load("data/assets/tiles/13.png")
        floatendimg = pygame.image.load("data/assets/tiles/15.png")
        tilew, tileh = 100, 100
        tiley = (self.core.screen.get_height() / 1.2) - tileh
        tiles = []
        
        tiles.append(Tile(self.core, floorstartimg, (0 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, floorimg, (1 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, floorimg, (2 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, waterimg, (3 * tilew, tiley, tilew, tileh), isfloor=False))
        tiles.append(Tile(self.core, floorimg, (4 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, waterimg, (5 * tilew, tiley, tilew, tileh), isfloor=False))
        tiles.append(Tile(self.core, floorimg, (6 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, waterimg, (7 * tilew, tiley, tilew, tileh), isfloor=False))
        tiles.append(Tile(self.core, floorimg, (8 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, waterimg, (9 * tilew, tiley, tilew, tileh), isfloor=False))
        tiles.append(Tile(self.core, floorendimg, (10 * tilew, tiley, tilew, tileh)))

        tiles.append(Tile(self.core, floatstartimg, ((12 * tilew), tiley - 50, tilew, tileh)))
        tiles.append(Tile(self.core, floatendimg, ((13 * tilew), tiley - 50, tilew, tileh)))

        tiles.append(Tile(self.core, floorstartimg, (15 * tilew, tiley - 100, tilew, tileh)))
        for x in range(16, 26):
            tiles.append(Tile(self.core, floorimg, (x * tilew, tiley - 100, tilew, tileh)))
        tiles.append(Tile(self.core, floorendimg, (26 * tilew, tiley - 100, tilew, tileh)))
        
        for tile in tiles:
            self.add(tile)        
