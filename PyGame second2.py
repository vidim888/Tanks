__author__ = 'Vadim'

import pygame
import time
import math
import random
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')
# icon = pygame.image.load("apple.png")
# pygame.display.set_icon(icon)
white = (255, 255, 255)
grey = (170, 170, 170)
black = (0, 0, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
green = (34, 177, 76)
light_green = (0, 255, 0)
clock = pygame.time.Clock()
FPS = 30
tankWidth = 40
tankHeight = 20
turretWidth = 3
wheelWidth = 5
tankSpeed = 5
barrier_width = 50
start_health = 500
max_power = 100
tankY = display_height * 0.9
ground_height = display_height - tankY - tankHeight - wheelWidth
a = 9.8
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)
# img = pygame.image.load('snakehead.png')
# appleimg = pygame.image.load('apple.png')
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])
def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
def message_to_screen(msg,color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)
def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("Controls", green, -100, "large")
        message_to_screen("Fire: Spacebar", black, -30)
        message_to_screen("Move Turret: Up and Down arrows", black, 10)
        message_to_screen("Move Tank: Left and Right arrows", black, 50)
        message_to_screen("Pause: P", black, 90)
        button("Play", 150, 500, 100, 50, green, light_green, "play")
        button("Main", 350, 500, 100, 50, yellow, light_yellow, "main")
        button("Quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
        clock.tick(FPS)
def button(text, x, y, width, height, inactive_color, active_color, action=None, xx=0):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                time.sleep(0.1)
                game_controls()
            if action == "play":
                gameLoop(xx % 4)
            if action == "main":
                time.sleep(0.1)
                game_intro()
            if action == "difficulty":
                time.sleep(0.2)
                return xx + 1
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)
    if action == 'difficulty':
        return xx
def pause():
    paused = True
    message_to_screen("Paused", black, -100, "large")
    message_to_screen("Press C to continue playing or Q to quit", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(FPS)
def game_intro():
    intro = True
    difficulty = ['easy', 'medium', 'hard', 'impossible']
    x = 0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks!", green, -100, "large")
        message_to_screen("The objective is to shoot and destroy", black, -30)
        message_to_screen("the enemy tank before they destroy you.", black, 10)
        message_to_screen("The more enemies you destroy, the harder they get.", black, 50)
        # message_to_screen("Press C to play, P to pause or Q to quit",black,180)
        button("Play", 150, 500, 100, 50, green, light_green, "play", x)
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, "controls", x)
        button("Quit", 550, 500, 100, 50, red, light_red, "quit", x)
        # x = button("Difficulty: "+difficulty[x % 4], 100, 550, 200, 50, white, grey, "difficulty", x)
        textSurface, textRect = text_objects("Difficulty: "+difficulty[x % 4], black)
        x = button("Difficulty: "+difficulty[x % 4], 190-textRect[2]/2, 550, textRect[2]+20, 50, white, grey, "difficulty", x)
        pygame.display.update()
        clock.tick(FPS)
