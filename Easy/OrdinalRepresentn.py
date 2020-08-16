"""
Problem Description:
Numbers can be represented in cardinal form or ordinal form.
Cardinal Form : 1, 2, 3, 4, 5, 6, etc.
Ordinal Form : 1st, 2nd, 3rd, 4th, 5th, 6th, etc.
You will be given cardinal form of a digit. You have to print its ordinal form.

Input:
A single digit positive digit.

Output:
Print the ordinal from of the digit.

Constraints:
1 ≤ N ≤ 9

Sample Input:
3

Sample Output:
3rd
"""

n = int(input())
if n == 1: print("1st")
elif n == 2: print("2nd")
elif n == 3: print("3rd")
else: print(str(n) + "th")
