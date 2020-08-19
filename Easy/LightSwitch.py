"""
Problem Description:
There is a light bulb on the stairs, which has two switches. The light turns on if and only if one of them is on(binary 1) and other is off(binary 0).You are given combinations of these switch find whether the bulb glow or not?

Input:
Two bits a and b separated by space, each representing a switch position,(0=off , 1=on)

Output:
Print 1 if bulb will turn on else print 0.

Constraints:
a=b=0/1

Sample Input:
1 1

Sample Output:
0
"""

a = input().split()
print(0) if a[0] == a[1] else print(1) 
