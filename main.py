#Project Blah Blah hahahahahah
#Kinky Product by RaVeN the menace.... KALPA FERNANDO

from game import *
import os

screen_width = 200

## TITLE SCREEN STUFF ##

def title_select():
    opt = input('> ')
    optl = opt.lower()
    if optl == ('play'):
        intro_game()
    elif opt.lower() == ('quit'):
        quit()
    elif opt.lower() == ('help'):
        help_menu()
    elif opt.lower() == ('load'):
        load()
    while opt.lower() not in ['play', 'quit', 'help', 'load']:
        os.system('cls')
        print('Your input is not valid bro')
        print('Choose between play, load, help and quit')
        print('                                              ')
        os.system('pause')
        title_screen()
        opt = input('> ')
        if opt.lower() == ('play'):
            intro_game()
        elif opt.lower() == ('quit'):
            quit()
        elif opt.lower() == ('help'):
            help_menu()
        elif opt.lower() == ('load'):
            load()

def title_screen():
    os.system('cls')
    print(' _____________________________________________')
    print('|            ---TEXT LEGEND---               |')
    print('|--------------------------------------------|')
    print('|                  -Play-                    |')
    print('|                  -Load-                    |')
    print('|                  -Help-                    |')
    print('|                  -Quit-                    |')
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

    if list[8] == 'eden':
        eden_town()
    else:
        title_screen()


def quit():
    print('Are you sure that you want to quit?')
    print('-Yes      -No')
    opt2 = input()
    if opt2.lower() == ('yes'):
        sys.exit()
    elif opt2.lower() == ('no'):
        title_screen()
    while opt2.lower() not in ['yes', 'no']:
        os.system('cls')
        print('Your input is not valid bro')
        print('Choose between yes and no')
        print('                                              ')
        os.system('pause')
        quit()
        opt2 = input('> ')
        if opt2.lower() == ('yes'):
            sys.exit()
        elif opt2.lower() == ('no'):
            title_screen()


def main():
    title_screen()

if __name__ == "__main__":
    main()


