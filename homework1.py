# Draw shapes with turtle

import turtle

pen = turtle.Turtle()

print("1. Triangle")
print("2. Square")
print("3. Pentagon")
print("4. Hexagon")
print("5. Pentagram")
choice = int(input("Choose figure: "))

if choice == 1:
    while True:
        pen.forward(90)
        pen.left(120)
        pen.forward(90)
        pen.left(120)
        pen.forward(90)
        pen.left(120)
elif choice == 2:
    while True:
        pen.forward(90)
        pen.left(90)
        pen.forward(90)
        pen.left(90)
        pen.forward(90)
        pen.left(90)
        pen.forward(90)
        pen.left(90)
elif choice == 3:
    while True:
        pen.forward(90)
        pen.left(72)
        pen.forward(90)
        pen.left(72)
        pen.forward(90)
        pen.left(72)
        pen.forward(90)
        pen.left(72)
        pen.forward(90)
        pen.left(72)
elif choice == 4:
    while True:
        pen.forward(90)
        pen.left(60)
        pen.forward(90)
        pen.left(60)
        pen.forward(90)
        pen.left(60)
        pen.forward(90)
        pen.left(60)
        pen.forward(90)
        pen.left(60)
        pen.forward(90)
        pen.left(60)
elif choice == 5:
    while True:
        pen.left(72)
        pen.forward(90)
        pen.right(144)
        pen.forward(90)
        pen.right(144)
        pen.forward(90)
        pen.right(144)
        pen.forward(90)
        pen.right(144)
        pen.forward(90)
        pen.left(144)
else:
    print("Invalid")
    
    
