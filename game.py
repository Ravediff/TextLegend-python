#The Whole game lies here men

from map import *
from time import sleep
import sys
import os

class player:
    def __int__(self):
        self.name = ''
        self.hp = 0
        self.atk = 0
        self.defs = 0
        self.mp = 0
        self.job= ''
        self.money = 0
        self.location = ''

myPlayer=player()

def award(item):
    Res = print(f'You Recieved {item}')
    return Res

def intro_game():
    os.system('cls')
    print(' _____________________________________________')
    print('|                  -INTRO-                   |')
    print(' _____________________________________________')
    print('                                              ')
    intro_text= 'Hello adventurer...\n \nThis is a Text RPG made by a Genius\n \nwho dont know anything.\n \nAnyways lets get started\n '
    for char in intro_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    os.system('pause')
    os.system('cls')
    print(' _____________________________________________')
    print('|                  -INTRO-                   |')
    print(' _____________________________________________')
    print('                                              ')
    myPlayer.name = input('\nEnter Your Name here: ')
    print('_____________________________________________')
    print(f'Ok your name is....{myPlayer.name}')
    print('_____________________________________________')
    intro_text2 = 'Ok there are Several Job classes you could Choose.\nAnd it will decide How much HP and MP you have\nofcourse it doesnt effect your ATK or DEF\n '
    for char in intro_text2:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    os.system('pause')
    Job_classes()


