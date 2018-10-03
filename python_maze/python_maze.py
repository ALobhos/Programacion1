import turtle
import easy_maze
import wall_creator
import replay
import colision_checker


def maincore():

    screen = turtle.Screen()
    screen.clear()
    screen.setup(700, 700)
    register = []

    screen.title("Loading...")

#playground
    easy_maze.draw()

#invisible walls
    wall_creator.create_walls()

#victory goal
    goal = turtle.Turtle()
    goal.shape('turtle')
    goal.color('green')
    goal.penup()
    goal.goto(262.5, 337.5)

    def checkwin():

        if player.position() == goal.position():

            plays = ("Total movements: ", len(register))
            screen.title('¡VICTORY!')
            screen.textinput("¡You win!", plays)
            option = screen.numinput(
                '¡You Win!',
                'What do yo want to do?: (1)Review game (2)Play again (3)Exit',
                None, 1, 3)

            if option == 1:
               replay.remake(register)

            elif option == 2:
                screen.clear()
                screen.reset()
                maincore()

            else:
                turtle.bye()
                exit()

#Player

    player = turtle.Turtle()
    player.hideturtle()
    player.color('red')
    player.penup()
    player.shape('circle')
    player.goto(-262.5, -262.5)
    player.showturtle()

    screen.title("Play!")

#move commands and wall checks

    def move_left():

        intention = player.position() - (37.5, 0)
        wall = wall_creator.check(intention)

        if wall:
            pass

        else:
            player.setx(player.xcor() - 75)
            register.append('L')
            checkwin()

    def move_right():

        intention = player.position() + (37.5, 0)
        wall = wall_creator.check(intention)

        if wall:
            pass

        else:
            player.setx(player.xcor() + 75)
            register.append('R')
            checkwin()

    def move_up():

        intention = player.position() + (0, 37.5)
        wall = wall_creator.check(intention)

        if wall:
            pass

        else:
            player.sety(player.ycor() + 75)
            register.append('U')
            checkwin()

    def move_down():

        intention = player.position() - (0, 37.5)
        wall = wall_creator.check(intention)

        if wall:
            pass

        else:
            player.sety(player.ycor() - 75)
            register.append('D')
            checkwin()

    screen.textinput("Instructions", "Use the arrow keys to move arround")
    screen.listen()

    screen.onkeypress(move_left, 'Left')
    screen.onkeypress(move_right, 'Right')
    screen.onkeypress(move_up, 'Up')
    screen.onkeypress(move_down, 'Down')

    screen.mainloop()


def credits():

#basic setup
    screen = turtle.Screen()
    screen.clear()
    screen.setup(500, 500)
    screen.title("Credits")
    turtle.penup()
    turtle.hideturtle()
    turtle.speed('slowest')


#position of the pen and writing

    turtle.goto(0, 200)
    turtle.write("Made on Python 3.6.6\n", False, align="center")

    turtle.goto(0, 150)
    turtle.write("By Arturo Adolfo Lobos Castillo\n",
                 False, align="center", font=('Arial', 16, "bold"))

    turtle.goto(0, 100)
    turtle.write("Professor: Fabio Duran Verdugo\n",
                 False, align="center", font=('Arial', 16, "bold"))

    turtle.goto(0, 50)
    turtle.write("Civil engineer in bioinformatics\n",
                 False, align="center", font=('Arial', 16, "bold"))

    turtle.goto(0, 0)
    turtle.write("October 2nd 2018\n", False, align="center")

    turtle.goto(0, -100)
    turtle.write("Press M to return to main tittle\n",
                 False, align="center")

    screen.listen()
    screen.onkeypress(maintitle, 'm')
    screen.mainloop()


def maintitle():

#starting setup and options
    screen = turtle.Screen()
    screen.clear()
    screen.setup(500, 500)
    screen.bgpic("title.gif")
    screen.title("Python Maze")

    screen.listen()

    screen.onkeypress(maincore, 'p')
    screen.onkeypress(credits, 'c')
    screen.mainloop()

maintitle()
