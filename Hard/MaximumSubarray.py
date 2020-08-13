"""
Problem Description:
Given an array of integers, find out and print the maximum sub-array of non-negative numbers. The sub-array should be continuous. Sub-array A is greater than subarray B if sum(A) > sum(B). And in case if the sum of two subarrays A and B is same, print the subarray with more number of elements.

Input:
First line contains N, the number of elements.
The next line contains N space-separated elements representing the elements of array A.

Output:
Print the maximum sub-array.

Constraints:
1 ≤ N ≤ 100
-1000 ≤ A[i] ≤ 1000

Sample Input:
5
2 7 9 -5 12 3

Sample Output:
2 7 9
"""

n = int(input())
a = input().split()

a = [int(a[i]) for i in range(n)]   # converting to integer values

longli = []
for i in range(n):
    li = []   # logic: create nested lists that contain continuous positive or 0 elements and then check for max length
    for j in range(i, n):
        if a[j] >= 0:
            li.append(a[j])
        else:
            break     # if the element is negative, exit that loop and move on to next element
        longli.append(li)

maxi = []
for i in range(len(longli)):    # storing max length element (a list) as a new variable to print its elements later
    if len(longli[i]) > len(maxi):
        maxi = longli[i]

for i in maxi:
    print(i, end = " ")
