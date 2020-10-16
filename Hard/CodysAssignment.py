# problem description will be added if required

L, n = [int(i) for i in input().split()]
s = input()

for i in range(n):
  a, b = [int(j) for j in input().split()]
  g = [ord(j) for j in s[a - 1:b]]        # this list contains the ASCII values of individual characters in the range from the input
  print(chr(min(g)))                      # the problem asked for minimum lexicological value
