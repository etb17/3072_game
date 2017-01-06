import pygame
import intersects
import random

pygame.init()

#window

WIDTH = 1200
HEIGHT = 575
SIZE = (WIDTH, HEIGHT)
TITLE = '3072'
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

gameimg = pygame.image.load('3072screen.png')


#Walls
wall1 = [112, 381, 217, 1]
wall2 = [112, 382, 1, 130]
wall3 = [112, 512, 217, 1]
wall4 = [328, 382, 1, 130]
wall5 = [519, 381, 160, 1]
wall6 = [519, 381, 1, 133]
wall7 = [519, 514, 160, 1]
wall8 = [679, 381, 1, 133]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]

#players

player1 = [300, 400, 5, 5]
player1_vx = 0
player1_vy = 0
player1_speed = 5

player2 = [599, 498, 5, 5]
player2_vx = 0 
#mouse
#pygame.mouse.set_visible(0)
pygame.mouse.set_pos([599, 498])

#player2 Enemies
enemy = []
for i in range(40):
    x = random.randrange (519, 679)
    y = 376
    speed = 1
    enemy.append([x, y, speed])


# Game loop
ship_health = 100
done = False
hit = False
immunity = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            location = pygame.mouse.get_pos()
            player2[0] = location[0]
            
            if player2[0] >= 679:
                player2[0] = 673
            elif player2[0] <= 519:
                player2[0] = 518
    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_w]
    down = pressed[pygame.K_s]
    left = pressed[pygame.K_a]
    right = pressed[pygame.K_d]

    if up:
        player1_vy = -player1_speed
    elif down:
        player1_vy = player1_speed
    else:
        player1_vy = 0
        
    if left:
        player1_vx = -player1_speed
    elif right: 
        player1_vx = player1_speed
    else:
        player1_vx = 0

    for e in enemy:
        e[1] += e[2]
        if e[1] > 519:
            e[0] = random.randrange(519, 679)
            e[1] = 376
        
    #Game logic
    hit_list = [e for e in enemy if intersects.rect_rect(player2, [e[0], e[1], 5, 5])]
    if len(hit_list) == 0:
        hit = False
    else:
        if hit == False:
            ship_health -= 10
            hit = True
            print('hit')

        if ship_health == 0:
            print('Game Over')
            ship_health == 100
        
    ''' move the player in horizontal direction '''    
    player1[0] += player1_vx    
    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if player1_vx > 0:
                player1[0] = w[0] - player1[2]
            elif player1_vx < 0:
                player1[0] = w[0] + w[2]

        elif intersects.rect_rect(player2, w):       
            if player2_vx > 0:
                player2[0] = w[0] - player2[2]
            elif player2_vx < 0:
                player2[0] = w[0] + w[2]
    ''' move the player in vertical direction '''
    player1[1] += player1_vy
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if player1_vy > 0:
                player1[1] = w[1] - player1[3]
            if player1_vy < 0:
                player1[1] = w[1] + w[3]

        
 # Drawing code
    screen.fill(BLACK)

    for e in enemy:
        pygame.draw.rect(screen, RED, (e[0], e[1], 5, 5))

    screen.blit(gameimg, (0,0))
    
    pygame.draw.rect(screen, WHITE, player1)

    pygame.draw.rect(screen, WHITE, player2)

    #for w in walls:
        #pygame.draw.rect(screen, BLUE, w)

 # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()
# Close window and quit
pygame.quit()
