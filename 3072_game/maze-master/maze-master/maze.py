# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1280
HEIGHT = 950
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#images
img = pygame.image.load('splashscreen.jpg')
playerimg = pygame.image.load('player.png')
enemyimg = pygame.image.load('enemy.png')
coinimg = pygame.image.load('coin.png')
teleportimg = pygame.image.load('teleport.png')

#sound
sounda = pygame.mixer.Sound('cowburp.wav')
soundb = pygame.mixer.Sound('teleport.wav')
soundc = pygame.mixer.Sound('deathsound.wav')
soundd = pygame.mixer.Sound('splashscreen.wav')

#stages
START = 0
PLAYING = 1
END = 2

def setup():
    global coins, stage, player, player_vx, player_vy, score, enemy, enemy_vx, enemy_vy
    
    # Make coins
    coin1 = [50, 175, 25, 25]
    coin2 = [50, 200, 25, 25]
    coin3 = [50, 150, 25, 25]

    coins = [coin1, coin2, coin3]
    
    player =  [50, 25, 25, 25]
    player_vx = 0
    player_vy = 0

    enemy = [1205, 25, 25, 25]
    enemy_vx = 0
    enemy_vy= 0
    
    stage = START

    score = 0
# Make a player

enemy_speed = 3.5
player_speed = 5.3

# make walls
wall1 =  [100, 275, 200, 25]
wall2 =  [100, 350, 25, 200]
wall3 =  [100, 25, 25, 200]
wall4 =  [0, 0, 1280, 25]
wall5 =  [0, 925, 1280, 25]
wall6 =  [0, 0, 25, 950]
wall7 =  [1255, 0, 25, 950]
wall8 =  [0, 550, 440, 25]
wall9 =  [100, 450, 200, 25]
wall10 = [980, 275, 200, 25]
wall11 = [1155, 350, 25, 200]
wall12 = [1155, 25, 25, 200]
wall13 = [930, 550, 300, 25]
wall14 = [980, 450, 200, 25]
wall15 = [100, 350, 200, 25]
wall16 = [325, 350, 25, 200]
wall17 = [980, 350, 200, 25]
wall18 = [930, 350, 25, 200]
wall19 = [415, 275, 185, 25]
wall20 = [655, 275, 200, 25]
wall21 = [415, 275, 25, 500]
wall22 = [575, 275, 25, 450]
wall23 = [495, 775, 800, 25]
wall24 = [655, 775, 200, 25]
wall25 = [655, 300, 25, 425]
wall26 = [830, 275, 25, 500]
wall27 = [495, 325, 25, 475]
wall28 = [340, 775, 100, 25]
wall29 = [340, 600, 25, 175]
wall30 = [240, 600, 100, 25]
wall31 = [240, 600, 25, 100]
wall32 = [240, 700, 75, 25]
wall33 = [290, 650, 25, 50]
wall34 = [215, 750, 150, 25]
wall35 = [190, 650, 25, 125]
wall36 = [115, 625, 100, 25]
wall37 = [115, 650, 25, 250]
wall38 = [75, 875, 140, 25]
wall39 = [25, 850, 15, 25]
wall40 = [65, 825, 25, 25]
wall41 = [55, 775, 25, 25]
wall42 = [90, 725, 25, 25]
wall43 = [25, 725, 25, 25]
wall44 = [25, 675, 65, 25]
wall45 = [50, 625, 65, 25]
wall46 = [50, 600, 25, 25]
wall47 = [200, 875, 240, 25]
wall48 = [415, 800, 25, 75]
wall49 = [440, 850, 750, 25]
wall50 = [500, 825, 25, 75]
wall51 = [550, 800, 25, 25]
wall52 = [600, 825, 25, 75]
wall53 = [650, 800, 25, 25]
wall54 = [700, 825, 25, 75]
wall55 = [750, 800, 25, 25]
wall56 = [800, 825, 25, 75]
wall57 = [850, 800, 25, 25]
wall58 = [900, 825, 25, 75]
wall59 = [950, 800, 25, 25]
wall60 = [1000, 825, 25, 75]
wall61 = [1050, 800, 25, 25]
wall62 = [1100, 825, 25, 75]
wall63 = [1150, 800, 25, 25]
wall64 = [1150, 900, 25, 25]
wall65 = [1050, 900, 25, 25]
wall66 = [950, 900, 25, 25]
wall67 = [850, 900, 25, 25]
wall68 = [750, 900, 25, 25]
wall69 = [650, 900, 25, 25]
wall70 = [550, 900, 25, 25]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9,
         wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17,
         wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25,
         wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33,
         wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41,
         wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49,
         wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57,
         wall58, wall59, wall60, wall61, wall62, wall63, wall64, wall65,
         wall66, wall67, wall68, wall69, wall70]


