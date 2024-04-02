'''Task 6 Remove Duplicates from a List 
Create a Python function that takes a list 
as input and removes duplicate elements, 
preserving the order of the elements. Return the new list.'''

l = []
def string_duplicate(l):
    count = []
    for i in l:
        if i in count:
            pass
        else:
            count.append(i)
        
    return count
n = int(input("How many items do you want in the list? \n"))
for i in range(n):
    l.append(input("Enter the items: "))

print("the list after removing duplicates : ", string_duplicate(l))


