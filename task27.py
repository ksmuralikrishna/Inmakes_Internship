'''Task 27
To write a program in python find the second smallest and third largest number in a list.'''

numbers = [4, 8, 1, 9, 3, 7, 5]

for i in range(len(numbers)):
    current = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[current]:
            current = j
    numbers[i], numbers[current] = numbers[current], numbers[i]

print("Sorted :", numbers)


print("Sorted list" , numbers)
list_2 = [("second smallest number", numbers[1]),("3rd largest number", numbers[-3]) ]
print(list_2)
