"""
Which Century is it?

Lestrade has been teaching his kids about centuries. He told them that
they are currently living in the 21st century. Over the next few days,
the kids kept coming to him with a year and asked him which century does
it belong to. This keeps Lestrade very distracted from his work. 
Help Lestrade by writing a code that does Lestrade's work for him.
You will be given a year, print the century it belongs to in its ordinal form
(19th, 20th, 21st, etc.)

Input
One positive integer representing the year

Sample Input
2010

Output
print the century the year belongs to in its ordinal value

Sample Output
21st

Constraints
year is between 1 and 3000, both included

"""

special = {"1":"st", "2":"nd", "3":"rd"}
n = int(input())

if n % 100 != 0:
  century = str((n // 100) + 1)
  
else:
  century = str(n // 100)
  
#else:
  #century = "1"

if century[-1] in "123":
  print(century + special[century[-1]])
  
else:
  print(century + "th") 
