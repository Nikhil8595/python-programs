"""Create a program that will play the game of cow and bull,write a function
that takes input from user (4 digit number) and play until the user guess
the correct number """
n1=int(input("Enter the number:"))
import random
value=random.randint(1000,9999)
print(value)
def cow_bull(n1):
    for i in range(0,4):
        if n1[i]==value[i]:
            print("cow")
    else:
            print("bull")
cow_bull(n1)

