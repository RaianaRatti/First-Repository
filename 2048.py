#MODULES-------------------------------------------------------------------------------------------------------------

import pygame
import numpy as np
import random

pygame.init()

#VARIABLES-----------------------------------------------------------------------------------------------------------

#Screen variables
screen = pygame.display.set_mode((900,900))
running = True
two = pygame.image.load("images/2048/2.png")
four = pygame.image.load("images/2048/4.png")
eight = pygame.image.load("images/2048/8.png")
sixteen = pygame.image.load("images/2048/16.png")
threetwo = pygame.image.load("images/2048/32.png")
sixfour = pygame.image.load("images/2048/64.png")
onetwoeight = pygame.image.load("images/2048/128.png")
twofivesix = pygame.image.load("images/2048/256.png")
fiveonetwo = pygame.image.load("images/2048/512.png")
onezerotwofour = pygame.image.load("images/2048/1024.png")
twozerofoureight = pygame.image.load("images/2048/2048.png")
lose = pygame.image.load("images/lose.png")
win = pygame.image.load("images/win.png")

matrix = np.empty([45,45])
check_matrix = np.empty([6,6])
win = 0
time = 0
checker = 0

#DEFINTION FUNCTIONS-------------------------------------------------------------------------------------------------

def zero_finder():
    global matrix, counter, a
    counter = 0
    for i in range(0,4):
        for j in range(0,4):
            if(matrix[i*10 + 5][j*10 + 5] == 0):
                counter = counter + 1

def create_two():
    global matrix, counter
    temporary = 0
    zero_finder()
    if(counter > 2):
        counter = 2
    while(temporary < counter):
        x = random.randint(0,3)
        y = random.randint(0,3)
        if(matrix[x*10 + 5][y*10 + 5] == 0):
            d = random.randint(1,10)
            if(d == 1):
                matrix[x*10 + 5][y*10 + 5] = 4
            else:
                matrix[x*10 + 5][y*10 + 5] = 2
            temporary = temporary + 1
    
def move_up_matrix():
    global matrix
    for i in range(0,40):
        for j in range(0,40):
            if(i>5):
                if(matrix[i][j] > matrix[i-1][j] and matrix[i-1][j] == 0 and (matrix[i-10][j] == 0 or matrix[i-10][j] == matrix[i][j])):
                    (matrix[i][j],matrix[i-1][j]) = (matrix[i-1][j],matrix[i][j])
                if(matrix[i-1][j] == matrix[i][j]):
                    matrix[i-1][j] = matrix[i-1][j] + matrix[i][j]
                    matrix[i][j] = 0

def move_down_matrix():
    global matrix
    for i in range(0,35):
        for j in range(0,40):
            x = 34 - i
            if(matrix[x][j] > matrix[x+1][j] and matrix[x+1][j] == 0 and (matrix[x+10][j] == 0 or matrix[x+10][j] == matrix[x][j])):
                (matrix[x][j],matrix[x+1][j]) = (matrix[x+1][j],matrix[x][j])
            if(matrix[x+1][j] == matrix[x][j]):
                    matrix[x+1][j] = matrix[x][j] + matrix[x+1][j]
                    matrix[x][j] = 0

def move_left_matrix():
    global matrix
    for i in range(0,40):
        for j in range(0,40):
            if(j>5):
                if(matrix[i][j] > matrix[i][j-1] and matrix[i][j-1] == 0 and (matrix[i][j-10] == 0 or matrix[i][j-10] == matrix[i][j])):
                    (matrix[i][j],matrix[i][j-1]) = (matrix[i][j-1],matrix[i][j])
                if(matrix[i][j] == matrix[i][j-1]):
                    matrix[i][j-1] = matrix[i][j] + matrix[i][j-1]
                    matrix[i][j] = 0

def move_right_matrix():
    global matrix
    for j in range(0,35):
        for i in range(0,40):
            y = 34 - j
            if(matrix[i][y] > matrix[i][y+1] and matrix[i][y+1] == 0 and (matrix[i][y+10] == 0 or matrix[i][y+10] == matrix[i][y])):
                (matrix[i][y],matrix[i][y+1]) = (matrix[i][y+1],matrix[i][y])
            if(matrix[i][y] == matrix[i][y+1]):
                matrix[i][y+1] = matrix[i][y] + matrix[i][y+1]
                matrix[i][y] = 0

def show():
    global matrix
    screen.fill((0,0,0))
    for i in range(0,40):
        for j in range(0,40):
            if(matrix[i][j] == 2):
                screen.blit(two,(j*20,i*20))
            elif(matrix[i][j] == 4):
                screen.blit(four,(j*20,i*20))
            elif(matrix[i][j] == 8):
                screen.blit(eight,(j*20,i*20))
            elif(matrix[i][j] == 16):
                screen.blit(sixteen,(j*20,i*20))
            elif(matrix[i][j] == 32):
                screen.blit(threetwo,(j*20,i*20))
            elif(matrix[i][j] == 64):
                screen.blit(sixfour,(j*20,i*20))
            elif(matrix[i][j] == 128):
                screen.blit(onetwoeight,(j*20,i*20))
            elif(matrix[i][j] == 256):
                screen.blit(twofivesix,(j*20,i*20))
            elif(matrix[i][j] == 512):
                screen.blit(fiveonetwo,(j*20,i*20))
            elif(matrix[i][j] == 1024):
                screen.blit(onezerotwofour,(j*20,i*20))
            elif(matrix[i][j] == 2048):
                screen.blit(twozerofoureight,(j*20,i*20))

def move_up():
    global matrix
    for i in range(0,40):
        move_up_matrix()
        show()
        pygame.display.update()

def move_down():
    global matrix
    for i in range(0,40):
        move_down_matrix()
        show()
        pygame.display.update()

def move_left():
    global matrix
    for i in range(0,40):
        move_left_matrix()
        show()
        pygame.display.update()

def move_right():
    global matrix
    for i in range(0,40):
        move_right_matrix()
        show()
        pygame.display.update()

def check():
    global matrix, check_matrix, running, win, time
    for i in range(0,6):
        for j in range(0,6):
            if(i == 0 or i == 5 or j == 0 or j == 5):
                check_matrix[i][j] = -1
            else:
                check_matrix[i][j] = matrix[(i-1)*10 + 5][(j-1)*10 + 5]
    
    counter = 0
    for i in range(1,5):
        for j in range(1,5):
            if(check_matrix[i][j] == 2048):
                win = 1
                time = time + 1
            if(check_matrix[i][j] != 0):
                if((check_matrix[i][j] != check_matrix[i-1][j]) and (check_matrix[i][j] != check_matrix[i+1][j]) and (check_matrix[i][j] != check_matrix[i][j-1]) and (check_matrix[i][j] != check_matrix[i][j+1])):
                    counter = counter + 1
    if(counter == 16):
        time = time + 1

#lOOP--------------------------------------------------------------------------------------------------------------------

for i in range(0,45):
    for j in range(0,45):
        matrix[i][j] = 0

create_two()

while running:
    show()

    check()

    if(time > 50):
        screen.fill((0,0,0))
    if(time == 80):
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            checker = 1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move_up()
                valid = 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move_down()
                valid = 1
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_left()
                valid = 1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_right()
                valid = 1
            else:
                valid = 0
        if (event.type == pygame.KEYUP) and (valid == 1):
            create_two()
        
    pygame.display.update()

if(checker == 0):
    going = True
else:
    going = False

while going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    if(win == 1):
        screen.blit(win,(0,350))
    else:
        screen.blit(lose,(0,350))
    pygame.display.update()