import turtle

screen = turtle.Screen()
screen.setup(700, 700)
walls = []

def check(move):

    import colision_checker
    value = colision_checker.check(move, walls)

    return value

def create_walls():

#generating the walls

    for i in range(80):
        walls.append(0)
        walls[i] = turtle.Turtle()
        walls[i].speed('fastest')
        walls[i].hideturtle()
        walls[i].penup()
        walls[i].color('red')

#right wall

    for i in range(8):

        walls[i].goto(300, 262.5 - i*75)

#bottom wall


    for i in range(8):

        walls[i+8].goto(262.5 - i*75, -300)

#left wall

    for i in range(8):

        walls[i+16].goto(-300, -262.5 + i*75)

#top wall

    for i in range(7):

        walls[i+24].goto(-262.5 + i*75, 300)


#individual walls
#I must be honnest, I don't like how it's done this part.
#But by the way the maze is done, I don't know an easier way to do it.

    walls[31].goto(0, 262.5)
    walls[32].goto(262.5, 225)
    walls[33].goto(187.5, 225)
    walls[34].goto(112.5, 225)
    walls[35].goto(-37.5, 225)
    walls[36].goto(-112.5, 225)
    walls[37].goto(-187.5, 225)

    walls[38].goto(150, 187.5)
    walls[39].goto(75, 187.5)
    walls[40].goto(-75, 187.5)

    walls[41].goto(262.5, 150)
    walls[42].goto(37.5, 150)
    walls[43].goto(-187.5, 150)
    walls[44].goto(-262.5, 150)

    walls[45].goto(150, 112.5)
    walls[46].goto(-75, 112.5)

    walls[47].goto(187.5, 75)
    walls[48].goto(112.5, 75)
    walls[49].goto(-37.5, 75)
    walls[50].goto(-112.5, 75)
    walls[51].goto(-187.5, 75)

    walls[52].goto(225, 37.5)
    walls[53].goto(75, 37.5)
    walls[54].goto(0, 37.5)
    walls[55].goto(-225, 37.5)

    walls[56].goto(225, -37.5)
    walls[57].goto(150, -37.5)
    walls[58].goto(0, -37.5)
    walls[59].goto(-75, -37.5)
    walls[60].goto(-150, -37.5)

    walls[61].goto(37.5, -75)
    walls[62].goto(112.5, -75)
    walls[63].goto(-187.5, -75)
    walls[64].goto(-262.5, -75)

    walls[65].goto(75, -112.5)
    walls[66].goto(-75, -112.5)

    walls[67].goto(187.5, -150)
    walls[68].goto(37.5, -150)
    walls[69].goto(-37.5, -150)
    walls[70].goto(-187.5, -150)

    walls[71].goto(225, -187.5)
    walls[72].goto(150, -187.5)
    walls[73].goto(75, -187.5)
    walls[74].goto(-75, -187.5)
    walls[75].goto(-225, -187.5)

    walls[76].goto(-37.5, -225)
    walls[77].goto(-112.5, -225)

    walls[78].goto(150, -262.5)
    walls[79].goto(-225, -262.5)

