from random_id_generator import *

class Conversation:

	def __init__(self, chirp_list): # chirp_list is a list of chirp ids
		self.convo_id = random_id_generator()
		self.chirp_list = chirp_list

class PublicConvo(Conversation):

	def __init__(self, chirp_list):
		super().__init__(chirp_list)
		self.permission = "public"

class PrivateConvo(Conversation):

	def __init__(self, chirp_list):
		super().__init__(chirp_list)
		self.permission = "private"