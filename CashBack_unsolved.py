"""
Problem Description:
Joel wants to buy N items. He came to know that for each item there is a cash back of some amount. The i th item will have cost Ci dollar and cash back of Xi dollar. Initially, Joel has M dollars. Find the minimum value of M, that Joel must have initially, so Joel can buy all the N items.
Note: Joel can buy items in any order.

Input:
The first line will contain N, the number of items Joel has to buy. Next, N lines will have two space-separated integers Ci and Xi, representing the cost of the item and cashback Joel will get respectively for ith Item.

Output:
Output a single integer M that is the minimum dollars Joel requires initially.

Constraints:
1 <= N,Ci,Xi <=10^5

Sample Input:
2
1 1
2 1

Sample Output:
2
"""

# THIS CODE IS NOT RIGHT YET

n = int(input())
mx = []
plus_minus = []

for i in range(n):
    a = input().split()
    x, y = a
    x, y = int(x), int(y)
    plus_minus.append([x, y])
    
k = 0

def minval(sta):
    global k
    k = start
    for i in range(n):
        if i == (n - 1) and sta >= 0:
            if (sta - plus_minus[n - 1][0] < 0):
                k += (plus_minus[n - 1][0] - sta)
                sta += (plus_minus[n - 1][0] - sta)
                break
        else:
            sta -= plus_minus[i][0]
            if sta < 0:
                k += 1
                sta += 1
                minval(sta)
            else:
                sta += plus_minus[i][1]
                
    return k
                
start = plus_minus[0][0]

s = minval(start)

print(s)
