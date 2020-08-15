"""
Problem Description:
Ron is weak in mathematics.Knowing this fact John challenges him to find the sum of first and last digit of a given number. Help Ron to find the sum of first and last digit of a number.

Input:
The first line contains an integer T denoting total number of test cases.
Then in the following T lines, each line contains an integer N.

Output:
For each test case, print the sum of first and last digit of N.

Constraints:
1<=T<=100.
10<=N<=100000.

Sample Input:
3
1234
85694
234

Sample Output:
5
12
6
"""

n = int(input())

for i in range(n):
    a = input()
    first = int(a[0])
    last = int(a[-1])
    print(first + last)
