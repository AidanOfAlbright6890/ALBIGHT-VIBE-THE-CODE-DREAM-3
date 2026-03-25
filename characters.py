import time

class Character:
    def __init__(self, name):
        self.name = name

class Customer(Character):
    def __init__(self, name, hunger_level=100, patience=10):
        super().__init__(name)
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
    def __init__(self, name, role, experience=1, salary=15.0):
        super().__init__(name)
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
# customer = Customer("John")
# customer.animate()
# employee = Employee("Jane", "cooker")
# employee.animate()
 
