"""
Problem Description:
Cody is now in 1st standard, he is learning tables. Help him printing table of n.

Input:
Input containts n, an integer.

Output:
Print Table of n.

Constraints:
1≤n≤10000

Sample Input:
2

Sample Output:
2
4
6
8
10
12
14
16
18
20
"""

n = int(input())

for i in range(1, 11):
    print(n * i)
