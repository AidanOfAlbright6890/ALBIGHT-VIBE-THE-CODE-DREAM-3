import pygame

class Character:
    def __init__(self, window, imagePath, loc, imageTuple, speed, size=None, moveSpeed=2):
        self.window = window
        self.x, self.y = loc
        self.startX, self.startY = loc
        self.speed = speed
        self.moveSpeed = moveSpeed
        self.frames = []
        self.frameIndex = 0
        self.playing = False
        self.targetX = self.x
        self.targetY = self.y
        self.moving = False

        for fileName in imageTuple:
            image = pygame.image.load(fileName).convert_alpha()
            if size is not None:
                image = pygame.transform.smoothscale(image, size)
            self.frames.append(image)

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=loc)

    def play(self, targetPos=None):
        self.playing = True
        self.frameIndex = 0
        self.image = self.frames[0]

        if targetPos is not None:
            self.targetX, self.targetY = targetPos
            self.moving = True
        else:
            self.targetX, self.targetY = self.x, self.y
            self.moving = False

    def update(self):
        if not self.playing:
            return

        self.frameIndex += self.speed
        if self.frameIndex >= len(self.frames):
            self.frameIndex = 0

        self.image = self.frames[int(self.frameIndex)]

        if self.moving:
            if self.x < self.targetX:
                self.x += self.moveSpeed
                if self.x >= self.targetX:
                    self.x = self.targetX
            elif self.x > self.targetX:
                self.x -= self.moveSpeed
                if self.x <= self.targetX:
                    self.x = self.targetX

            if self.y < self.targetY:
                self.y += self.moveSpeed
                if self.y >= self.targetY:
                    self.y = self.targetY
            elif self.y > self.targetY:
                self.y -= self.moveSpeed
                if self.y <= self.targetY:
                    self.y = self.targetY

            if self.x == self.targetX and self.y == self.targetY:
                self.moving = False
                self.playing = False
                self.frameIndex = len(self.frames) - 1
                self.image = self.frames[self.frameIndex]

        self.rect.topleft = (self.x, self.y)

    def draw(self):
        self.window.blit(self.image, self.rect)
 
