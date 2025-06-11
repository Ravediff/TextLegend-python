#The Whole game lies here men

from main import *
from time import sleep
from map import *
from qu_sys import *
import sys
import os
import pickle

tempLoc = ''


class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.atk = 0
        self.defs = 0
        self.mp = 0
        self.job = ''
        self.money = 0
        self.location = ''
        self.city = ''
        self.rank = ''
        self.inventory = []
        self.weapon = 'None'
        self.armor = 'None'
        self.shield = 'None'


myPlayer=player()

def save():
    global Quest
    list = [myPlayer.name, myPlayer.hp, myPlayer.mp, myPlayer.job, myPlayer.atk, myPlayer.defs, myPlayer.money, myPlayer.location, myPlayer.city, myPlayer.rank]
    if len(Quest) > 0:
        list.append(Quest[0])
    with open('save.dat', 'wb') as f:
        pickle.dump(list, f)

def award(item):
    myPlayer.inventory.append(item)
    print(f'You received {item}!')
    return

def watch_stats():
    os.system('cls')
    print('--------------------PLAYER STATS--------------------')
    print(f'Name : {myPlayer.name}')
    print(f'Job : {myPlayer.job}')
    print(f'Rank : {myPlayer.rank}')
    print(f'HP : {myPlayer.hp}')
    print(f'MP : {myPlayer.mp}')
    print(f'ATK : {myPlayer.atk}')
    print(f'DEF : {myPlayer.defs}')
    print(f'Money : {myPlayer.money} gold')
    print('----------------------------------------------------')
    print(f'Weapon : {myPlayer.weapon}')
    print(f'Armor : {myPlayer.armor}')
    print(f'Shield : {myPlayer.shield}')
    print('----------------------------------------------------')
    os.system('pause')

def watch_Inve():
    os.system('cls')
    print('--------------------PLAYER INVENTORY--------------------')
    print('Inventory:')
    if len(myPlayer.inventory) == 0:
        print('- Empty -')
    else:
        num = 0
        for item in myPlayer.inventory:
            num = num + 1
            print(f'[{num}] {item}')
    print('----------------------------------------------------')
    os.system('pause')

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
        sleep(0.02)
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
        sleep(0.02)
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
        sleep(0.02)
    print('\n[1] Hero\n[2] Mage\n[3] Assasin\n[4] Priest\n[5] Thief')
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
            sleep(0.02)
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
                sleep(0.02)
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
            sleep(0.02)
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
                sleep(0.02)
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
            sleep(0.02)
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
            sleep(0.02)
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
                sleep(0.02)
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
            sleep(0.02)
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
                sleep(0.02)
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

    while opt.lower() not in ['1', '2', '3', '4', '5']:
            Job_classes()


#----------------Start Game-------------------

def story1():
    os.system('cls')
    text = f'*Wakes up*\n...\n"What a weird dream, maybe im playing too much video games"\n \n*Gets up from the bed and getting ready for school*\n \n"Alright lets go"\n*Got out from the house and started walking*\n \n YOU DIED.. WASTED.\n \n"Actually it was a Truck that ran over you"\n"And truck-kun is one of my employe that brings me new people"\n \n"BTW im god, u will be reincarnated in another world as a {myPlayer.job}"\n"NO EXCUSES. NOW GO, DONT BOTHER ME AGAIN"\n\n'
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.02)
    os.system('pause')
    os.system('cls')
    text2 = f'All things whent BLACK\n \n*Wakes up in a new room*\n \n{myPlayer.name}: "Where am i?\n\nMysterious Girl: "Oh.. You awake, im glad you are ok.\nI found you on the forest, you were unconscious and some wolves Attacked you\nIm the one who saved you\n\n{myPlayer.name}: "Oh thank you! anyways Where am i?"\n\nLucia : "You are in "Eden Town", I am Lucia and you?\n\n{myPlayer.name}: I am {myPlayer.name}, Nice to meet you Lucia!\n"'
    for char in text2:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.02)
    os.system('pause')
    text3 = f'\nLucia: Nice to meet you too!, Anyways i think you dont have money since you were unconcious.\nSo This Inns Owner gave this money to you\nYou can Pay it Back later\nWhats your Job {myPlayer.name}?\n\n{myPlayer.name} : I am a .... i rather not say it. I am a Adventurer basically\n\nLucia : Then it settles, Theres a Town Guild to the north from here\nTake this 1000 gold and take on a Quest, so you can payback\nTheres a Shop inside the guild, you can buy weapons from there\nTo buy Armors you should visit "IronWorks" shop\nFor Magic stuff and Mana stuff visit "GrannyChad" shop\nI think thats all\n\n{myPlayer.name} : Thank you so much, i will repay it soon as possible.\nI should head out now, will visit again\n'
    for char in text3:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.02)
    os.system('pause')
    os.system('cls')
    Gold = '1000 gold'
    myPlayer.money = 1000
    print('\nHeads Out')
    myPlayer.city = ('eden')
    myPlayer.location = ('central')
    os.system('pause')
    eden_town()

