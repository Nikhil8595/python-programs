
def arm(x):
    l=len(x)
    count1=0
    for i in x:
        count1=count1+int(i)**l
    if count1==l:
        print("armstrong number")
    else:
        print("not arm")
arm('532')