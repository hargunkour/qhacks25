import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Image Example")

# Boolean variables
scene = 0
points = 0
bathroom_done = False
plasticbag_chosen = False
sandwich_done = False

# --------------------------------------------------------- BATHROOM ---------------------------------------------------------
bathroom = pygame.image.load("assets/bgs/bathroom/sink3.png")
bathroom = pygame.transform.scale(bathroom, (WIDTH, HEIGHT))

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

background = sink3  # Start with sink3
sink_animation = False  # Sink animation state
sink_timer = 0
brush_animation = False  # Brush movement animation state
brush_x = 200  # Initial x-position for the closebrush
brush_speed = 10  # Speed of the horizontal movement

# --------------------------------------------------------- STREET ---------------------------------------------------------
street = pygame.image.load("assets/bgs/street/street.png")
street = pygame.transform.scale(street, (WIDTH, HEIGHT))

buspass = pygame.image.load("assets/bgs/street/busID.jpg")
buspass = pygame.transform.scale(buspass, (100, 100))
buspass_rect = buspass.get_rect(topleft=(300, 400))

keys = pygame.image.load("assets/bgs/street/keys.png")
keys = pygame.transform.scale(keys, (100, 100))
keys_rect = keys.get_rect(topleft=(500, 400))

# --------------------------------------------------------- KITCHEN ---------------------------------------------------------
kitchen = pygame.image.load("assets/bgs/kitchen/kitchen.png")
kitchen = pygame.transform.scale(kitchen, (WIDTH, HEIGHT))

# Load Plasticbag image (clickable element)
plasticbag = pygame.image.load("assets/bgs/kitchen/plasticbag.png")
plasticbag = pygame.transform.scale(plasticbag, (180, 180))
plasticbag_rect = plasticbag.get_rect(topleft=(300, -10))

container = pygame.image.load("assets/bgs/kitchen/container.png")
container = pygame.transform.scale(container, (180, 180))
container_rect = container.get_rect(topleft=(500, -10))

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
sandwichbag = pygame.transform.scale(sandwichbag, (150, 150))
sandwichbag_rect = sandwichbag.get_rect(topleft=(10000, 10000))

sandwichcontainer = pygame.image.load("assets/bgs/kitchen/sandwichcontainer.png")
sandwichcontainer = pygame.transform.scale(sandwichcontainer, (200, 200))
sandwichcontainer_rect = sandwichcontainer.get_rect(topleft=(10000, 10000))

cafeteria = pygame.image.load("assets/bgs/cafeteria/cafeteria.png")
cafeteria = pygame.transform.scale(cafeteria, (WIDTH, HEIGHT))

milk = pygame.image.load("assets/bgs/cafeteria/milk.png")
milk = pygame.transform.scale(milk,(200,200))
milk_rect = milk.get_rect(topleft=(200, 300))


peel = pygame.image.load("assets/bgs/cafeteria/peel.png")
peel = pygame.transform.scale(peel,(150,150))
peel_rect = milk.get_rect(topleft=(300, 300))
# --------------------------------------------------------- GAME LOOP ---------------------------------------------------------

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
    global sink_animation, brush_animation
    
    global brush_x, brush_speed
    brush_x += brush_speed

    if brush_x > 400 or brush_x < 200:
        brush_speed *= -1

    if faucet_rect.collidepoint(mouse_pos):
        sink_animation = False  # Toggle sink animation
                    
    if not sink_animation:
        background = sink3  # Reset to sink3 when animation stops
                    
    if brush_rect.collidepoint(mouse_pos):
        brush_animation = False  # Toggle brush animation

mouse_pos = (0, 0)  # Default value for mouse_pos

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position when clicked
            mouse_pos = pygame.mouse.get_pos()

            if (scene == 0):
                print('scene 0')
                sink_animation = True
                brush_animation = True
                scene = 1
            
            elif (scene == 1):
                print('scene 1')

                screen.blit(background, (0, 0))  # Draw the background
                screen.blit(faucet, faucet_rect.topleft)  # Draw the faucet
                screen.blit(brush, brush_rect.topleft)  # Draw the static brush
                screen.blit(closebrush, (brush_x, HEIGHT // 2 - 75))

                if sink_animation:
                    bathroom_animation()
                if brush_animation:
                    brush_movement_animation()
                    bathroom_done = True

                
                if bathroom_done == True:
                    sink_animation = False
                    brush_animation = False
                    scene = 2
                    
                    

            
            elif (scene == 2):

                print('scene 2')
                # Check collisions
                if bread_rect.collidepoint(mouse_pos):
                    bread_rect.x, bread_rect.y = 425, 250

                if bread1_rect.collidepoint(mouse_pos):
                    bread1_rect.x, bread1_rect.y = 425, 250

                if t_ham_rect.collidepoint(mouse_pos):
                    ham_rect.x, ham_rect.y = 430, 260

                if t_lettuce_rect.collidepoint(mouse_pos):
                    lettuce_rect.x, lettuce_rect.y = 450, 280

                if t_mayo_rect.collidepoint(mouse_pos):
                    mayo_rect.x, mayo_rect.y = 470, 290

                if plasticbag_rect.collidepoint(mouse_pos):
                    bread_rect.x = bread1_rect.x = ham_rect.x = lettuce_rect.x = mayo_rect.x = plasticbag_rect.x = 10000
                    sandwichbag_rect.x, sandwichbag_rect.y = 430, 250
                    plasticbag_chosen = True
                    points += 1
                    sandwich_done = True
                    scene = 3

                if container_rect.collidepoint(mouse_pos):
                    bread_rect.x = bread1_rect.x = ham_rect.x = lettuce_rect.x = mayo_rect.x = container_rect.x = 10000
                    sandwichcontainer_rect.x, sandwichcontainer_rect.y = 410, 230
                    plasticbag_chosen = False
                    sandwich_done = True
                    scene = 3
                
                screen.blit(kitchen, (0, 0))
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

                print(points)
            
            elif (scene == 3):
                print('scene 3')
                if buspass_rect.collidepoint(mouse_pos):
                    print('public bus has been chosen')

                if keys_rect.collidepoint(mouse_pos):
                    print('driving yourself has been chosen')
                    points += 1
            
                screen.blit(street, (0, 0))
                screen.blit(keys, keys_rect.topleft)
                screen.blit(buspass, buspass_rect.topleft)

                scene = 4

                print(points)
            
            elif (scene == 4):
                print('scene 4')
            
                if plasticbag_chosen == True:
                    plasticbag_rect.topleft = (800, 400)
                    screen.blit(plasticbag, plasticbag_rect.topleft)
                else:
                    None
                
                screen.blit(cafeteria, (0, 0))
                screen.blit(milk, milk_rect.topleft)
                screen.blit(peel, peel_rect.topleft)

                print(points)

        pygame.display.flip()

pygame.quit()