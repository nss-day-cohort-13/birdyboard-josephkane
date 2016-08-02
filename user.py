import random
import csv

class User:

	def __init__(self, full_name, screen_name):
		self.screen_name = screen_name
		self.full_name = full_name
		self.user_id = self.random_id_generator()

	def random_id_generator(self):
		random_id = int((random.random() + 1) * 10000)
		return random_id
