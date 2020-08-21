"""
Problem Description:
Cody was solving a programming puzzle in Dcoder, and as always he is unable to do it alone.
Puzzle statement is You are given three integers l,h,d and you have to find that how many integers between l and h (inclusive) are divisible by d.Lets help Cody.

Input:
Input contains 3 integers l,h and d respectively separated by a space.

Output:
Print the number of divisors as stated in the problem.

Constraints:
1≤l,h,d≤1000

Sample Input:
3 15 5

Sample Output:
3
"""

l, h, d = [int(x) for x in input().split()]
c = 0
for i in range(l, h + 1):
    if i % d == 0: c += 1
print(c)
