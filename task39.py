'''Task 39 
Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals.'''
class NumIterator:
    def __init__(self):
        self.current = 1.0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 10:
            result = self.current
            self.current += 0.5
            return result
        else:
            raise StopIteration
numbers = NumIterator()

i = iter(numbers)

for number in i:
    print(number)

