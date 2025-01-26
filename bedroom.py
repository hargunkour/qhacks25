import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
bedroom = pygame.image.load("assets/bgs/home/bedroom.png")
bedroom = pygame.transform.scale(bedroom, (WIDTH, HEIGHT))
f_bedroom = pygame.image.load("assets/font/f_bedroom.png")
f_bedroom = pygame.transform.scale(f_bedroom, (741, 165))

running = True
while running:
    screen.blit(bedroom, (0, 0))
    screen.blit(f_bedroom, (150, 500))


    pygame.display.flip()  # Update the screen after blitting the images

pygame.quit()