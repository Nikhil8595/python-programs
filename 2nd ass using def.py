n=input("enter the number:")
def arm(n):
    l = len(n)
    sum1 = 0
    for i in n:
        sum1 = sum1 + int(i) ** l
    if sum1 == (int(n)):
        return "the number is armstrong number"
    else:
        return "the number is not armstrong number"
print(arm(n))