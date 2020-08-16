"""
Problem Description:
Dcoder Team is working on an exciting new update in the app, but before releasing it to the public, our team has decided to test the app out on small percentage of users. This is known as the Beta Test. For a user to be eligible for a Beta Test, his android version must be greater or equal to version V. You will be given a string X denoting the android version of user. Tell us whether he is eligible for the Beta Test or not by printing "Yes" or "No", without the double quotes.

Input:
Two strings, V and X.
V : minimum android version required for Beta Test
X : user's android version

Output:
"Yes" or "No"

Constraints:
1 ≤ V.length, X.length ≤ 6
(The versions would have no more than 2 integer parts, i.e, only one '.' )

Sample Input:
3.02 4.10

Sample Output:
Yes
"""

n = input().split()
n = [float(x) for x in n]
if n[1] >= n[0]: print("Yes")
else: print("No")
