import time #module with timer functions

start = time.time() #starting time for game
room=1
TimeLeft = 1000 #how many seconds to give the user to complete the game

while TimeLeft > 0:
    print()
    newTime = time.time() #get current time
    timeElapsed = start - newTime #check how much times has passed
    print(int(timeElapsed *-1), "seconds have passed.") #print how many seconds has passed
    TimeLeft += timeElapsed #decrement the counter
    print("You have", int(TimeLeft), "seconds left to complete the game!") #print time left
    
    if room ==1:
        choice = input("You are in room 1, you can go south")
        if choice == "south":
            room = 2
        else:
            print("Sorry not an option")
    if room == 2:
        choice = input("You are in room 2, you can go north")
        if choice == "north":
            room = 1
        else:
            print("Sorry not an option")
