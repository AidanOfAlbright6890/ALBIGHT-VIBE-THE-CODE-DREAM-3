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

    def play(self):
        if self.playing:
            return
        self.playing = True
        self.imageStartTime = time.time()
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
        theImage = self.imageList[self.index]
        self.window.blit(theImage, self.loc)

        
        


        

            
        

        

        
    
            

class Customer(Character):
    def __init__(self, window, name, loc, hunger_level=100, patience=10):
        super().__init__(window, name, loc)
        self.hunger_level = hunger_level
        self.patience = patience

    def animate(self): 

        frames = [
            "  O  ",
            " /|\\ ",
            " / \\ ",
            "Walking...",
            "  O  ",
            " /|\\ ",
            " / \\ ",
            "Entering McDonald's..."
        ]
        for frame in frames:
            print(frame)
            time.sleep(0.5)
            print("\n" * 10)  # Clear screen effect

class Employee(Character):
    def __init__(self, window, name, loc, role, experience=1, salary=15.0):
        super().__init__(window, name, loc)
        self.role = role
        self.experience = experience
        self.salary = salary

    def animate(self):
        if self.role == "cashier":
            print("Cashier: Taking order...")
            time.sleep(1)
            print("Cashier: Processing payment...")
        elif self.role == "cooker":
            print("Cooker: Preparing food...")
            time.sleep(1)
            print("Cooker: Cooking burger...")
            time.sleep(1)
            print("Cooker: Food ready!")
        elif self.role == "manager":
            print("Manager: Supervising...")
            time.sleep(1)
            print("Manager: Checking inventory...")

    

        

# Example usage
# ocustomer1 = Customer("John")
# ocustomer1.animate()
# oemployee1 = Employee("Jane", "cooker")
# oemployee1.animate()
 
