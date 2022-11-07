#1-------
color=input("Enter a color:")
if color == 'blue':
    print("The sky is blue!")
elif color == 'green':
    print("The grass is green!")
else:
    print("Idk that color")
#2-------
age=int(input("How old are you:"))
if age < 43:
    print("You are too young.")
elif age > 43:
    print("You are too old.")
else:
    print("You're the right age!")
#3-------
for i in range (50, 31, -3):
    print(i, end=" ")
#4-------
print(" ")
num = 10
while num <= 60:
    print(num, end= " ")
    num+=5
#5-------
quit = False
while quit == False:
    bruh=input("Enter a phrase:")
    if bruh != 'stop':
        print(bruh)
    else:
        quit = True
#6--------
print(" ")
def parameters (x, y):
    return x/y
print(parameters(25,6))
#7--------
def phrase():
    for s in range (13):
        print("snorfle")
phrase()
