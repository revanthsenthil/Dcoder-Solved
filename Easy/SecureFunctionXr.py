"""
Problem Description:
Cody is learning cryptography and security.The security book starts with a mathematics based problem. Say set X is collection of elements, for example X = {1,2,3} .
Given 2 sets X and Y, We define a function f such that it maps every element of X to precisely 1 element in Y.
Example:
X = {1,2,3}
Y= {a,b,c,d}
f(1) = a , f(2) = b, f(3) = d
Let's define a function f1(x) = Xr , where x∈X Xr∈Y.
Here Xr is defined by reminder of x when divided by 7
Your task is to return Xr for a given x.

Input:
Input contains an integer x.

Output:
Print Xr.

Constraints:
1≤x≤10000

Sample Input:
35

Sample Output:
0
"""

print(int(input()) % 7)   # yeah, just one line.
