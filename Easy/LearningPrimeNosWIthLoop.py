"""
Problem Description:
Raja Beta is bad at maths, his teacher always complaints about him.Help him in his prime numbers homework.

Input:
Two space separated positive integer m and n

Output:
Print all prime numbers p such that m <= p <= n, one number per line

Constraints:
1 <= m <= n <= 1000000000

Sample Input:
1 10

Sample Output:
2
3
5
7
"""

n = input().split()
x, y = [int(h) for h in n]

for i in range(x, y + 1):
    if i == 2:
        print(2)
    
    elif i > 2:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            print(i)
