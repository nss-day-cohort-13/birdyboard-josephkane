import random

def random_id_generator():
	"""
	Generates a random 5-digit ID

	Args- None
	"""
	random_id = int((random.random() + 1) * 10000)
	return random_id