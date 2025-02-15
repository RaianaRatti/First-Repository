import random
import numpy as np

#variables
guess = -1
counter = 0

#creating lists / arrays
number_array = np.empty([20])
guess_array = np.empty([20])
answer_array = np.empty([20])

#asking user for number of desired digits
digits = int(input("\nEnter n for n-digit number: "))

#computer will generate a random number
number = random.randint(0,10**digits)
if (number == 0):
    number == -2 #because it was not registering as correct answer when asnwer was 0

def reset_array():
    for i in range(0,(digits)):
        answer_array[i] = -1

#converting M/C generated number into a array
def number_convert():
    for i in range(0,digits):
        element = (int(number/10**(digits - 1 - i)))%10
        number_array[i] = element

#programme to ask you to guess the number
def guessing():
    global guess
    print("\n\nEnter guess: ")
    guess = int(input())
    if(guess == 0):
        guess == -2
    guess_convert()

#programme to convert your guess into array format
def guess_convert():
    for i in range(0,digits):
        element = (int(guess/10**(digits - 1 - i)))%10
        guess_array[i] = element

def check():
    #finds all greens
    for i in range(0,digits):
        if (number_array[i] == guess_array[i]):
            answer_array[i] = 2
            number_array[i] = -(number_array[i]) - 0.01
            guess_array[i] = -(guess_array[i]) - 0.01
            continue
    #finds all browns
    for i in range(0,digits):
        for j in range(0,digits):
            if(guess_array[i] == number_array[j] and answer_array[i] != 2):
                answer_array[i] = 1
                number_array[j] = -(number_array[j]) - 0.01
                guess_array[i] = -(guess_array[i]) - 0.01
    #labels the rest as red
    for i in range(0,digits):
        if(answer_array[i]<0):
            answer_array[i] = 0
    answer()

def answer():
    for i in range(0,digits):
        if (answer_array[i] == 2):
            print("🟩",end="")
        elif (answer_array[i] == 1):
            print("🟫",end="")
        elif (answer_array[i] == 0):
            print("🟥",end="")

while(guess != number):
    reset_array()
    number_convert()
    guessing()
    if(guess == -1):
        print("\n\nThe number was:",number)
        exit()
    check()
    counter = counter + 1

if(guess != -1):
    print("\n\nCongrats! You got the number!")
    print("It took you",counter,"tries!\n\n")