"""
Problem Description:
The problem is simple, you are given a word. You need to remove the repeating characters.

Input:
Input contains a word w.

Output:
Print the output according to the problem explained.

Constraints:
1≤w length≤100

Sample Input:
AaabBbbc

Sample Output:
AabBc
"""

a = input()
b = ""
for i in a:
    if i not in b: b += i
        
print(b)
