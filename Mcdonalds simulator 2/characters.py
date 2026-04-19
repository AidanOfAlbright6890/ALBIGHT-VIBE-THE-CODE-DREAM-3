import time
import pygame
class Character:
    def __init__(self, window, name, loc, picPaths, durationPerImage):
        self.window = window
        self.name = name
        self.loc = loc
        self.imageList = []
        for picPath in picPaths:
            image = pygame.image.load(picPath)
            image = pygame.Surface.convert_alpha(image)
            self.imageList.append(image)
            self.playing = False
            self.durationPerImage = durationPerImage
            self.nImages = len(self.imageList)
            self.index = 0

    def playing(self):
        if self.playing:
            return
        self.imageStartTime = time.time()
        self.playing = True
        self.index = 0

    def update(self):
        if not self.playing:
            return
        self.elapsed = time.time() - self.imageStartTime

        if self.elapsed > self.durationPerImage:
            self.index = self.index + 1

            if self.index < self.nImages:
                self.imageStartTime = time.time()
            else:
                self.playing = False
                self.index = 0

    def draw(self):
        theimage = self.imageList[self.index]
        self.window.blit(theimage, self.loc)