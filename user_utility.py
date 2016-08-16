from user import *
from random_id_generator import *

class UserUtility:

	def create_user(full_name, screen_name):
		"""
		Creates and returns a new user

		Args-user full name, user screen name
		"""
		user = User(full_name, screen_name, random_id_generator())
		return user

	def select_a_user(users_dict, current_user):
		"""
		Displays a list of users (all users if current use is none, all but current user if not),
		selects and returns new user based on input

		Args-dictionary of signed-up users, currently logged in user (may be None)
		"""
		print("\nPlease choose a user:")
		# counter and empty list to be used for user select
		# (display counter as choice number, append each user to user_list,
		# user int(counter - 1) to find user in user_list by index
		counter = 1
		user_list = list()
		print("\nUSER DICT: ", users_dict)
		for user_id, user_info in users_dict.items():
			# if a user is signed in
			if current_user:
				# display all but the current user
				if user_info[0] != current_user:
					print("{0}: {1}".format(counter, user_info[0]))
					user_list.append(user_id)
					counter += 1
			# print all in users_dict if no one is signed in
			else:
				print("{0}: {1}".format(counter, user_info[0]))
				user_list.append(user_id)
				counter += 1
		selection = input("> ")
		# use user input to grab the correct user id from user_list
		selected_user_id = user_list[int(selection) - 1]
		# make new User() with info from user_list
		current_user = User(
			users_dict[selected_user_id][1],
			users_dict[selected_user_id][0],
			selected_user_id
		)

		return current_user
