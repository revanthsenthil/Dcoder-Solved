"""
Problem Description:
Garry and Sharry are colleague, assuming they work at Dcoder. 
They are our Problem Setters.One day we decide to judge their work. 
Both were given an assignment to make some problems to display at Dcoder, 
and they were awarded points based on clarity, originality and difficulty of the problem. 
You have to tell us who performed better in the assignment and what's the difference of their points acquired.

Input:
The first line contains 3 space separated integers, describing the points acquired by Garry, next line contains 3 space separated integers, describing the points acquired by Sharry.

Output:
Print who performed better and by how much points, separated by a space.
In case of draw, print None and 0,separated by space.

Constraints:
Points, on a scale of 1 to 10.

Sample Input:
4 6 3
5 6 1

Sample Output:
Garry 1
"""

G = sum([int(x) for x in input().split()])
S = sum([int(x) for x in input().split()])
if G == S:
    print(None, 0)
else:
    print("Garry", G - S) if G > S else print("Sharry", S - G)
