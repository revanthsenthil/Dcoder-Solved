# problem description will be added if required

L, n = [int(i) for i in input().split()]
s = input()

for i in range(n):
  a, b = [int(j) for j in input().split()]
  g = [ord(j) for j in s[a - 1:b]]
  print(chr(min(g)))
