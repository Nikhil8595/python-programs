"""Create a program that will play the game of cow and bull,write a function
that takes input from user (4 digit number) and play until the user guess
the correct number """
import random
def main():
    x=input("enter the value:")
    y=str(random.randint(1000,9999))
    print('comp:',y)
    check(x,y)
def check(x,y):
    for i in range(0,4):
        if x==y:
            print('cow'*4)
            print('you win')
            break
        if x[i]==y[i]:
            print("cow",end=' ')
        else:
            print("bull",end=' ')
    print('\nenter 1 to play again 0 to exit')
    z=int(input())
    if z==1:
        main()
    else:
        return
main()
