#Project Blah Blah hahahahahah
#Kinky Product by RaVeN the menace.... KALPA FERNANDO

import sys
import os

screen_width = 100

## TITLE SCREEN STUFF ##

def title_select():
    opt = input('> ')
    if opt.lower() == ('play'):
        sys.exit()
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
            sys.exit()
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
    print('I will edit this later, dude you just need to \ntype inputs that shows up. is it hard WHY THE F*** U NEED HELP')
    print('                                              ')
    os.system('pause')
    title_screen()

def load():
    os.system('cls')
    print('Save function still in work')
    os.system('pause')
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


