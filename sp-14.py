# Python Program to Print all Integers that Aren’t Divisible by Either 2 or 3 and Lie between 1 and 50.

start_range=int(input("Enter start range :"))
end_range=int(input("Enter end range :"))

for i in range(start_range,end_range+1):
    if(i%2!=0 & i%3!=0):
        print(i)
