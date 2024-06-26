'''Task 34
You are developing a class called MathUtils that provides various mathematical
utility functions. Implement a static method called calculateSum() in the
MathUtils class. The calculateSum() method should accept an array of numbers
and return the sum of those numbers.
Write the MathUtils class with the static calculateSum() method and provide
code to test the functionality.'''

class MathUtils:
    @staticmethod
    def calculateSum(numbers):
        return sum(numbers)

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = MathUtils.calculateSum(numbers)
print("Sum of numbers:", sum_of_numbers)  
