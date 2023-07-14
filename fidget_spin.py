from turtle import *

s={'turn': 0}

def spin():
    clear()
    ang=s['turn']/10
    right(ang)

    forward(100)
    dot(120, "maroon")
    back(100)

    "second dot"
    right(120)
    forward(100)
    dot(120, "hotpink")
    back(100)

    "third dot"
    right(120)
    forward(100)
    dot(120, "pink")
    back(100)
    right(120)

    update()

def animate_spin():
    if s['turn']>0: s['turn']-=1
    spin()
    ontimer(animate_spin,20)

def acc():
    s['turn']+=40

setup(600,400,370,0)
bgcolor("black")

tracer(False)

width(60)
color("white")

onkey(acc,'space')

listen()
animate_spin()
done()