"""
Problem Description:
A Power Number is a positive number that can be expressed as x^x, i.e. x raise to the power of x, where x is any positive number. You will be given an integer array A and you need to print if the elements of array A are Power Numbers or not.

Input:
First line contains N, a positive integer.
Next line contain N space-separated integers.

Output:
For every integer, print 'Yes' if its a power number, else print 'No'. These outputs must be separated by space.

Constraints:
1 ≤ N ≤ 100
1 ≤ A[i] ≤ 10^16

Sample Input:
3
1 3 4

Sample Output:
Yes No Yes
""" 

n = int(input())
a = input().split()     #space separated input is converted to list containing elements as strings

for i in range(n):      #converting all input strings in list to integers
    a[i] = int(a[i]) 
    for j in range(1, a[i] + 1):    #checking condition
        if a[i] == pow(j, j):
            print("Yes", end = ' ')
            break       #if one satisfies, then exit the inner loop
    else:
        print("No", end = ' ')
