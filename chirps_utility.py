from chirps import *
from main import *
from csv_utility import *
from user_utility import *
from random_id_generator import *

class ChirpsUtility:

	def view_chirps(public_convos, private_convos, chirps_dict, current_user):
		"""
		Prints out all public and private chirps that the current user is a part of

		Arg- chirps dictionary (from CSV file), currently selected user
		"""
		counter = 1
		chirps_id_list = list()
		if current_user != None:
			print("\n ~ PRIVATE CHIRPS ~ ")
			for k, v in private_convos.items():
				if chirps_dict[v[0]][1] == current_user.screen_name:
					print("{0}. {1}: {2}".format(counter, chirps_dict[v[0]][0], chirps_dict[v[0]][2]))
					chirps_id_list.append(v[0])
					counter += 1
				elif chirps_dict[v[0]][0] == current_user.screen_name:
					print("{0}. to {1}: {2}".format(counter, chirps_dict[v[0]][1], chirps_dict[v[0]][2]))
					chirps_id_list.append(v[0])
					counter += 1
			return ChirpsUtility.print_public_chirps(public_convos, chirps_id_list, chirps_dict, counter)
		else:
			return ChirpsUtility.print_public_chirps(public_convos, chirps_id_list, chirps_dict, counter)

	def print_public_chirps(public_convos, chirps_id_list, chirps_dict, counter):
		"""
		Loops through chirps dictionary and prints out each one
		Takes user input and sends back chirp id for the selected chirp

		Args- chirps dictionary, counter value post private chirps
		"""
		print("\n ~ PUBLIC CHIRPS ~ ")
		for k, v in public_convos.items():
			print("{0}. {1}: {2}".format(counter, chirps_dict[v[0]][0], chirps_dict[v[0]][1]))
			chirps_id_list.append(v[0])
			counter += 1
		print("\nSelect a chirp, or enter 'q' to quit")
		chirp = input("> ")
		try:
			print("selected chirp id: ", chirps_id_list[int(chirp) - 1])
			if int(chirp) <= counter:
				selected_chirp_id = chirps_id_list[int(chirp) - 1]
				return selected_chirp_id
			elif chirp == "q":
				show_menu()
		except IndexError as ex:
			print("\n{}".format(ex))
			print("Sorry, thats an invalid entry. Try again:\n")

	def new_public_chirp(current_user):
		"""
		Adds a new public chirp

		Args- currently selected user
		"""
		if current_user != None:
			print("\nEnter new public chirp:")
			user_input = input("> ")
			public_chirp = PublicChirp(
				user_input,
				current_user.screen_name,
				random_id_generator()
			)
			CSV.write_public_chirp_to_csv_file(public_chirp, "chirps.csv")
			return public_chirp
		else:
			print("\nPlease select a user first")

	def new_private_chirp(current_user, users_dict):
		"""
		Adds a new private chirp

		Args- currently selected user, dictionary of users
		"""
		if current_user != None:
			recipient = UserUtility.select_a_user(users_dict, current_user)
			print("\nEnter new private chirp:")
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
			print("\nPlease select a user first")
