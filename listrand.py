import random
inventory = ['empty', 'empty', 'empty', 'empty', 'empty']

num = random.randrange(0,100)

def slots():
    slot = random.randrange (0,4)
    if num < 25:
        inventory[slot]=('book')
    elif num < 40:
        inventory[slot]=('frog')
    elif num < 80:
        inventory[slot]=('potion')
    else:
        inventory[slot]=('cupcake')
    
    print(inventory)
    
    
slots()
slots()
slots()
slots()
slots()
