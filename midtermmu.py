#Code 4----------------------------------------------------------
def bruh(num):
    num = 100
    while num >= 50:
        print(num)
        num-=10
bruh(5)

#Code 5----------------------------------------------------------
quit=False
while quit == False:
    joke= input("Knock knock, whos there?:")
    if joke != 'orange':
        print("....banana!")
    else:
        print("orange you glad i said banana?!")
        quit = True
#Code 6----------------------------------------------------------
def parameters (x, y, z):
    return x*y*z

print(parameters(2,3,4))
 
#Code 7----------------------------------------------------------
def rootbeer(x):
    x = int(input("Enter number:"))
    while x!=0:
       print(x, "bottles of root beer on the wall") 
       x-=1
rootbeer('x')
