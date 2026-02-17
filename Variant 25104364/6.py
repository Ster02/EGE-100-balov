import turtle as t

t.tracer(1000)
k = 15

for i in range(2):
    t.forward(3 * k)
    t.right(90)
    t.forward(20 * k)
    t.right(90)

t.up()
t.backward(8 * k)
t.right(90)
t.forward(9 * k)
t.left(90)
t.down()

for i in range(2):
    t.forward(16 * k)
    t.right(90)
    t.forward(8 * k)
    t.right(90)

t.up()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * k, y * k)
        t.dot(5, "red")

t.done()