# python
# write program to remove the duplicates in a list

numbers = [1, 3, 5, 6, 6, 8, 1, 1, 4, 4, 4, 7, 7]
 
for number in numbers:
    counting = numbers.count(number)
    if counting > 1:
        numbers.remove(number)

print(numbers)
