"""
Problem Description:
Cody has a sequence of characters N. He likes a sequence if it contains his favourite sequence as a substring.
Given the sequence and his favourite sequence F, check whether the favourite sequence is present in the sequence.

Input:
The first line of input contains a single line T, which represents the number of test cases.
Each test case consists of 2 strings separated by space N and F respectively.

Output:
Print "Yes" if the sequence contains the favorite sequence in it, otherwise print "No".

Constraints:
1<=T<=10.
1<=|N|,|F|<=100.
All the characters are lowercase alphabets.

Sample Input:
2
abcde abc
pqrst pr

Sample Output:
Yes
No
"""
n = int(input())

for i in range(n):
    a = input().split()
    if a[1] in a[0]:
        print("Yes")
    else:
        print("No")
