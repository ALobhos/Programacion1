import turtle
screen = turtle.Screen()

def remake(register):

    screen.clear()

    import easy_maze

    easy_maze.draw()

#creating a replay player

    player = turtle.Turtle()
    player.hideturtle()
    player.color('red')
    player.penup()
    player.shape('circle')
    player.goto(-262.5, -262.5)
    player.showturtle()
    player.pendown()
    player.speed('slowest')

#replaying the game from the register

    for i in range(len(register)):

        if register[i] == 'U':
            player.sety(player.ycor() + 75)

        elif register[i] == 'D':
            player.sety(player.ycor() - 75)

        elif register[i] == 'R':
            player.setx(player.xcor() + 75)

        else:
            player.setx(player.xcor() - 75)

    screen.title("Thanks for playing")
    screen.textinput("Thanks for playing", "Press enter to exit")
    turtle.bye()
    exit()
