# problem description will be added if necessary

n = int(input())

for i in range(n):
  a, b = [int(i) for i in input().split()]
  s = 0
  
  for i in range(1, a + 1):
    k = 0
    binary = str(bin(i))[2:]
    for i in range(len(binary) - 2):
      if binary[i:i + 3] == "101":
        k += 1
    if k >= b:
      s += 1
  print(s)
