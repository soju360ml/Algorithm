import turtle

swidth, sheight = 500, 500
a = swidth, sheight

turtle.shape('turtle')
turtle.setup(width = a[0] + 50, height = a[1] + 50)
turtle.screensize(a[0], a[1])
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.speed(10)

for radius in range(1, 2500):
    remainder = radius % 7
    colorList = 'red', 'orange', 'yellow', 'green', 'blue', 'navyblue', 'purple'
    turtle.pencolor(colorList[remainder])

    radius = radius if radius % 2 == 0 else -radius
    turtle.circle(radius)

turtle.done()