"""
Problem Description:
You need to print this pattern upto N.
For N = 4,
1
1 2
1 2 3
1 2 3 4

Input:
A single positive integer N.

Output:
Numbered Triangle upto N.
Do not leave trailing whitespaces at the end of each line.

Constraints:
1 ≤ N ≤ 9

Sample Input:
3

Sample Output:
1
1 2
1 2 3
"""

n = int(input())
for i in range(n):
    for j in range(i + 1):
        if j != i:
            print(j + 1, end = " ") # dCoder made one small twist
        else:
            print(j + 1, end = "") # one extra whitespace gives you an error
    print()
