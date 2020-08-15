"""
Problem Statement
Cody's teacher taught him the concept of arrays. She gave different types of homework for all the students so they won't able to copy. Cody has to find the largest gap between any two elements in the array. As Cody has a date with his girlfriend he asks your help to complete his homework.

Input
The first line of the input consists of single integer N denoting the array size. The second line consists of N-space separated integer denoting the array elements.

Output
Print the largest gap present in the array. Explanation for sample Input: Here, we can see largest gap can be found between 3 and 10 which is 7

Constraints
2<=N<=10^3 .1<=Array elements<=10^4.

Sample Input
4
3 10 6 7

Sample Output

7
"""

n = int(input())

a = input().split()
ar = [int(x) for x in a]

print(max(ar) - min(ar))
