import numpy as np

array = np.empty([100])

#inputting values into the array
n = int(input("Enter number of elements: "))
print("Enter the elements: \n")

for i in range(0,n):
    element = int(input())
    array[i] = element

#printing the original array
print("The original array is: ")

for i in range(0,n):
    if(i<n-1):
       print(int(array[i]),end=", ")
    else:
       print(int(array[i]),end="")

print("\n\nThe sorted array is: ")

#BUBBLE SORT
for k in range(0,n):
    for m in range(0,n-1):
        if(array[m] > array[m+1]):
            [array[m],array[m+1]] = [array[m+1],array[m]]

#printing the array
for i in range(0,n):
    if(i<n-1):
        print(int(array[i]),end=", ")
    else:
        print(int(array[i]),end="")