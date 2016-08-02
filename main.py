import time
from user import *
from csv_methods import *
from random_id_generator import *
from chirps import *
from view_chirps import *

class MainMenu:

	def __init__(self):
		print("")
		print(" ~ WELCOME TO BIRDYBOARD ~ ")
		self.users = dict()
		self.current_user = None
		try:
			self.users = get_users_from_csv_file("users.csv")
			self.chirps = get_chirps_from_csv_file("chirps.csv")
		except FileNotFoundError:
			pass

	def show_menu(self):
		"""
		Displays menu from which users will navigate app

		Args- None
		"""
		print("")
		print("What would you like to do?")
		print("1. New user account")
		print("2. Select user")
		print("3. View chirps")
		print("4. Public chirp")
		print("5. Private chirp")
		print("6. Quit")
		action = input("> ")

		try:
			if int(action) > 0 and int(action) < 7:
				if action == "1":
					print("")
					print("Enter full name")
					full_name = input("> ")
					print("")
					print("Enter screen name")
					screen_name = input("> ")
					user = User(full_name, screen_name, random_id_generator())
					write_user_to_csv_file(user, "users.csv")
					self.current_user = user
					print("Welcome, {}!".format(self.current_user.screen_name))

				elif action == "2":
					print("")
					print("Please choose a user:")
					counter = 1
					user_list = list()
					for k, v in self.users.items():
						print("{0}: {1}".format(counter, v[0]))
						user_list.append(k)
						counter += 1
					selection = input("> ")
					selected_user_id = user_list[int(selection) - 1]
					current_user = User(
						self.users[selected_user_id][1],
						self.users[selected_user_id][0],
						selected_user_id
					)
					self.current_user = current_user
					print("Welcome, {}!".format(self.current_user.screen_name))

				elif action == "3":
					view_chirps(self.chirps)
				elif action == "4":
					if self.current_user:
						print("")
						print("Enter new public chirp:")
						user_input = input("> ")
						public_chirp = PublicChirp(
							user_input,
							self.current_user.screen_name,
							random_id_generator()
						)
						write_public_chirp_to_csv_file(public_chirp, "chirps.csv")

					else:
						print("")
						print("Please select a user first")
				elif action == "5":
					print("new private chirp")
				elif action == "6":
					exit()

				if action != "6":
					time.sleep(1)
					self.show_menu()

		except ValueError as ex:
			print(ex)
			print("")
			print("Please enter a valid choice.")
			print("")
			time.sleep(1)
			self.show_menu()

if __name__ == "__main__":
	mm = MainMenu()
	mm.show_menu()
