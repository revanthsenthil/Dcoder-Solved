# problem description can be added if required

n = int(input())
hou = [int(i) for i in input().split()]
p = int(input())

for i in range(p):
  a, b = [int(i) for i in input().split()]
  print(sum(hou[a - 1:b]))      # sum was to be including both the 'a'th and 'b'th index
