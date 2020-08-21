"""
Problem Description:
There are 3 numbers given as input sort them in increasing order.

Input:
Three space separated positive integer m,n,p

Output:
Print the integers in sorted incresing order separated by space.

Constraints:
0<=m<=500
0<=n<=500
0<=p<=500
Try not using any library function to sort.

Sample Input:
4 86 56

Sample Output:
4 56 86
"""

a, b, c = [int(x) for x in input().split()]

if a < b and a <= c: print(a, b, c) if b <= c else print(a, c, b)
elif b < a and b < c: print(b, a, c) if a <= c else print(b, c, a)
else: print(c, a, b) if a < b else print(c, b, a)
