#MODULES-----------------------------------------------------------------------------------------------------------

import pygame
import random

pygame.init()
pygame.font.init()


#VARIABLES---------------------------------------------------------------------------------------------------------

#Forever variables
screen = pygame.display.set_mode((1500,775))
running = True
bird = pygame.image.load("images/flappy_bird/ghost.png")

#Backgrounds
background = pygame.image.load("images/flappy_bird/cave.jpg")
lose = pygame.image.load("images/lose.png")

#Bird variables
X = 600
Y = 350
velocity = 0
acceleration = 0.002
time = 0
direction = 0

#Score variables
score = -1
font = pygame.font.Font(None, 128)

#Pipe varibles
p1 = pygame.image.load("images/flappy_bird/down_pipe_pink.png")
p2 = pygame.image.load("images/flappy_bird/down_pipe_pink.png")
p3 = pygame.image.load("images/flappy_bird/up_pipe_pink.png")
p4 = pygame.image.load("images/flappy_bird/up_pipe_pink.png")
firstx = 2300
firsty = 0
secondx = 1500
secondy = 0
    
#DEFINITION FUNCTIONS----------------------------------------------------------------------------------------------

def position_check():
    global Y, running
    if(Y > 760):
        running = False

def set_up():
    global time, velocity
    time = 0
    velocity = 3

def up_check(): #set_down
    global time, velocity, acceleration, Y, bird, pipe_2, pipe_2_X, pipe_2_Y, direction
    if(velocity <= 0):
        direction = 0
        time = 0
        velocity = 0

def up():
    global time, velocity, acceleration, Y, bird, pipe_2, pipe_2_X, pipe_2_Y
    time = time + 1
    velocity = velocity - acceleration * time
    Y = Y - velocity

def down():
    global time, velocity, acceleration, Y, bird
    time = time + 1
    velocity = velocity + acceleration * time
    Y = Y + velocity

def gap_first():
    global firsty
    firsty = random.randint(-680,-230)

def gap_second():
    global secondy
    secondy = random.randint(-680,-230)

def print_pipes():
    global p1, p2, p3, p4, firstx, firsty, secondx, secondy
    screen.blit(p1,(firstx, firsty))
    screen.blit(p3,(firstx, firsty + 890))
    screen.blit(p2, (secondx, secondy))
    screen.blit(p4, (secondx, secondy + 890))

def move_pipes():
    global p1, p2, p3, p4, firstx, firsty, secondx, secondy
    firstx = firstx - 2
    secondx = secondx - 2

def check_pipes():
    global p1, p2, p3, p4, firstx, firsty, secondx, secondy, score
    if(firstx < -150):
        firstx = 1500
    if(secondx < -150):
        secondx = 1500

def score_counter():
    global score, X, firstx, secondx
    if(firstx == 1500 or secondx == 1500):
        score = score + 1

def collide():
    global bird_rect, p1_rect, p2_rect, p3_rect, p4_rect, firstx, firsty, secondx, secondy, X, Y, running, bird
    bird_rect = pygame.Rect(X,Y,bird.get_width(), bird.get_height())
    p1_rect = pygame.Rect(firstx, firsty, p1.get_width(), p1.get_height())
    p2_rect = pygame.Rect(secondx, secondy, p2.get_width(), p2.get_height())
    p3_rect = pygame.Rect(firstx, firsty + 920, p3.get_width(), p3.get_height())
    p4_rect = pygame.Rect(secondx, secondy + 920, p4.get_width(), p4.get_height())

    if bird_rect.colliderect(p1_rect) or bird_rect.colliderect(p3_rect) or bird_rect.colliderect(p2_rect) or bird_rect.colliderect(p4_rect):
        running = False


#LOOP----------------------------------------------------------------------------------------------------------------

gap_first()
gap_second()

while running:

    score_counter()

    #screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            direction = 1
            set_up()

    if(direction == 0): 
        down()
    else:
        up()
        up_check()

    position_check()
    move_pipes()
    screen.blit(bird,(X,Y))
    print_pipes()

    score_text = font.render(f'{score}', True, (255, 255, 255))
    screen.blit(score_text, (1400, 50))

    check_pipes()
    collide()
    pygame.display.update()

going = True
going_counter = 0

font = pygame.font.Font(None, 64)

while going:
    screen.fill((0,0,0))
    going_counter = going_counter + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    screen.blit(lose,(300,300))
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (650, 500))
    if(going_counter == 200):
        exit()
    pygame.display.update()