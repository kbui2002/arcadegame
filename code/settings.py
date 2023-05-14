# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
ANIMATION_SPEED = 8

# editor graphics 
EDITOR_DATA = {
	0: {"style": "player", "type": "object", "menu": None, "menu_surf": None, "preview": None, "graphics": "./graphics/player/idle_right"},
	1: {"style": "sky",    "type": "object", "menu": None, "menu_surf": None, "preview": None, "graphics": None},
	
	2: {"style": "terrain", "type": "tile", "menu": "terrain", "menu_surf": "./graphics/menu/land.png",  "preview": "./graphics/preview/land.png",  "graphics": None},
	3: {"style": "water",   "type": "tile", "menu": "terrain", "menu_surf": "./graphics/menu/water.png", "preview": "./graphics/preview/water.png", "graphics": "./graphics/terrain/water/animation"},
	
	4: {"style": "coin", "type": "tile", "menu": "coin", "menu_surf": "./graphics/menu/banana.png","preview": "./graphics/preview/banana.png",    "graphics": "./graphics/items/banana"},
	5: {"style": "coin", "type": "tile", "menu": "coin", "menu_surf": "./graphics/menu/melon.png","preview": "./graphics/preview/melon.png",  "graphics":"./graphics/items/melon"},
	6: {"style": "coin", "type": "tile", "menu": "coin", "menu_surf": "./graphics/menu/orange.png","preview": "./graphics/preview/orange.png", "graphics":"./graphics/items/orange"},

	7:  {"style": "enemy", "type": "tile", "menu": "enemy", "menu_surf": "./graphics/menu/spikes.png","preview": "./graphics/preview/spikes.png","graphics":"./graphics/enemies/spikes"},
	8:  {"style": "enemy", "type": "tile", "menu": "enemy", "menu_surf": "./graphics/menu/hunter.png", "preview": "./graphics/preview/hunter.png","graphics":"./graphics/enemies/hunter/idle"},
	9:  {"style": "enemy", "type": "tile", "menu": "enemy", "menu_surf": "./graphics/menu/shell_left.png","preview": "./graphics/preview/shell_left.png","graphics":"./graphics/enemies/shell_left/idle"},
	10: {"style": "enemy", "type": "tile", "menu": "enemy", "menu_surf": "./graphics/menu/shell_right.png","preview": "./graphics/preview/shell_right.png", "graphics":"./graphics/enemies/shell_right/idle"},
	
	11: {"style": "palm_fg", "type": "object", "menu": "palm fg", "menu_surf": "./graphics/menu/small_fg.png", "preview": "./graphics/preview/small_fg.png", "graphics":"./graphics/terrain/palm/small_fg"},
	12: {"style": "palm_fg", "type": "object", "menu": "palm fg", "menu_surf": "./graphics/menu/large_fg.png", "preview": "./graphics/preview/large_fg.png", "graphics":"./graphics/terrain/palm/large_fg"},
	13: {"style": "palm_fg", "type": "object", "menu": "palm fg", "menu_surf": "./graphics/menu/left_fg.png",  "preview": "./graphics/preview/left_fg.png",  "graphics":"./graphics/terrain/palm/left_fg"},
	14: {"style": "palm_fg", "type": "object", "menu": "palm fg", "menu_surf": "./graphics/menu/right_fg.png", "preview": "./graphics/preview/right_fg.png", "graphics":"./graphics/terrain/palm/right_fg"},

	15: {"style": "palm_bg", "type": "object", "menu": "palm bg", "menu_surf": "./graphics/menu/small_bg.png", "preview": "./graphics/preview/small_bg.png", "graphics":"./graphics/terrain/palm/small_bg"},
	16: {"style": "palm_bg", "type": "object", "menu": "palm bg", "menu_surf": "./graphics/menu/large_bg.png", "preview": "./graphics/preview/large_bg.png", "graphics":"./graphics/terrain/palm/large_bg"},
	17: {"style": "palm_bg", "type": "object", "menu": "palm bg", "menu_surf": "./graphics/menu/left_bg.png",  "preview": "./graphics/preview/left_bg.png",  "graphics":"./graphics/terrain/palm/left_bg"},
	18: {"style": "palm_bg", "type": "object", "menu": "palm bg", "menu_surf": "./graphics/menu/right_bg.png", "preview": "./graphics/preview/right_bg.png", "graphics":"./graphics/terrain/palm/right_bg"},

	19: {"style": "coin","type":"tile", "menu": "coin" , "menu_surf": "./graphics/menu/flag.png",  "preview": "./graphics/preview/flag.png",  "graphics": "./graphics/items/flag"},
 
	20: {"style": "save", "type": "tile", "menu":"save", "menu_surf": "./graphics/menu/save.png", "preview": None, "graphics": None},
    21: {"style": "load", "type": "tile", "menu":"load", "menu_surf": "./graphics/menu/load.png", "preview": None, "graphics": None},
 
}

NEIGHBOR_DIRECTIONS = {
	"A": (0,-1),
	"B": (1,-1),
	"C": (1,0),
	"D": (1,1),
	"E": (0,1),
	"F": (-1,1),
	"G": (-1,0),
	"H": (-1,-1)
}

LEVEL_LAYERS = {
	"clouds": 1,
	"ocean": 2,
	"bg": 3,
	"water": 4,
	"main": 5
}

# colors 
SKY_COLOR = "#cbecfb" #33CCFF"
SEA_COLOR = "#92a9ce"
HORIZON_COLOR = "#f5f1de"
LINE_COLOR = "black"
BUTTON_BG_COLOR = "#33323d"
BUTTON_LINE_COLOR = "#f5f1de"