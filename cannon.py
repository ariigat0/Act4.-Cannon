"""
Cannon, hitting targets with projectiles.

La velocidad del movimiento para el proyectil y los balones es más rápida
El juego nunca termina, de manera que los balones al salir de la ventana se re posicionan.

"""
import random
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-300, -300)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 300) / 25
        speed.y = (y + 300) / 25

def inside(xy):
    "Return True if xy within screen."
    return -300 < xy.x < 300 and -300 < xy.y < 300

colors = ['blue', 'orange', 'yellow', 'green', 'purple']
def selectRandom(colors):
    color = random.choice(colors)
    colors.remove(color)
    return color

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, target_color) 

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

target_color = selectRandom(colors)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
