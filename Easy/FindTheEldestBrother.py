"""
Problem Description:
There are 5 brothers in a family, you need to tell eldest brother's age. You are given age of all the brothers.

Input:
Input contains 5 numbers separated by space indicating the ages of 5 brothers.

Output:
Print the age of eldest brother.

Constraints:
1≤age≤100

Sample Input:
6 3 24 12 22

Sample Output:
24
"""

n = input().split()

n =[int(x) for x in n]
print(max(n))
