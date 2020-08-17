"""
Problem Statement
You will be given two numbers, a and b, in their binary form. You need to print their sum and their product in binary.

Input
Two strings separated by space representing the binary values of a and b.

Output
Print their sum(a+b) in the first line. Print their product(a*b) in the second line.

Constraints
1 ≤ string.length ≤ 16

Sample Input
101 10

Sample Output

111
1010
"""

n = input().split()
dec = []

for i in n:         # for converting binary to decimal and store it in a list
    num = 0
    for j in range(-1, -len(i) - 1, -1):
        if i[j] == '1':
            num += 2 ** (-j - 1)
    dec.append(num)   

summ = sum(dec)
mult = dec[0] * dec[1]

conv = [summ, mult]

for i in conv:
    print(bin(i).replace("0b",""))    # converts decimal to binary
