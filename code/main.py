import pygame, sys
from pygame.math import Vector2 as vector
from settings import *
from support import *
from pygame.mouse import get_pos as mouse_pos
from pygame.mouse import get_pressed as mouse_buttons
from pygame.image import load
from os import walk
from editor import Editor
from level import Level

from os import walk

class Main:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		self.imports()
  
		self.editor_active = True
		self.transition = Transition(self.toggle)
		self.editor = Editor(self.land_tiles, self.switch)
		self.start = True
		# cursor 
		surf = load('./graphics/cursors/mouse.png').convert_alpha()
		cursor = pygame.cursors.Cursor((0,0), surf)
		pygame.mouse.set_cursor(cursor)

	def imports(self):
		# terrain
		self.land_tiles = import_folder_dict('./graphics//terrain/land')
		self.water_bottom = load('./graphics/terrain/water/water_bottom.png').convert_alpha()
		self.water_top_animation = import_folder('./graphics//terrain/water/animation')

		# coins
		self.gold = import_folder('./graphics/items//banana')
		self.silver = import_folder('./graphics/items/melon')
		self.diamond = import_folder('./graphics/items/orange')
		self.flag = import_folder('./graphics/items//flag')
		self.particle = import_folder('./graphics/items/particle')

		# palm trees
		self.palms = {folder: import_folder(f'./graphics/terrain/palm/{folder}') for folder in list(walk('./graphics/terrain/palm'))[0][1]}

		# enemies
		self.spikes = load('./graphics/enemies/spikes/spikes.png').convert_alpha()
		self.hunter = {folder:import_folder(f'./graphics/enemies/hunter/{folder}') for folder in list(walk('./graphics/enemies//hunter'))[0][1]}
		self.shell = {folder:import_folder(f'./graphics/enemies/shell_left/{folder}') for folder in list(walk('./graphics/enemies/shell_left'))[0][1]}
		self.pearl = load('./graphics/enemies/pearl/pearl.png').convert_alpha()

		# player
		self.player_graphics = {folder: import_folder(f'./graphics/player/{folder}') for folder in list(walk('./graphics/player'))[0][1]}

		# clouds
		self.clouds = import_folder('./graphics/clouds')

		# sounds
		self.level_sounds = {
			'coin': pygame.mixer.Sound('./audio/coin.wav'),
			'hit': pygame.mixer.Sound('./audio/hit.wav'),
			'jump': pygame.mixer.Sound('./audio/jump.wav'),
			'music': pygame.mixer.Sound('./audio/SuperHero.wav'),
  		}

	def toggle(self):
		self.editor_active = not self.editor_active
		if self.editor_active:
			self.editor.editor_music.play()

	def switch(self, grid = None):
		self.transition.active = True
		if grid:
			self.level = Level(
				grid, 
				self.switch,{
					'land': self.land_tiles,
					'water bottom': self.water_bottom,
					'water top': self.water_top_animation,
					'gold': self.gold,
					'silver': self.silver,
					'diamond': self.diamond,
					'flag': self.flag,
					'particle': self.particle,
					'palms': self.palms,
					'spikes': self.spikes,
					'hunter': self.hunter,
					'shell': self.shell,
					'player': self.player_graphics,
					'pearl': self.pearl,
					'clouds': self.clouds},
				self.level_sounds)

	def run(self):
		if self.start:
				self.display_surface.blit(load("./graphics/menu/start.png"),(0,0))
		run = True
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[0]:
					x = mouse_pos()[0]
					y = mouse_pos()[1]

					if 410 <= x <= 852 and 69 <= y <= 257:
						run = False
			pygame.display.update()
   
		while True:
			dt = self.clock.tick() / 1000
			if self.editor_active:
				self.editor.run(dt)
			else:
				self.level.run(dt)
			self.transition.display(dt)
			pygame.display.update()


class Transition:
	def __init__(self, toggle):
		self.display_surface = pygame.display.get_surface()
		self.toggle = toggle
		self.active = False

		self.border_width = 0
		self.direction = 1
		self.center = (WINDOW_WIDTH /2, WINDOW_HEIGHT / 2)
		self.radius = vector(self.center).magnitude()
		self.threshold = self.radius + 100

	def display(self, dt):
		if self.active:
			self.border_width += 1000 * dt * self.direction
			if self.border_width >= self.threshold:
				self.direction = -1
				self.toggle()
			
			if self.border_width < 0:
				self.active = False
				self.border_width = 0
				self.direction = 1
			pygame.draw.circle(self.display_surface, 'black',self.center, self.radius, int(self.border_width))

if __name__ == '__main__':
	main = Main()
	main.run() 