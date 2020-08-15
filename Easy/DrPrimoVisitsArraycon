"""
Problem Statement
Dr. Primo is a famous mathematician in Codeland. He is known to have numbers as his friends. He is especially in love with Prime Numbers. He goes to the city festival ArrayCon. Every time he is given an array, he tells how many prime numbers are present in the array in few seconds. You will be given an array filled with positive integers, print the response of Dr. Primo, i.e, print how many prime numbers exist in the array.

Input
First line contains N, the size of the array A. Next line contains N space separated integers.

Output
Print the number of prime numbers in the array

Constraints
1 ≤ N ≤ 1000 1 ≤ A[i] ≤ 10^8

Sample Input
5
1 2 3 4 5

Sample Output

3
"""

n = int(input())
counter = 0

a = input().split()
ar = [int(x) for x in a]
    
for j in ar:

    if j == 2:    # 2 is the only even prime
        counter += 1
        continue
    elif j == 1:      # 1 is neither prime nor composite
        continue
    else:
        for k in range(2, j):
            if j % k == 0:  # composite
                break
        else:
                counter += 1
    
print(counter)
