"""
Problem Description:
In mathematics and computer science, the floor and ceiling functions map a real number to the largest previous and the smallest following integer, respectively. consider a number x.
ceil(x) : Returns the smallest integer that is greater than or equal to x.
floor(x) : Returns the largest integer that is smaller than or equal to x.Given a number print ceil and floor of that number.

Input:
Each input consist of 1 real Number.

Output:
Print two integer denoting ceil and floor of the given number respectively.

Constraints:
1<=X<=100

Sample Input:
5.67

Sample Output:
6 5
"""

import math

n = float(input())
print(math.ceil(n), math.floor(n))
