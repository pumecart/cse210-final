from constants import *
from game.scripting.action import Action
from game.casting.music import Music


class PlayAction(Action):

    def __init__(self, audio_service, filename):
        self._audio_service = audio_service
        self._filename = filename
        
    def execute(self, cast, script, callback):
        sound = Music(self._filename)
        self._audio_service.play_sound(sound)
        script.remove_action(OUTPUT, self)