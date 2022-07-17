import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "pong/assets/sounds/boing.wav"
WELCOME_SOUND = "pong/assets/sounds/start.wav"
OVER_SOUND = "pong/assets/sounds/over.wav"
MUSIC_SOUND = "pong/assets/sounds/MyMess.mp3"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
UP = "up"
DOWN = "down"
S = "s"
W = "w"
I = "i"
K = "k"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
START_GAME = 2
IN_PLAY = 3
GAME_OVERL = 4
GAME_OVERR = 5


# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP1 = "stats1"
STATS_GROUP2 = "stats2"
WINNING_POINTS = 5

# HUD
HUD_MARGIN = 15
SCORE_GROUP1 = "score1"
SCORE_GROUP2 = "score2"
SCORE_FORMAT_RACKET1 = "PLAYER LEFT: {}"
SCORE_FORMAT_RACKET2 = "PLAYER RIGHT: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pong/assets/images/001.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP_LEFT = "racketLeft"
RACKET_GROUP_RIGHT = "racketRight"
RACKET_IMAGES = [f"pong/assets/images/{n:03}.png" for n in range(300, 310)]
RACKET_IMAGES2 = [f"pong/assets/images/{n:03}.png" for n in range(320, 330)]
RACKET_WIDTH = 28 
RACKET_HEIGHT = 106 
RACKET_RATE = 10 
RACKET_VELOCITY = 9

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "LEFT: W/S          PRESS ENTER TO START          RIGHT: I/K"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAMEL = "RIGHT PLAYER WINS"
WAS_GOOD_GAMER = "LEFT PLAYER WINS"