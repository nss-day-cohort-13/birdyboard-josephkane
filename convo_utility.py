from conversation import *
from csv_utility import *

class ConvoUtility:

	def new_public_convo(chirp_id, current_user):
		"""
		Creates a new public conversation based on a chirp id

		Args- chirp id, current user
		"""
		if current_user != None:
			public_convo = PublicConvo(chirp_id)
			CSV.write_public_convo_to_csv_file(public_convo, "convos.csv")
			return public_convo
		else:
			print("\nPlease select a user first")
