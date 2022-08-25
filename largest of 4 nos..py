#to find largest of four entered numbers

a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
c= int(input("Enter number 3:"))
d= int(input("Enter number 4:"))

if a>b and a>c and a>d:
    print("The largest number is:", a)
if b>a and b>c and b>d:
    print("The largest number is:", b)
if c>a and c>b and c>d:
    print("The largest number is:", c)
if d>a and d>b and d>c:
    print("The largest number is:", d)
