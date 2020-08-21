"""
Problem Description:
Cody is Professor at Zing University. He teaches English there. 
During his first class, he found the students are very talkative. 
So,he decided to divide the class into two sections, A & B such that the difference between the strength of two sections is minimum. 
Print the strength of two sections in non decreasing order.

Input:
First line of the input contains number of test cases T,followed by T integers (n) (total sum of their strengths)

Output:
For each test cases print strength of both section in non decreasing order.

Constraints:
1≤T≤100
1≤n≤10000

Sample Input:
2
10
15

Sample Output:
5 5
7 8
"""

t = int(input())

for i in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n // 2, n // 2)
    else:
        print(n // 2, (n // 2) + 1)
