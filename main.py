from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)

user_bet=screen.textinput(title="Make a bet",prompt="which turtle will win the race: Type a color: ")
colors=['red','yellow','blue','black','pink','green']
y=[-70,-40,-10,20,50,80]
turtles=[]
for x in range(6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[x])
    tim.goto(-230,y[x])
    turtles.append(tim)

is_game_on=False

if user_bet in colors:
    is_game_on=True

while is_game_on:
    for turtle in turtles:
        distance=random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you won, The winning turtle is:{winning_color}")
            else:
                print(f"you lose, The winning turtle is:{winning_color}")
            is_game_on=False

screen.exitonclick()