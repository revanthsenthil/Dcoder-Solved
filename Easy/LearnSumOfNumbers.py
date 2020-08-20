"""
Problem Description:
Given 2 natural numbers, find sum of them.

Input:
Two natural numbers n1 and n2 separated by a space.

Output:
Sum of the numbers

Constraints:
1<=n1<=1000
1<=n2<=1000

Sample Input:
2 5

Sample Output:
7
"""

a = [int(x) for x in input().split()]
print(sum(a))
