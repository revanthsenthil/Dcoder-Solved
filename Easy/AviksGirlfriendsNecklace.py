"""
Problem Description:
Avik's Girlfriend is a Sorted Girl and she is also a Coder and loves arrays. So on her birthday Avik decided to gift her a necklace of pearls, now these pearls have numbers printed on them. When he bought the necklace its pearls were in sorted order, as his girlfriend likes, but while he was showing it to her on the day of birthday, it fell down and all the pearls scattered. Seeing this his girlfriend started crying, so he promised her that he will correct this. Now Avik dont know sorting, your job is to sort these peaarls so that he could make the necklace back and make his girlfriend happy.

Input:
First line conains N, no. of element/pearls , next line contains N integer separated by space, to be sorted.

Output:
print the sorted integers.

Constraints:
1<=N<=100
PS: Try improving your algorithm by using a more efficient sort algo.

Sample Input:
5
1 5 7 3 4

Sample Output:
1 3 4 5 7
"""

n = int(input())      # we don't require this for this algo
a = [int(x) for x in input().split()]
a.sort()
for i in a:
    print(i, end = " ")
