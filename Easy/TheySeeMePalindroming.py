"""
Problem Description:
In india there is a puzzle"5 characters my name, reverse- forward is the same." You will be presented with a 5 character String, you have to tell whether it satisfy above puzzle, if yes output "Yes" else "No"

Input:
Input is String S of 5 characters.

Output:
Print "Yes" if the String S satisfies above constraints, else "No".

Constraints:
String length = 5

Sample Input:
level

Sample Output:
Yes
"""

a = input()
print("Yes") if a == a[::-1] else print("No")
