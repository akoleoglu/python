#This program finds the losest fibonacci number to the given number
# Limits:

# 0 <n <= 1000.

# Fibonacci numbers: 0 1 1 2 3 5 8 13 …

#Given list of 
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,1597]
number = int(input("Enter a number between 0-1000 to find closest fibonacci # : "))

for i in range(len(fibonacci)):
    if number in fibonacci:
        print(number,"is a fibonacci")
        break
    elif (fibonacci[i+1] - number) > (number-fibonacci[i]):
        print("Closest fibonacci number is",fibonacci[i])
        break
    else:
        pass