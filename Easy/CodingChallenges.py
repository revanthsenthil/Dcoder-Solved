"""
Problem Description:
There are n participants appearing for one on one coding challenge.Each participant plays twice (challenges) with each of his opponents.You need to compute the total number of challenges.

Input:
First line contains an integer n, represent number of participants.

Output:
Print the total number of challenges.

Constraints:
1≤n≤100

Sample Input:
16

Sample Output:
240
"""

n = int(input())
print(n * (n - 1)) # n * (n-1) // 2 would give the total no. of games in one round and * 2 as there are two rounds
