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

n = int(input())
shoe, left, right = [], [], []      # creating lists to compare corresponding indices
counts = 0              # for counting the required number of pairs

for i in range(n):
    a, b = input().split()
    a = int(a)
    if a in shoe:       # if the shoe size is already present, we add the count in either the left or right list
        if b == "L":
            left[shoe.index(a)] += 1
        elif b == "R":
            right[shoe.index(a)] += 1
    else:               # if the shoe size appears for the first time while parsing the loop, we add a new element in each list for comparision
        shoe.append(a)
        left.append(0)
        right.append(0)
        if b == "L":
            left[shoe.index(a)] += 1
        elif b == "R":
            right[shoe.index(a)] += 1
            
for i in range(len(shoe)):
    if left[i] != 0 and right[i] != 0:          # if either R or L for a given size is not present, then we don't consider it as a pair can't be formed
        lists = [left[i], right[i]]
        counts += min(lists)                    # we take minimum of the right and left value as that represents the no. of complete pairs
    
print(counts)  
