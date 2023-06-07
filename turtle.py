import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# Function to move the turtle
def move():
    x = player.xcor()
    y = player.ycor()
    player.setheading(90)
    player.forward(3)

    # Check for collision with food
    for food in foods:
        if player.distance(food) < 20:
            food.goto(random.randint(-380, 380), random.randint(-280, 280))
            food.color(random.choice(["red", "blue", "orange", "purple", "pink"]))

    # Check for collision with borders
    if y > 290:
        player.sety(290)
    elif y < -290:
        player.sety(-290)
    if x > 390:
        player.setx(390)
    elif x < -390:
        player.setx(-390)

    screen.update()
    screen.ontimer(move, 10)

# Create food items
foods = []
for _ in range(10):
    food = turtle.Turtle()
    food.shape("circle")
    food.color(random.choice(["red", "blue", "orange", "purple", "pink"]))
    food.penup()
    food.goto(random.randint(-380, 380), random.randint(-280, 280))
    foods.append(food)

# Keyboard bindings
screen.onkeypress(lambda: player.setheading(90), "Up")
screen.onkeypress(lambda: player.setheading(270), "Down")
screen.onkeypress(lambda: player.setheading(180), "Left")
screen.onkeypress(lambda: player.setheading(0), "Right")
screen.listen()

# Start moving the turtle
move()

# Start the main loop
turtle.mainloop()

