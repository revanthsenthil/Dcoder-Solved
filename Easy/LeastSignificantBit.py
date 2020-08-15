"""
Problem Description:
In mathematics and digital electronics, a binary number is a number expressed in the base-2 numeric system or binary numeric system, which uses only two symbols: typically 0 (zero) and 1 (one). The least significant bit (LSB), is the lowest bit in a series of numbers in binary. The LSB is located at the far right of a binary string. For example, in the binary number: 00111001, the least significant bit is the far right -> 1. John wants to know whether the given numbers has LSB equal to 1 or not.

Input:
The first line of input contains a single integer T denoting the number of test cases.
Each test case will have one integer A.

Output:
For each test case, print "Yes" if LSB is equal to 1 else print "No", without the double quotes.

Constraints:
1 ≤ T ≤ 100
1 ≤ A ≤ 1000

Sample Input:
2
2
1

Sample Output:
No
Yes
"""

n = int(input())

for i in range(n):
    a = int(input())
    if a % 2 != 0:        # the last bit stands for a value of 1. Hence, all odd numbers satisfy the given condition
        print("Yes")
    else:
        print("No")
