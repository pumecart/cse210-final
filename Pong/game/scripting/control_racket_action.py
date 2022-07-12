from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racketLeft = cast.get_first_actor(RACKET_GROUP_LEFT)
        racketRight = cast.get_first_actor(RACKET_GROUP_RIGHT)
        if self._keyboard_service.is_key_down(W): 
            racketLeft.swing_up()
        elif self._keyboard_service.is_key_down(S): 
            racketLeft.swing_down()
        elif self._keyboard_service.is_key_down(I): 
            racketRight.swing_up()
        elif self._keyboard_service.is_key_down(K): 
            racketRight.swing_down()
        else: 
            racketLeft.stop_moving()
            racketRight.stop_moving()

        
        
        
   
            
           