'''Task 14 
Convert two lists into a dictionary in Python without using a built-in method.'''


n = int(input("Enter the Number of items should be in the list\n"))
userList1 = []
userList2 = []
for i in range(n):
    userList1.append(input(f"Enter the item {i+1} in list 1 : "))
    userList2.append(input(f"Enter the item {i+1} in list 2 : "))
print("List 1 \n", userList1)
print("List 2 \n", userList2)

resultDict = {}
for i in range(len(userList1)):
    resultDict[userList1[i]] = userList2[i]
print("Result : ", resultDict)