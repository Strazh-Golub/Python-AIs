from pynput.keyboard import Key, Controller as c1
from pynput.mouse import Button, Controller as c2

from abc import ABC, abstractmethod

keyboard = c1()

mouse = c2()

class SAIEngine(ABC):

	def __init__(self, typeOfInput, pixels):
		self.typeOfInput = typeOfInput
		self.pixels = pixels

    def openProcess(self, process_name):
		self.process_name = process_name
        return exec(self.process_name + '.exe')

	@abstractmethod
    def processKeyboardInput(self):
		pass
		
	@abstractmethod
	def processMouseInput(self):
		pass
