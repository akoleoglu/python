# A librarian wants to sort books depending on their complexity. 
# To be able to do this, he/she has to read through all the books in the library. 
# Since this would take months, he/she asks you to perform the task using python. 
# He/she wants you to measure the average length of a book and provide the needed detail.
# 
# Once you complete the program, you are going to test the program by comparing 
# excerpts from Hemingway and Charles Dickens. Hemingway is known for his short 
# sentences and simple sentences. On the other hand, Charles Dickens is known for 
# his long and complex sentences.

# Write a program that reads a file and understand whether the author is Hemingway 
# or Charles Dickens. Your program should report when it opens and closes files. It 
# should also print the average length of the sentences in order (text1,text2).
#  Finally, it should prompt a message indicating the owners of the excerpts. 
# The text1.txt and text2.txt files are provided within the folder.

# To find the average length of a sentence, count the number of words, sum them up and divide the total amount to the number of sentences.

# Expected Output:
# text1.txt is opened
# text1.txt is closed
# text2.txt is opened
# text2.txt is closed
# (7, 36)
# ('The first text belongs to ', 'Hemingway', ' and the second one belongs to ', 'Charles Dickens', '.')

author1 = 'Hemingway'
author2 = 'Charles Dickens'
text_1 = 'The first text belongs to'
text_2 = 'The second one belongs to'
with open('/Users/ahmetkoleoglu/Desktop/github/working-on-it/python-code-challenges/FindTheAuthor/text1.txt','r') as file:
    print("text1.txt is opened")
    text1 = file.read()

    avr_text1 = round(len(text1.split())/text1.count('.'))

    print("text1.txt is closed")

with open('/Users/ahmetkoleoglu/Desktop/github/working-on-it/python-code-challenges/FindTheAuthor/text2.txt','r') as file:
    print("text2.txt is opened")
    text2 = file.read()

    avr_text2 = round(len(text2.split())/text2.count('.'))

    print("text2.txt is closed")

print('('+str(avr_text1)+', '+str(avr_text2)+')')

if avr_text1 < avr_text2:
    print(text_1,author1,'and',text_2,author2,'.')
else:
    print(text_2,author1,'and',text_1,author2,'.')




