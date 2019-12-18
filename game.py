"""rock paper sicssor"""

print('enter \n r for rock \n s for scissor\n p for paper\n')
x=input('player1:')
y=input('player2:')
a='rsp'
b='spr'
for i in range(3):
    if x==a[i] and y==b[i]:
        print('player1 wins')
    elif y==a[i] and x==b[i]:
        print('player2 wins')
    elif x==y:
        print('tie')
        break
