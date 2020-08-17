"""
Problem Description:
Jimmy wants to buy books for N students. He went to the bookshop to buy a bundle of books, each bundle has a different number of books. He wants to buy such a bundle that contains the number of books, which can be distributed equally amongst all the students.

Input:
First line contains T, number of test cases.
Each test case contains two integers, N and M. where is N is number of students and M is number of books in a bundle.

Output:
In each test case output "Yes" if he can buy that bundle and "No" if he can't buy that bundle.

Constraints:
1<=T<=20
1<=N<=100
1<=M<=10^5

Sample Input:
2
5 14
3 21

Sample Output:
No
Yes
"""

n = int(input())

for i in range(n):
    d = input().split()
    print("Yes") if int(d[1]) % int(d[0]) == 0 else print("No")
