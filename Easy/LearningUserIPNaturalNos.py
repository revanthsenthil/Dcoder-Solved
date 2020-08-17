"""
Problem Description:
The numbers 1,2,3.. are known as Natural numbers. Calculate the sum of all the natural numbers from 1 to N, where N will be the input.

Input:
A positive integer N

Output:
Output will be sum of numbers from 1 to N

Constraints:
1<N<1000

Sample Input:
5

Sample Output:
15
"""

n = int(input())
print((n * (n + 1)) // 2)
