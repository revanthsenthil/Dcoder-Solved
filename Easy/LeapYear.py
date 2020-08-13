"""
Problem Description:
Steve is playing a quiz game with his brother John. As Steve just learned the concept of leap year, John wanted to test his knowledge. For that, John started to ask Steve whether a year is a leap year or not by giving him a random year. Steve is little confused and he asks your help to the quiz.

Input:
The first line of input contains one integer T.
Next T lines will have years given by John.

Output:
For each test case print "Yes" if it is a leap year else "No".

Constraints:
1<=T<=100.
10^3<=Year<=10^5.

Sample Input:
2
2000
2017

Sample Output:
Yes
No
"""

n = int(input())

for i in range(n):
    a = int(input())
    if a % 400 == 0:    #multiples of 400 are leap years
        print("Yes")
    elif a % 100 == 0:  #multiples of 100 that aren't multiples of 400 aren't leap years
        print("No")
    elif a % 4 == 0:    #multiples of 4 are leap years
        print("Yes")
    else:
        print("No")
