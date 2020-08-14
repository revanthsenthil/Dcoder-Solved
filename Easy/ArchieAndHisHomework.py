"""
Problem Description:
Archie was given a homework by his teacher. He is given a fraction and he needs to write it in its reduced form. Archie is not good at Maths. Help Archie finish his homework.

Input:
2 integers separated by space denoting the numerator and denominator respectively.

Output:
Print the reduced form of the fraction

Constraints:
1 ≤ N ≤ D ≤ 1000

Sample Input:
20 40

Sample Output:
1 2
"""

from math import gcd

a = input().split()
x, y = [int(x) for x in a]
g = gcd(x, y)

print(x // g, y // g)
