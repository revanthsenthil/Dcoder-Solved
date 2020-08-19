"""
Problem Description:
Cody always wanted to have some psychic powers so that he could showoff his skills, and magic to people and impress them, specially his girlfriend.But, in spite all his efforts, hardwork, dedication, Googling, watching youtube videos he couldn't garner any psychic abilities!
He knew everyone was making fun of him, so to stop all of that - he came up with a smart plan. Anyone who came to him to know about their future, he asked them to write a binary number for him - and then, he smartly told them if the future for that person had good in store, or bad.The trick Cody used was if the binary number has six consecutive 0's or 1's their future is bad, else their Future is Good.

Input:
Input contains a single line a binary number n

Output:
Print "Good" or "Bad" without quotes (for fututre prediction) based on Cody's trick

Constraints:
0≤n≤10000
"""

n = input()

print("Bad") if "000000" in n or "111111" in n else print("Good")
