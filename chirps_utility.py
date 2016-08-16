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
		# counter and empty list to be used for convo select
		# (display counter as choice number, append each convo to convo_id_list,
		# convo int(counter - 1) to find convo in convo_id_list by index
		counter = 1
		convo_id_list = list()
		# if a user is signed in
		if current_user != None:
			try:
				print("\n ~ PRIVATE CHIRPS ~ ")
				for convo_key, chirps_list in private_convos.items():
					# chirp info that started convo
					convo_start = chirps_list[0]
					# if current user is the recipient of a private chirp
					if chirps_dict[convo_start][1] == current_user.screen_name:
						print("{0}. {1}: {2}".format(counter, chirps_dict[convo_start][0], chirps_dict[convo_start][2]))
						convo_id_list.append(convo_key, "private")
						counter += 1
					# if current user sent a private chirp
					elif chirps_dict[convo_start][0] == current_user.screen_name:
						print("{0}. to {1}: {2}".format(counter, chirps_dict[convo_start][1], chirps_dict[convo_start][2]))
						convo_id_list.append([convo_key, "private"])
						counter += 1
				# print all public chirps
				return ChirpsUtility.print_public_chirps(public_convos, convo_id_list, chirps_dict, counter)
			except AttributeError:
				return ChirpsUtility.print_public_chirps(public_convos, convo_id_list, chirps_dict, counter)
			except KeyError:
				return ChirpsUtility.print_public_chirps(public_convos, convo_id_list, chirps_dict, counter)
		else:
			return ChirpsUtility.print_public_chirps(public_convos, convo_id_list, chirps_dict, counter)

	def print_public_chirps(public_convos, convo_id_list, chirps_dict, counter):
		"""
		Loops through chirps dictionary and prints out each one
		Takes user input and sends back chirp id for the selected chirp

		Args- chirps dictionary, counter value post private chirps
		"""
		print("\n ~ PUBLIC CHIRPS ~ ")
		for convo_key, chirps_list in public_convos.items():
			# chirp info that started convo
			convo_start = chirps_list[0]
			print("{0}. {1}: {2}".format(counter, chirps_dict[convo_start][0], chirps_dict[convo_start][1]))
			convo_id_list.append([convo_key, "public"])
			counter += 1
		print("\nSelect a chirp, or enter 'q' to quit")
		convo = input("> ")
		# select convo based on user input
		try:
			if int(convo) <= counter:
				selected_convo_id = convo_id_list[int(convo) - 1]
				return selected_convo_id
			elif convo == "q":
				show_menu()
		except IndexError as ex:
			print("\n{}".format(ex))
			print("Sorry, thats an invalid entry. Try again:\n")

	def new_public_chirp(current_user):
		"""
		Adds a new public chirp

		Args- currently selected user
		"""
		# if a user is signed in
		if current_user != None:
			print("\nEnter new public chirp:")
			user_input = input("> ")
			# take user input and create new PublicChirp()
			public_chirp = PublicChirp(
				user_input,
				current_user,
				random_id_generator()
			)
			# write new PublicChirp() to CSV file
			CSV.write_public_chirp_to_csv_file(public_chirp, "chirps.csv")
			return public_chirp
		else:
			print("\nPlease select a user first")

	def new_private_chirp(current_user, users_dict):
		"""
		Adds a new private chirp

		Args- currently selected user, dictionary of users
		"""
		# if a user is signed in
		if current_user != None:
			recipient = UserUtility.select_a_user(users_dict, current_user)
			print("\nEnter new private chirp:")
			user_input = input("> ")
			# create new PrivateChirp() with arguments and user input
			private_chirp = PrivateChirp(
				user_input,
				current_user,
				recipient.screen_name,
				random_id_generator()
			)
			# write new PrivateChirp() to CSV file
			CSV.write_private_chirp_to_csv_file(private_chirp, "chirps.csv")
			return private_chirp
		else:
			print("\nPlease select a user first")

	def new_private_reply(current_user, recipient):
		"""
		Adds a new private chirp

		Args- currently selected user, dictionary of users
		"""
		# if a user is signed in
		if current_user != None:
			print("\nEnter new private chirp:")
			user_input = input("> ")
			# create PrivateChirp() with arguments and user input
			private_chirp = PrivateChirp(
				user_input,
				current_user,
				recipient,
				random_id_generator()
			)
			# write new PublicChirp() to CSV file
			CSV.write_private_chirp_to_csv_file(private_chirp, "chirps.csv")
			return private_chirp
		else:
			print("\nPlease select a user first")
