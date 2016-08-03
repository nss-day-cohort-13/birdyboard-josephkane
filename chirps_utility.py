from chirps import *
from csv_utility import *
from user_utility import *
from random_id_generator import *

class ChirpsUtility:

	def view_chirps(chirps_dict, current_user):
		"""
		Prints out all public and private chirps that the current user is a part of

		Arg- chirps dictionary (from CSV file), currently selected user
		"""
		counter = 1
		if current_user != None:
			print("")
			print(" ~ PRIVATE CHIRPS ~ ")
			for k, v in chirps_dict.items():
				if v[1] == current_user.screen_name:
					print("{0}. {1}: {2}".format(counter, v[0], v[2]))
					counter += 1
			print("")
			ChirpsUtility.print_public_chirps(chirps_dict, counter)
		else:
			ChirpsUtility.print_public_chirps(chirps_dict, counter)

	def print_chirps(chirps_dict, counter):
		"""
		Loops through chirps dictionary and prints out each one

		Args- chirps dictionary, counter value post private chirps
		"""



	def new_chirp(current_user, private=False):
		"""
		Adds a new public chirp

		Args- currently selected user
		"""
		if current_user != None:
			if private == True:
				print("")
				print("Chirp at who?")
				recipient = UserUtility.select_a_user(current_user)
				print("")
				print("Enter new chirp:")
				user_input = input("> ")
				chirp = Chirp(
					user_input,
					current_user.screen_name,
					random_id_generator(),
					private=True,
					recipient=recipient
				)
			else:
				print("")
				print("Enter new chirp:")
				user_input = input("> ")
				chirp = Chirp(
					user_input,
					current_user.screen_name,
					random_id_generator()
				)
			CSV.write_chirp_to_csv_file(chirp, "chirps.csv")
			return chirp

		else:
			print("")
			print("Please select a user first")

