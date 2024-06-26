'''Task 47 
Write a function in Python to count words in 
a text file those are ending with alphabet "e".'''

def countWords():
    file = open("task47.txt","r")
    count = 0
    data = file.read()
    print("The data in the file is :-", data)
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count+=1
    print("No of words ends with 'e' is :-", count)
    file.close()

countWords()