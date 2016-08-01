import random
import csv

class User:

	def __init__(self):
		self.screen_name = None
		self.full_name = None
		self.user_id = None

	def random_id_generator(self):
		random_id = int((random.random() + 1) * 10000)
		return random_id
