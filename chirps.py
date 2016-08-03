class Chirp:

	def __init__(self, message, author, chirp_id):
		self.message = message
		self.author = author
		self.chirp_id = chirp_id

class PublicChirp(Chirp):

	def __init__(self, message, author, chirp_id):
		super().__init__(message, author, chirp_id)
		self.permission = "public"

class PrivateChirp(Chirp):

	def __init__(self, message, author, recipient, chirp_id):
		super().__init__(message, author, chirp_id)
		self.permission = "private"
		self.recipient = recipient

