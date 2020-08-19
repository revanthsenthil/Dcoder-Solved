"""
Problem Description:
You are given with a String, you have to output count of vowels in the String.

Input:
Input contains a String.

Output:
Print vowel count in the String.

Constraints:
1≤String lenght≤1000

Sample Input:
Dcoder,A mobile coding platform

Sample Output:
10
"""

n = input()
c = 0
for i in n:
    if i in "AEIOUaeiou":
        c += 1
print(c)
