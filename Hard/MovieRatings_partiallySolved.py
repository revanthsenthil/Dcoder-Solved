# Will include problem description later, if necessary

a, b = [int(i) for i in input().split()]
rate = []

for i in range(a):
  mov = input()
  rating = float(mov[-3:])
  movie = mov[:-4]
  rate.append([movie, rating])
 
for i in range(a):
  for j in range(a - i - 1):
    if rate[j][1] < rate[j + 1][1]:
      rate[j], rate[j + 1] = rate[j + 1], rate[j]
      
for i in rate[::b]:
  print(i[0], i[1])
  
