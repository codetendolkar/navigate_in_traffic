import math

# Media #
CAR_IMAGE_GREY_H = "simulator/media/images/car-red.png"
CAR_IMAGE_WHITE_H = "simulator/media/images/car-grey.png"
BACKGROUND_IMAGE = "simulator/media/images/grass.png"
COW_IMAGE_0 = "simulator/media/images/cow0.png"
STOP_SIGN_IMAGE = "simulator/media/images/stop.png"
POTHOLE_IMAGE = "simulator/media/images/stop.png"


# Cow #
COW_SPEED = 1


# Simulation Params #
NUM_LANES = 5
NUM_ORDINARY_CARS = 5
NUM_INTELLIGENT_CARS = 1
SIM_DT = 0.1
LANE_WIDTH = 4

# Car #
GAS_PEDAL_TO_ACC = 1
BRAKE_PEDAL_TO_DEACC = 1

# Road #
ROAD_DRAG_COEFF = 0.05
INFINITE_ROAD_MAX_LENGTH = 100000
NUM_POTHOLES_PER_M = 0.004
CROSSING_WIDTH = 50
ROAD_CROSSING_IMAGE = "simulator/media/images/crossing.png"

# Display #
PIXELS_PER_METER = 10
SCREEN_WIDTH = NUM_LANES*LANE_WIDTH*2*PIXELS_PER_METER
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
ROAD_GREY = (255,255,255)#(43, 43, 43)
WHITE = (43, 43, 43)
PIXEL_PER_METER = 5
CAR_LENGTH = 6
CAR_WIDTH = 3

# Safety #
CAR_SAFETY_DIST = 100
CAR_CUE_SAFETY_DIST = 50
CAR_HURDLE_SAFETY_DIST = 50
CAR_SHOULD_STOP_BEFORE = 10
CAR_MAX_ACCELERATION = 5
CAR_SMOOTH_BRAKE = 8
CAR_HARD_BRAKE = 15
CAR_MAX_SAFE_VEL = 25.0
CAR_COLLISION_D = 10
CAR_RULE_VIOLATION_D = 4
CAR_MAX_STEERING = 40*math.pi/1800
CAR_MAX_BRAKE = 10

# Cow #
COW_FOV_Y = 10*PIXEL_PER_METER

# Object types #
CUE = 'cue'
VEHICLE = 'vehicle'
HURDLE = 'hurdle'
ROW_OBJECT = 'row_object'

# RL #
ALPHA = -100 # Collisions
BETA = -20 # Traffic violations
GAMMA = 1 # Distance covered
DELTA = -0.5 # Very slow speed cost





MIN_HEADING = 0
MAX_HEADING = 2*math.pi
MIN_SPEED = 0
MAX_SPEED = CAR_MAX_SAFE_VEL*2
MIN_DISTANCE = 0
MAX_DISTANCE = CAR_SAFETY_DIST*2
