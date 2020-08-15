"""
Problem Statement
You will be given a group of words. You need to print all unique words in that group in descending order of their frequency, i.e the word repeated most number of times will come first. In case of two words having the same frequency, the word listed earlier in the group will be printed first.

Input
First line contains N, the number of words. Next line contains N space-separated words.

Output
Print the words in descending order of their frequency

Constraints
1 ≤ N ≤ 20 1 ≤ word[i].length ≤ 40

Sample Input
12
can you can a can as a canner can can a can

Sample Output

can a you as canner
"""

n = int(input())
a = input().split()
lis_element = []
lis_value = []

for i in a:
    if i in lis_element:
        lis_value[lis_element.index(i)] += 1
    else:
        lis_element.append(i)
        lis_value.append(1)
        
lis_new = list(sorted(tuple(lis_value)))[::-1]
for i in lis_new:
    if i in lis_value:
        print(lis_element[lis_value.index(i)], end = " ")
        lis_element.pop(lis_value.index(i))
        lis_value.remove(i)
