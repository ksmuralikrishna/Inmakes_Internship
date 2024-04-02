'''Task 10 Calculate Average Age
Write a Python program that takes a list of person tuples (name, age) and calculates and prints the average age of the group.'''



persons = (['abi',30], ['Subi',25], ['Ebi', 28])
age = 0
for i in persons:
    age = age + i[1]
avg_age = age/len(persons)
print("Average age of the group is ", avg_age)   