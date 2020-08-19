"""
Problem Description:
You are given a linked list, you just need to reverse its order without changing any pointer, ie print the tail first and head last.

Input:
Input contains elements of linked list separated by space and terminated by -1

Output:
Print reversed linked list.

Constraints:
0≤element of list≤100

Sample Input:
1 2 3 4 -1

Sample Output:
4 3 2 1
"""

n = input().split()
a = [int(x) for x in n[::-1]]

for i in a:           # -1 is the first element after reversal and that is not included while printing
    print(i, end = " ")
