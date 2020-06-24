"""
Problem Description:
Zack has messed up all his shoes. He has N shoes(single shoe, not paired). 
You have to search for the partner of each shoe. Find the maximum pair you can make out of them.
You will be given description of each shoe, the size of the shoe and if it is Left shoe(L) or Right shoe(R). 
Two shoes can be paired if they are having same size and , one is L and other is R.

Input:
First line contains single integer 'N', number of shoes
Next N lines has description for each shoe, with space separated | size and L/R

Output:
Single integer, maximum pairs can be made out of the given shoes

Constraints:
1<=N<=1000
shoe size will be a positive integer less than 100

Sample Input:
5
1 L
3 L
1 R
2 R
2 L

Sample Output:
2

"""

l = ex = wy = []
n = int(input())
c = 0

for i in range(n):
    x, y = input().split()
    x = int(x)
    t = [x, y]
    ex.append(x)
    wy.append(y)
    l.append(t) #nested list containing each of the inputs

for i in range(n):
    for j in range(n):
        if ex[i] == ex[j] and wy[i] != wy[j]:
            l.remove([ex[i],wy[i]])
            l.remove([ex[j],wy[j]])
            c+= 1
            
print(c)
