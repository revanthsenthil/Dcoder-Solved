"""
Problem Statement
John has a magical chessboard. It looks like a normal chessboard except its size is N. Therefore the number of cells in the chessboard is N * N. He is interested in counting the number of squares in the chessboard. It is a very tough task for him, so he is looking for your help.

Input
First Line of the input contains an integer T denoting the number of test cases. The next T lines contain N, the size of the magic chessboard for each case.

Output
Print the number of squares in the chessboard.

Constraints
1 <= T <= 100 1 <= N <= 100

Sample Input
3
1
2
3

Sample Output

1
5
14
"""

n = int(input())

for i in range(n):
  t = int(input())
  s = 0
  for j in range(1, t+1):
    s += j ** 2
    print(s)
