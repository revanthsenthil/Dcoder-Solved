"""
Problem Statement
Cody is preparing for a programming competition. He needs k more members for his team to be eligible for the competition. 
So he organizes a coding test for all his juniors to select the best group. His teacher has instructed him to only select students with consecutive roll numbers. 
Cody wants to know the total score of the k members selected. Cody is in a hurry and needs your help. 
You are given the list of marks of N juniors in ascending order of their roll numbers,i.e., the ith number represents the marks of the student with roll no. 'i'. 
Find k consecutive students with highest total of marks and output the sum of marks of those k students.

Input
The first line contains N, the number of juniors, and k, the number of students needed. The second line contains N integers separated by space.

Output
Print the highest total among any k consecutive students.

Constraints
1 ≤ k ≤ n ≤ 10000 -1000 ≤ marks ≤ 1000

Sample Input
4 3
2 1 3 4

Sample Output

8
"""

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

if n == k: print(sum(a))
else:
    sums = []
    for i in range(n - k + 1):
        sums.append(sum(a[i : i + k]))      # find sum of k consecutive elements, append them onto a list and print max of the list
    print(max(sums))
