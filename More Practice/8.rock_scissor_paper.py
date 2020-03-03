# -*- coding: utf-8 -*-
"""
THIS IS ROCK PAPER SCISSOR GAME

WHERE
ROCK BEATS SCISSOR
SCISSOR BEATS PAPER
PAPER BEATS ROCK

Created on Sun Jun 23 21:42:12 2019

@author: Abirmoy

"""

def win_check(u1, u2):
    if u1==u2:
        print("\nIt's a tie!")
    elif u1=='r' and u2 == 's':
        print("\nRock wins!")
    elif u1=='r' and u2=='p':
        print("\nPaper wins!")
    elif u1=='s' and u2== 'p':
        print("\nScissor wins!")
    elif u1=='s' and u2 == 'r':
        print("\nRock wins!")
    elif u1=='p' and u2 == 'r':
        print("\nPaper wins!")
    elif u1=='p' and u2 == 's':
        print("\nScissor wins!")
    else:
        print("\nEnter valid keyword")

        


user1 = input("Player 1 What's your name? ")
user2 = input("Player 2 What's your name? ")
user1_answer = input("%s do you want to chose Rock(r), scissor(s), or paper(p)? " %user1)
user2_answer = input("%s do you want to chose Rock(r), scissor(s), or paper(p)? " %user2)

win_check(user1_answer, user2_answer)