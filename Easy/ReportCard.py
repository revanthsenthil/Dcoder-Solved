"""
Problem Description:
Priyanka is Professor at Zing University. Help the professor in assigning grades to her students.
The mean score of three subjects is to graded into 'A', 'B', 'C' or 'D' or 'F' depending upon the marks scored.
For the score >90 and score =<100, 'A' is graded.
For score >80 and score =<90, 'B' is graded.
For the score >70 and score <=80, 'C' is graded.
For the score >60 and score <=70, 'D' is graded.
For the score =< 60 'F' is graded.

Input:
Input contains the marks obtained by student in 3 subjects separated by a space.

Output:
Output should be the grade scored by the student.

Constraints:
0 ≤ Marks obtained in each subject ≤ 100

Sample Input:
100 75 54

Sample Output:
C
"""

n = input().split()

for i in range(len(n)):
    n[i] = int(n[i])
    
mean = sum(n) // len(n)
if 100 >= mean > 90:
    print("A")
elif 90 >= mean > 80:
    print("B")
elif 80 >= mean > 70:
    print("C")
elif 70 >= mean > 60:
    print("D")
else:
    print("F")
