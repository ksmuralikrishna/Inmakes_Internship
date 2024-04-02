'''Task 9 Count the Occurrences of an Element
Write a Python function that takes a tuple and an element as input and counts how many times that element appears in the tuple.'''

t = ()
def count_items(n, t):
    count = 0
    for i in t:
        if n == i:
            count += 1
    return count

input1 = input("Enter the tuple items(use space to separate items)\n")
input1 = input1.split()
l = list(t)
for i in input1:
    l.append(i)
t = tuple(l)
n = input("Enter the item to be searched\n")

print(n, "appears", count_items(n, t), "times in the tuple" )
print(type(t))