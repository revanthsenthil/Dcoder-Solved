"""
Problem Description:
A happy string is a string in which each character is lexicographically greater than its next character. You are given a positive integer N as an input. You need to print the smallest lexicographical string possible of length N.
NOTE: All characters in a happy string are in lowercase.

Input:
A single integer N.

Output:
Print the lexicographically smallest string of length N.

Constraints:
1 ≤ N ≤ 26

Sample Input:
2

Sample Output:
ba
"""

n = int(input())

# we make use of the fact that the ordinal value in ASCII for 'a' is 97
k, string = 97, ""
for i in range(n):
    string += str(chr(k))
    k += 1

# the string is actually in ascending order as we increased the value of k each time, so we need to print its reverse
print(string[::-1])   
