"""
Problem Description:
There are N students in a class and Teacher want to divide these students into some groups . Teacher told  that groups consisting of two or less students not allowed , so Teacher want to have as many groups consisting of three or more students as possible.

Divide the students so that the number of groups consisting of three or more students is maximized.

Input:
Single integer N

Output:
Maximum number of groups can be formed

Constraints:
1<=N<100000

Sample Input:
6

Sample Output:
2
"""

n = int(input())
print(n // 3)

# the simple logic here is that how many ever groups are present, there is no limit to the no. of students in one group.
# Hence, the last group can have more than 3 too.
# We use the // operator to check for max condition
