"palindrome number"

n=list(input("enter list"))
len(n)
def pali_no(n):
    pal= False
    for i in range(len(n)):
        if n[i]==n[-i-1]:
            pal=True
        else:
            pal=False
    if pal==True:
        return 'pal'
    else:
        return 'not pal'
print(pali_no(n))
