class Chirp:

	def __init__(self, message, author, chirp_id, private=False, recipient=None):
		self.message = message
		self.author = author
		self.chirp_id = chirp_id
		self.private = private
		self.recipient = recipient
