"""
Problem Statement
The Jones Trucking Company tracks the location of each of its trucks on a grid similar to an (x, y) plane. The home office is at location (0, 0). Read the coordinates of truck A and the coordinates of truck B and determine which is closer to the office.

Input
Input contains 4 space separated integers, first 2 are x,y for truck A, next are x,y for truck B.

Output
Output will be either A or B, bases on which one is closer to home office.

Constraints
The x-coordinate is in the range –20 .. 20. The y-coordinate is in the range –20 .. 20

Sample Input
3 -2 -5 -3

Sample Output

A
"""

n = input().split()
x1, y1 = int(n[0]), int(n[1])
x2, y2 = int(n[2]), int(n[3])

one = ((x1 - 0) ** 2) + ((y1 - 0) ** 2)   # distance formulas
two = ((x2 - 0) ** 2) + ((y2 - 0) ** 2)

print("A") if one < two else print("B")
