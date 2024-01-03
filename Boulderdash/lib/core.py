from data.scenes.worldone.levelone import LevelOne
from data.scenes.worldone.levelthree import LevelThree
from data.scenes.worldone.leveltwo import LevelTwo

class Core:

    def __init__(self, screen):
        self.screen = screen
        self.scene = None
        self.currentscene = 0 # set to 0 to start at beginning
        self.initScenes()

    def loop(self, events):
        self.events = events
        if self.scene is None:
            self.scene = self.scenes[self.currentscene]
        else:
            self.scene.loop()

    def initScenes(self):
        self.scenes = [
            LevelOne(self),
            LevelTwo(self),
            LevelThree(self)
        ]
