"""
Problem Description:
Cody is stuck in a problem and needs your help to get out of trouble. He was given a sorted array by his teacher. After his teacher left, he mistakenly rearranged some elements of the array. Help Cody sort the array before his teacher arrives.

Input:
The first line of input contains N, the number of elements in the array A. The second line of input contains N space separated integers.

Output:
Print the sorted array.

Constraints:
3 ≤ N ≤ 50
-1000 ≤ A[i] ≤ 1000

Sample Input:
5
8 4 12 2 10

Sample Output:
12 10 8 4 2
"""

n = int(input())
x = input().split()
f = [int(i) for i in x]
f.sort()

for i in f[::-1]:     # descending order
    print(i, end = " ")
