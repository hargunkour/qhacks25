import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
street = pygame.image.load("assets/bgs/street/street.png")
street = pygame.transform.scale(street, (WIDTH, HEIGHT))

buspass = pygame.image.load("assets/bgs/street/busID.jpg")
buspass = pygame.transform.scale(buspass, (120, 120))
buspass_rect = buspass.get_rect(topleft=(380, 450))
    
keys = pygame.image.load("assets/bgs/street/keys.png")
keys = pygame.transform.scale(keys, (190, 190))
keys_rect = keys.get_rect (topleft=(480, 400))

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
            print('entering while loop now')

    # SCENE 3 --> STREET VIEW
    screen.blit(street, (0, 0))
    screen.blit(keys, keys_rect.topleft)
    screen.blit(buspass, buspass_rect.topleft)

    pygame.display.flip()  # Update the screen after blitting the images

pygame.quit()
