import random

for x in range(0,6):
    def npcGen():
        num = random.randrange(0,106)
        if num < 20:
            print("Hey, I like shorts!")
        elif num < 65:
            print("What is a man? A miserable little pile of secrets")
        elif num < 85:
            print("I used to be an adventurer like you. Then I took an arrow to the knee")
        elif num < 95:
            print("Do a barrel roll!")
        else:
            print("Science isn't about why, its about why not!")
        
npcGen()
