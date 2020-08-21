"""
Problem Description:
Given two binary strings, A (of length 10) and B (of length 5), output 1 if B is a substring of A and 0 otherwise.

Input:
Binary string A and B separated by a space.

Output:
The logical value of: 'B is a substring of A'.
ie. 1 if B is substring of A else 0.

Constraints:

Sample Input:
1010110010 10110

Sample Output:
1
"""

a = input().split()
print(int(a[1] in a[0]))      # True and False have int values 1 and 0 respectively