def game_over():
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("Game Over", green, -100, "large")
        message_to_screen("You died", black, -30)
        button("Play again", 150, 500, 120, 50, green, light_green, "play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, "controls")
        button("Quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
        clock.tick(FPS)
def you_win():
    you_win = True
    while you_win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("You won!", green, -100, "large")
        message_to_screen("Congratulations!", black, -30)
        button("Play again", 150, 500, 120, 50, green, light_green, "play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, "controls")
        button("Quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
        clock.tick(FPS)
def barrier(xlocation, randomHeight, barrier_width):
    pygame.draw.rect(gameDisplay, black, [xlocation, display_height-randomHeight, barrier_width, randomHeight])
def explosion(x, y, mainTankX, enemyTankX, player_health, enemy_health, size=50):
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        colorChoices = [red, light_red, yellow, light_yellow]
        magnitude = 1
        while magnitude < size:
            exploding_bit_x = x + random.randrange(-1*magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude, magnitude)
            r = random.randrange(1, 5)
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0, 4)], (int(exploding_bit_x), int(exploding_bit_y)), r)
            magnitude += 1
            if mainTankX - tankWidth/2 <= exploding_bit_x <= mainTankX + tankWidth/2 and tankY <= exploding_bit_y <= display_height - ground_height or mainTankX - tankHeight/2 <= exploding_bit_x <= mainTankX + tankHeight/2 and tankY - tankHeight/2 <= exploding_bit_y <= tankY:
                player_health -= r
            if enemyTankX - tankWidth/2 <= exploding_bit_x <= enemyTankX + tankWidth/2 and tankY <= exploding_bit_y <= display_height - ground_height or enemyTankX - tankHeight/2 <= exploding_bit_x <= enemyTankX + tankHeight/2 and tankY - tankHeight/2 <= exploding_bit_y <= tankY:
                enemy_health -= r
            pygame.display.update()
            clock.tick(100)
        return(player_health, enemy_health)
def fireShell(x, angle, fire_power, xlocation, randomHeight, draw, mainTankX, enemyTankX, player_health, enemy_health, enemy_power=0, turretAngle=0, enemyAngle=0):
    fire = True
    turPosY = tankHeight*math.cos(angle)
    turPosX = tankHeight*math.sin(angle)
    shellPos = [x + turPosX, tankY - turPosY]
    # yo = shellPos[1]
    # xo = shellPos[0]
    dt = 0.1
    t = dt
    power_x = fire_power*math.sin(angle)
    power_y = fire_power*math.cos(angle)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        shellPos[0] += power_x*dt
        dy = power_y*t - a*(t**2)/2
        shellPos[1] = tankY - turPosY - dy
        t += dt
        check_x1 = shellPos[0] >= xlocation
        check_x2 = shellPos[0] <= xlocation + barrier_width
        check_y1 = shellPos[1] >= display_height - randomHeight
        check_y2 = shellPos[1] <= display_height
            # if shellPos[0] < 0 or shellPos[0] > 800 or shellPos[1] > 600 or shellPos[1] < -5000:
        if check_x1 and check_x2 and check_y1 and check_y2:
            if draw:
                player_health, enemy_health = explosion(shellPos[0], shellPos[1], mainTankX, enemyTankX, player_health, enemy_health)
                return player_health, enemy_health
            if not draw:
                return 1
            fire = False
        if draw:
            if mainTankX - tankWidth/2 <= shellPos[0] <= mainTankX + tankWidth/2 and tankY <= shellPos[1] <= display_height - ground_height \
                    or mainTankX - tankHeight/2 <= shellPos[0] <= mainTankX + tankHeight/2 and tankY - tankHeight/2 <= shellPos[1] <= tankY \
                    or enemyTankX - tankWidth/2 <= shellPos[0] <= enemyTankX + tankWidth/2 and tankY <= shellPos[1] <= display_height - ground_height \
                    or enemyTankX - tankHeight/2 <= shellPos[0] <= enemyTankX + tankHeight/2 and tankY - tankHeight/2 <= shellPos[1] <= tankY:
                player_health, enemy_health = explosion(shellPos[0], shellPos[1], mainTankX, enemyTankX, player_health, enemy_health)
                return player_health, enemy_health
        if shellPos[1] > display_height - ground_height:
            # hit_x = xo + power_x*((power_y+(power_y**2 + 2*a*(turPosY + display_height - ground_height - yo))**0.5)/a)
            hit_x = shellPos[0]
            hit_y = display_height - ground_height - 2
            if not draw:
                return hit_x
            if draw:
                player_health, enemy_health = explosion(hit_x, hit_y, mainTankX, enemyTankX, player_health, enemy_health)
                return player_health, enemy_health
            fire = False
        if draw:
            gameDisplay.fill(white)
            power(fire_power, 'player')
            power(enemy_power, 'enemy')
            health_bars(player_health, enemy_health)
            tank(mainTankX, turretAngle)
            tank(enemyTankX, enemyAngle)
            barrier(xlocation, randomHeight, barrier_width)
            gameDisplay.fill(green, rect = [0, display_height - ground_height, display_width, ground_height])
            pygame.draw.circle(gameDisplay, red, (int(shellPos[0]), int(shellPos[1])), 5)
            pygame.display.update()
            clock.tick(FPS/dt)
def power(lvl, whos):
    text = smallfont.render("Power: " + str(lvl) + "%", True, black)
    if whos == 'player':
        gameDisplay.blit(text, [display_width*0.78, 1])
    elif whos == 'enemy':
        gameDisplay.blit(text, [display_width*0.08, 1])
def tank(x, angle):
    x = int(x)
    y = int(tankY)
    turPosY = tankHeight*math.cos(angle)
    turPosX = tankHeight*math.sin(angle)
    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x - tankHeight, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, black, (x, y), (int(x+turPosX), int(y-turPosY)), turretWidth)
    startX = int(tankWidth/2)
    for i in range(7):
        pygame.draw.circle(gameDisplay, black, (x-startX+wheelWidth, y+tankHeight), wheelWidth)
        startX -= wheelWidth
