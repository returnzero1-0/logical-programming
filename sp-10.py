# Python Program to Find the Sum of Digits in a Number

print("Way 1")
number=int(input("Enter the number :"))

l1=[]
while number>0:
    digit=number%10
    l1.append(digit)
    number=number//10

print("sum of  digit in a number is ",sum(l1))



print("Way 2 ")
number=int(input("Enter the number :"))

total=0

while number>0:
    digit=number%10
    total=total+digit
    number=number//10

print("sum of  digit in a number is ",total)