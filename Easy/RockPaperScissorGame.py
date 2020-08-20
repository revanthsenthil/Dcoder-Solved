"""
Problem Description:
Glin and Rick are school friends. One day they thought to play Rock, Paper, Scissor but they don't understand the game. So the Dcoder team decided to help them playing.They need your help to show them a demo of the game, but as you Guys know Dcoder is all about programming, You have to code the game and play it with one of the engineer at Dcoder, will be represented by "Dcoder"

Input:
First Line contains the number of times game was played (n), next line contains n pairs of R ,P or S, The first letter in the pair is for player "Dcoder" and next letter is for player "You"

Output:
For each Pair output Dcoder or You in a new line, based on which player wins.In case of draw output Draw.
Winning Criteria:
The game is a draw if both players choose the same item.
Paper wins over rock because paper covers rock.
Scissors wins over paper because scissors cuts paper.
Rock wins over scissors because rock breaks scissors.

Constraints:
R represents rock, P represents paper, and S represents scissors.

Sample Input:
3
RRRSSR

Sample Output:
Draw
Dcoder
You
"""

n = int(input())
a = input()

for i in range(n):
    d = a[2 * i]
    y = a[(2 * i) + 1]
    if d == y: print("Draw")
    elif (d == "R" and y == "P") or (y == "R" and d == "S") or (y  == "S" and d == "P"): print("You")
    else: print("Dcoder")
