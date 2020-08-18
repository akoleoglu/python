 #Write a program that takes a number from the user and prints the result to check if it is a prime number.


num = int(input("Enter a number: "))
prime = False
for i in range(3,num-1):
    if num%i == 0:
        prime = False
        break
    else:
        prime = True

if num==2:
    print("Number", num, "is a prime number.")
   
elif prime==False:
     print(num,'is not a prime number.')
else:
    print("Number", num, "is a prime number.")
    


