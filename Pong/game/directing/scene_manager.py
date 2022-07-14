import csv
from constants import *
from game.casting.animation import Animation
from game.casting.ball import Ball
from game.casting.body import Body
# from game.casting.brick import Brick
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.racketLeft import RacketLeft
from game.casting.racketRight import RacketRight
from game.casting.stats_racket1 import Stats_Racket1
from game.casting.stats_racket2 import Stats_Racket2
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
# from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
# from game.scripting.collide_brick_action import CollideBrickAction
from game.scripting.collide_racket_action import CollideRacketAction
from game.scripting.control_racket_action import ControlRacketAction
from game.scripting.draw_ball_action import DrawBallAction
# from game.scripting.draw_bricks_action import DrawBricksAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    # CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    # COLLIDE_BRICKS_ACTION = CollideBrickAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE)
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    # DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_RACKET_ACTION = MoveRacketAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVERL:    
            self._prepare_game_overL(cast, script)
        elif scene == GAME_OVERR:    
            self._prepare_game_overR(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats_racket1(cast)
        self._add_stats_racket2(cast)
        # self._add_level(cast)
        # self._add_lives(cast)
        self._add_score_racket1(cast)
        self._add_score_racket2(cast)
        self._add_ball(cast)
        # self._add_bricks(cast)
        self._add_racket_left(cast)
        self._add_racket_right(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_ball(cast)
        # self._add_bricks(cast)
        self._add_racket_left(cast)
        self._add_racket_right(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, MUSIC_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_ball(cast)
        self._add_racket_left(cast)
        self._add_racket_right(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_RACKET_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_overL(self, cast, script):
        self._add_ball(cast)
        #self._left(cast)
        self._add_dialog(cast, WAS_GOOD_GAMEL)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)
    
    def _prepare_game_overR(self, cast, script):
        self._add_ball(cast)
        #self._left(cast)
        self._add_dialog(cast, WAS_GOOD_GAMER)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # Casting Methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()

    def _add_ball(self, cast):
        cast.clear_actors(BALL_GROUP)
        x = CENTER_X - BALL_WIDTH / 2
        y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_score_racket1(self, cast):
        cast.clear_actors(SCORE_GROUP1)
        text = Text(SCORE_FORMAT_RACKET1, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        # position = Point(CENTER_X, HUD_MARGIN)
        position = Point(0 + HUD_MARGIN, HUD_MARGIN)
        label1 = Label(text, position)
        cast.add_actor(SCORE_GROUP1, label1)

    def _add_score_racket2(self, cast):
        cast.clear_actors(SCORE_GROUP2)
        text = Text(SCORE_FORMAT_RACKET2, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label2 = Label(text, position)
        cast.add_actor(SCORE_GROUP2, label2)

    def _add_stats_racket1(self, cast):
        cast.clear_actors(STATS_GROUP1)
        stats = Stats_Racket1()
        cast.add_actor(STATS_GROUP1, stats)

    def _add_stats_racket2(self, cast):
        cast.clear_actors(STATS_GROUP2)
        stats = Stats_Racket2()
        cast.add_actor(STATS_GROUP2, stats)

    def _add_racket_left(self, cast):
        cast.clear_actors(RACKET_GROUP_LEFT)
        x = CENTER_X - RACKET_WIDTH / 2
        y = SCREEN_HEIGHT - RACKET_HEIGHT
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES, RACKET_RATE)
        racket = RacketLeft(body, animation)
        cast.add_actor(RACKET_GROUP_LEFT, racket)

    def _add_racket_right(self, cast):
        cast.clear_actors(RACKET_GROUP_RIGHT)
        x = CENTER_X - RACKET_WIDTH / 2
        y = SCREEN_HEIGHT - RACKET_HEIGHT
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES2, RACKET_RATE)
        racket = RacketRight(body, animation)
        cast.add_actor(RACKET_GROUP_RIGHT, racket)
        

    # ----------------------------------------------------------------------------------------------
    # Scripting Methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)