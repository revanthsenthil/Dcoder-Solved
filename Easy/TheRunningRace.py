"""
Problem Description:
Alex and Ryan are having a running competition between themselves. They have to cover a distance of D meter. The speed of Alex and Ryan are X meter/second and Y meter/second respectively. Help the judge by telling him who will win the competition.

Input:
Input consists of a single line, contains 3 integers D, X and Y .

Output:
Print "Alex" if Alex wins, print "Ryan" if Ryan wins. If it is a draw print "Draw".

Constraints:
1<=D,X,Y<=100

Sample Input:
10 2 3

Sample Output:
Ryan
"""

n = input().split()
n = [int(x) for x in n]
if n[1] == n[2]: print("Draw")
elif n[1] > n[2]: print("Alex") 
else: print("Ryan")
