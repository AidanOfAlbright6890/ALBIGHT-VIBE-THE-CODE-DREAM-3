# Credit for the obackroundimage code snippet goes to Irv Kalb's Solo Code 5 - GUI TEMPERATURE CONVERTER
# Credit for idea for oscreen code also goes to the obackroundimage snippet from Irv Kalb's Solo Code 5 - GUI TEMPERATURE CONVERTER 
import pygame
import pygwidgets
import sys
from characters import Character
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680
WHITE = (255, 255, 255)
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
obackroundimage = pygwidgets.Image(window, (0,0), '5c88fc01b1c7dcad608ac839a67968fc.jpg')
oscreen = pygwidgets.Image(window, (0, 0), 'Custom Mcdonalds jpg 5.jpg')

class Customscreen():
    def __init__(self, window, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.window = window
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        self.customscreen = pygame.image.load('Custom Mcdonalds jpg 5.jpg')
        self.customscreenRect = self.customscreen.get_rect()
        self.width = self.customscreenRect.width
        self.height = self.customscreenRect.height
        self.maxHeight = WINDOW_HEIGHT - self.height
        self.maxWidth = WINDOW_WIDTH - self.width
        self.x = (20)
        self.y = (0)

    def draw(self):
        self.window.blit(self.customscreen, (self.x, self.y))
def main():
    customscreen = Customscreen(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill(WHITE)
        customscreen.draw()
        obackroundimage.draw()
        oscreen.draw()
        pygame.display.flip()
main()
