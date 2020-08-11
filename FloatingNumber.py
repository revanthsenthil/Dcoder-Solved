"""
Floating Number
Problem Description:
Bob has a floating point number N. He wants to set the precision for 2 digits after the decimal point for the number.
He is not good at coding, hence looking for your help.

Input:
The first line contains T, the number of test cases.
Next T line contains floating point number N.

Output:
Print N in a separate line after setting precision for 2 digits after the decimal point:

Constraints:
1 <= T <= 1000
1 <= N <= 10000

Sample Input:
1
713.166

Sample Output:
713.17
"""
n = int(input())
for i in range(n):
    a = float(input())
    print(format(a, '.2f'))
