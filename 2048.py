import random
import numpy as np
import sys

matrix = np.empty((6,6))
copy = np.empty((6,6))
inp = 0
counter = 0
index = 0

#setting all values in matrix to zero and corner ones to -1
for i in range(0,6):
    for j in range(0,6):
        if (j==0 or j==5 or i==0 or i==5):
            matrix[i][j] = -1
        else:
            matrix[i][j] = 0

#asking for input
def asking_input():
    global inp
    inp = input("")

#finding number of empty cells in matrix
def zero_finder():
    global matrix
    counter = 0
    for i in range(1,5):
        for j in range(1,5):
            if(matrix[i][j] == 0):
                counter = counter + 1
    return counter

def two():
    global matrix
    c = 0
    index = 0
    counter = zero_finder()
    if(counter > 2):
        counter = 2    
    while (c < counter):
        i = random.randint(1,4)
        j = random.randint(1,4)
        if(matrix[i][j] == 0):
            #generating random number as 4 10% of time and 2 90% of time
            index = random.randint(1,10)
            if (index == 10):
                matrix[i][j] = 4
            else:
                matrix[i][j] = 2
            c = c + 1

#SORTING
def sort(a):
    for j in range(1,5):
        for p in range(0,4):
            for i in range(1,4):
                if((a[i][j] != -1) and (a[i+1][j] != -1)):
                    if ((a[i][j] < a[i+1][j]) and a[i][j]==0):
                        [a[i+1][j],a[i][j]] = [a[i][j],a[i+1][j]]

def add(a):
    for j in range(1,5):
        for i in range(1,4):
            if((a[i][j] != -1) and (a[i+1][j] != -1)):
                if (a[i][j] == a[i+1][j]):
                    a[i][j] = a[i][j] + a[i+1][j]
                    a[i+1][j] = 0
    sort(a)

#copying the matrix into the copy
def copy_matrix(a,b):
    for i in range(0,6):
        for j in range(0,6):
            b[i][j] = a[i][j]

#TRANSPOSE
def transpose(a, b):
    global inp, matrix, copy
    copy_matrix(matrix, copy)
    for i in range(1,5):
        for j in range(1,5):
            if(inp == 'w'):
                b[i][j] = a[i][j]
            if(inp == 'd'):
                b[5-j][i] = a[i][j]
            if(inp == 's'):
                b[5-i][5-j] = a[i][j]
            if(inp == 'a'):
                b[j][5-i] = a[i][j]
    sort(b)
    add(b)

def detranspose(a,b):
    global inp, matrix, copy
    for i in range(1,5):
        for j in range(1,5):
            if(inp == 'w'):
                a[i][j] = b[i][j]
            if(inp == 'd'):
                a[j][5-i] = b[i][j]
            if(inp == 's'):
                a[i][j] = b[5-i][5-j]
            if(inp == 'a'):
                a[5-j][i] = b[i][j]

def ask():
    ask = input("Would you like to retry? ")
    if(ask == 'yes' or ask == 'Yes'):
        retry()
    else:
        exit()


def retry():
    global matrix
    for i in range(1,5):
        for j in range(1,5):
            if(matrix[i][j] == 2 or matrix[i][j] == 4 or matrix[i][j] == 8):
                matrix[i][j] = 0
    colour()

def check():
    global matrix, counter
    counter = 0
    for i in range(1,5):
        for j in range(1,5):
            if(matrix[i][j] == 2048):
                print("\n\nYou won!\n\n")
                exit()
            if(matrix[i][j] != 0):
                if((matrix[i][j] != matrix[i-1][j]) and (matrix[i][j] != matrix[i+1][j]) and (matrix[i][j] != matrix[i][j-1]) and (matrix[i][j] != matrix[i][j+1])):
                    counter = counter + 1
    if(counter == 16):
        print("\n\nYou lost\n\n")
        #ask()
        exit()

def colour():
    for i in range(1,5):
        print("\n")
        for j in range(1,5):
            if(matrix[i][j] == 0): print("⬛",end="  ")
            if(matrix[i][j] == 2): print("🟫",end="  ")
            if(matrix[i][j] == 4): print("🟥",end="  ")
            if(matrix[i][j] == 8): print("🟨",end="  ")
            if(matrix[i][j] == 16): print("🟩",end="  ")
            if(matrix[i][j] == 32): print("🟦",end="  ")
            if(matrix[i][j] == 64): print("🟪",end="  ")
            if(matrix[i][j] == 128): print("⬜",end="  ")
            if(matrix[i][j] == 256): print("🔳",end="  ")
            if(matrix[i][j] == 512): print("👀",end="  ")
            if(matrix[i][j] == 1024): print("☢️",end="   ")
            if(matrix[i][j] == 2048): print("✨",end="  ")

def erase():
    global index
    for i in range(0,(9+index)):
        sys.stdout.write("\x1b[1A\x1b[2K") #brings the cursor back one line --> I put it in loop
    index = 0

print("\n\n")

two()
colour()

while(inp != 'n'):
    #will not add random two's if you entered something besides the given commands - otherwise infinite glitch
    if(inp == 'w' or inp == 'a' or inp == 's' or inp == 'd'):
        two()
        colour()
    check()
    asking_input()
    #will not erase the matrix if random two's were not added (AKA when w a s d commands not used)
    if (inp == 'w' or inp == 'a' or inp == 's' or inp == 'd'):
        erase()
    else:
        index = index + 1
    transpose(matrix, copy)
    detranspose(matrix, copy)