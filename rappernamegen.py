import random

adjectives = ['Lil', 'Young', 'That', 'Wavy', 'Emotional', 'Gangsta', 'Playboi', 'Dummy', 'Blessed', 'Coldest']
nouns = ['Boat', 'Geode', 'Coat', 'Flower', 'Act', 'God', 'King', 'Champ', 'Baby', 'Conflict']
 


quit = False
while quit == False:
    name = random.randrange(0,10)
    bruh= random.randrange (0,10)
    name1= adjectives[name]
    name2= nouns[bruh]
    choice=input("Press any key to continue and q to quit")
    
    if choice != 'q':
        print("Your stagename is:", name1, name2)
    else:
        print("Goodbye")
        quit = True
