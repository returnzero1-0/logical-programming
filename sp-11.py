# Python Program to Find the Smallest Divisor of an Integer

num=int(input("Enter the number :"))

small_divisor=[]

for i in range(2,num+1):
    if(num%i==0):
        small_divisor.append(i)

small_divisor.sort(reverse=False)

print("Smallest Divisor is : ",small_divisor[0])