# In this coding challenge, you are going to write a program that takes a 
# string and checks if it contains consecutive vowels or not. 
# It should give Positive as an output if it contains consecutive vowels and Negative otherwise.
#  For example saetqi string contains a adjacent to e, which means that it contains consecutive vowels.
#  So it should give Positive as an output. On the other hand, if you take the string of statoqag,
#  the output should be Negative.

# Expected Output:
# Please enter a string: gasdph
# Negative

# Please enter a string: aiou
# Positive

# Please enter a string: taoum
# Positive

# Please enter a string: a
# Negative


#import regular expressions
import re
word = input("Please enter a string: ")
# Check if the word has two consecutive wovels or not
if(re.findall(r"[aeiou]{2,}",word)):
    print("Positive")
else:
    print("Negative")