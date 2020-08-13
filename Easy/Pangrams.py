"""
Problem Description:
A word or a sentence is called a pangram if all the characters of this language appear in it at least once, either in lowercase or in uppercase. You are given a string S consisting of lowercase and uppercase English letters. If the string is a pangram, print "YES" else print "NO", without the double quotes.

Input:
A single string S.

Output:
Print "YES", if the string is a pangram, else print "NO".

Constraints:
1 ≤ S.length ≤ 100

Sample Input:
QuickWaftingZephyrsVexBoldJim

Sample Output:
YES
"""

string = input()
ordi = [x for x in range(65, 91)]      # ordinal values from 'A' to 'Z'
length = len(string)

lis = []
for i in range(length):
    
    if string[i].isalpha() and ord(string[i].upper()) in ordi:    # checking if alphabet is present in ordinal value list created above  
            lis.append(ord(string[i].upper()))    # upper as we need to compare with ordinal list

for x in range(26):
    if ordi[x] in lis:    
        continue
    else:
        print("NO")
        break
else:
    print("YES")