def Job_classes():
    os.system('cls')
    print(' _____________________________________________')
    print('|                  -INTRO-                   |')
    print(' _____________________________________________')
    print('                                              ')
    job_class_text = 'These are the Jobs that you will be able to choose..'
    for char in job_class_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    print('\n1) Hero\n2) Mage\n3) Assasin\n4) Priest\n5) Thief')
    opt = input('\nInput the Number That indicates your job: ')

    #HERO STUFF
    if opt == '1':
        os.system('cls')
        print('_________________HERO____________________')
        print('HP = 80')
        print('MP = 30')
        print('-----------------------------------------')
        Hero_text= 'This Job class IS Perfect for Starters Because\nIDK i think it is\n'
        for char in Hero_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        hero_opt = input('You wanna Go with Hero? y/n: ')
        if hero_opt.lower() == ('y'):
            os.system('cls')
            print(' _____________________________________________')
            print('|                  -INTRO-                   |')
            print(' _____________________________________________')
            print('                                              ')
            print('You are a Hero Now, save the day hahahHAHH')
            myPlayer.job = 'Hero'
            myPlayer.hp = 80
            myPlayer.mp = 30
            myPlayer.atk = 8
            myPlayer.defs = 7
            os.system('pause')
            story1()
        elif hero_opt.lower() == ('n'):
            os.system('cls')
            Job_classes()
        while hero_opt.lower() not in ['y', 'n']:
            os.system('cls')
            print('_________________HERO____________________')
            print('HP = 80')
            print('MP = 30')
            print('-----------------------------------------')
            Hero_text = 'This Job class IS Perfect for Starters Because\nIDK i think it is\n'
            for char in Hero_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                sleep(0.05)
            hero_opt = input('You wanna Go with Hero? y/n: ')
            if hero_opt.lower() == ('y'):
                os.system('cls')
                print(' _____________________________________________')
                print('|                  -INTRO-                   |')
                print(' _____________________________________________')
                print('                                              ')
                print('You are a Hero Now, save the day hahahHAHH')
                myPlayer.job = 'Hero'
                myPlayer.hp = 80
                myPlayer.mp = 30
                myPlayer.atk = 8
                myPlayer.defs = 7
                os.system('pause')
                story1()
            elif hero_opt.lower() == ('n'):
                os.system('cls')
                Job_classes()


    #MAGE STUFF
    elif opt == '2':
        os.system('cls')
        print('_________________MAGE____________________')
        print('HP = 60')
        print('MP = 50')
        print('-----------------------------------------')
        Hero_text= 'You wanna be a MAGE, wth dude\nANYWAYS, IDC\n'
        for char in Hero_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        hero_opt = input('You wanna Go with Mage? y/n: ')
        if hero_opt.lower() == ('y'):
            os.system('cls')
            print(' _____________________________________________')
            print('|                  -INTRO-                   |')
            print(' _____________________________________________')
            print('                                              ')
            print('You are a Mage Now, Do some Magic')
            myPlayer.job = 'Mage'
            myPlayer.hp = 60
            myPlayer.mp = 50
            myPlayer.atk = 6
            myPlayer.defs = 8
            os.system('pause')
            story1()
        elif hero_opt.lower() == ('n'):
            os.system('cls')
            Job_classes()
        while hero_opt.lower() not in ['y', 'n']:
            os.system('cls')
            os.system('cls')
            print('_________________MAGE____________________')
            print('HP = 60')
            print('MP = 50')
            print('-----------------------------------------')
            Hero_text = 'You wanna be a MAGE, wth dude\nANYWAYS, IDC\n'
            for char in Hero_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                sleep(0.05)
            hero_opt = input('You wanna Go with Mage? y/n: ')
            if hero_opt.lower() == ('y'):
                os.system('cls')
                print(' _____________________________________________')
                print('|                  -INTRO-                   |')
                print(' _____________________________________________')
                print('                                              ')
                print('You are a Mage Now, Do some Magic')
                myPlayer.job = 'Mage'
                myPlayer.hp = 60
                myPlayer.mp = 50
                myPlayer.atk = 6
                myPlayer.defs = 8
                os.system('pause')
                story1()
            elif hero_opt.lower() == ('n'):
                os.system('cls')
                Job_classes()

    #Assasin stuff
    elif opt == '3':
        os.system('cls')
        print('_________________Assasin____________________')
        print('HP = 60')
        print('MP = 45')
        print('--------------------------------------------')
        Hero_text= 'You wanna be assasin, thats cool\nyou like james bond movies?\n'
        for char in Hero_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        hero_opt = input('You wanna Go with Assasin? y/n: ')
        if hero_opt.lower() == ('y'):
            os.system('cls')
            print(' _____________________________________________')
            print('|                  -INTRO-                   |')
            print('|____________________________________________|')
            print('                                              ')
            print('You are a Assasin Now, lets take down hitler\n oh he''s dead')
            myPlayer.job = 'Assasin'
            myPlayer.hp = 60
            myPlayer.mp = 45
            myPlayer.atk = 10
            myPlayer.defs = 4
            os.system('pause')
            story1()
        elif hero_opt.lower() == ('n'):
            os.system('cls')
            Job_classes()
        while hero_opt.lower() not in ['y', 'n']:
            os.system('cls')
            print('_________________Assasin____________________')
            print('HP = 60')
            print('MP = 45')
            print('--------------------------------------------')
            Hero_text = 'You wanna be assasin, thats cool\nyou like james bond movies?\n'
            for char in Hero_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                sleep(0.05)
            hero_opt = input('You wanna Go with Assasin? y/n: ')
            if hero_opt.lower() == ('y'):
                os.system('cls')
                print(' _____________________________________________')
                print('|                  -INTRO-                   |')
                print('|____________________________________________|')
                print('                                              ')
                print('You are a Assasin Now, lets take down hitler\n oh he''s dead')
                myPlayer.job = 'Assasin'
                myPlayer.hp = 60
                myPlayer.mp = 45
                myPlayer.atk = 10
                myPlayer.defs = 4
                os.system('pause')
                story1()
            elif hero_opt.lower() == ('n'):
                os.system('cls')
                Job_classes()

    #Priest
    elif opt == '4':
        os.system('cls')
        print('_________________Priest____________________')
        print('HP = 55')
        print('MP = 50')
        print('-------------------------------------------')
        Hero_text= 'You wanna be Priest, ok\n....\n'
        for char in Hero_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        hero_opt = input('You wanna Go with Priest? y/n: ')
        if hero_opt.lower() == ('y'):
            os.system('cls')
            print(' _____________________________________________')
            print('|                  -INTRO-                   |')
            print('|____________________________________________|')
            print('                                              ')
            print('You are a Priest Now, Become bishop now')
            myPlayer.job = 'Priest'
            myPlayer.hp = 55
            myPlayer.mp = 50
            myPlayer.atk = 5
            myPlayer.defs = 5
            os.system('pause')
            story1()
        elif hero_opt.lower() == ('n'):
            os.system('cls')
            Job_classes()
        while hero_opt.lower() not in ['y', 'n']:
            os.system('cls')
            print('_________________Priest____________________')
            print('HP = 55')
            print('MP = 50')
            print('-------------------------------------------')
            Hero_text = 'You wanna be Priest, ok\n....\n'
            for char in Hero_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                sleep(0.05)
            hero_opt = input('You wanna Go with Priest? y/n: ')
            if hero_opt.lower() == ('y'):
                os.system('cls')
                print(' _____________________________________________')
                print('|                  -INTRO-                   |')
                print('|____________________________________________|')
                print('                                              ')
                print('You are a Priest Now, Become bishop now')
                myPlayer.job = 'Priest'
                myPlayer.hp = 55
                myPlayer.mp = 50
                myPlayer.atk = 5
                myPlayer.defs = 5
                os.system('pause')
                story1()
            elif hero_opt.lower() == ('n'):
                os.system('cls')
                Job_classes()

    #Thief
    elif opt == '5':
        os.system('cls')
        print('_________________Thief____________________')
        print('HP = 80')
        print('MP = 20')
        print('-----------------------------------------_')
        Hero_text= 'You wanna be Thief, sure\ni dont ask why tho\n'
        for char in Hero_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        hero_opt = input('You wanna Go with Thief? y/n: ')
        if hero_opt.lower() == ('y'):
            os.system('cls')
            print(' _____________________________________________')
            print('|                  -INTRO-                   |')
            print('|____________________________________________|')
            print('                                              ')
            print('You are a Thief Now, Steal bish')
            myPlayer.job = 'Thief'
            myPlayer.hp = 80
            myPlayer.mp = 20
            myPlayer.atk = 4
            myPlayer.defs = 8
            os.system('pause')
            story1()
        elif hero_opt.lower() == ('n'):
            os.system('cls')
            Job_classes()
        while hero_opt.lower() not in ['y', 'n']:
            os.system('cls')
            print('_________________Thief____________________')
            print('HP = 80')
            print('MP = 20')
            print('------------------------------------------')
            Hero_text = 'You wanna be Thief, sure\ni dont ask why tho\n'
            for char in Hero_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                sleep(0.05)
            hero_opt = input('You wanna Go with Thief? y/n: ')
            if hero_opt.lower() == ('y'):
                os.system('cls')
                print(' _____________________________________________')
                print('|                  -INTRO-                   |')
                print('|____________________________________________|')
                print('                                              ')
                print('You are a Thief Now, Steal bish')
                myPlayer.job = 'Thief'
                myPlayer.hp = 80
                myPlayer.mp = 20
                myPlayer.atk = 4
                myPlayer.defs = 8
                os.system('pause')
                story1()
            elif hero_opt.lower() == ('n'):
                os.system('cls')
                Job_classes()

    while opt.lower() not in ['hero', 'mage', 'assasin', 'priest', 'thief']:
            Job_classes()


