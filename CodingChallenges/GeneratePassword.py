# Write a Python program that prompts the user to enter 
# his/her full name (without any spaces) and then creates 
# a secret password consisting of three letters (in lowercase)
#  randomly picked up from his/her full name, and a random 
# four-digit number. For example, if the user enters "JackClarusway", 
# a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250".

# Expected Output:
# Please enter your full name: StephenClarkson
# rto8807

# Please enter your full name: BillJames
# ils6032

# Please enter your full name: MarkJackson
# jkr7034

# Please enter your full name: CarlSmith
# iih7800

import random

fullname = input("Please enter your full name: ")
lowercase = fullname.lower()
letter3=''.join(random.choice(fullname) for i in range(3))
numbers = random.randint(1,9999)

print(letter3+str(numbers))