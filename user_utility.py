from user import *
from random_id_generator import *

class UserUtility:

	def create_user(full_name, screen_name):
		user = User(full_name, screen_name, random_id_generator())
		return user

	def select_a_user(users_dict, current_user):
		print("\nPlease choose a user:")
		counter = 1
		user_list = list()
		for k, v in users_dict.items():
			if current_user:
				if v[0] != current_user.screen_name:
					print("{0}: {1}".format(counter, v[0]))
					user_list.append(k)
					counter += 1
			else:
				print("{0}: {1}".format(counter, v[0]))
				user_list.append(k)
				counter += 1
		selection = input("> ")
		selected_user_id = user_list[int(selection) - 1]
		current_user = User(
			users_dict[selected_user_id][1],
			users_dict[selected_user_id][0],
			selected_user_id
		)

		return current_user
