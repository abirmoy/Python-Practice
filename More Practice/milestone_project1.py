# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:01:45 2019

@author: Abirmoy
"""

# display the board
def display_board(board):
    print('\n'*100) # in order to clean the display
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('\n'*10)
    
# get user marker
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = ''
    # KEEP ASKING PLAYER 1 to chose X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, chose X or O: ').upper()
    # ASSIGN PLAYE 2, to oposite marker
     
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    return ( # row check
            (board[1]==mark and board[2]==mark and board[3]==mark) or 
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[7]== mark and board[8]==mark and board[9]==mark) or
            # column check
            (board[1]==mark and board[4]==mark and board[7]==mark) or
            (board[2]==mark and board[5]==mark and board[8]==mark) or
            (board[3]==mark and board[6]==mark and board[9]==mark) or
            # diagonal check
            (board[1]==mark and board[5]==mark and board[9]==mark) or
            (board[3]==mark and board[5]==mark and board[7]==mark) )

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check (board, position):
    return board[position]== ' '

def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
    # board is full if we return true
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4.5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position (1-9): '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
        




######################################################################
    




# WHILE LOOP TO KEEP RUNING THE GAME
print("\nWelcome to TIC TAC TOE!!!\n")

while True:
    # PLAY THE GAME
    
    ## SET EVERYTHING UP
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print('\n', turn, 'will go first.')
    
    play_game = input("Ready to play? y or n? ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    
    ## GAME PLAY
    while game_on:
        
        if turn == 'Player1':
            
            # SHOW THE BOARD
            display_board(the_board)
            
            # CHOSE A POSITION
            position = player_choice(the_board)
            # PLACE A MARKER ON THE POSITION
            place_marker(the_board, player1_marker, position)
            # CHECK IF P1 WON
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("\nPLAYER 1 HAS WON!!\n")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\nIT'S A TIE, TRY AGAIN!\n")
                    game_on = False
                else:
                    turn = 'Player 2'
            
        else:
            # SHOW THE BOARD
            display_board(the_board)
            
            # CHOSE A POSITION
            position = player_choice(the_board)
            # PLACE A MARKER ON THE POSITION
            place_marker(the_board, player2_marker, position)
            # CHECK IF P1 WON
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("\nPLAYER 2 HAS WON!!\n")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\nIT'S A TIE, TRY AGAIN!\n")
                    game_on = False
                else:
                    turn = 'Player 1'

    
    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP ON replay()























