import uuid

def random_id_generator():
	"""
	Generates a random 5-digit ID

	Args- None
	"""
	random_id = uuid.uuid4()
	return random_id