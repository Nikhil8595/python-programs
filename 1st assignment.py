"""Add and remove items from set,while checking if present then remove"""

x={"apple","banana","ashish k"}
print("banana" in x)
x.add("nikhil")
print(x)
#x.pop()
x.update(["sanket","ashish more","bandukbazz"])
print(x)
print(len(x))
x.remove("banana")
print(x)



