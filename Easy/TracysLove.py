"""
Problem Description:
Hey, my name is Tracy.I am 4 year old and love the number 6.I want to play a number game with you, I'll give you two numbers and you just need to tell whether their sum or difference can be the number I love,6.

Input:
Input contains 2 integers a, b separated by a space character.

Output:
Print "Love" if the condition described met else "Hate" without quotes

Constraints:
0≤a,b≤10

Sample Input:
2 8

Sample Output:
Love
"""

n = input().split()
n = [int(x) for x in n]

print("Love") if max(n) - min(n) == 6 or sum(n) == 6 else print("Hate")
