'''Task 13 Find Keys with Maximum Value
Write a Python function that takes a dictionary of items and their prices as input 
and finds and prints the keys (items) with the highest prices.'''



def dictfun(userDict):
    maxPrice = max(userDict.values())
    for key, value in userDict.items():
        if maxPrice == value:
            return key

userDict = {}
n = int(input("How many items you want in the dictionary: "))
for i in range(n):
    key = input("Enter Key element: ")
    value = input("Enter value: ")
    userDict[key] = value
print("user inputed dictionary is\n",userDict)

print("The key with max price is = ", dictfun(userDict))
