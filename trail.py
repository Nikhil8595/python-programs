def main():
    import random
    y=str(random.randint(1000,9999))
    x=(input('enter the number:'))
    check(x,y)
def check(x,y):
    for i in range(0,4):
        if x==y:
            print("cow"*4)
            print("You Win")
            break
        if x[i]== y[i]:
            print('cow',end=' ')
        else:
            print('bull',end=' ')

    print('\n enter 1 to play again enter 0 to exit ')
    z=int(input())
    if z==1:
        main()
    else:
        return
main()
