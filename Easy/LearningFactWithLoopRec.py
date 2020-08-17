"""
Problem Description:
If n is an integer greater than 0, n factorial (n!) is the product: n* (n-1) * (n-2) * ( n-3)… *
By convention, 0! = 1.
Write a Program to compute n Factorial(n!), where n is input.

Input:
n is a positive integer

Output:
Output will be n factorial(n!)

Constraints:
0<=n<=12

Sample Input:
4

Sample Output:
24
"""

n = int(input())
f = 1
for i in range(1, n + 1):
    f *= i
print(f)
