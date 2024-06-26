'''Task 46 
Write a function in python to count the number of lines 
from a text file "story.txt" which is not starting with an alphabet "T".'''

def lineCount():
    file = open("story.txt","r")
    xount = 0
    count = 0
    for line in file:
        xount += 1
        if line[0] not in 'T':
            count+= 1
    file.close()
    print("total number of lines=", xount)
    print("No of lines not starting with T=",count)

lineCount()