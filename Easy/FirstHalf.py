"""
Problem Description:
Given a string return its first half.Assume string to have even number of characters.

Input:
Input contains a string

Output:
Print the first half of string.

Constraints:
0≤string length≤100

Sample Input:
Dcoder

Sample Output:
Dco
"""

n = input()
print(n[:len(n)//2])
