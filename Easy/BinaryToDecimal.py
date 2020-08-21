"""
Problem Description:
Write a code which converts a binary number (written as string) into a decimal number.

Input:
Input is a binary number.

Output:
The output is a decimal number.(interger value)

Constraints:
The binary number is non-negative and the resultant decimal number is an integer.

Sample Input:
101

Sample Output:
5
"""

n, s = input()[::-1], 0

for i in range(len(n)):
    if n[i] == '1': s += 2 ** i 
    
print(s)
