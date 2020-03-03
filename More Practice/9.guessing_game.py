# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:55:53 2019

@author: Abirmoy
"""

import random

my_guess = random.randint(1,10)
count = 1
print("\nWelcome to guessing game.\n")
print("\nI have a number for you from 1 to 10.")

for i in range (5,1,-1):
    print("\nYou have", i, "chance left.")
    player_guess = int(input("\nEnter your guess: "))
    
    if player_guess == my_guess:
        print("\nYOU GUESSED it CORRECT\n")
        break
        
    elif player_guess < my_guess:
        print("\nMY NUMBER IS GRATER THAN", player_guess, "\n")
    elif player_guess > my_guess:
        print("\nMY NUMBER IS SMALLAR THAN", player_guess, "\n")
    else:
        print(input("\nGAME OVER!"))
        break
    count += 1
print("It took yon", count, "tries.")   
