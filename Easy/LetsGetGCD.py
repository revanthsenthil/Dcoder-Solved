"""
Problem Description:
Cody was doing his maths homework, suddenly he found a GCD(Greatest Comman divisor) problem. He is very lazy to do all the calculations for this exercise, so he just took his mobile and opened the Dcoder App, decided to code a program to find solution to GCD problem. You have to help him making this program, where you are presented with 2 integers, and you have to find their Greatest Comman Divisor.
The HCF or GCD of two integers is the largest integer that can exactly divide both numbers (without a remainder).

Input:
Input contains 2 integers n1 and n2 separated by a newline.

Output:
Print the GCD of n1 and n2

Constraints:
1≤n1,n2≤1000

Sample Input:
54
24

Sample Output:
6
"""

import math

m = int(input())
n = int(input())

print(math.gcd(m,n))
