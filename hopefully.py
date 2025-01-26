import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scene Transitions Example")

# Load background images for each scene
bathroom = pygame.image.load("assets/bgs/bathroom/sink3.png")
bathroom = pygame.transform.scale(bathroom, (WIDTH, HEIGHT))

kitchen = pygame.image.load("assets/bgs/kitchen/kitchen.png")
kitchen = pygame.transform.scale(kitchen, (WIDTH, HEIGHT))

street = pygame.image.load("assets/bgs/street/street.png")
street = pygame.transform.scale(street, (WIDTH, HEIGHT))

cafeteria = pygame.image.load("assets/bgs/cafeteria/cafeteria.png")
cafeteria = pygame.transform.scale(cafeteria, (WIDTH, HEIGHT))

# Load interactive items for each scene (bathroom, kitchen, street, cafeteria)
faucet = pygame.image.load("assets/bgs/bathroom/faucet.png")
faucet = pygame.transform.scale(faucet, (1000, 900))
faucet_rect = faucet.get_rect(topleft=(-5, -35))

brush = pygame.image.load("assets/bgs/bathroom/brush.png")
brush = pygame.transform.scale(brush, (130, 130))
brush_rect = brush.get_rect(topleft=(175, 300))

plasticbag = pygame.image.load("assets/bgs/kitchen/plasticbag.png")
plasticbag = pygame.transform.scale(plasticbag, (180, 180))
plasticbag_rect = plasticbag.get_rect(topleft=(300, -10))

buspass = pygame.image.load("assets/bgs/street/busID.jpg")
buspass = pygame.transform.scale(buspass, (120, 120))
buspass_rect = buspass.get_rect(topleft=(380, 450))

# Cafeteria items
milk = pygame.image.load("assets/bgs/cafeteria/milk.png")
milk = pygame.transform.scale(milk, (200, 200))
milk_rect = milk.get_rect(topleft=(200, 300))

peel = pygame.image.load("assets/bgs/cafeteria/peel.png")
peel = pygame.transform.scale(peel, (150, 150))
peel_rect = peel.get_rect(topleft=(300, 300))

# Scene state variable
scene = 0

# Initialize other variables
sink_animation = False
brush_animation = False
plasticbag_chosen = False
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Scene transitions
            if scene == 0:  # Bathroom
                if faucet_rect.collidepoint(mouse_pos):
                    sink_animation = not sink_animation
                if brush_rect.collidepoint(mouse_pos):
                    brush_animation = not brush_animation
                scene = 1  # Transition to Kitchen
            elif scene == 1:  # Kitchen
                if plasticbag_rect.collidepoint(mouse_pos):
                    plasticbag_chosen = True
                scene = 2  # Transition to Street
            elif scene == 2:  # Street
                scene = 3  # Transition to Cafeteria
            elif scene == 3:  # Cafeteria
                # Optional: Handle interactions in cafeteria if needed
                pass

    # Update animations for Bathroom (sink) and Brush
    if scene == 0:  # Bathroom Scene
        # Sink animation and brush movement (if needed)
        screen.blit(bathroom, (0, 0))
        screen.blit(faucet, faucet_rect.topleft)
        screen.blit(brush, brush_rect.topleft)
        if brush_animation:
            # Handle brush movement if necessary (brush movement animation logic)
            pass

    elif scene == 1:  # Kitchen Scene
        screen.blit(kitchen, (0, 0))
        screen.blit(plasticbag, plasticbag_rect.topleft)
        if plasticbag_chosen:
            plasticbag_rect.topleft = (800, 400)  # Adjust position if plasticbag is chosen
        # Handle other kitchen interactions (e.g., sandwich making)

    elif scene == 2:  # Street Scene
        screen.blit(street, (0, 0))
        screen.blit(buspass, buspass_rect.topleft)

    elif scene == 3:  # Cafeteria Scene
        screen.blit(cafeteria, (0, 0))
        screen.blit(milk, milk_rect.topleft)
        screen.blit(peel, peel_rect.topleft)
        if plasticbag_chosen:
            plasticbag_rect.topleft = (800, 400)  # Position plasticbag in cafeteria if chosen
            screen.blit(plasticbag, plasticbag_rect.topleft)

    pygame.display.flip()  # Update the screen

pygame.quit()
