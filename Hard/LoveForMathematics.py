"""
Problem Description:
Students of Dcoder school love Mathematics. They love to read a variety of Mathematics books. To make sure they remain happy,their Mathematics teacher decided to get more books for them.
A student would become happy if there are at least X Mathematics books in the class and not more than Y books because they know "All work and no play makes Jack a dull boy".The teacher wants to buy a minimum number of books to make the maximum number of students happy.

Input:
The first line of input contains an integer N indicating the number of students in the class. This is followed up by N lines where every line contains two integers X and Y respectively.

Output:
Output two space-separated integers that denote the minimum number of mathematics books required and the maximum number of happy students.
Explanation:
The teacher could buy 5 books and keep student 1, 2, 4 and 5 happy.

Constraints:
1<=N<=10000
1<=X,Y<=10^9

Sample Input:
5
3 6
1 6
7 11
2 15
5 8

Sample Output:
5 4
"""

n = int(input())
l, mi, ma = [], [], []

for i in range(n):
    x, y = input().split()
    mi.append(int(x))
    ma.append(int(y))
    
mi.sort()
ma.sort()

happy_result = 1
happy_stu = 1
books = mi[0]

i = 1
j = 0
while (i < n and j < n):
    if mi[i] <= ma[j]:
        happy_stu += 1
        i += 1
    elif mi[i] > ma[j]:
        happy_stu -= 1
        j += 1
    if happy_stu > happy_result:
        happy_result = happy_stu
        books = mi[i - 1]

print(books, happy_result)
