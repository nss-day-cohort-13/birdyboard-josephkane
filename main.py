import time
from user import *
from csv_utility import *
from random_id_generator import *
from chirps import *
from chirps_utility import *
from user_utility import *

class MainMenu:

	def __init__(self):
		print("")
		print(" ~ WELCOME TO BIRDYBOARD ~ ")
		self.users = dict()
		self.current_user = None
		try:
			self.users = CSV.get_users_from_csv_file("users.csv")
			self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")
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
					user = UserUtility.create_user()
					CSV.write_user_to_csv_file(user, "users.csv")
					self.current_user = user
					self.users = CSV.get_users_from_csv_file("users.csv")
					print("Welcome, {}!".format(self.current_user.screen_name))

				elif action == "2":
					self.current_user = UserUtility.select_a_user(self.users, self.current_user)
					print("Welcome, {}!".format(self.current_user.screen_name))

				elif action == "3":
					ChirpsUtility.view_chirps(self.chirps, self.current_user)

				elif action == "4":
					public_chirp = ChirpsUtility.new_public_chirp(self.current_user)
					self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")

				elif action == "5":
					private_chirp = ChirpsUtility.new_private_chirp(self.current_user, self.users)
					self.chirps = CSV.get_chirps_from_csv_file("chirps.csv")

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
