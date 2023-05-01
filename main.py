#Project Blah Blah hahahahahah
#Kinky Product by RaVeN the menace.... KALPA FERNANDO

from game import *
import os

screen_width = 200

## TITLE SCREEN STUFF ##

def title_select():
    opt = ''
    while opt.lower() not in ['1', '2', '3', '4']:
        opt = input('> ')
        if opt == '1':
            intro_game()
        elif opt == '2':
            load()
        elif opt == '3':
            help_menu()
            title_select()
        elif opt == '4':
            quit()
        elif opt == '5':
            myPlayer.name = 'Kalpa'
            myPlayer.job = 'Hero'
            myPlayer.hp = 80
            myPlayer.mp = 30
            myPlayer.atk = 8
            myPlayer.defs = 7
            myPlayer.money = 900000
            myPlayer.city = 'eden'
            myPlayer.location = 'central'
            eden_town()
        else:
            os.system('cls')
            print('Your input is not valid bro')
            print('Choose between play, load, help and quit')
            print('                                              ')
            os.system('pause')
            title_screen()

def title_screen():
    os.system('cls')
    print(' _____________________________________________')
    print('|            ---TEXT LEGEND---               |')
    print('|--------------------------------------------|')
    print('|                [1]Play-                    |')
    print('|                [2]Load-                    |')
    print('|                [3]Help-                    |')
    print('|                [4]Quit-                    |')
    print('|____________________________________________|')
    print('                                              ')
    print('                               @RaVeN Projects')
    print('                                              ')
    title_select()

def help_menu():
    os.system('cls')
    print('|                 ---HELP---                 |')
    print('                                              ')
    print('* Take it easy, if you want to move movable locations\nwill be displayed in screen.\nJust type it when u want to move\n\n* Type "save" to save (This only works inside the game, cutscene and battles will not work\n\nTHATS ALL FOR NOW')
    os.system('pause')
    title_screen()



def load():
    os.system('cls')
    global Quest
    list = pickle.load(open("save.dat", "rb"))
    myPlayer.name = list[0]
    myPlayer.hp = list[1]
    myPlayer.mp = list[2]
    myPlayer.job = list[3]
    myPlayer.atk = list[4]
    myPlayer.defs = list[5]
    myPlayer.money = list[6]
    myPlayer.location = list[7]
    myPlayer.city = list[8]
    myPlayer.rank = list[9]
    if len(Quest) > 0:
        Quest.append(list[10])

    if list[8] == 'eden':
        eden_town()
    else:
        title_screen()


def quit():
    print('Are you sure that you want to quit?')
    print('-[1]Yes      -[2]No')
    opt2 = input()
    if opt2 == '1':
        sys.exit()
    elif opt2 == '2':
        title_screen()
    while opt2.lower() not in ['1', '2']:
        os.system('cls')
        print('Your input is not valid bro')
        print('Choose between yes and no')
        print('                                              ')
        os.system('pause')
        quit()
        opt2 = input('> ')
        if opt2 == '1':
            sys.exit()
        elif opt2 == '2':
            title_screen()

def Ani_screen():
    print('                                                                                         ')
    print('                                                                                         ')
    print('                                                                                         ')
    print('████████╗███████╗██╗  ██╗████████╗    ██╗     ███████╗ ██████╗ ███████╗███╗   ██╗██████╗')
    print('╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██║     ██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗')
    print('   ██║   █████╗   ╚███╔╝    ██║       ██║     █████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║')
    print('   ██║   ██╔══╝   ██╔██╗    ██║       ██║     ██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║')
    print('   ██║   ███████╗██╔╝ ██╗   ██║       ███████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝')
    print('   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝')
    print('                                                                                         ')
    os.system('pause')
    os.system('cls')

def main():
    Ani_screen()
    title_screen()

if __name__ == "__main__":
    main()


