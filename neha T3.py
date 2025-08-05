# Task 1
f=int(input("enter the number:"))

def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial (n-1))
r=factorial(f)
print(f"factorial of {f} is:" ,r)


#Task 2
import math
a=int(input("enter the number:"))
print(f"square root  is: {a ** (1/2)} ")
print(f"logarithm is: {math.log(a)}")
print(f"sine is : {math.sin(a)}")


