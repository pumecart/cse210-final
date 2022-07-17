from constants import *
from game.casting.actor import Actor
from game.casting.stats_racket1 import Stats_Racket1


class Stats_Racket2(Stats_Racket1):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._score = 0


    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score  

    def reset(self):
        """Resets the stats back to their default values."""
        self._score = 0