# Python Program to Count the Number of Digits in a Number

num=int(input("Enter the number :"))

count=0

while(num>0):
    count+=1
    num=num//10

print("Number of Digits in number : ",count)