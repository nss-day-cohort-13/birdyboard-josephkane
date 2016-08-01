import time
from create_user import *
from csv_methods import *

class MainMenu:

	def __init__(self):
		print("")
		print(" ~ WELCOME TO BIRDYBOARD ~ ")
		self.users = dict()
		try:
			self.users = get_users_from_csv("users.csv").split(",")
		except FileNotFoundError:
			pass

	def show_menu(self):
		"""
		Displays menu from which users will navigate app
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
					user = User()
					print("create a new user")
					print("")
					print("Enter full name")
					full_name = input("> ")
					print("")
					print("Enter screen name")
					screen_name = input("> ")
					user.full_name = full_name
					user.screen_name = screen_name
					user.user_id = user.random_id_generator()
					write_user_to_csv_file(user, "users.csv")

				elif action == "2":
					print("select a user")
				elif action == "3":
					print("view all chirps")
				elif action == "4":
					print("new public chirp")
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
