'''Task 5 Reverse a List
Write a Python function that takes a list and returns a new list 
with the elements reversed. Do this without using the built-in reverse method.'''

l = []
def list_reverse(l):
    l_reversed = []
    for i in l:
        l_reversed = l[::-1]
    return l_reversed


n = int(input("How many elements you want in list? \n"))
for i in range(n):
    l.append(input("Enter the element: "))
print(list_reverse(l))