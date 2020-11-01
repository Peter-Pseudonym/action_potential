HEIGHT, WIDTH = 500, 500
ION_WIDTH = 10

MEMBRANE_START_Y, MEMBRANE_END_Y = 225, 275

R, T, z, F = 1.98, 310, 1, 2.34*(10**4)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (200, 0, 0)
BLUE = (200, 200, 255)
GREEN = (0, 200, 0)

SODIUM_COL = (255, 100, 255)
POTASSIUM_COL = (100, 100, 255)
CHLORINE_COL = (160, 200, 200)

SODIUM_CHANNEL_COL = (225, 75, 225)
POTASSIUM_CHANNEL_COL = (75, 75, 225)
CHLORINE_CHANNEL_COL = (120, 150, 150)

CHANNEL_NUM = 3

ION_CHOICES = ['Na', 'K', 'Cl-']
ION_CHARGES = {'Na': 1, 'K': 1, 'Cl-': -1}
ION_COLORS = {'Na': SODIUM_COL, 'K': POTASSIUM_COL, 'Cl-': CHLORINE_COL}
CHANNEL_COLORS = {'Na': SODIUM_CHANNEL_COL, 'K': POTASSIUM_CHANNEL_COL, 'Cl-': CHLORINE_CHANNEL_COL}

MIN_DT, MAX_DT = 1, 20

SCROLL_BAR_START_X, SCROLL_BAR_START_Y = 50, HEIGHT - 50
SCROLL_BAR_WIDTH, SCROLL_BAR_HEIGHT = 10*(MAX_DT-MIN_DT), 25
SCROLL_BAR_COLOR = GREEN

SCROLL_CIRCLE_RAD = 25
SCROLL_CIRCLE_COLOR = GRAY

def clamp(val, minval, maxval):
	return min(max(minval, val), maxval)