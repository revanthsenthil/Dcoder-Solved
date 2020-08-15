"""
Problem Description:
Cody loves even numbers. He was bored and decided to print all the even numbers at the even indexes of an array(1-indexed). He wants your help to complete this task.

Input:
The first line of the input contains an integer N denoting the size of an array.
The second line contains N-space separated integers denoting the array.

Output:
Print all the numbers separated by space which satisfies the condition.

Constraints:
1<=N<=10^3.
1<=Array Elements<=10^5.

Sample Input:
6
2 3 5 4 7 8

Sample Output:
4 8
"""

n = int(input())

a = input().split()
ar = [int(x) for x in a]

for i in range(n):
    if i % 2 != 0 and ar[i] % 2 == 0:       # index starts from 0, hence the odd no. index would be the even index
        print(ar[i], end = " ")
