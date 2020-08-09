"""
Problem Statement
You will be given a single string and two positive integers denoting indices. You need to change the case of the characters at those indices,i.e change uppercase to lowercase and lowercase to uppercase. It is guaranteed that all characters in the string are alphabets.

Input
The first line contains N, the length of string. The next line contains a single string. Two integers, x and y, in next line separated by space.

Output
Print the string after altering the case of characters at those indices

Constraints
1 ≤ string.length ≤ 40 0 ≤ x,y ≤ string.length

Sample Input
6
Dcoder
0 3

Sample Output

dcoDer
"""

n = int(input())
string = input()
a = input().split()

for i in range(len(a)):
  a[i] = int(a[i])
  
s = ""

for i in range(n):
  if i in a:
    if string[i].islower():
      s += string[i].upper()
    elif string[i].isupper():
      s += string.lower()
  else:
    s += string[i]
    
print(s)