def enemy_move(enemyTankX, tankSpeed, enemyAngle, fire_power, enemy_power, player_health, enemy_health, mainTankX, turretAngle, xlocation, randomHeight, d_power):
    r_t = random.randint(5, 20)
    direction = random.randint(-2, 1)
    if enemyTankX + tankWidth/2 > xlocation - tankSpeed*1.1:
        tankMove = -tankSpeed
    elif enemyTankX - tankWidth/2 < tankSpeed*1.1:
        tankMove = tankSpeed
    elif direction >= 0:
        tankMove = tankSpeed
    elif direction < 0:
        tankMove = -tankSpeed
    if enemyTankX + tankWidth/2 + tankMove*r_t > xlocation:
        move_change = xlocation - enemyTankX - tankWidth/2 - tankSpeed
    elif enemyTankX - tankWidth/2 + tankMove*r_t < 0:
        move_change = -enemyTankX + tankWidth/2 + tankSpeed
    else:
        move_change = tankMove*r_t
    aiming_point = [xlocation, display_height - randomHeight*1.3]
    dx = aiming_point[0] - enemyTankX - move_change + tankWidth/2
    dy = tankY - aiming_point[1]
    found = False
    trying_angle = math.atan(dx/dy)
    newEnemyAngle = trying_angle
    ideal_power = 0
    while not found:
        for turn in range(30, max_power+1):
            hit_dot = fireShell(enemyTankX+move_change, trying_angle, turn, xlocation, randomHeight, False, mainTankX, enemyTankX, player_health, enemy_health)
            ideal_power = turn
            if mainTankX < hit_dot < mainTankX + 20:
                newEnemyAngle = trying_angle
                found = True
                break
        trying_angle -= math.pi/90
        if trying_angle < 0:
            found = True
    this_angle = enemyAngle
    this_power = enemy_power
    for x in range(r_t):
        enemyTankX += move_change/r_t
        enemyAngle += (newEnemyAngle-this_angle)/r_t
        enemy_power += (ideal_power-this_power)/r_t
        if enemyTankX + tankWidth/2 > xlocation or enemyTankX - tankWidth/2 < 0:
            enemyAngle -= (newEnemyAngle-this_angle)/r_t
        gameDisplay.fill(white)
        power(fire_power, 'player')
        power(int(enemy_power), 'enemy')
        health_bars(player_health, enemy_health)
        tank(mainTankX, turretAngle)
        tank(enemyTankX, enemyAngle)
        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(green, rect=[0, display_height - ground_height, display_width, ground_height])
        pygame.display.update()
        clock.tick(FPS)
    # ideal_power = ((2*(((enemyTankX+tankHeight*math.sin(enemyAngle)-mainTankX-2*math.sin(enemyAngle)*a*(2*tankHeight*math.cos(enemyAngle)+display_height-ground_height-tankY))**2-(a**2-1)*((enemyTankX+tankHeight*math.sin(enemyAngle))**2+mainTankX**2-2*(enemyTankX+tankHeight*math.sin(enemyAngle))*mainTankX))**0.5-enemyTankX-tankHeight*math.sin(enemyAngle)+mainTankX+2*math.sin(enemyAngle)*a*(2*tankHeight*math.cos(enemyAngle)+display_height-ground_height-tankY)))/((a**2-1)*math.sin(2*enemyAngle)))**0.5
    if d_power == 0:
        i_power = ideal_power
    else:
        i_power = ideal_power + random.randrange(-d_power/2, d_power)
    return enemyTankX, enemyAngle, ideal_power, i_power
