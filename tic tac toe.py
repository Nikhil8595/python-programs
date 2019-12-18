p1=int(input("Player1 name:"))
p2=int(input("Player2 name:"))
count1=0
x=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
y=[]

def display():
    print('{}' + '|' + '{}' + '|' + '{}').format(x[0], x[1], x[2])
    print('________')
    print('{}' + '|' + '{}' + '|' + '{}').format(x[3], x[4], x[5])
    print('________')
    print('{}' + '|' + '{}' + '|' + '{}').format(x[6], x[7], x[8])
    print('________')
    for i in range(4):
        x.pop(p1-1)
        x.insert(p1-1,'x')
display()

