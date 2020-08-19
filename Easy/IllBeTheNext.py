"""
Problem Description:
You are given a string, you have to convert each letter in the string with the next one.For example a becomes b and C becomes D.

Input:
Input contains a string s.

Output:
Print the manipulated string according to the problem.

Constraints:
1≤length of string≤100

Sample Input:
Dcoder

Sample Output:
Edpefs
"""

a, s = input(), ""
for i in a:
    s += chr(ord(i) + 1)
    
print(s)