#----------------Start Game-------------------

def story1():
    os.system('cls')
    text = f'*Wakes up*\n...\n"What a weird dream, maybe im playing too much video games"\n \n*Gets up from the bed and getting ready for school*\n \n"Alright lets go"\n*Got out from the house and started walking*\n \n YOU DIED.. WASTED.\n \n"Actually it was a Truck that ran over you"\n"And truck-kun is one of my employe that brings me new people"\n \n"BTW im god, u will be reincarnated in another world as a {myPlayer.job}"\n"NO EXCUSES. NOW GO, DONT BOTHER ME AGAIN"\n\n'
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    os.system('pause')
    os.system('cls')
    text2 = f'All things whent BLACK\n \n*Wakes up in a new room*\n \n{myPlayer.name}: "Where am i?\n\nMysterious Girl: "Oh.. You awake, im glad you are ok.\nI found you on the forest, you were unconscious and some wolves Attacked you\nIm the one who saved you\n\n{myPlayer.name}: "Oh thank you! anyways Where am i?"\n\nLucia : "You are in "Eden Town", I am Lucia and you?\n\n{myPlayer.name}: I am {myPlayer.name}, Nice to meet you Lucia!\n"'
    for char in text2:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    os.system('pause')
    text3 = f'\nLucy: Nice to meet you too!, Anyways i think you dont have money since you were unconcious.\nSo This Inns Owner gave this money to you\nYou can Pay it Back later\nWhats your Job {myPlayer.name}?\n\n{myPlayer.name} : I am a .... i rather not say it. I am a Adventurer basically\n\nLucy : Then it settles, Theres a Town Guild to the north from here\nTake this 1000 gold and take on a Quest, so you can payback\nTheres a Shop inside the guild, you can buy weapons from there\nTo buy Armors you should visit "IronWorks" shop\nFor Magic stuff and Mana stuff visit "GrannyChad" shop\nI think thats all\n\n{myPlayer.name} : Thank you so much, i will repay it soon as possible.\nI should head out now, will visit again\n'
    for char in text3:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    os.system('pause')
    os.system('cls')
    Gold = '1000 gold'
    award(Gold)
    myPlayer.money = 1000
    print('\nHeads Out')
    myPlayer.location = ('central')
    os.system('pause')
    eden_town()

def eden_town():
    loc = myPlayer.location
    os.system('cls')
    print('---------------------Eden Town---------------------')
    print('___________________________________________________')
    print('                                                   ')
    print(f'current location: Eden {loc}')
    print(f'Money : {myPlayer.money} gold')
    print('                                                   ')
    print('---------------------------------------------------')
    print(f'Can move to {eden[loc]}')
    print('                                                   ')
    print('Type the name of the place to visit')
    ip = input('What you wanna do? > ')
    if ip.lower() == ('north'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'north'
            eden_town()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('south'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'south'
            eden_town()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('east'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'east'
            eden_town()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('west'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'west'
            eden_town()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('guild'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'guild'
            guild()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('market'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'market'
            market()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('maryinn'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'MaryInn'
            maryInn()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('ironworks'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'ironworks'
            ironWorks()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('grannychad'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'grannychad'
            grannyChad()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()
    elif ip.lower() == ('inferno'):
        if ip.lower() in eden[loc]:
            myPlayer.location = 'inferno'
            inferno()
        else:
            print('Cant go there')
            os.system('pause')
            eden_town()

    while ip.lower() not in eden[loc]:
        print('Your output is invalid')
        os.system('pause')
        eden_town()
    os.system('pause')
