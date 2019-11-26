import pygame
import numpy as np

pygame.init()

class Input():
	def __init__(self):
		super(Input, self).__init__()


	def getKeyboard(self, key):
		return pygame.key.get_pressed()[key]

class SAIEngine():

	def __init__(self, typeOfInput, pixels):
		self.typeOfInput = typeOfInput
		self.pixels = pixels

    def openProcess(self, process_name):
		self.process_name = process_name
        return exec(self.process_name + '.exe')

    def processInput(self, typeOfInput):
		self.typeOfInput = typeOfInput
		self.typeOfInput.
