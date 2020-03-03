# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:26:49 2019

@author: Abirmoy
"""
print('''Please pick one:
                        rock
                        scissor
                        paper''')

game_dict = {'rock':1, 'scissor':2, 'paper':3}

while True:
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")
    a = game_dict.get(player1)
    b = game_dict.get(player2)
    dif = a-b
    
    if dif in [-1, 2]:
        print("\nPlayer 1 wins!")
    elif dif in [-2, 1]:
        print("\nPlayer 2 wins!")
        if input("Do you want to play another game? yes or no? ")=='yes':
            continue
        else:
            print("GAME OVER")
            break
    
        