a=int(input("enter the number:"))
if a % 2==0:
   print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")

#Task 2
total_sum=0
for x in range(1, 51):
    total_sum += x
print(f"the sum of integers from 1 to 50 is: {total_sum} ")