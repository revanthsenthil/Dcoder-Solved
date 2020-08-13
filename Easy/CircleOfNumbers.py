"""
Problem Description:
All numbers in NumberLand are standing in a circle for a dancing ceremony. Every number needs a dancing partner. Dancing partner of any number is the number which is standing radially opposite to it in the circle. The numbers are from 0 to N-1. A certain number X wants to know who will be its dancing partner. Please help X.

Input:
Two positive integers denoting the value of N and X.

Output:
Print the number radially opposite to X in a circle of N numbers.

Constraints:
4 ≤ N ≤ 20
0 ≤ X < N

Sample Input:
8 2

Sample Output:
6
"""

n = input().split()

for i in range(len(n)):
    n[i] = int(n[i])

d = n.pop()
for i in range(n[0]): 
    if i != d:
        if i - d == n[0] // 2 or d - i == n[0] // 2:  # The no. selected can be bigger or smaller than the other
            print(i)

# i'm using the logic that the difference of radially opposite elemnts arranged in a circle is always equal to the integral half of the no. of elements
