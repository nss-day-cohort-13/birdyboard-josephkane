from random_id_generator import *

class Conversation:

	def __init__(self, chirp_list, convo_id): # chirp_list is a list of chirp ids
		self.convo_id = convo_id
		self.chirp_list = chirp_list

class PublicConvo(Conversation):

	def __init__(self, chirp_list, convo_id):
		super().__init__(chirp_list, convo_id)
		self.permission = "public"

class PrivateConvo(Conversation):

	def __init__(self, chirp_list, convo_id):
		super().__init__(chirp_list, convo_id)
		self.permission = "private"
