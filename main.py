import turtle as t
from random import randint

screen = t.Screen()
race_is_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")

if user_bet:
    race_is_on = True

colors = ["red", "black", "blue", "gold", "green", "magenta", "aquamarine", "pink"]
turtles = []

# generate turtles and place at starting line
for i in range(140, -170, -40):
    new_turtle = t.Turtle()
    new_turtle.color(colors.pop())
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=i)
    turtles.append(new_turtle)
  

# draw finish line 
timmy = t.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.goto(210, 200)
timmy.right(90)

for _ in range(40):
    timmy.dot(5, "black")
    timmy.forward(10)

# race loop 
while race_is_on:
    for turtle in turtles:
        turtle.forward(randint(0,10))
        if turtle.position()[0] >= 210:
            if turtle.color()[0].lower() == user_bet.lower():
                print(f"You won! {user_bet} won the ravce.")
            else:
                print(f"You lost! {turtle.color()[0]} is the winner.")
            race_is_on = False
            break

screen.exitonclick()
