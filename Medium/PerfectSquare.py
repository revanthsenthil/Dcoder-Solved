"""
Problem Description:
Cody was once understanding numbers, their squares and perfect squares from his teacher.
A perfect square is a number that can be expressed as square of an integer. 
To check how much Cody understood the concept his teacher kept a test. He has to find the nearest perfect square of the given number N.

Input:
The first line of input consists of a single integer T denoting the number of test cases.
The first line of each test case consists of single integer N.

Output:
For each test case print the nearest perfect square.

Constraints:
1<=T<=100.
1<=N<=10^4.

Sample Input:
2
1602
2

Sample Output:
40
1
"""

t = int(input())

for i in range(t):
    n = int(input())
    l = []
    boo = True
    i = 1
    while boo:
        i += 1
        if i ** 2 <= n:
            l.append(i)
            
        else:
            l.append(i)
            boo = False
        
    if n == 2 or n == 1: print(1)
    elif l[-2] == n: print(n)
    else: 
        if len(l) >= 3:
            print(l[-1]) if l[-1] ** 2 - n <= n - l[-2] ** 2 else print(l[-2])
