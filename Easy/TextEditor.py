"""
Problem Description:
John has created a text editor, which has lots of features but he forgot to add the conversion of Lowercase alphabet to an Uppercase Alphabet. He asks you for help to complete this task for him.

Input:
The first line of input consists of single integer T denoting the number of test cases.
Then in the following T lines, each line has a String s of lowercase alphabet.

Output:
For each test case print the uppercase of given string.

Constraints:
1<=T<=100.
1<=String Length<=10^2.

Sample Input:
2
dcoder
john

Sample Output:
DCODER
JOHN
"""

n = int(input())

for i in range(n):
    s = input()
    if s.isalpha():
        print(s.upper())
