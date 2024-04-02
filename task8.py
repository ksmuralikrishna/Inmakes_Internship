'''Task 8 Count the Occurrences of an Element
Write a Python function that takes a list and an element as input and counts how many times that element appears in the list.'''



l = []
def count_items(n, l):
    count = 0
    for i in l:
        if n == i:
            count += 1
    return count

input1 = input("Enter the list items(use space to separate items)\n")
l = input1.split()
n = input("Enter the item to be searched\n")

print(n, "appears", count_items(n, l), "times in the list" )