"""
Problem Statement
John loves gardening. He believes that for good growth of the plant, the land should be quadrilateral. Given angles of 4 sides of the land. Find whether the land is a valid quadrilateral or not. A quadrilateral is valid if the sum of all four angles is equal to 360 degrees.

Input
The first line contains an integer T, total number of test cases. The next T lines, each, contain four angles A, B, C and D of a quadrilateral separated by space.

Output
Print "YES" if the quadrilateral is valid, else print "NO", without the double quotes.

Constraints
1 ≤ T ≤ 100 1 ≤ A,B,C and D ≤ 360

Sample Input
2
90 90 90 90
180 180 45 55

Sample Output

YES
NO
"""

n = int(input())

for i in range(n):
    a = input().split()
    ar = [int(x) for x in a]
    if sum(ar) == 360:
        print("YES")
    else:
        print("NO")
