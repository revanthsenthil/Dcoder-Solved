"""
Problem Description:
Draw the pattern specified using loops.

Input:

Output:
The pattern as shown in sample output.
First line contain 4 space and 1 star, next line contains 3 space and 3 stars and so on..

Constraints:
Try not to hardcode the output.

Sample Input:

Sample Output:
    *
   ***
  *****
 *******
*********
"""

for i in range(5):
    print(" " * (4 - i), end = "")
    print("*" * ((2 * i) + 1))
