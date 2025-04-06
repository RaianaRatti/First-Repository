#MODULES-------------------------------------------------------------------------------------------------------------

import pygame
import random
import math

pygame.init()


#VARIABLES----------------------------------------------------------------------------------------------------------

#forever variables
screen = pygame.display.set_mode((1500,775))
running = True
background = pygame.image.load("images/ufo/background.jpg")

#player
player = pygame.image.load("images/ufo/spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#bullet
bullet = pygame.image.load("images/ufo/bullet.png")
bulletX = playerX + 15
bulletY = playerY
bullet_tracker = 1

#enemy
enemy = pygame.image.load("images/ufo/ufo.png")
enemyX = random.randint(64,(1500-64))
enemyY = 100
enemyX_change = 0
tracker = random.randint(0,1)


#DEFINTION FUNCTIONS-----------------------------------------------------------------------------------------------

#making things appear
def position(z,x,y):
    screen.blit(z,(x,y))

#boundary checker for player
def boundary():
    global playerX, playerY, enemyY
    if(playerX <= 0):
        playerX = 0
    if(playerX >= (1500 - 64)):
        playerX = (1500 - 64)
    if(playerY <= (enemyY + 200)):
        playerY = (enemyY + 200)
    if(playerY >= (775 - 64)):
        playerY = (775 - 64)
    if(enemyY >= 600):
        exit()

#resets bullet's positions to those of player
def bullet_position_set():
    global bulletX, bulletY, playerX, playerY
    bulletX = playerX + 15
    bulletY = playerY

#moves bullet up after launch while keeping on same x-value
def bullet_launch():
    global bulletX, bulletY, bullet_tracker, playerY, a, playerX, playerY
    if(bullet_tracker == 1):
        bulletY = bulletY - 10
        position(bullet, bulletX, bulletY)
        if(bulletY <= 0):
            bullet_tracker = 1
            bullet_position_set()

#moves enemy back and forth
def moving_enemy():
    global enemyX, enemyY, tracker, enemyX_change
    enemyX_change = 0
    position(enemy,enemyX,enemyY)
    if(tracker == 1):
        if(enemyX <= (1500-64)):
            enemyX_change = enemyX_change + 1
        else:
            tracker = 0
            enemyX_change = 0
            enemyY = enemyY + 20
    elif(tracker == 0):
        if(enemyX >= 20):
            enemyX_change = enemyX_change - 1
        else:
            tracker = 1
            enemyX_change = 0
            enemyY = enemyY + 20
    enemyX = enemyX + enemyX_change

#checks to see if collision has occured
def collision_check():
    global bulletY, playerY, bulletX, playerX, enemyX, enemyY, bullet_tracker
    distance = math.sqrt(math.pow(((bulletX) - (enemyX + 15)), 2)) + math.pow(((bulletY) - (enemyY + 15)), 2)
    if (distance < 50):
        bulletY = playerY
        bulletX = playerX + 15
        enemyX = random.randint(64,(1500-64))
        enemyY = 100
        bullet_tracker = 1
        bullet_position_set()


#RUNNING LOOP--------------------------------------------------------------------------------------------------------

while running:
    #background
    screen.blit(background, (0,0))

    #exiting out of game if you click cross button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #changing position of ship accordingly by key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_change = playerY_change - 3
            if event.key == pygame.K_s:
                playerY_change = playerY_change + 3
            if event.key == pygame.K_d:
                playerX_change = playerX_change + 3
            if event.key == pygame.K_a:
                playerX_change = playerX_change - 3
            if event.key == pygame.K_SPACE:
                bullet_tracker = 1
  
    #stopping change in position of ship accordingly after you lift your finger off key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerY_change = 0
            if event.key == pygame.K_s:
                playerY_change = 0
            if event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_a:
                playerX_change = 0

    playerX = playerX + playerX_change
    playerY = playerY + playerY_change

    position(player, playerX, playerY)

    if(bullet_tracker == 0):
        bullet_position_set()

    boundary()

    moving_enemy()

    bullet_launch()

    collision_check()

    pygame.display.update()