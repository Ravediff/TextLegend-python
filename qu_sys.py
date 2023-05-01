


import random
Quest = []

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


