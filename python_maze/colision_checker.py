import turtle

def check(move, walls):

    collision = False
    for i in range(80):

        if move == walls[i].position():

            collision = True

    return collision
