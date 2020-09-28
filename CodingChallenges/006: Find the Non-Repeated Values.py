products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]


count = 0
unique = []
for i in range(len(products)):
    count = products.count(products[i])
    if count == 1:
        unique.append(products[i])
for i in unique:
    print(i)
    
