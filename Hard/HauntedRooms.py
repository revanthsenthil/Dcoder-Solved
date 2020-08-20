"""
Problem Statement
Students of Cambridge University went for a Hack-a-thon in Massachusetts. They decided to stay there overnight. 
So they all went in a hotel named Hawthorne Hotel. The hotel is represented here by a rectangular matrix of rooms. 
Matrix cell value contains the cost of that room. Some of the rooms in the hotel are available for free (cost=0). 
Upon further investigation by the President Nicole, he got to know that the rooms are for free because they are haunted. 
So, being responsible for the safety of all the team members, he decided not to book the rooms if it satisfies any of the below conditions: 
1] Room is haunted 
2] Rooms below a haunted room in same column 
These rooms are unsafe!
Help Nicole to calculate the total price of all the suitable safe rooms for the team.

Input
[2 Dimensional array] The first line contains a positive integer N(number of rows) and M(number of columns) Each of the next N lines contains M space separated integers denoting a row of the matrix. Each element of the matrix represent the cost of that room.

Output
Single integer denoting the sum of the cost of all the safe rooms

Constraints
1 ≤ matrix.length ≤ 5 1 ≤ matrix[i].length ≤ 5 0 ≤ matrix[i][j] ≤ 10

Sample Input
3 4
0 1 1 0
0 5 0 2
2 0 3 3

Sample Output

7
"""

x, y = [int(x) for x in input().split()]
rows = []
s = 0

for i in range(x):
    a = [int(x) for x in input().split()]
    rows.append(a)

haunted = []        # use this list to add all y indices of haunted rooms for 2nd condition

for i in range(x):
    for j in range(y):
        if rows[i][j] == 0:
            haunted.append(j)     # appending the value of y in haunted so the following iterations that contain this y will not be included in final sum
        elif j in haunted:        # when the following iteration happens, the element will be below the previous row
            continue
        else:
            s += rows[i][j]
        
print(s) 
