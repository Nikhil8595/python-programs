x=int(input('enter no.'))
x_box=x//2+1
low=0
high=x-1
n=1
x_list=[['-' for i in range(x)] for j in range(x)]
#print(x_list)
for j in range(x_box):


    for i in range(low,high+1):
        x_list[low][i]=n
        n=n+1
    for i in range(low+1,high+1):
        x_list[i][high]=n
        n+=1

    for i in range(high-1,low-1,-1):
        x_list[high][i]=n
        n+=1
    for i in range(high-1,low,-1):
        x_list[i][low]=n
        n+=1

    low=low+1
    high=high-1

for i in range(x):
    for j in range(x):
        print(x_list[i][j],end="\t")
    print()