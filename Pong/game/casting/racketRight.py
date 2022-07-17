from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.racketLeft import RacketLeft


class RacketRight(RacketLeft):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new racket
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(body, animation)
        self._body.set_position(Point((SCREEN_WIDTH - 50), (SCREEN_HEIGHT/2)))
