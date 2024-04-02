'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

# k = 0
# n = int(input("Enter the limit: "))
# for i in range(1, 5+1):
#     for j in range(i):
#         k = k+1
#         print(f"{k}", end=' ')
#     print()

'''
    *
   ***
  *****
 *******
'''
# n = 4
# for i in range(n):
#     print(" "*(n-i)+"*"*((2*i)+1))

'''
*
**
***
****
****
***
**
*

'''
# n = 4
# for i in range(n+1):
#     print("*"*i)
# for i in range(n,0,-1):
#     print("*"*i)


'''

'''

n = 6
for i in range(n, 0, -1):
    for j in range(i-1, n):
        print(j+1, end=' ')
    print()