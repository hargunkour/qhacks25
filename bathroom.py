import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bathroom Animation Example")

# Load images
sink1 = pygame.image.load("assets/bgs/bathroom/sink1.png")
sink1 = pygame.transform.scale(sink1, (WIDTH, HEIGHT))

sink2 = pygame.image.load("assets/bgs/bathroom/sink2.png")
sink2 = pygame.transform.scale(sink2, (WIDTH, HEIGHT))

sink3 = pygame.image.load("assets/bgs/bathroom/sink3.png")
sink3 = pygame.transform.scale(sink3, (WIDTH, HEIGHT))

faucet = pygame.image.load("assets/bgs/bathroom/faucet.png")
faucet = pygame.transform.scale(faucet, (1000, 900))
faucet_rect = faucet.get_rect(topleft=(-5, -35))

brush = pygame.image.load("assets/bgs/bathroom/brush.png")
brush = pygame.transform.scale(brush, (130, 130))
brush_rect = brush.get_rect(topleft=(175, 300))

closebrush = pygame.image.load("assets/bgs/bathroom/closebrush.png")
closebrush = pygame.transform.scale(closebrush, (800, 400))

# Initialize variables
background = sink3  # Start with sink3
sink_animation = False  # Sink animation state
sink_timer = 0
brush_animation = False  # Brush movement animation state
brush_x = 200  # Initial x-position for the closebrush
brush_speed = 10  # Speed of the horizontal movement

# Function to handle sink animation
def bathroom_animation():
    global sink_timer, background
    sink_timer += 0.2
    if sink_timer > 10:
        sink_timer = 0
    if 0 <= sink_timer <= 5:
        background = sink1
    elif 5 < sink_timer <= 10:
        background = sink2

# Function for closebrush horizontal movement animation
def brush_movement_animation():
    global brush_x, brush_speed

    # Move the brush horizontally
    brush_x += brush_speed
    # Reverse direction when reaching bounds
    if brush_x > 400 or brush_x < 200:
        brush_speed *= -1

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             # Check if faucet is clicked
#             if faucet_rect.collidepoint(mouse_pos):
#                 sink_animation = not sink_animation  # Toggle sink animation
#                 if sink_animation == False:
#                     background = sink3  # Reset to sink3 when animation stops
#             # Check if brush is clicked
#             if brush_rect.collidepoint(mouse_pos):
#                 brush_animation = not brush_animation  # Toggle brush animation

#     # Update animations
#     if sink_animation:
#         bathroom_animation()
#     if brush_animation:
#         brush_movement_animation()

#     # Draw elements
#     screen.blit(faucet, faucet_rect.topleft)  # Draw the faucet
#     screen.blit(background, (0, 0))  # Draw the background
#     screen.blit(brush, brush_rect.topleft)  # Draw the static brush
#     screen.blit(closebrush, (brush_x, HEIGHT // 2 - 75))  # Draw the moving brush

#     pygame.display.flip()  # Update the screen

# pygame.quit()