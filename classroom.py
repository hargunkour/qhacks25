import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
classroom = pygame.image.load("assets/bgs/classroom/classroom.jpg")
classroom = pygame.transform.scale(classroom, (WIDTH, HEIGHT))

notebook = pygame.image.load("assets/bgs/classroom/notebook.png")
notebook = pygame.transform.scale(notebook, (300, 300))
notebook_rect = notebook.get_rect(topleft=(600, 350))
    
ipad = pygame.image.load("assets/bgs/classroom/ipad.png")
ipad = pygame.transform.scale(ipad, (600, 600))
ipad_rect = ipad.get_rect (topleft=(300, 350))

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
    screen.blit(classroom, (0, 0))
    screen.blit(notebook, notebook_rect.topleft)
    screen.blit(ipad, ipad_rect.topleft)

    pygame.display.flip()  # Update the screen after blitting the images

pygame.quit()