#--------------------------------------------------Eden Town----------------------------------------------------------------
def eden_town():
    global tempLoc
    while True:
        loc = myPlayer.location
        os.system('cls')
        print('---------------------Eden Town---------------------')
        print('___________________________________________________')
        print('                                                   ')
        print(f'Current location: Eden {loc}')
        print(f'Money :  {myPlayer.money} gold')
        print('                                                   ')
        print('---------------------------------------------------')
        print(f'Can move to: {eden[loc]}')
        print('                                                   ')
        print('Other Prompts: Stats (See Stats)')
        print('             : Inv (See Inventory)\n ')
        print('Type the name of the place to visit (or type "save")')
        ip = input(f'What you wanna do? > ').lower()

        if ip == 'save':
            print('Game has been saved\n')
            save()
            os.system('pause')
            continue

        if ip.lower() == 'stats':
            watch_stats()
            continue
        if ip.lower() == 'inv':
            watch_Inve()
            continue


        if ip in eden[loc]:
            tempLoc = myPlayer.location
            myPlayer.location = ip

            # Check if ip is a special location (shop) by checking if its value is an int
            if isinstance(eden[ip], int):
                if eden[ip] == 0:
                    guild()
                elif eden[ip] == 1:
                    ironWorks()
                elif eden[ip] == 2:
                    maryInn()
                elif eden[ip] == 3:
                    gChad()
                elif eden[ip] == 4:
                    market()
            else:
                # It's a regular map location — just continue loop to refresh display
                continue

        else:
            print('\nYour input is invalid')
            os.system('pause')




#Shops

def guild():
    global Quest
    global tempLoc
    rank = myPlayer.rank

    if rank == '':
        os.system('cls')
        text = ('So you want to Register to the Guild,\n'
                'You will start at rank D. Then you can go up to Rank S\n'
                'Better The rank Better the Rewards and Harder the challenge\n'
                'You will earn Rank points by completing quests\n'
                'You can use them to Upgrade your rank.\nTHATS ALL!\n')
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.02)
        os.system('pause')
        myPlayer.rank = 'D'

    while True:
        os.system('cls')
        print(' _____________________________________________')
        print('|               ---Guild---                  |')
        print('|--------------------------------------------|')
        print('|                [1]Quest-                   |')
        print('|                [2]Rank-                    |')
        print('|                [3]Quit-                    |')
        print('|____________________________________________|')
        print('                                              ')
        ip = input('> ')

        if ip == '1':
            if len(Quest) == 0:
                ran_Goal()
            while True:
                os.system('cls')
                print(' _____________________________________________')
                print('|               ---QUESTS---                 |')
                print('|--------------------------------------------|')
                print('                                             ')
                print(f'{Quest[0]}')
                print('                                             ')
                print(' [0]Back-                                     ')
                print('|--------------------------------------------|')
                ip2 = input('> ')
                if ip2 == '0':
                    break
                else:
                    print('Your input is not valid')
                    os.system('pause')

        elif ip == '2':
            while True:
                os.system('cls')
                print(' _____________________________________________')
                print('|                ---RANK---                  |')
                print('|--------------------------------------------|')
                print(f'|              Current Rank {myPlayer.rank}          |')
                print('                                              ')
                print('|                [1]Upgrade-                 |')
                print('|                [0]Back-                    |')
                print('|--------------------------------------------|')
                ip2 = input('> ')
                if ip2 == '0':
                    break
                elif ip2 == '1':
                    rank_Up()
                    break
                else:
                    print('Your input is not valid')
                    os.system('pause')

        elif ip == '3':
            os.system('cls')
            if myPlayer.city == 'eden':
                myPlayer.location = tempLoc
                return  # Go back to eden_town()

        else:
            print('Your input is not valid')
            os.system('pause')



