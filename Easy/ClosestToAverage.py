"""
Problem Description:
You are given an array, you have to find the closest integer to its average, look it has to be closest,not just the truncated version of the average.

Input:
First line contains n , number of elements of array, next line contains n integer separated by a space, which are elements of the array.

Output:
Print output according to given condition.See Sample output.

Constraints:
1≤n≤100
1≤ element of array ≤ 1000

Sample Input:
2
10 15

Sample Output:
12
"""

n = int(input())
a = input().split()
an = [int(x) for x in a]

s = sum(an)
if s % n == 0:
    print(s // n)
elif s / n - s // n > 0.5:      # Dcoder took 0.5 to be rounded off to 0 for decimal -> integer and that took me a while to figure out
    print((s // n) + 1)
else:
    print(s // n)
