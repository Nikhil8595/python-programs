def main():
    p1='x'
    p2='o'
    p1 = input("Enter the Player1 name:")
    p2 = input("Enter the Player2 name:")
    x2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    x22=[]
    count_x=0
    count_o=0
    for i in range(4):
        player1= int(input('Enter p1:'))
        while player1 in x22:
            print('space already occupied please enter again:')
            player1=int(input())
        x22.append(player1)
        count_x+=1
        i_val=player1-1
        x2.pop(i_val)
        x2.insert(i_val,'x')
        display(x2)
        if count_x>=3:
            result = check(x2,'x')
            if result == 1:
                print(p1 + " wins")
                break
        player2 = int(input('Enter p2:'))
        while player2 in x22:
            print('space already occupied please enter again:')
            player2 = int(input())
        x22.append(player2)
        count_o += 1
        i_val = player2 - 1
        x2.pop(i_val)
        x2.insert(i_val,'o')
        display(x2)
        if count_o >= 3:  # or count_x>=3:
            result = check(x2, 'o')
            if result == 1:
                print(p2 + " wins")
                break
    else:
        print('match tie')
def display(x2):
    print(" {} | {}  | {} ".format(x2[0], x2[1], x2[2]))
    print("------------")
    print(" {} | {}  | {} ".format(x2[3], x2[4], x2[5]))
    print("------------")
    print(" {} | {}  | {} ".format(x2[6], x2[7], x2[8]))
    print("------------")
def check(x4,x_o):

    if x4[0]==x_o and x4[1]==x_o and x4[2]==x_o:
        return 1
    elif x4[3]==x_o and x4[4]==x_o and x4[5]==x_o:
        return 1
    elif x4[6]==x_o and x4[7]==x_o and x4[8]==x_o:
        return 1
    elif x4[0] ==x_o and x4[3]==x_o and x4[6]==x_o:
        return 1
    elif x4[1] ==x_o and x4[4]==x_o and  x4[7]==x_o:
        return 1
    elif x4[2] == x_o and x4[5]==x_o and x4[8]==x_o:
        return 1
    elif x4[0] ==x_o and x4[4]==x_o and x4[8]==x_o :
        return 1
    elif x4[2] ==x_o and x4[4]==x_o and x4[6]==x_o:
        return 1
    else:
        return 0
main()
