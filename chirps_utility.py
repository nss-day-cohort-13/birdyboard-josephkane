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

	def print_public_chirps(chirps_dict, counter):
		"""
		Loops through chirps dictionary and prints out each one

		Args- chirps dictionary, counter value post private chirps
		"""
		print(" ~ PUBLIC CHIRPS ~ ")
		chirps_id_list = list()
		for k, v in chirps_dict.items():
			if v[2] == "public":
				print("{0}. {1}: {2}".format(counter, v[0], v[1]))
				chirps_id_list.append(k)
				counter += 1

	def new_public_chirp(current_user):
		"""
		Adds a new public chirp

		Args- currently selected user
		"""
		if current_user != None:
			print("")
			print("Enter new public chirp:")
			user_input = input("> ")
			public_chirp = PublicChirp(
				user_input,
				current_user.screen_name,
				random_id_generator()
			)
			CSV.write_public_chirp_to_csv_file(public_chirp, "chirps.csv")
			return public_chirp
		else:
			print("")
			print("Please select a user first")

	def new_private_chirp(current_user, users_dict):
		"""
		Adds a new private chirp

		Args- currently selected user, dictionary of users
		"""
		if current_user != None:
			print("")
			recipient = UserUtility.select_a_user(users_dict, current_user)
			print("Enter new private chirp:")
			user_input = input("> ")
			private_chirp = PrivateChirp(
				user_input,
				current_user.screen_name,
				recipient.screen_name,
				random_id_generator()
			)
			CSV.write_private_chirp_to_csv_file(private_chirp, "chirps.csv")
			return private_chirp
		else:
			print("")
			print("Please select a user first")
