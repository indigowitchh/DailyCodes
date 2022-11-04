#4---------------
def bruh(num):
    num = 20
    while num <= 60:
        print(num)
        num+=2

bruh(5)

#5---------------
quit=False
while quit == False:
    password= int(input("Enter password:"))
    if password != 12345 :
        print("Access denied")
    else:
        print("Access granted")
        quit = True

#6---------------
def parameters (w, x, y, z):
    return w+x-y+z

print(parameters(10,20,30,40))

#7---------------
def garden(seeds):
    seeds = int(input("Enter number of seeds you are growing:"))
    print("The pumpkins are growing!")
    while seeds != 0 :
        seeds+=
        print("Now you have", seeds, "pumpkins!") 
garden('seeds')
