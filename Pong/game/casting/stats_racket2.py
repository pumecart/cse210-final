from constants import *
from game.casting.actor import Actor
from game.casting.stats_racket1 import Stats_Racket1


class Stats_Racket2(Stats_Racket1):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._score = 0
