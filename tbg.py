inventory = ["wood sword"]
import random
def monster(biome):
    num = random.randrange(0,100)
    if biome == "hallway":
        if num < 20:
            print("A creature approaches quickly at you.")
        elif num < 50: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 90:
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else:
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
     
    elif biome == "room?":
        if num < 25:
            print("A creature approaches quickly at you.")
        elif num < 75: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 85:
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else:
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
     
    elif biome == "different":
        if num < 20:
            print("A creature approaches quickly at you.")
        elif num < 50: #30 percent chance
            print("A tall figure peers from around the corner. He has no face.")
        elif num < 90:
            print("A clown doll sits in the corner of the room. Watching your every move.")
        else:
            print("A tall black figure walks towards you with open arms, but for some reason you feel like you can trust him.")
print("You wake up in your room. But, something feels off. Everything is the same as when you layed down and nothing is out of place. Except, it's quiet. No sound of family talking or the dogs walking around. Crap, you can't even hear the birds chirping. Curious, you decide to explore.")
room = 1
while True:
    if room == 1:
        print("You are in your bedroom, you can go (e)ast to enter the hallway, (n)orth to enter your closet, or (s)outh to go into the bathroom.")
        choice = input()
        if choice == 'e' or choice == 'E'or choice == 'east':
            room = 4
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 3
        else:
            print("Sorry, not an option!")
            
    if room == 2:
        print("You open the closet door. It is pitch black. Even if you flash your phone's flashlight, nothing appears. It is just dark. You don't want to enter, so you put your hand in. It just dissapears. You can go (s)outh to go back to your bedroom")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 1
        else:
            print("Sorry not an option!")
            
    if room == 3:
        print("You swing your bathroom door open. To your surprise, it is completely trashed, almost like a tornado hit it. As you walk through the bathroom and check the mirror, your reflection smiles back at you. Even though you are not smiling. Freaked out, you decide to run back to your room. You can go (n)orth.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 1
        else:
            print("Sorry not an option!")
            
    if room == 4:
        print("You are in the hallway. Or what you remember as the hallway. But, there still is no sound... You are alone. You can go (w)est to go back to your room, (n)orth into your baby siblings room, (s)outh to enter the random door you've never seen before, or (e)ast to go to your living room!")
        monster("hallway")
        choice = input()
        if choice == 'w' or choice == 'W'or choice == 'west':
            room = 1
        elif choice == 's' or choice == 'S'or choice == 'south':
            room = 6
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 5
        elif choice == 'e' or choice == 'E' or choice == 'east':
            room = 8
        else:
            print("Sorry, not an option!")
            
    if room == 5:
        print("Although your house is silent and no one seems to be around, the sound of your baby sibling crying rings through your ears. Yet, they are no where to be found. The longer you spend in the room, the louder the crying gets. Save your eardrums and go (s)outh to enter the hallway")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 4
        else:
            print("Sorry, not an option!")
            
    if room == 6:
        print("You are in your room again? Its a different room, yet everything is the same as your bedroom. Are you in a loop? However, instead of feeling alone, the feeling of being watched appears. You should leave immediately! You can go (n)orth back to what you think is the hallway, or (s)outh to another door!")
        monster("room?")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 4
        elif choice == 's' or choice == 'S'or choice == 'south':
            room = 7
        else:
            print("Sorry, not an option!")
            
    if room == 7:
        print("You are in a different room. One you do not recognize. That feeling of being watched creeps up on you. Yet, there's no door to lead you away. You're cornered! The only way back is to your supposed bedroom. You can go (n)orth")
        monster("different")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 6
        else:
            print("Sorry, not an option!")
    
    if room == 8:
        print("Huh.. the living room seems normal. Everything is in place, no sign of weird happenings. The only weird think is a random door to your left. Do you dare to explore? You can go (n)orth to enter the random door, or (s)outh into your kitchen.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 10
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 9
        else:
            print("Sorry, not an option!")
            
    if room == 9:
        print("Holy cow! The kitchen is covered in blood! It looks like a crazy crime scene. Your stomach drops and you feel like throwing up. You need to leave. You weren't supposed to see this. Go (n)orth into the living room.")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 8
        else:
            print("Sorry, not an option!")
            
    if room == 10:
        print("Another hallway? However, theres no ending. Or so it seems. You walk down the hallway for what seems like forever. The door back to your living room gets smaller and smaller. You finally reach a dead end. The only way back to 'society' is to go (n)orth")
        choice = input()
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 8
        else:
            print("Sorry, not an option!")