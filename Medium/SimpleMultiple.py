"""
Problem Statement
You are given 2 numbers N and M. You have to find the smallest number which when multiplied to N makes it a multiple of M.

Input
First line contains T, number of test cases. Each of the next T lines contains two numbers, N and M.

Output
For each test case, print the required answer.

Constraints
1 <= T <= 100 1 <= N, M <= 10^6

Sample Input
2
4 7
18 6

Sample Output

7
1
"""

import math
n = int(input())

for i in range(n):
    a = input().split()
    ar = [int(x) for x in a]
    gc = math.gcd(ar[0], ar[1])   # calculation of GCD a.k.a. HCF
    print(((ar[0] * ar[1]) // gc) // ar[0])  # GCD * LCM = product of the two numbers
