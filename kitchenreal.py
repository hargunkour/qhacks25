import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Image Example")

# Boolean variables
plasticbag_chosen = False
sandwich_done = False

# Load background image
kitchen = pygame.image.load("assets/bgs/kitchen/kitchen.png")  # Replace with your image file
kitchen = pygame.transform.scale(kitchen, (WIDTH, HEIGHT))  # Scale to fit the screen

# Load Plasticbag image (clickable element)
plasticbag = pygame.image.load("assets/bgs/kitchen/plasticbag.png")
plasticbag = pygame.transform.scale(plasticbag, (180, 180))  # Resize image
plasticbag_rect = plasticbag.get_rect(topleft=(300, -10))  # Position Plastic Bag

container = pygame.image.load("assets/bgs/kitchen/container.png")
container = pygame.transform.scale(container, (180, 180))  # Resize image
container_rect = container.get_rect(topleft=(500, -10))  # Position Plastic Bag

bread1 = pygame.image.load("assets/bgs/kitchen/bread.png")
bread1 = pygame.transform.scale(bread1, (150, 150))
bread1_rect = bread1.get_rect(topleft=(10, 0))

bread = pygame.image.load("assets/bgs/kitchen/bread.png")
bread = pygame.transform.scale(bread, (150, 150))
bread_rect = bread.get_rect(topleft=(140, 0))

mayo = pygame.image.load("assets/bgs/kitchen/mayo.png")
mayo = pygame.transform.scale(mayo, (80, 80))
mayo_rect = mayo.get_rect(topleft=(800, 350))

t_mayo = pygame.image.load("assets/bgs/kitchen/t_mayo.png")
t_mayo = pygame.transform.scale(t_mayo, (100, 250))
t_mayo_rect = t_mayo.get_rect(topleft=(800, 250))

ham = pygame.image.load("assets/bgs/kitchen/ham.png")
ham = pygame.transform.scale(ham, (140, 140))
ham_rect = ham.get_rect(topleft=(90, 190))

t_ham = pygame.image.load("assets/bgs/kitchen/t_ham.png")
t_ham = pygame.transform.scale(t_ham, (250, 250))
t_ham_rect = t_ham.get_rect(topleft=(50, 150))

lettuce = pygame.image.load("assets/bgs/kitchen/lettuce.png")
lettuce = pygame.transform.scale(lettuce, (100, 100))
lettuce_rect = lettuce.get_rect(topleft=(730, 10))

t_lettuce = pygame.image.load("assets/bgs/kitchen/t_lettuce.png")
t_lettuce = pygame.transform.scale(t_lettuce, (150, 150))
t_lettuce_rect = t_lettuce.get_rect(topleft=(730, 10))

sandwichbag = pygame.image.load("assets/bgs/kitchen/sandwichbag.jpg")
sandwichbag = pygame.transform.scale(sandwichbag, (150, 150))  # Corrected line
sandwichbag_rect = sandwichbag.get_rect(topleft=(10000, 10000))\

sandwichcontainer = pygame.image.load("assets/bgs/kitchen/sandwichcontainer.png")
sandwichcontainer = pygame.transform.scale(sandwichcontainer, (200, 200))  # Corrected line
sandwichcontainer_rect = sandwichcontainer.get_rect(topleft=(10000, 10000))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            
            # Check if Sammy was clicked
            if bread_rect.collidepoint(mouse_pos):
                bread_rect.x = 425
                bread_rect.y = 250
            
            if bread1_rect.collidepoint(mouse_pos):
                bread1_rect.x = 425
                bread1_rect.y = 250
                 
            if t_ham_rect.collidepoint(mouse_pos):
                ham_rect.x = 430
                ham_rect.y = 260 
            
            if t_lettuce_rect.collidepoint(mouse_pos):
                lettuce_rect.x = 450
                lettuce_rect.y = 280
            
            if t_mayo_rect.collidepoint(mouse_pos):  # Corrected line
                mayo_rect.x = 470
                mayo_rect.y = 290

            if plasticbag_rect.collidepoint(mouse_pos):
                bread_rect.x = bread1_rect.x = ham_rect.x = lettuce_rect.x = mayo_rect.x = plasticbag_rect.x = 10000  # Corrected line
                sandwichbag_rect.x = 430
                sandwichbag_rect.y = 250
            
            if container_rect.collidepoint(mouse_pos):
                bread_rect.x = bread1_rect.x = ham_rect.x = lettuce_rect.x = mayo_rect.x = container_rect.x = 10000  # Corrected line
                sandwichcontainer_rect.x = 410
                sandwichcontainer_rect.y = 230

    # Draw background and plastic bag
    screen.blit(kitchen, (0, 0))  # Draw the background
    screen.blit(plasticbag, plasticbag_rect.topleft)
    screen.blit(container, container_rect.topleft)
    screen.blit(bread1, bread1_rect.topleft)
    screen.blit(ham, ham_rect.topleft)
    screen.blit(t_ham, t_ham_rect.topleft)
    screen.blit(lettuce, lettuce_rect.topleft)
    screen.blit(t_lettuce, t_lettuce_rect.topleft)
    screen.blit(mayo, mayo_rect.topleft)
    screen.blit(t_mayo, t_mayo_rect.topleft)
    screen.blit(bread, bread_rect.topleft)
    screen.blit(sandwichbag, sandwichbag_rect.topleft)
    screen.blit(sandwichcontainer, sandwichcontainer_rect.topleft)

    pygame.display.flip()  # Update the display

pygame.quit()
