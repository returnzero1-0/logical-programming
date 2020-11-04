# Python Program to Print Odd Numbers Within a Given Range


start_num=int(input("Enter the starting number :"))
end_number=int(input("Enter the ending number :"))

for i in range(start_num,end_number+1):
    if(i%2!=0):
        print(i)