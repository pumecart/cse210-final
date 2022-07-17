from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class RacketLeft(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Racket
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._body.set_position(Point(25, (SCREEN_HEIGHT/2)))

    def get_animation(self):
        """Gets the racket's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the racket's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the racket using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)
    
    def stop_moving(self):
        """Stops the racket from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)

    def swing_up(self):
        """Steers the racket up"""
        velocity = Point(0, -RACKET_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_down(self):
        """Steers the racket down"""
        velocity = Point(0, RACKET_VELOCITY)
        self._body.set_velocity(velocity)