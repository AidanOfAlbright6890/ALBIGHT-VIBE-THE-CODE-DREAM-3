from characters import MenuItem, Menu, Cashier
import pygame 

# Initialize pygame (required for Character parent class)
pygame.init()
window = pygame.display.set_mode((100, 100))

# Test MenuItem class
print("Testing MenuItem class...")
burger = MenuItem("Burger", 8.99, 500, 5)
fries = MenuItem("Fries", 3.49, 320, 3)
print(f"Created: {burger}")
print(f"Created: {fries}")
print(f"Burger info: {burger.get_info()}\n")

# Test Menu class
print("Testing Menu class...")
menu = Menu()
menu.add_item(burger)
menu.add_item(fries)
menu.display_menu()
print(f"Retrieved item: {menu.get_item('Burger')}\n")

# Test Cashier class
print("Testing Cashier class...")
cashier = Cashier(window, "Alice", (10, 10), experience=2, salary=16.0)
print(f"Cashier created: {cashier.name}")

# Simulate taking an order
order_items = [burger, fries]
total = cashier.take_order(None, order_items)
cashier.process_payment(total)

print(f"\nCashier stats: {cashier.get_stats()}\n")

print("✓ All tests passed!")
pygame.quit() 
