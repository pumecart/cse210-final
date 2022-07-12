from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        racketLeft = cast.get_first_actor(RACKET_GROUP_LEFT)
        body = racketLeft.get_body()

        if racketLeft.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = racketLeft.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        racketRight = cast.get_first_actor(RACKET_GROUP_RIGHT)
        bodyR = racketRight.get_body()

        if racketRight.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = racketRight.get_animation()
        image = animation.next_image()
        positionR = bodyR.get_position()
        self._video_service.draw_image(image, positionR)