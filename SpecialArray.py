"""
Problem Description:
Natural numbers are the set of positive integers, which ranges from 1 to infinity excluding fractional part. Natural numbers are whole numbers excluding zero. Zero is the only whole number which is not a natural number. An array is special if all the elements are natural numbers. Find whether the given array is special or not.

Input:
The first line of input contains a single integer N denoting the array size.
The second line of input contains N-space separated integers denoting the array.

Output:
Print "Yes" if the array is special else print "No".

Constraints:
1<=N<=100.
0<=Arrays elements<=100.

Sample Input:
4
0 1 2 3

Sample Output:
No
"""

n = int(input())
a = input().split()
a_int = [int(x) for x in a]
if all(a_int):      # all() returns boolean value False if even one element is 0 or False or has an equivalent bool value
    print("Yes")
else:
    print("No")
