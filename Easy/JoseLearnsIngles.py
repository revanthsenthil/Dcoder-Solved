"""
Problem Description:
José is from South America and hence, Spanish is his mother tongue. He wants to travel around the world and, therefore, decides to learn various languages, starting with English. He tries to learn the alphabetical order.. You being a good teacher will help him in doing so. He said he would learn just by asking questions. You have to answer his questions. You will be given few characters. You need to arrange them in alphabetical order and print them.
NOTE: Do not mind the case. (example : 'D' will come after 'a' in alphabetical order)

Input:
First line of input is N, the number of characters.
Next line contains N space-separated characters.

Output:
Print the characters in ascending form

Constraints:
1 ≤ N ≤ 26
It is guaranteed that no character will be repeated.

Sample Input:
4
D c a M

Sample Output:
a c D M
"""

n = int(input())
a = input().split()

for i in range(n):      # bubble sort
    for j in range(n - i - 1):
        if a[j].lower() > a[j + 1].lower():   #don't mind the case...
            a[j], a[j + 1] = a[j + 1], a[j]
            
for i in range(n):
    print(a[i], end = " ")
