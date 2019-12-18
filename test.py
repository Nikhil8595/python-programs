n=str(input("enter"))
l=len(n)
s=0
for i in n:
    s=s+int(i)**l
    if s==int(n):
        print("arm")

