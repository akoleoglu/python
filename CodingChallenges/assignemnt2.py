# Write a program that;

# Finds out the most frequent number in the given list.
# Calculates its frequency.
# Prints out the result such as :


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3 , 3 , 1, 10 , 3, 7]
new_numbers = []
count = 0
value = []
for i in range(len(numbers)):
    new_numbers.append(numbers.count(numbers[i]))
    if numbers.count(numbers[i]) >= count:
        count=numbers.count(numbers[i])
        value.append(numbers[i])
repeat_times=max(new_numbers)
most_freq_num =max(value)

print(f"The most frequent number is {most_freq_num} and it was {repeat_times} times repeated ")

