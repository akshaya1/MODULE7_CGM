import turtle

t = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
t.speed(0)

for i in range(200):
    t.color(colors[i % 7])
    t.pensize(i % 7 + 1)
    t.forward(i)
    t.right(59)

turtle.done()
