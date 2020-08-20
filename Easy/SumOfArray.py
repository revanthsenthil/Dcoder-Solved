"""
Problem Description:
Given the array of N numbers, you have to find its sum.

Input:
The first line contains an integer N, number of elements in array.Next line contains N integers separated by space.

Output:
Print the sum of the array's elements.

Constraints:
1<=N<=100

Sample Input:
6
1 2 3 4 10 12

Sample Output:
32
"""

n = int(input())      # this line doesn't even matter for this code, but part of the input
a = input().split()
aa = [int(x) for x in a]
print(sum(aa))
