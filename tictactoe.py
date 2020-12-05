# -*- coding: utf-8 -*-
import os
os.system('title TicTacToe Game by Deepak Play && cls')

player = []
play = False
game_area = {}

def print_align(prnt, h=0, w=0, cls=True, vcenter=True, hcenter=True):
    size = os.get_terminal_size()
    height, width = 0, 0
    if cls:
        os.system('cls')
    if vcenter:
        height = size[1]//2
    if hcenter:
        width = size[0]//2-(len(prnt)//2)        
    print('\n'*(height+h)+' '*(width+w)+prnt, end='')
    
def set_player():
    global player, game_area
    game_area = {
        '7':' ','8':' ','9':' ',
        '4':' ','5':' ','6':' ',
        '1':' ','2':' ','3':' '
    }
    player = []
    while len(player)==0:
        print_align("Enter the Player X or O: ")
        pl = input()
        if pl.lower() == 'x':
            player = ['X', 'O']
        elif pl.lower() == 'o':
            player = ['O', 'X']
        else:
            print_align("Invalid input!!, Please Enter X or O")
            input()
            continue

def print_area():
    print_align(f"Player 1: [{player[0]}]           Player 2: [{player[1]}]\n",h=-6)
    print_align(f"{game_area['7']:^3}|{game_area['8']:^3}|{game_area['9']:^3}\n",h=3, cls=False, vcenter=False)
    print_align('-'*11+'\n', cls=False, vcenter=False)
    print_align(f"{game_area['4']:^3}|{game_area['5']:^3}|{game_area['6']:^3}\n", cls=False, vcenter=False)
    print_align('-'*11+'\n', cls=False, vcenter=False)
    print_align(f"{game_area['1']:^3}|{game_area['2']:^3}|{game_area['3']:^3}\n", cls=False, vcenter=False)
    
def check_win():
    for p in player:
        if game_area['1'] == p and game_area['2'] == p and game_area['3'] == p:
            return True
        elif game_area['4'] == p and game_area['5'] == p and game_area['6'] == p:
            return True
        elif game_area['7'] == p and game_area['8'] == p and game_area['9'] == p:
            return True
        elif game_area['1'] == p and game_area['4'] == p and game_area['7'] == p:
            return True
        elif game_area['2'] == p and game_area['5'] == p and game_area['8'] == p:
            return True
        elif game_area['3'] == p and game_area['6'] == p and game_area['9'] == p:
            return True
        elif game_area['1'] == p and game_area['5'] == p and game_area['9'] == p:
            return True
        elif game_area['3'] == p and game_area['5'] == p and game_area['7'] == p:
            return True
    return False
    pass
    
def get_input(choice):
    print_align(f"Player [{choice+1}] Enter the Cell : ",h=2 , cls=False, vcenter=False)
    cell = input()
    if cell in [str(x) for x in range(1,11)]:
        if game_area[cell] == ' ':                
            game_area[cell] = player[choice]
            return True
        else:
            print_align(f"Cell already used",h=2 , cls=False, vcenter=False)
            input()
    else:
        print_align(f"Invalid Input!, try again",h=2 , cls=False, vcenter=False)
        input()
    return False
    
def replay():
    global play
    input()
    print_align(f"Do You want to Play again (Y/N)")
    if input().lower() != 'y':
        raise KeyboardInterrupt
    play=False
    
while True:
    try:
        choice = 0
        play = True
        set_player()
        while play:
            print_area()
            if get_input(choice):
                if check_win():
                    print_area()
                    print_align(f"!!! Player {choice+1} Winns !!!", h=2, cls=False, vcenter=False)
                    replay()
                elif ' ' not in game_area.values():
                    print_area()
                    print_align(f"!!! Game Draw !!!",h=2 , cls=False, vcenter=False)
                    replay()
                choice = 0 if choice==1 else 1
        os.system('cls')
    except KeyboardInterrupt as e:
        print_align("Thankyou for Playing, See you Next time\n")
        input()
        os.system('cls')
        exit(0)

