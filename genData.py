import random
from datetime import datetime

now = datetime.now()

with open('data-20M.csv','wb') as data:

    data.write("id, A, B, C, D \n")

    a_chance = 0.9
    b_chance = 0.7
    c_chance = 0.5
    d_chance = 0.1

    for i in range(0,20000000):

        tags = [0,0,0,0]

        a_rand = random.random()
        b_rand = random.random()
        c_rand = random.random()
        d_rand = random.random()

        if a_rand < a_chance: tags[0] = 1 
        if b_rand < b_chance: tags[1] = 1
        if c_rand < c_chance: tags[2] = 1
        if d_rand < d_chance: tags[3] = 1

        data.write(str(i) +", " +str(tags).strip('[]') + "\n")

        