def market():
    global tempLoc
    while True:
        os.system('cls')
        print('--------------------MARKET--------------------')
        print(f'Money : {myPlayer.money} gold')
        print('----------------------------------------------')
        print('[1] Small HP Potion - 50 gold')
        print('[2] Large HP Potion - 150 gold')
        print('[3] Food Ration - 30 gold')
        print('[0] Leave Market')
        print('----------------------------------------------')
        ip = input('> ')

        if ip == '0':
            if myPlayer.city == 'eden':
                myPlayer.location = tempLoc
                return

        elif ip == '1':
            if myPlayer.money >= 50:
                myPlayer.money -= 50
                award('Small HP Potion')
            else:
                print('Bro, you poor!')
            os.system('pause')

        elif ip == '2':
            if myPlayer.money >= 150:
                myPlayer.money -= 150
                award('Large HP Potion')
            else:
                print('Not enough gold for this!')
            os.system('pause')

        elif ip == '3':
            if myPlayer.money >= 30:
                myPlayer.money -= 30
                award('Food Ration')
            else:
                print('Not enough gold!')
            os.system('pause')

        else:
            print('Invalid choice')
            os.system('pause')


def ironWorks():
    global tempLoc
    while True:
        os.system('cls')
        print('------------------IRONWORKS------------------')
        print(f'Money : {myPlayer.money} gold')
        print('----------------------------------------------')
        print('[1] Wood Sword - 200 gold')
        print('[2] Wood Shield - 150 gold')
        print('[3] Leather Armor - 180 gold')
        print('[0] Leave IronWorks')
        print('----------------------------------------------')
        ip = input('> ')

        if ip == '0':
            if myPlayer.city == 'eden':
                myPlayer.location = tempLoc
                return

        elif ip == '1':
            if myPlayer.money >= 200:
                myPlayer.money -= 200
                award('Wood Sword')
            else:
                print('Go kill some goblins for money lol')
            os.system('pause')

        elif ip == '2':
            if myPlayer.money >= 150:
                myPlayer.money -= 150
                award('Wood Shield')
            else:
                print('Gold not enough bruh')
            os.system('pause')

        elif ip == '3':
            if myPlayer.money >= 180:
                myPlayer.money -= 180
                award('Leather Armor')
            else:
                print('No gold no armor')
            os.system('pause')

        else:
            print('Invalid choice')
            os.system('pause')


def maryInn():
    global tempLoc
    while True:
        os.system('cls')
        print('-------------------MARY INN-------------------')
        print(f'Money : {myPlayer.money} gold')
        print('----------------------------------------------')
        print('[1] Rest (Heal fully) - 25 gold')
        print('[0] Leave Inn')
        print('----------------------------------------------')
        ip = input('> ')

        if ip == '0':
            if myPlayer.city == 'eden':
                myPlayer.location = tempLoc
                return

        elif ip == '1':
            if myPlayer.money >= 25:
                myPlayer.money -= 25
                myPlayer.hp = 100
                myPlayer.mp = 100
                print('You are fully rested! Go fight again!')
            else:
                print('Poor adventurer can’t rest...')
            os.system('pause')

        else:
            print('Invalid choice')
            os.system('pause')


def gChad():
    global tempLoc
    while True:
        os.system('cls')
        print('------------GRANNY CHAD MAGIC SHOP------------')
        print(f'Money : {myPlayer.money} gold')
        print('----------------------------------------------')
        print('[1] Small MP Potion - 50 gold')
        print('[2] Large MP Potion - 150 gold')
        print('[3] Magic Juice - 300 gold')
        print('[0] Leave Magic Shop')
        print('----------------------------------------------')
        ip = input('> ')

        if ip == '0':
            if myPlayer.city == 'eden':
                myPlayer.location = tempLoc
                return

        elif ip == '1':
            if myPlayer.money >= 50:
                myPlayer.money -= 50
                award('Small MP Potion')
            else:
                print('You need more gold!')
            os.system('pause')

        elif ip == '2':
            if myPlayer.money >= 150:
                myPlayer.money -= 150
                award('Large MP Potion')
            else:
                print('Granny says come back with more gold')
            os.system('pause')

        elif ip == '3':
            if myPlayer.money >= 300:
                myPlayer.money -= 300
                award('Magic Juice')
            else:
                print('Granny says: no money no Juice!')
            os.system('pause')

        else:
            print('Invalid choice')
            os.system('pause')


def inferno():
    global tempLoc
    print('On Work')
    os.system('pause')
    if myPlayer.city == 'eden':
        myPlayer.location = tempLoc
        eden_town()
