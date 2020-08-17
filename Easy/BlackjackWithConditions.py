"""
Problem Description:
Write a program to play a variety of BlackJack. In general, given two numbers, a and b, return their sum.
If the sum is greater than 21, return 0, unless one of the numbers is 11. In such a case, the 11 should be 'converted' to a 1 to prevent the sum from being exceeded.
For example, given a 11 and 13 as input, the 11 should be 'converted' into a 1 so the total sum will be 14.

Input:
Input contains 2 space separated integers, a and b

Output:
Output will be in general sum of a and b, if sum exceed 21, return 0, unless one of the numbers is 11. In such a case, the 11 should be 'converted' to a 1 to prevent the sum from being exceeded.
For example, given a 11 and 13 as input, the 11 should be 'converted' into a 1 so the total sum will be 14.

Constraints:
0<=a<50
0<=b<50

Sample Input:
11 13

Sample Output:
14
"""

n = input().split()
x, y = [int(x) for x in n]

if x == 11:
    x = 1
elif y == 11:
    y = 1

print(x + y) if x + y <= 21 else print(0)
