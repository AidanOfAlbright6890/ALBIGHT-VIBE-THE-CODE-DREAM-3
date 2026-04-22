import pygame
import pygwidgets
import sys
from characters import *
from pygame.locals import *

WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Blue = (0, 0, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("McDonald's Order Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
bigFont = pygame.font.SysFont(None, 40)

employee1AnimTuple = ('Employee 2.png', 'Employee 3.png')
customerAnimTuple = ('customer.png', 'customer 1 animation one.png', 'Customer animation 2.png')

oEmployee1Animation = Character(window, 'Employee 2.png', (532, 311), employee1AnimTuple, .12)
oEmployee2Animation = Character(window, 'Employee 2.png', (40, 321), employee1AnimTuple, .12)

oCustomerAnimation = Character(
    window,
    'customer.png',
    (50, 50),
    customerAnimTuple,
    .15,
    size=(70, 100),
    moveSpeed=3
)

obackroundimage = pygwidgets.Image(window, (0, 0), '5c88fc01b1c7dcad608ac839a67968fc.jpg')
oscreen = pygwidgets.Image(window, (0, 0), 'Custom Mcdonalds jpg 5.jpg')

oplaybutton = pygwidgets.TextButton(window, (20, 120), "Walk To Counter")
oplaybutton3 = pygwidgets.TextButton(window, (330, 120), "Employee 1")
oplaybutton4 = pygwidgets.TextButton(window, (460, 120), "Employee 2")
oresetbutton = pygwidgets.TextButton(window, (620, 120), "Reset Order")

oDollar1 = pygwidgets.TextButton(window, (80, 560), "$1")
oDollar5 = pygwidgets.TextButton(window, (180, 560), "$5")
oDollar10 = pygwidgets.TextButton(window, (280, 560), "$10")


class Customscreen:
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
        self.x = 20
        self.y = 0

    def draw(self):
        self.window.blit(self.customscreen, (self.x, self.y))


class Food:
    def __init__(self, window, imagePath, loc, size, name, price):
        self.window = window
        self.name = name
        self.price = price
        self.delivered = False

        originalimage = pygame.image.load(imagePath).convert_alpha()
        self.image = pygame.transform.smoothscale(originalimage, size)
        self.rect = self.image.get_rect(topleft=loc)

    def draw(self):
        self.window.blit(self.image, self.rect)

    def drawLabel(self, font):
        label = font.render(f"{self.name} - ${self.price}", True, BLACK)
        self.window.blit(label, (self.rect.x - 10, self.rect.y + self.rect.height + 5))


class Itemlist:
    def __init__(self, window):
        self.items = []
        self.items.append(Food(window, 'French_Fries.png', (100, 200), (80, 80), "Fries", 3))
        self.items.append(Food(window, 'cheeseburger.png', (250, 200), (80, 80), "Cheeseburger", 5))
        self.items.append(Food(window, 'Big mac.png', (400, 200), (80, 80), "Big Mac", 7))
        self.items.append(Food(window, 'Mcchicken.png', (550, 200), (80, 80), "McChicken", 6))

    def draw(self, font):
        for item in self.items:
            item.draw()
            item.drawLabel(font)


def run():
    customscreen = Customscreen(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    oItemlist = Itemlist(window)

    selectedItem = None
    moneyPaid = 0
    message = "Click 'Walk To Counter', then click a food item."
    customerAtCounter = False
    foodGiven = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if oplaybutton.handleEvent(event):
                oCustomerAnimation.play((260, 50))
                message = "Customer is walking to the counter..."

            if oplaybutton3.handleEvent(event):
                oEmployee1Animation.play()

            if oplaybutton4.handleEvent(event):
                oEmployee2Animation.play()

            if oresetbutton.handleEvent(event):
                selectedItem = None
                moneyPaid = 0
                foodGiven = False
                customerAtCounter = False
                message = "Order reset. Click 'Walk To Counter'."
                oCustomerAnimation.x = 50
                oCustomerAnimation.y = 50
                oCustomerAnimation.rect.topleft = (50, 50)
                oCustomerAnimation.playing = False
                oCustomerAnimation.moving = False
                oCustomerAnimation.image = oCustomerAnimation.frames[0]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if customerAtCounter and not foodGiven:
                    for item in oItemlist.items:
                        if item.rect.collidepoint(event.pos):
                            selectedItem = item
                            moneyPaid = 0
                            message = f"You chose {item.name}. Price: ${item.price}. Pay cash now."

            if selectedItem is not None and customerAtCounter and not foodGiven:
                if oDollar1.handleEvent(event):
                    moneyPaid += 1

                if oDollar5.handleEvent(event):
                    moneyPaid += 5

                if oDollar10.handleEvent(event):
                    moneyPaid += 10

        oCustomerAnimation.update()
        oEmployee1Animation.update()
        oEmployee2Animation.update()

        if oCustomerAnimation.x == 260 and oCustomerAnimation.y == 50:
            customerAtCounter = True
            if selectedItem is None and not foodGiven:
                message = "Customer is at the counter. Click a food item."

        if selectedItem is not None and not foodGiven:
            if moneyPaid < selectedItem.price:
                amountLeft = selectedItem.price - moneyPaid
                message = f"{selectedItem.name} costs ${selectedItem.price}. Paid: ${moneyPaid}. Need ${amountLeft} more."
            else:
                foodGiven = True
                oEmployee1Animation.play()
                message = f"Payment complete. Employee hands over the {selectedItem.name}!"

        window.fill(WHITE)
        obackroundimage.draw()
        customscreen.draw()
        oscreen.draw()

        oItemlist.draw(font)

        oEmployee1Animation.draw()
        oEmployee2Animation.draw()
        oCustomerAnimation.draw()

        oplaybutton.draw()
        oplaybutton3.draw()
        oplaybutton4.draw()
        oresetbutton.draw()

        if selectedItem is not None and not foodGiven:
            oDollar1.draw()
            oDollar5.draw()
            oDollar10.draw()

        messageSurface = bigFont.render(message, True, Blue)
        window.blit(messageSurface, (30, 20))

        if selectedItem is not None:
            infoSurface = font.render(f"Selected: {selectedItem.name}    Paid: ${moneyPaid}", True, BLACK)
            window.blit(infoSurface, (30, 520))

        pygame.display.flip()
        clock.tick(FRAMES_PER_SECOND)

run()
