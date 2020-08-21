"""
Problem Description:
Compute the sum of squares for the given numbers: a, a+1, ..., b-1, b.

Input:
Two natural numbers a and b separated by a space.

Output:
Computed sum: a*a + (a+1)*(a+1) + ... + (b-1)*(b-1) + b*b

Constraints:
1 <= a <= b <=100

Sample Input:
2 4

Sample Output:
29
"""

a, b = [int(x) for x in input().split()]
s = 0
for i in range(a, b + 1):
    s += i ** 2
print(s)
