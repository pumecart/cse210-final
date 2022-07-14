from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        # Movement for the left racket
        racketLeft = cast.get_first_actor(RACKET_GROUP_LEFT)
        body = racketLeft.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        y = position.get_y()
        
        position = position.add(velocity)

        if y < 50:
            position = Point(position.get_x(), 50)
        elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
             position = Point(position.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
            
        body.set_position(position)
        
        # Movement for the right racket
        racketRight = cast.get_first_actor(RACKET_GROUP_RIGHT)
        bodyRight = racketRight.get_body()
        velocityR = bodyRight.get_velocity()
        positionRight = bodyRight.get_position()
        yRight = positionRight.get_y()
        
        positionRight = positionRight.add(velocityR)

        if yRight < 50:
            positionRight = Point(positionRight.get_x(), 50)
        elif yRight > (SCREEN_HEIGHT - RACKET_HEIGHT):
             positionRight = Point(positionRight.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
            
        bodyRight.set_position(positionRight)