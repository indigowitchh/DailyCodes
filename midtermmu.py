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
