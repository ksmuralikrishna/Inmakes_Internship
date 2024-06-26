'''Task 40
Write a Python program to sort a list of tuples using Lambda. 
Original list of tuples: [('English', 88), ('Science', 90), 
('Maths', 97), ('Social sciences', 82)]'''



original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]


sorted_list = sorted(original_list, key=lambda x: x[1])


print("Sorted list of tuples:", sorted_list)