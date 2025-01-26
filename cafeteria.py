import pygame
import kitchen

#from testtest import plasticbag, plasticbag_rect, plasticbag_chosen

plasticbag_chosen = True

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
cafeteria = pygame.image.load("assets/bgs/cafeteria/cafeteria.png")
cafeteria = pygame.transform.scale(cafeteria, (WIDTH, HEIGHT))

milk = pygame.image.load("assets/bgs/cafeteria/milk.png")
milk = pygame.transform.scale(milk,(200,200))
milk_rect = milk.get_rect(topleft=(200, 300))


peel = pygame.image.load("assets/bgs/cafeteria/peel.png")
peel = pygame.transform.scale(peel,(150,150))
peel_rect = milk.get_rect(topleft=(300, 300))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()

    # SCENE 3 --> STREET VIEW
    screen.blit(cafeteria, (0, 0))
    screen.blit(milk, milk_rect.topleft)
    screen.blit(peel, peel_rect.topleft)

    if plasticbag_chosen == True:
        kitchen.plasticbag_rect.topleft = (800, 400)
        screen.blit(kitchen.plasticbag, kitchen.plasticbag_rect.topleft)
    else:
        None

    pygame.display.flip()  # Update the screen after blitting the images

pygame.quit()
