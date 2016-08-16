from conversation import *
import chirps_utility
from csv_utility import *
from random_id_generator import *

class ConvoUtility:

	def new_public_convo(chirp_id, current_user):
		"""
		Creates a new public conversation based on a chirp id

		Args- chirp id, current user
		"""
		if current_user != None:
			public_convo = PublicConvo(chirp_id, random_id_generator())
			return public_convo
		else:
			print("\nPlease select a user first")

	def new_private_convo(chirp_id, current_user):
		"""
		Creates a new public conversation based on a chirp id

		Args- chirp id, current user
		"""
		if current_user != None:
			private_convo = PrivateConvo(chirp_id, random_id_generator())
			return private_convo
		else:
			print("\nPlease select a user first")

	def show_public_reply_menu(chirp_list, convo_list, current_user):
		"""
		Allows users to reply to a selected chirp

		Args-
			list of all chirps,
			conversation selected chirp is a part of,
			currently selected user
		"""
		print("")
		for id_num in convo_list:
			print("{0}: {1}".format(chirp_list[id_num][0], chirp_list[id_num][1]))
		reply_chirp = chirps_utility.ChirpsUtility.new_public_chirp(current_user)
		convo_list.append(reply_chirp.chirp_id)
		return convo_list

	def show_private_reply_menu(chirp_dict, convo_list, current_user):
		"""
		Allows users to reply to a selected chirp

		Args-
			dict of all chirps,
			conversation selected chirp is a part of,
			currently selected user
		"""
		print("chirp list: ", chirp_dict)
		print("convo list: ", convo_list)
		for id_num in convo_list:
			print("\n{0}: {1}".format(chirp_dict[id_num][0], chirp_dict[id_num][1]))
		reply_chirp = chirps_utility.ChirpsUtility.new_private_chirp(current_user)
		convo_list.append(reply_chirp.chirp_id)
		return convo_list
