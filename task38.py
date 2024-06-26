'''Task 38 
Write a program to create an iterator to print English alphabets from A to Z.'''

class AlphIter:
    def __init__(self):
        self.current = ord('A')

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= ord('Z'):
            result = chr(self.current)
            self.current += 1 
            return result
        else:
            raise StopIteration

alphabets = AlphIter()

i = iter(alphabets)

for alphabet in i:
    print(alphabet)