def health_bars(player_health, enemy_health):
    if player_health > 0.75*start_health:
        player_health_color = green
    elif player_health > 0.5*start_health:
        player_health_color = yellow
    else:
        player_health_color = red
    if enemy_health > 0.75*start_health:
        enemy_health_color = green
    elif enemy_health > 0.5*start_health:
        enemy_health_color = yellow
    else:
        enemy_health_color = red
    pygame.draw.rect(gameDisplay, black, (int(display_width*0.8)-2, int(display_height*0.06)-2, 104, 29))
    pygame.draw.rect(gameDisplay, black, (int(display_width*0.1)-2, int(display_height*0.06)-2, 104, 29))
    pygame.draw.rect(gameDisplay, white, (int(display_width*0.8), int(display_height*0.06), 100, 25))
    pygame.draw.rect(gameDisplay, white, (int(display_width*0.1), int(display_height*0.06), 100, 25))
    pygame.draw.rect(gameDisplay, player_health_color, (int(display_width*0.8), int(display_height*0.06), player_health*100/start_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (int(display_width*0.1), int(display_height*0.06), enemy_health*100/start_health, 25))
def gameLoop(dif):
    gameExit = False
    gameOver = False
    if dif == 0:
        d_power = 10
    elif dif == 1:
        d_power = 6
    elif dif == 2:
        d_power = 2
    elif dif == 3:
        d_power = 0
    mainTankX = display_width * 0.9
    enemyTankX = display_width * 0.1
    tankMove = 0
    turretAngle = -math.pi/4
    enemyAngle = math.pi/4
    turretAngled = 0
    fire_power = int(max_power/2)
    enemy_power = max_power
    power_change = 0
    player_health = start_health
    enemy_health = start_health
    xlocation = int((display_width/2)+random.randint(-0.2*display_width, 0.2*display_width))-25
    randomHeight = random.randrange(display_height*0.2, display_height*0.7)
    while not gameExit:
        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, "large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -tankSpeed
                if event.key == pygame.K_RIGHT:
                    tankMove = tankSpeed
                if event.key == pygame.K_UP:
                    turretAngled = math.pi/90
                if event.key == pygame.K_DOWN:
                    turretAngled = -math.pi/90
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_SPACE:
                    player_health, enemy_health = fireShell(mainTankX, turretAngle, fire_power, xlocation, randomHeight, True, mainTankX, enemyTankX, player_health, enemy_health, enemy_power, turretAngle, enemyAngle)
                    enemyTankX, enemyAngle, enemy_power, i_power = enemy_move(enemyTankX, tankSpeed, enemyAngle, fire_power, enemy_power, player_health, enemy_health, mainTankX, turretAngle, xlocation, randomHeight, d_power)
                    player_health, enemy_health = fireShell(enemyTankX, enemyAngle, i_power, xlocation, randomHeight, True, mainTankX, enemyTankX, player_health, enemy_health, enemy_power, turretAngle, enemyAngle)
                if event.key == pygame.K_a:
                    power_change = -1
                if event.key == pygame.K_d:
                    power_change = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and tankMove < 0:
                    tankMove = 0
                elif event.key == pygame.K_RIGHT and tankMove > 0:
                    tankMove = 0
                if event.key == pygame.K_DOWN and turretAngled < 0:
                    turretAngled = 0
                elif event.key == pygame.K_UP and turretAngled > 0:
                    turretAngled = 0
                if event.key == pygame.K_a and power_change < 0:
                    power_change = 0
                elif event.key == pygame.K_d and power_change > 0:
                    power_change = 0
        if turretAngle <= -math.pi/2 and turretAngled <= 0 or turretAngle >= math.pi/2 and turretAngled >= 0:
            turretAngled = 0
        mainTankX += tankMove
        if mainTankX - tankWidth/2 < xlocation + barrier_width or mainTankX + tankWidth/2 > display_width:
            mainTankX -= tankMove
        if fire_power >= max_power and power_change > 0 or fire_power <= 0 and power_change < 0:
            fire_power -= power_change
        if player_health < 0:
            game_over()
        elif enemy_health < 0:
            you_win()
        turretAngle += turretAngled
        fire_power += power_change
        gameDisplay.fill(white)
        power(fire_power, 'player')
        power(enemy_power, 'enemy')
        health_bars(player_health, enemy_health)
        tank(mainTankX, turretAngle)
        tank(enemyTankX, enemyAngle)
        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(green, rect = [0, display_height - ground_height, display_width, ground_height])
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
game_intro()