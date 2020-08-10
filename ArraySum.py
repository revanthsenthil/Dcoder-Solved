"""
Problem Description:
You are given an integer array and you have to find the sum of the elements of the array and find the remainder when the sum is divided by the largest number of the array.

Input:
First line contains N, the number of elements. Next line contains N space separated integers (elements of the array).

Output:
Print the remainder when sum is divided by the maximum element.

Constraints:
1 ≤ n ≤ 100
0 ≤ A[i] ≤ 1000

Sample Input:
5
1 2 3 4 5

Sample Output:
0
"""

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

print(sum(a) % max(a))
