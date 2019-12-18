"""Write a function that takes parameter integer returns true if
armstrong number or false if no"""

n=str(input("enter the number:"))
l=len(n)
sum1=0
for i in n:
    sum1=sum1+int(i)**l
if sum1==(int(n)):
    print("the number is armstrong number")
else:
    print("the number is not armstrong number")



