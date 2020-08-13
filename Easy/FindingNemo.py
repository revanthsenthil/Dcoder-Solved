"""
Problem Statement
Nemo is a little kid in Word-World who always gets mixed in a group of other words and gets lost. Marlin and Coral (Nemo's parents) are quite desperate and called you for help every time Nemo got lost. You helped for the first few times but got irritated when you were called upon again and again. So write an algorithm that would do your work for you. You will be given a group of words. You need to find 'Nemo' among these words and print its position.

Input
First line contains N, the number of words. The next line contains N space-separated words.

Output
Print the position of the word 'Nemo' in the group.

Constraints
1 ≤ N ≤ 1000 1 ≤ word.length ≤ 50

Sample Input
6
This is a Nemo sample input

Sample Output

4
"""

n = int(input())
g = input()
h = g.split()

for i in h:
  if i == "Nemo":
    print(h.index(i) + 1)