'create teleporter'
teleport1 = [265, 675, 25, 25]

teleports = [teleport1]

'speed trap'
speedtrapslow = [500, 800, 25, 25]
speedtrapfast = [500, 900, 25, 25]

# Game loop
case = 1
win = False
lose = False
done = False
setup()
stage = START
score = 0

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

                    
    if stage == PLAYING:
        
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_w]
        down = pressed[pygame.K_s]
        left = pressed[pygame.K_a]
        right = pressed[pygame.K_d]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right: 
            player_vx = player_speed
        else:
            player_vx = 0

        enemy_up = pressed[pygame.K_UP]
        enemy_down = pressed[pygame.K_DOWN]
        enemy_left = pressed[pygame.K_LEFT]
        enemy_right = pressed[pygame.K_RIGHT]

        if enemy_up:
            enemy_vy = -enemy_speed
        elif enemy_down:
            enemy_vy = enemy_speed
        else:
            enemy_vy = 0
            
        if enemy_left:
            enemy_vx = -enemy_speed
        elif enemy_right: 
            enemy_vx = enemy_speed
        else:
            enemy_vx = 0


        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx
    enemy[0] += enemy_vx
    
    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]
        if intersects.rect_rect(enemy, w):
            if enemy_vx > 0:
                enemy[0] = w[0] - enemy[2]
            elif enemy_vx < 0:
                enemy[0] = w[0] + w[2]
                
    ''' move the player in vertical direction '''
    player[1] += player_vy
    enemy[1] += enemy_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]
        if intersects.rect_rect(enemy, w):
            if enemy_vy > 0:
                enemy[1] = w[1] - enemy[3]
            if enemy_vy < 0:
                enemy[1] = w[1] + w[3]
        
    ''' here is where you should resolve player collisions with screen edges '''
    top = player[1]
    bottom = player[1] + player[3]
    left = player[0]
    right = player[0] + player[2]
    if case == 1:
        ''' if the block is moved out of the window, nudge it back on. '''
        if top < 0:
            player[1] = 0
        elif bottom > HEIGHT:
            player[1] = HEIGHT - player[3]

        if left < 0:
            player[0] = 0
        elif right > WIDTH:
            player[0] = WIDTH - player[2]




    ''' get the coins '''
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score += 1
        sounda.play(0)
        
    if len(coins) == 0:
        win = True
        stage = END

    if intersects.rect_rect(player, enemy):
        lose = True
        stage = END
        soundc.play(0)

    if intersects.rect_rect(player, teleport1):
        player = [475, 800, 25, 25]
        player_speed = 5.3
        enemy_speed = 3.5
        soundb.play(0)
        
    if intersects.rect_rect(player, speedtrapslow):
        player_speed = 3.4
        enemy_speed = 3.9
        
    if intersects.rect_rect(player, speedtrapfast):
        player_speed = 5.3
        enemy_speed = 3.5
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
      
    for t in teleports:
        screen.blit(teleportimg, (t[0], t[1]))


    
    screen.blit(playerimg, (player[0], player[1]))
    
    screen.blit(enemyimg, (enemy[0], enemy[1]))

    pygame.draw.rect(screen, RED, speedtrapslow)
    pygame.draw.rect(screen, GREEN, speedtrapfast)
    
    for w in walls:
        pygame.draw.rect(screen, BLUE, w)
        

    
    for c in coins:
        #pygame.draw.rect(screen, YELLOW, c)
        screen.blit(coinimg, (c[0], c[1]))
        
    font = pygame.font.Font(None, 48)
    text = font.render(str(score), 1, WHITE) 
    screen.blit(text, [5, 10])
    
    #if END:
        
    if stage == START:
        screen.blit(img, (0,0))
        soundd.play(0)
    if stage == END and win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, WHITE)
        screen.blit(text, [565, 200])
        text2 = font.render("Press SPACE to Play Again!", 1, WHITE)
        screen.blit(text2, [565, 300])
    if stage == END:
        player_vx = 0
        player_vy = 0
        enemy_vx = 0
        enemy_vy = 0
    if lose == True and stage == END:
        text2 = font.render("Press SPACE to Play Again!", 1, WHITE)
        screen.blit(text2, [565, 300])
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
