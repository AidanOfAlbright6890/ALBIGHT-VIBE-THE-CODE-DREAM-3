# Credit for the obackroundimage code snippet goes to Irv Kalb's Solo Code 5 - GUI TEMPERATURE CONVERTER
# Credit for idea for oscreen code also goes to the obackroundimage snippet from Irv Kalb's Solo Code 5 - GUI TEMPERATURE CONVERTER 
import pygame
import pygwidgets
import sys
from characters import *
from pygame.locals import * 
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
#customer2AnimTuple = ('2nd Customer 2.png', '2nd Customer 2 animation one.png', '2nd Customer 2 animation 2.png')

#customer1AnimTuple = ('customer.png', 'customer 1 animation one.png', 'Customer animation 2.png')

#oCustomer1Animation = Character(window, 'customer.png', (700, 140), customer1AnimTuple, .1)

#oCustomer2Animation = Character(window, '2nd Customer 2.png', (222, 140), customer2AnimTuple, .1)

employee1AnimTuple = ('Employee 2.png', 'Employee 3.png')

oEmployee1Animation = Character(window, 'Employee 2.png', (332, 140), employee1AnimTuple, .1)

obackroundimage = pygwidgets.Image(window, (0,0), '5c88fc01b1c7dcad608ac839a67968fc.jpg')

oscreen = pygwidgets.Image(window, (0, 0), 'Custom Mcdonalds jpg 5.jpg')

oplaybutton = pygwidgets.TextButton(window, (0, 120), "Play1")

oplaybutton2 = pygwidgets.TextButton(window, (220, 120), "Play2")

oplaybutton3 = pygwidgets.TextButton(window, (330, 120), "Play3")

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
def run():
    customscreen = Customscreen(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if oplaybutton.handleEvent(event):
                #oCustomer1Animation.play()

            #if oplaybutton2.handleEvent(event):
                #oCustomer2Animation.play()
            
            if oplaybutton3.handleEvent(event):
                oEmployee1Animation.play()

                

            

        #oCustomer1Animation.update()
        #oCustomer2Animation.update()
        oEmployee1Animation.update()
        window.fill(WHITE)
        customscreen.draw()
        obackroundimage.draw()
        oscreen.draw()
        oEmployee1Animation.draw()
        #oCustomer1Animation.draw()
        #oCustomer2Animation.draw()
        oplaybutton.draw()
        oplaybutton2.draw()
        oplaybutton3.draw()
        pygame.display.flip()

class Character:
    def __init__(self, window, image_path, pos, picPaths, duration):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=pos)
        self.window = window

    def draw(self):
        self.window.blit(self.image, self.rect) 
class Itemlist:
    def __init__(self):
        self.items = []
    itemlist = []
    itemlist.append(Character(window, 'French_Fries.webp', (100, 200), itemlist, .1))
    itemlist.append(Character(window, 'cheeseburger.png', (250,200), itemlist, .1))
    itemlist.append(Character(window, 'Big mac.png', (400,200), itemlist, .1)) 
    itemlist.append(Character(window,'Mchicken.png', (550,200), itemlist, .1))  
run()



