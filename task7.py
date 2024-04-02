'''Task 7 Find Common Elements
Create a Python program that takes two lists and returns a new list containing elements that are common in both input lists.'''

l1 = []
l2 = []
l3 = []



def com_element_list(l1, l2):
    for i in l1:
        if i in l2:
            l3.append(i)

    return l3


input_string1 = input("Enter the items of List 1(use space to separate items)\n")
input_string2 = input("Enter the items of List 2(use space to separate items)\n")

l1 = input_string1.split()

l2 = input_string2.split()

print("common elements are ->", com_element_list(l1, l2))