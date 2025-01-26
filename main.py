import pygame
import bathroom

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sammy at School")

# variables/objects

background = pygame.image.load("assets/bgs/home/bedroom.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

play_button = pygame.image.load("assets/bgs/home/play_button.png")

#timers
brush_move = "NO"
sink_move = "NO"


scene = 0

def draw():
    global scene
    if scene == 0:
        screen.blit(background, (0, 0))
        screen.blit(play_button, (735, 365))

    elif scene == 1:
        screen.clear()
        screen.blit(bathroom.faucet, (-5,-35))
        background = pygame.image.load("assets/bgs/bathroom/sink3.png")
        screen.blit(background, (0, 0))
        screen.blit(bathroom.brush, (175,300))
        screen.blit(bathroom.closebrush, (800,400))



def update():
    global scene
    if scene == 1:
        if sink_move == "YES":
            bathroom.bathroom_animation()
        if brush_move == "YES":
            bathroom.brush_animation()

def on_mouse_down(pos, buttons):
    global scene
    if scene == 0:
        if play_button.collidepoint(pos):
            scene = 1

    elif scene == 1:
        if bathroom.faucet.collidepoint(pos):
            if sink_move == "YES":
                sink_move = "NO"
            elif sink_move == "NO":
                sink_move == "YES"
        if bathroom.brush.collidepoint(pos):
            if brush_move == "YES":
                brush_move = "NO"
            elif brush_move == "NO":
                brush_move = "YES"


        





# # Load cafeteria image
# try:
#     cafeteria_image = pygame.image.load("assets\Screen5.png")
#     cafeteria_image = pygame.transform.scale(cafeteria_image, (WIDTH, HEIGHT))  # Scale to fit window
# except FileNotFoundError:
#     # Create a placeholder if image is not found
#     cafeteria_image = pygame.Surface((WIDTH, HEIGHT))
#     cafeteria_image.fill((255, 0, 0))  # Red placeholder

# # Game loop
running = True
while running:
    draw
    update()
    

pygame.quit()
