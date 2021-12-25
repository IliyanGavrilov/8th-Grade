print("You can miss only twice")

import turtle
from random import randint


RIGHT = 0
DOWN = 270
LEFT = 180
UP = 90
PLAYER_STEP = 20  # пиксела на придвижване
ENEMY_STEP = 10   # пиксела на придвижване
ENEMY_SPEED = 200  # едно движение на 0.2 sec

screen = turtle.Screen()


def create_player():
    player = turtle.Turtle()
    player.shape('turtle')
    player.penup()
    player.fillcolor('blue')
    player.speed(0)  # това означава без анимация (най-бързото движение)
    return player


def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape('turtle')
    enemy.penup()
    enemy.fillcolor('red')
    enemy.speed(0)  # това означава без анимация (най-бързото движение)
    enemy.right(90)  # гледа надолу
    return enemy


def draw_border():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.hideturtle()
    for _ in range(4):
        t.forward(300)
        t.right(90)


player = create_player()
enemy = create_enemy()


def reset_enemy():
    enemy.goto(randint(-130, 130), randint(0, 130))


def move_enemy():
    enemy.forward(ENEMY_STEP)
    if enemy.ycor() < -130:
        return reset_enemy()
    if player.distance(enemy.pos()) < 20:
        reset_enemy()

    # напишете кода
    # Ако врага и извън игралното поле - рестартирайте позицията му с reset_enemy
    # Ако врага е ударен - отбележете точка и рестартирайте позицията му
    # Използваъте player.distance(enemy.pos()) - то ви дава диатанцията между играчите

    screen.ontimer(move_enemy, ENEMY_SPEED)

 

# Тези функции се викат при натискане на бутон
# Те трябва да придвижат играча в дадената посока
# за да завивате вземете текущата посока на играча (ъгъл) с player.heading()
# и пресметнете новате посока


def move_right():
    
    player.right(90)
    
    
    

def move_down():
    player.forward(-PLAYER_STEP)
    


def move_left():
    player.left(90)
    
   

def move_up():
    player.forward(PLAYER_STEP)
    
    

   



move_enemy() 
draw_border()
reset_enemy()

# Движение:
#
#    W
#   A D
#    S
screen.onkey(move_up, 'w')
screen.onkey(move_down, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.ontimer(move_enemy, ENEMY_SPEED)

screen.listen()
screen.mainloop()
