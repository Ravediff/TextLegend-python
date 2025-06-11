

import os
import random
Quest = []
monAchieve = {'Goblin': 0, 'Slime': 0}

def ran_Goal():
    from game import myPlayer
    global Quest
    rank = myPlayer.rank
    if rank == 'D':
        num = random.randint(1, 10)
        reward = random.randint(50, 500)
        mob_1 = ['Goblin', 'Slime']
        mob = random.choice(mob_1)
        quest_Temp = [f'defeat {num} {mob} for {reward} gold']

        if len(Quest) == 0:
            Quest.append(quest_Temp[0])
    return Quest


def rank_Up():
    from game import myPlayer
    from game import guild
    global Quest
    rank = myPlayer.rank
    if rank == 'D':
        if monAchieve['Goblin'] >= 20 or monAchieve['Slime'] >=30:
            myPlayer.rank = 'C'
            print('You have been promoted to rank C')
            os.system('pause')
            Quest = []
            ran_Goal()
            guild()
        else:
            print('You need atleast 20 Goblin kills and 30 Slime kills to rank up')
            os.system('pause')
            guild()



