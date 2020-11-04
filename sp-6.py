#Python Program to Print all Numbers in a Range Divisible by a Given Number

start_num=int(input("Enter the starting number :"))
end_number=int(input("Enter the ending number :"))

divisor=int(input("Enter the number to divide range of numbers :"))

for i in range(start_num,end_number+1):
   
    if(i%divisor==0):
        print(i," is divisible by ",divisor)
