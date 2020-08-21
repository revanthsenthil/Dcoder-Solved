"""
Problem Description:
Glin was doing his maths homework , Rick came to his house. As Glin is week at Maths, Rick decided to help him in his homework. 
They both stuck at a problem of Right Angle Triangle. You have to help them both in this problem.
Input is a String, You have to process it and design a Right angle triangle as explained later.

Input:
Input is a String of characters, The right angle triangle is designed as explained through sample example.

Output:
Print 1 character in firstline, then 2 characters in next line and so on, to design a Right Angle Triangle like Structure.

Constraints:
Lenght of input String <= 20

Sample Input:
Dcoder

Sample Output:
D
Dc
Dco
Dcod
Dcode
Dcoder
"""

a =  input()
for i in range(len(a)):
    print(a[:i + 1])
