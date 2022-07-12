from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racketLeft = cast.get_first_actor(RACKET_GROUP_LEFT)
        body = racketLeft.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        # x = position.get_x()
        y = position.get_y()
        
        position = position.add(velocity)

        # if x < 0:
        #     position = Point(0, position.get_y())
        # elif x > (SCREEN_WIDTH - RACKET_WIDTH):
        #     position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
        if y < 0:
            position = Point(position.get_x(), 0)
        elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
             position = Point(position.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
            
        body.set_position(position)
        
        racketRight = cast.get_first_actor(RACKET_GROUP_RIGHT)
        bodyR = racketRight.get_body()
        velocityR = bodyR.get_velocity()
        positionR = bodyR.get_position()
        # x = position.get_x()
        yR = positionR.get_y()
        
        positionR = positionR.add(velocityR)

        # if x < 0:
        #     position = Point(0, position.get_y())
        # elif x > (SCREEN_WIDTH - RACKET_WIDTH):
        #     position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
        if yR < 0:
            positionR = Point(positionR.get_x(), 0)
        elif yR > (SCREEN_HEIGHT - RACKET_HEIGHT):
             position = Point(positionR.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
            
        bodyR.set_position(positionR)