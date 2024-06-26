'''Task 45 
Write a Python program to calculate the sum of the positive and 
negative numbers of a given list of numbers using the lambda function'''

nums = [1, 2, 3, 4, -1, -2, -3, -4]
print("Original list:", nums)
total_negative_nums = list(filter(lambda nums: nums < 0, nums))
total_positive_nums = list(filter(lambda nums: nums > 0, nums))
print("Sum of the negative numbers: ", sum(total_negative_nums))
print("Sum of the positive numbers: ", sum(total_positive_nums))