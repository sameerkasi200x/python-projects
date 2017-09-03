from __future__ import print_function
from IPython.display import clear_output
from IPython.display import clear_output

degree_of_board=3

def display_board(board):
    clear_output()
    x=1
    while x<degree_of_board+1 :
        print('   |   |')
        print(' ' + board[x][1] + ' | ' + board[x][2] + ' | ' + board[x][3])
        print('   |   |')
        if not (x==3):
            print('-----------')
        x=x+1;
    
def player_input():
    player_markers={'Player1':'','Player2':''}
    
    print("Player 1, Choose your marker - X or O ? ")
    player_markers['p1']=raw_input('Player 1: Do you want to be X or O? ').upper()
    if (player_markers['Player1']=='X'):
        player_markers['Player2']='O'
    elif(player_markers['Player1']=='O'):
        player_markers['Player2']='X'
    else:
        player_markers=player_input()
    return player_markers

def win_check(board,mark):
    ## Check horizontal
    x=1;
    y=1;
    
    
    win_status=False
    while x<degree_of_board+1 :
        while y<degree_of_board+1 :
        # Perform check for for all markers in a given X-axis line
            if not (board[x][y]==mark) :
                win_status=False;
                break
            else :
                y=y+1
                win_status=True
        
        ## If the win status remains true by the end of the given X-axis line, player with given marker has won
        if win_status :
            return win_status
        else: 
            x=x+1
            y=1

    ## Check vertical
    x=1;
    y=1;
    win_status=False
    while y<degree_of_board+1 :
        while x<degree_of_board+1 :
            # Perform check for all markers in given Y-axis
            if not (board[x][y]==mark) :
                win_status=False;
                break
            else :
                x=x+1
                win_status=True
        
        ## If the win status remains true by the end of the given Y-axis line, player with given marker has won
        if win_status :
            return win_status
        else: 
            y=y+1
            x=1
    
    ## Check diagonal Right-top to bottom-left
    x=1;
    while x<degree_of_board+1 :
        if not (board[x][x]==mark) :
            win_status=False
            break
        else :
            x=x+1
            win_status=True
    if win_status :
            return win_status

    ## Check diagonal bottom-left to top-right
    x=1;
    while x<degree_of_board+1 :
        if not (board[x][degree_of_board+1-x]==mark) :
            win_status=False
            break
        else :
            x=x+1
            win_status=True
    if win_status :
            return win_status
        
    return False

def place_marker(board, marker, position):
    x=position[0]
    y=position[1]
    board[x][y]=marker
    return board

import random
def choose_first():
        if random.randint(0, 1) == 0:
            return 'Player2'
        else:
            return 'Player1'

def full_board_check(board):
    x=1
    y=1
    while x<degree_of_board+1 :
        y=1
        while y<degree_of_board+1 :
            if not (board[x][y]=='X' or board[x][y]=='O') :
                return False
            y=y+1 
        x=x+1
        
    return True
